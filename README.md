# simulatorProcess Simulación de Planificación de Procesos (FCFS y SRTF)
En este archivo se presenta la simulación de un conjunto de procesos con distintos tiempos de llegada y duración, utilizando dos algoritmos de planificación: First-Come, First-Served (FCFS) y Shortest Remaining Time First (SRTF) utilizando Python y Streamlit.

## Características

- Simulación de 5 procesos con tiempos de llegada y duración distintos.
- Visualización en **diagramas de Gantt**.
- Cálculo y visualización de:
  - Tiempo de espera.
  - Tiempo de retorno.
  - Tiempo de respuesta.
- Comparación de resultados entre FCFS y SRTF.

## Cómo acceder

Puedes acceder a la simulación en línea en el siguiente enlace:
[https://simulator-alg-plan-process.streamlit.app/](https://simulator-alg-plan-process.streamlit.app/)

## Cómo ejecutar localmente

1. Clona este repositorio:
   ```bash
   git clone https://github.com/sulevilo/simulatorProcess.git
   cd simulatorProcess
   ```

2. Instala las dependencias:
   ```bash
   pip install streamlit matplotlib
   ```

3. Ejecuta la aplicación:
   ```bash
   streamlit run simulacion_streamlit.py
   ```

4. Se abrirá automáticamente en tu navegador (`http://localhost:8501`)
