# Código con el filtro simple (exponencial)
from controller import Robot
import csv
import math

def run_robot():
    robot = Robot()
    timestep = int(robot.getBasicTimeStep())
    max_speed = 6.28

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

    # Sensores de proximidad
    ps = []
    ps_names = ['ps0', 'ps1', 'ps2', 'ps3', 'ps4', 'ps5', 'ps6', 'ps7']
    for name in ps_names:
        sensor = robot.getDevice(name)
        sensor.enable(timestep)
        ps.append(sensor)

    wheel_radius = 0.0205
    prev_left  = None
    prev_right = None

    # Tiempo
    Ts = timestep / 1000.0
    time = 0.0

    save_interval = 0.5
    last_save_time = 0.0

    # FILTRO EXPONENCIAL
    alpha      = 0.3
    filtered_ps = None

    braitenberg = [
        [ 0.942, -0.22 ],
        [ 0.63,  -0.1  ],
        [ 0.5,   -0.06 ],
        [-0.06,  -0.06 ],
        [-0.06,  -0.06 ],
        [-0.06,   0.5  ],
        [-0.19,   0.63 ],
        [-0.13,   0.942]
    ]
    RANGE = 212.0

    # CSV
    file = open('datosFiltroExpo.csv', 'w', newline='')
    writer = csv.writer(file)
    writer.writerow([
        'time',
        'front_left', 'front_right',
        'filtered_front_left', 'filtered_front_right',
        'left_encoder', 'right_encoder',
        'delta_s'   
    ])

    while robot.step(timestep) != -1:

        # SENSORES
        ps_values   = [sensor.getValue() for sensor in ps]
        front_left  = ps_values[7]
        front_right = ps_values[0]

        # FILTRO EXPONENCIAL
        if filtered_ps is None:
            filtered_ps = ps_values.copy()
        else:
            for i in range(8):
                filtered_ps[i] = alpha * ps_values[i] + (1 - alpha) * filtered_ps[i]

        filtered_front_left  = filtered_ps[7]
        filtered_front_right = filtered_ps[0]

        # ENCODERS 
        left_pos  = left_encoder.getValue()
        right_pos = right_encoder.getValue()

        if prev_left is None or prev_right is None:
            prev_left  = left_pos
            prev_right = right_pos

        delta_left  = left_pos  - prev_left
        delta_right = right_pos - prev_right

        if math.isnan(delta_left)  or math.isinf(delta_left):  delta_left  = 0.0
        if math.isnan(delta_right) or math.isinf(delta_right): delta_right = 0.0

        delta_s = (wheel_radius * delta_left + wheel_radius * delta_right) / 2.0

        prev_left  = left_pos
        prev_right = right_pos

        # TIEMPO
        time += Ts

        # GUARDAR DATOS
        if time - last_save_time >= save_interval:
            writer.writerow([
                time,
                front_left,
                front_right,
                filtered_front_left,
                filtered_front_right,
                left_pos,
                right_pos,
                delta_s
            ])
            file.flush()

            print(f"t={time:.2f} | FL={front_left:.1f} → {filtered_front_left:.1f} | delta_s={delta_s:.5f}")

            last_save_time = time

        # BRAITENBERG (usando filtro)
        vl = 0.0
        vr = 0.0

        for i in range(8):
            value      = filtered_ps[i]
            normalized = 1.0 - (value / RANGE)

            vl += braitenberg[i][0] * normalized
            vr += braitenberg[i][1] * normalized

        gain = 2
        vl *= gain
        vr *= gain

        vl = max(min(vl, max_speed), -max_speed)
        vr = max(min(vr, max_speed), -max_speed)

        left_motor.setVelocity(vl)
        right_motor.setVelocity(vr)

    file.close()


if __name__ == "__main__":
    run_robot()