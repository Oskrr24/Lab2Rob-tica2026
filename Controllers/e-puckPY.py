# Código con el filtro de Kalman
from controller import Robot
import csv
import math

def run_robot():
    robot = Robot()
    timestep = int(robot.getBasicTimeStep())
    max_speed = 4.28

    # Motores
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

    # Encoders
    left_encoder = left_motor.getPositionSensor()
    right_encoder = right_motor.getPositionSensor()
    left_encoder.enable(timestep)
    right_encoder.enable(timestep)

    # Sensores
    ps = []
    ps_names = ['ps0', 'ps1', 'ps2', 'ps3', 'ps4', 'ps5', 'ps6', 'ps7']
    for name in ps_names:
        sensor = robot.getDevice(name)
        sensor.enable(timestep)
        ps.append(sensor)

    # Tiempo
    Ts = timestep / 1000.0
    time = 0.0

    save_interval = 0.5
    last_save_time = 0.0

    # Encoders → movimiento
    wheel_radius = 0.0205
    prev_left  = None
    prev_right = None

    # KALMAN
    d_est = 1.0     # estimación inicial en metros
    P = 1.0         # incertidumbre inicial
    Q = 0.01        # ruido del modelo 
    R = 0.4        # ruido del sensor  

    RANGE = 212.0

    # CSV
    file = open('datosKalman.csv', 'w', newline='')
    writer = csv.writer(file)
    writer.writerow([
        'time',
        'front_left', 'front_right',
        'measurement_z',
        'kalman_estimate',
        'delta_s'
    ])

    while robot.step(timestep) != -1:

        # SENSORES
        ps_values = [sensor.getValue() for sensor in ps]
        front_left  = ps_values[7]
        front_right = ps_values[0]

        raw_front = (front_left + front_right) / 2.0

        if raw_front < 1.0:
            raw_front = 1.0

        constante_sensor = 0.05 * 1024.0
        z = constante_sensor / raw_front

        # ENCODERS
        left_pos  = left_encoder.getValue()
        right_pos = right_encoder.getValue()

        if prev_left is None or prev_right is None:
            prev_left  = left_pos
            prev_right = right_pos

        delta_left  = left_pos  - prev_left
        delta_right = right_pos - prev_right

        prev_left  = left_pos
        prev_right = right_pos

        if math.isnan(delta_left)  or math.isinf(delta_left):  delta_left  = 0.0
        if math.isnan(delta_right) or math.isinf(delta_right): delta_right = 0.0

        delta_s = (wheel_radius * delta_left + wheel_radius * delta_right) / 2.0

        # KALMAN — PREDICCIÓN
        d_pred = d_est - delta_s
        P = P + Q

        # KALMAN — CORRECCIÓN
        K     = P / (P + R)
        d_est = d_pred + K * (z - d_pred)
        P     = (1 - K) * P

        # TIEMPO
        time += Ts

        # GUARDAR
        if time - last_save_time >= save_interval:
            writer.writerow([
                time,
                front_left,   
                front_right,  
                z,
                d_est,
                delta_s
            ])
            file.flush()

            print(f"t={time:.2f} | z={z:.4f} | kalman={d_est:.4f}")

            last_save_time = time

        # NAVEGACIÓN REACTIVA (Kalman + sensores laterales)

        # Umbrales
        SAFE_DIST     = 0.2   # metros — distancia frontal mínima segura
        WALL_THRESH   = 78.0  # valor raw lateral — umbral de pared cercana

        # Sensores laterales
        lateral_left  = ps_values[6] #ps6 → lateral izquierdo
        lateral_right = ps_values[1] #ps1 → lateral derecho

        if d_est <= SAFE_DIST:
            #PRIORIDAD 1: obstáculo al frente → girar hacia el lado más despejado
            if lateral_left > lateral_right:
                vl =  max_speed * 0.6
                vr = -max_speed * 0.6
            else:
                vl = -max_speed * 0.6
                vr =  max_speed * 0.6

        elif lateral_left > WALL_THRESH:
            #PRIORIDAD 2: pared lateral izquierda → corrección suave hacia la derecha
            vl = max_speed * 0.8
            vr = max_speed * 0.0

        elif lateral_right > WALL_THRESH:
            #PRIORIDAD 2: pared lateral derecha → corrección suave hacia la izquierda
            vl = max_speed * 0.0
            vr = max_speed * 0.8

        else:
            #PRIORIDAD 3: camino libre → avanzar
            vl = max_speed * 0.5
            vr = max_speed * 0.5

        vl = max(min(vl, max_speed), -max_speed)
        vr = max(min(vr, max_speed), -max_speed)

        left_motor.setVelocity(vl)
        right_motor.setVelocity(vr)

    file.close()

if __name__ == "__main__":
    run_robot()