# Laboratorio 2 Robótica y Sist. Autónomos
ICI4150-2

- Integrantes
    - Oscar Ruiz
    - Milovan Fuentes
    - Marcos Cádiz
    - Andrés García
    - Amaro Fibla

Aquí el link de la carpeta de Google Drive para la visualización de los videos y captura mencionados en el informe:

[Drive](https://drive.google.com/drive/folders/1IMOf7NB3bM5jFQaK-MoyDHuZgLimQ4P9?usp=sharing)

La visualización de los datos de manera gráfica se realizó en este Google Colab:

[Colab](https://colab.research.google.com/drive/19CGSQK1C7pJxbpX06OsV5Nk0eq73zPJr?usp=sharing)

# Contenido

1. [Objetivo del trabajo](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)
2. [Instrucciones para ejecutar la simulación en Webots](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)
3. [Robot y Sensores](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)
4. [Lógica de navegación reactiva (Braitenberg)](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)
5. [Muestreo](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)
6. [Frecuencia de muestreo empleada](https://www.notion.so/Ingenier-a-de-Software-32d781d6c2de8047bcf1d26dd9fd37c7?pvs=21)
7. [Datos Crudos](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)
    1. [Resultados obtenidos](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)
    2. [Gráficos](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)
    3. [Análisis de señales registradas](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)
8. [Filtro Simple](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)
    1. [Resultados obtenidos](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)
    2. [Gráficos](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)
    3. [Análisis de señales registradas](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)
9. [Filtro de Kalman](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)
    1. [Resultados obtenidos](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)
    2. [Gráficos](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)
    3. [Análisis de señales registradas](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)
10. [Comparación entre controladores](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)
11. [Análisis final](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)
12. [Conclusiones](https://www.notion.so/Laboratorio-2-Rob-tica-y-Sist-Aut-nomos-34c781d6c2de80f0a27df68716554b5f?pvs=21)

# Objetivo del trabajo

El objetivo de este laboratorio es implementar un sistema de navegación reactiva para un robot móvil diferencial (e-puck) en el simulador Webots, utilizando sensores de distancia y encoders de rueda, aplicando un filtro normal y un filtro de Kalman para la fusión sensorial y la mejora en la toma de decisiones para la evasión de obstáculos.

Es importante aclarar desde este punto que los experimentos se realizaron en dos escenarios distintos, el Escenario Simple y el Escenario complejo

El escenario simple consta de 2 paredes, una caja y un pequeño pasillo de dos cajas, seguido de una línea recta, en donde el robot luego de girar tiene unos segundos de recuperación antes de volver a toparse con el obstáculo.

El escenario complejo consta de 3 paredes y unas cajas. Además del añadido de la pared, este tiene poco tiempo de recuperación (recta) antes de chocar con el siguiente objeto, esto con el fin de probar si la reacción es la correcta y los parámetros están bien establecidos en el código.

Además de que cada experimento se realizó en un tiempo aproximado en 60 segundos para así tener más de 100 registros para cada escenario y filtro, ya que el controlador guarda datos cada 0.5 segundos.

# Instrucciones para ejecutar la simulación en Webots

Para ejecutar la simulación, es necesario tener Python instalado en el dispositivo.

*Disclaimer: Se recomienda guardar una copia del mundo en otro lugar, esto en caso de su modificación.

1. Descargar el zip de GitHub
2. Descomprimir Lab2Robotica.rar
3. Entrar en al carpeta → worlds → abrir e-puck.wbt con Webots
4. Cargamos el mundo
5. En el panel izquierdo, seleccionamos el e-puck que se quiere probar, el del escenario simple o complejo y hacemos click en “controller” → “Select”, para seleccionar el que dice “e-puckPY” → OK, guardamos y preparamos para la simulación
6. Para probar distintos algoritmos, en “controller” cambiamos el controlador al algortimo que se quiera probar. Si se quiere editar el código, en “controller” al lado de “Select”, presionamos “Edit” y seleccionamos el código en la carpeta, luego se abrirá en el panel derecho.

**Ejemplo de simulación simple**

Una vez se tiene el mundo y el controlador cargado (es importante para este caso que el e-puckComplejo NO tenga controlador, seleccionar “None” para este caso), damos click en iniciar la simulación.

Para ejecutar con otro controlador, seleccionar “controller” para cambiar al deseado y luego recargar la simulación (importante NO guardar el mundo, ya que cambiará al robot de posición).

Finalmente si se quiere probar en el escenario complejo, se deja el e-puckSimple con controlador “None” y se selecciona el controlador deseado para el e-puck complejo

# Robot y Sensores

Se utilizo el modelo diferencial e-puck. Para percibir el entorno, se emplearon sus sensores infrarrojos (ps0 a ps7), específicamente, se promediaron los frontales (ps0 y ps7) para detectar los obstáculos de frente, y los laterales-diagonales (ps1 y ps6) para decidir la dirección de los giros. 

También se activaron los encoders de ambas ruedas para medir el giro de los motores y calcular la odometria del robot.

# Lógica de navegación reactiva (Braitenberg)

Para las dos primeras etapas de este experimento (datos crudos y filtro simple), se implementó un control de navegación continua Braitenberg. Este enfoque reactivo conecta directamente la percepción del robot con su actuación, sin necesidad de construir mapas ni planificar rutas complejas.

El algoritmo funciona mediante una matriz de pesos predefinida. En cada ciclo, el controlador lee y normaliza los valores de los ocho sensores infrarrojos. Estos valores se multiplican por los coeficientes de la matriz (positivos o negativos), generando comandos automáticos de giro para evadir obstáculos. Finalmente, el resultado se multiplica por una ganancia de velocidad y se restringe mediante la función max(min(…)) para no superar el límite físico del motor.

# Muestreo

### Frecuencia de muestreo empleada

El ciclo de control del robot está regido por el reloj interno de Webots. Para garantizar una precisión matemática en la odometria y el filtro de Kalman, el tiempo de ciclo se extrajo dinámicamente del simulador en lugar de asignarlo de forma manual.

**Tiempo de muestreo**

El simulador entrego un paso de tiempo (timestep) base de 32 milisegundos. Para trabajar correctamente con las formulas de velocidad y predicción, este valor se convirtió a segundos, estableciendo un Tiempo de Muestreo (Ts) fijo de 0.032 segundos para todos los algoritmos y escenarios de prueba.

**Frecuencia**

A partir de este dato, se calculo la Frecuencia de Muestreo del sistema mediante la relación inversa (1 / 0.032), resultando en una frecuencia de operación constante de 31.25 Hz. Esta velocidad demostró ser optima para procesar los datos del entorno y permitir una navegación reactiva fluida sin sobrecargar los recursos del simulador.

**Estimación del avance mediante encoders**

Para estimar el desplazamiento lineal del robot en cada paso de tiempo, se utilizaron los encoders de ambas ruedas. Estos sensores entregan el ángulo girado en radianes, por lo que se aplicó la relación  s = r * θ , donde s es el desplazamiento lineal, r = 0.0205 m es el radio de la rueda del e-puck y es θ el desplazamiento angular medido. El desplazamiento total del robot se calculó promediando ambas ruedas

# Datos Crudos

En esta etapa inicial se registraron las lecturas directas de los sensores infrarrojos frontales del e-puck sin aplicar ningún filtro. El objetivo fue evaluar el nivel de ruido ambiental y observar el comportamiento físico del algoritmo de navegación reactiva continua (Braitenberg) al interactuar con estas variaciones de luz en dos escenarios distintos.

## Resultados obtenidos

**Escenario simple**

En este entorno, el robot evadió dos paredes y una caja, para luego atravesar un pasillo estrecho entre dos cajas antes de seguir en línea recta durante varios segundos. Al usar datos crudos, el robot logró avanzar, pero presentó temblores constantes en sus ruedas. Al acercarse a los obstáculos y cruzar el pasillo estrecho, las fluctuaciones repentinas de luz provocaron giros de evasión muy bruscos e inestables antes de poder retomar su camino libre.

**Escenario complejo**

En este entorno densamente poblado, el robot chocó con una pared, luego con un grupo de tres cajas, rebotó hacia la primera pared y fue desviado por otras tres cajas hacia una pared final. El comportamiento físico fue sumamente errático. La señal cruda saturó el sistema de control, provocando un intenso "efecto ping-pong" en zigzag, sin darle al e-puck el espacio ni el tiempo para estabilizarse entre impactos.

## Gráficos

A continuación analizaremos cada escenario ocupando dos gráficos, el primero compara las señales crudas de ambos sensores frontales con el objetivo de ver cuanto ruido tiene el sensor sin procesar, la línea amarilla simbolizando el sensor izquierdo y la línea punteada morada el sensor derecho.

En el segundo vemos el recorrido del delta_s en color rojo en el tiempo para ver cuándo el robot avanza, frena o gira. Delta_s siendo el desplazamiento lineal del robot en cada paso de tiempo.

**Escenario simple**

![image.png](attachment:a5ff7bfb-58b3-4440-a408-3740f6d469b9:image.png)

En primer gráfico se aprecia un pico alto al principio y luego dos picos bajos, todos aislados. Corresponden al momento exacto donde el robot detecta las paredes y las caja. Entre cada obstáculo, la señal no cae a cero absoluto, mostrando fluctuaciones continuas que representan el ruido ambiental del simulador.

En el segundo gráfico observamos algo similar en el timeline del delta_s, agregando otro pico de altura cercano al segundo 40, donde representa el paso entre las cajas.

**Escenario complejo**

![image.png](attachment:bd852cc9-70f5-423f-b347-6611b4ccfa04:image.png)

La grafica expone una saturación evidente de la señal infrarroja debido a la estrecha cercanía de los múltiples obstáculos en el pasillo. Los picos de lectura se presentan de forma densa y aglomerada, demostrando que el sensor carece de tiempo para volver a su estado de reposo.

Esta visualización confirma que depender de datos crudos en espacios muy reducidos sobrecarga el sistema e imposibilita una evasión fluida.

## Análisis de señales registradas

**Escenario simple**

El análisis demuestra que la señal infrarroja reporta ruido constante incluso en el largo tramo recto final. Al enfrentar las paredes iniciales, la caja y el pequeño pasillo intermedio, la lectura da saltos repentinos y dentados que superan los 200 puntos. Como el control de Braitenberg usa estos valores directamente, estas micro-fluctuaciones explican los temblores físicos y las maniobras de evasión poco prolijas observadas en la simulación.

**Escenario complejo**

El registro de este entorno revela una saturación de la señal en la percepción debido a los constantes desvíos entre las paredes y los grupos de cajas. Los datos muestran picos extremos superpuestos que, si bien logran bajar a niveles de reposo antes del siguiente impacto, nunca se llega a un nivel de reposo total (línea recta).

Esta saturación ininterrumpida de datos de peligro justifica plenamente el comportamiento errático del robot, haciendo inviable una navegación suave con señales crudas en espacios tan reducidos.

# Filtro Simple

Para mitigar las constantes fluctuaciones observadas en la etapa anterior, se implemento un filtro de Media Móvil Exponencial (EMA) con un factor alfa de 0.3 sobre las lecturas crudas. El objetivo fue suavizar la señal en tiempo real para intentar estabilizar la navegación del robot, evaluando su desempeño tanto frente a obstáculos espaciados como en pasillos estrechos.

## Resultados obtenidos

**Escenario simple**

La implementación del filtro exponencial eliminó casi por completo los temblores durante el avance inicial y el largo tramo recto final. Sin embargo, al enfrentar las paredes, la primera caja y cruzar el pasillo de cajas, se evidenció un retraso en la reacción. La señal de peligro tardó más en alcanzar el umbral, provocando que el robot iniciara sus giros tarde y pasara peligrosamente cerca de los obstáculos en comparación a la etapa sin filtro.

**Escenario complejo**

En la secuencia de rebotes entre la pared y los múltiples grupos de cajas, el filtro logró reducir los temblores por "falso pánico", pero su retraso inherente fue una desventaja crítica. Al ser desviado constantemente hacia nuevas paredes con muy poco espacio, el e-puck se volvió lento de reflejos. Enfrentó cada nuevo obstáculo de forma torpe, resultando en un paso ineficiente y con roces.

## Gráficos

Nuevamente comparamos gráficos pero esta vez usaremos tres, el primero analiza el sensor izquierdo crudo contra el sensor izquierdo filtrado con el motivo de comparar cuánto suaviza el filtro en el sensor izquierdo.

El segundo gráfico tiene la misma lógica que el primero pero en vez de los sensores izquierdos analizamos los derechos.

El tercer y último gráfico revisa el delta_s en el tiempo de ejecución

**Escenario simple**

![image.png](attachment:41ec79a3-3904-4835-bb42-a4f57f5f360c:image.png)

En el primer y segundo gráfico se observa cómo la línea oscura del filtro suaviza las fluctuaciones de la señal cruda verde durante los tramos rectos. Sin embargo, en los tres grandes picos, la curva filtrada se eleva con un claro desfase temporal hacia la derecha respecto a la original.

En la línea temporal del delta_s, percibimos algo parecido al caso anterior pero con pequeñas mejoras, confirmando que el filtro suaviza el ruido obtenido por los sensores y el entorno.

**Escenario complejo**

![image.png](attachment:15b09b3c-9853-44ae-8564-f682ab039606:image.png)

Los primeros gráficos muestran cómo la señal filtrada intenta promediar la rápida y violenta sucesión de picos provocados por el estrecho pasillo. Debido a esta falta de agilidad, la línea verde se mantiene artificialmente alta sin lograr descender por completo debido a los constantes obstáculos

Además, en el gráfico de los encoders, vemos picos constantes debido a los repetidos obstáculos a los cuales el robot se enfrenta, logrando solo por breves momentos un valor constante antes de llegar a otro pico.

Esta visualización demuestra que el filtro exponencial es demasiado lento para un entorno denso, manteniendo al robot en estado de pánico constante.

## Análisis de señales registradas

**Escenario simple**

Los datos filtrados demuestran una reducción del ruido ambiental en las zonas despejadas. No obstante, al usar un factor alfa de 0.3, el sistema pondera fuertemente el historial pasado. Cuando el valor crudo se disparó ante las paredes o al cruzar el pasillo estrecho, la señal filtrada necesitó de múltiples ciclos de código para lograr igualar esos picos, evidenciando la inercia matemática que causó el peligroso retraso físico en los giros.

**Escenario complejo**

El registro de este recorrido expone la gran limitación de los filtros de paso bajo. La rápida sucesión de subidas y bajadas al rebotar entre las cajas y paredes es promediada por el algoritmo, generando una curva que se mantiene artificialmente alta. Los datos confirman que la señal filtrada carece de la agilidad necesaria para descender a niveles seguros, manteniendo alertas de colisión continuas que explican la falta de reflejos del robot.

# Filtro de Kalman

Para superar el retraso del filtro exponencial, se implemento un Filtro de Kalman unidimensional y se reemplazo el control continuo de Braitenberg por una maquina de estados. Este algoritmo avanzado fusiona el desplazamiento físico medido por los encoders (odometría) con las lecturas infrarrojas convertidas a metros, logrando estimar la distancia real a los obstáculos de forma predictiva y precisa.

Es importante aclarar los siguientes parámetros que se usaron para calibrar el filtro de Kalman:

- Ruido de proceso: 0.01
- Ruido de medición: 0.4
- Umbral de decisión: 0.20 metros

Estos valores se tomaron considerando los escenarios simple y complejo, para que el robot tenga un desempeño óptimo en ambos casos.

## Resultados obtenidos

**Escenario simple**

En el recorrido simple, el robot logró un desempeño superior. La máquina de estados basada en la distancia estimada permitió que el e-puck avanzara con total suavidad durante los tramos rectos. Al acercarse a cada obstáculo y al entrar al pasillo, la estimación de Kalman permitió que el robot detectara la proximidad real sin reaccionar a los picos de ruido, ejecutando el giro evasivo justo al cruzar el umbral crítico de 0.20 metros.

**Escenario complejo**

Frente a la secuencia compleja, el robot mostró una gran estabilidad. La fusión de sensores permitió al e-puck ignorar el "falso pánico" que antes causaba rebotes incontrolables. Si bien el robot se detenía en distancias seguras frente a las paredes, cuando detectaba una caja este respondía algo tarde, se propone que esto es debido a la cercanía de la caja con los otros obstáculos.

## Gráficos

**Escenario simple**

![image.png](attachment:c3bbcd69-be9b-4873-9b50-e0a8e4985170:image.png)

En el primer gráfico se observa nuevamente los 3 picos causados por los 3 obstáculos principales del primer escenario, la estimación Kalman concuerda con la medición z, pero cuando se trata se ir en línea recta, la medición z con Kalman sugieren constantes diferencias.

En el segundo gráfico se analiza la estabilidad de la estimación Kalman, donde se puede ver con más claridad el filtro sin la medición z como fue su desempeño durante el recorrido.

Finalmente en el desplazamiento por encoders podemos ver el mayor avance, pasamos de grandes picos a unos no tan amplios, significando el gran avance que se obtuvo aplicando el filtro.

**Escenario complejo**

![image.png](attachment:42b3216d-0b9b-49a7-b111-d1cf89c0b0b7:image.png)

Para el escenario complejo también tenemos mejoras, si bien tenemos 3 picos, la estimación Kalman coincide con la medición z, interpretando que el robot identificaba correctamente los obstáculos. 

Para el segundo gráfico destacamos la baja en picos altos comparado con los otros filtros además de unos segundos donde el valor estuvo completamente recto, verificando la efectividad de este filtro.

## Análisis de señales registradas

**Escenario simple**
Al comparar los datos, la diferencia entre la medición cruda y la estimación final es drástica. En los tramos despejados, el filtro confía casi totalmente en la odometría, lo que mantiene la distancia estimada estable y libre de ruido. 

Al aparecer las paredes o la caja, la etapa de corrección del filtro ajusta la predicción con el sensor infrarrojo, logrando una caída en la curva que es suave pero inmediata. Esto demuestra matemáticamente que, a diferencia del filtro exponencial que siempre va "detrás" de la señal, Kalman logra anticipar el obstáculo, optimizando el tiempo de respuesta y la seguridad del giro.

**Escenario complejo**

El registro numérico es la prueba de la efectividad de la fusión de sensores. Mientras que el sensor crudo reporta valores caóticos debido a las reflexiones múltiples en las paredes y el grupo de tres cajas, la estimación de Kalman traza una trayectoria físicamente coherente. 

Los datos confirman que el algoritmo prioriza la lógica de movimiento calculada por los encoders para descartar las mediciones lumínicas que no tienen sentido físico. Esta estabilidad en la estimación entrega a la máquina de estados una distancia confiable, lo que permite que el robot mantenga una ruta lógica y segura incluso cuando está rodeado de obstáculos apretados, demostrando que el filtro de Kalman es la solución técnica definitiva para este problema de navegación.

# Comparación entre controladores

Para evaluar de forma objetiva el desempeño de los tres algoritmos, se comparó el desplazamiento lineal acumulado (delta_s) durante los 60 segundos de cada experimento, junto con métricas de cantidad de muestras, desplazamiento total y variabilidad del movimiento.

**Escenario simple**

![image.png](attachment:14869b22-8cb0-4761-a796-f5009ecb49ef:image.png)

| **Controlador** | **Muestras** | **delta_s total (m)** | **delta_s std** |
| --- | --- | --- | --- |
| Sin filtro | 118 | 0.1561 | 0.00020 |
| Filtro exponencial | 118 | 0.1575 | 0.00019 |
| Kalman | 118 | 0.1629 | 0.00009 |

En el escenario simple se observa que el controlador sin filtro presenta la mayor variabilidad en delta_s, con caídas bruscas frecuentes que reflejan los giros inestables provocados por el ruido. El filtro exponencial suaviza levemente este comportamiento, pero las caídas siguen siendo profundas debido al retraso en la reacción. El controlador Kalman muestra el patrón más estable, con caídas menos frecuentes y más controladas, lo que se traduce en un mayor desplazamiento total acumulado.

**Escenario complejo**

![image.png](attachment:e0848249-55e7-4b49-a16a-c3a6b9e0ae8d:image.png)

| **Controlador** | **Muestras** | **delta_s total (m)** | **delta_s std** |
| --- | --- | --- | --- |
| Sin filtro | 118 | 0.1499 | 0.00028 |
| Filtro exponencial | 118 | 0.1466 | 0.00032 |
| Kalman | 118 | 0.1635 | 0.00007 |

En el escenario complejo las diferencias se acentúan. Los controladores sin filtro y con filtro exponencial presentan caídas de delta_s densas y continuas, evidenciando que el robot pasó gran parte del tiempo girando en lugar de avanzar. El controlador Kalman, en cambio, logra períodos más prolongados de avance constante, confirmando que la estimación predictiva permite reaccionar en el momento justo sin sobregirar ante falsas alarmas.

# Análisis final

La progresión de las tres etapas de este laboratorio demuestra claramente cómo el tratamiento matemático de los datos sensoriales impacta directamente en el comportamiento físico y lógico de un robot móvil.

Al comparar los tres escenarios, se evidencia que el lazo de control directo (Braitenberg con datos crudos) es sumamente vulnerable al ruido ambiental y a la saturación por reflexiones lumínicas en espacios cerrados. Aunque es computacionalmente ligero, resulta inviable para una navegación segura y fluida debido a la inestabilidad que transmite a los motores.

La introducción del **filtro de Media Móvil Exponencial (EMA)** demostró que eliminar el ruido de alta frecuencia resuelve parcialmente la inestabilidad en algunos tramos. Sin embargo, matemáticamente se comprobó que los filtros basados únicamente en datos históricos introducen un desfase temporal. En la robótica móvil, donde el entorno cambia rápidamente, este retraso en la reacción anula el beneficio del suavizado, provocando colisiones o evasiones tardías en escenarios densos.

Finalmente, el **Filtro de Kalman** probó ser la solución óptima al cambiar el paradigma de un "suavizado de datos" a una "estimación predictiva". Al fusionar la inercia del robot (odometría mediante encoders) con las lecturas de los sensores infrarrojos, el sistema logró descartar mediciones físicamente ilógicas (ruido o falsos rebotes de luz). Más importante aún, la obtención de una distancia precisa y en metros permitió sustituir el control reactivo continuo por una **máquina de estados**, otorgándole al robot la capacidad de tomar decisiones lógicas, pausadas y seguras, independientemente de la densidad de obstáculos a su alrededor.

# Conclusiones

A partir del desarrollo y los resultados de este laboratorio, se pueden extraer las siguientes conclusiones fundamentales:

- **El ruido es inherente a la percepción robótica:** Tanto en simuladores como en hardware real, los sensores no entregan medidas perfectas. Depender de lecturas directas para el control de actuadores sobrecarga el sistema y genera comportamientos físicos inestables.
- **Los filtros de paso bajo tienen límites dinámicos:** Si bien técnicas simples como el filtro exponencial son útiles para estabilizar señales constantes, su inercia matemática los hace deficientes para sistemas que requieren tiempos de reacción críticos frente a obstáculos inminentes.
- **Filtro de Kalman:** El Filtro de Kalman demostró que combinar múltiples fuentes de información imperfecta (la predicción del movimiento interno del robot y la medición externa del sensor) genera una estimación mucho más precisa y robusta que confiar en un solo sensor.
- **Mejores datos permiten mejor control:** El éxito en la navegación del escenario complejo no dependió de motores más rápidos, sino de la transición hacia una arquitectura de software superior (máquina de estados). Esta mejora lógica solo fue posible gracias a la confianza y estabilidad que el Filtro de Kalman aportó a los datos de entrada.
