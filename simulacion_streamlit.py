import streamlit as st
import matplotlib.pyplot as plt

# Datos de entrada
procesos = [
    {"id": "P1", "llegada": 0, "duracion": 8},
    {"id": "P2", "llegada": 1, "duracion": 4},
    {"id": "P3", "llegada": 2, "duracion": 9},
    {"id": "P4", "llegada": 3, "duracion": 5},
    {"id": "P5", "llegada": 6, "duracion": 2},
]

def fcfs(procesos):
    procesos_ordenados = sorted(procesos, key=lambda p: p["llegada"])
    tiempo = 0
    resultados = []
    for p in procesos_ordenados:
        inicio = max(tiempo, p["llegada"])
        fin = inicio + p["duracion"]
        retorno = fin - p["llegada"]
        espera = inicio - p["llegada"]
        respuesta = espera
        resultados.append({"id": p["id"], "inicio": inicio, "fin": fin, "espera": espera, "retorno": retorno, "respuesta": respuesta})
        tiempo = fin
    return resultados

def srtf(procesos):
    tiempo = 0
    completados = 0
    n = len(procesos)
    restantes = [p["duracion"] for p in procesos]
    inicio_dict = {}
    resultados = []
    ejecuciones = []
    proceso_actual = None

    while completados < n:
        elegibles = [i for i in range(n) if procesos[i]["llegada"] <= tiempo and restantes[i] > 0]
        if elegibles:
            idx = min(elegibles, key=lambda i: restantes[i])
            if procesos[idx]["id"] != proceso_actual:
                ejecuciones.append((tiempo, procesos[idx]["id"]))
                proceso_actual = procesos[idx]["id"]
            if procesos[idx]["id"] not in inicio_dict:
                inicio_dict[procesos[idx]["id"]] = tiempo
            restantes[idx] -= 1
            if restantes[idx] == 0:
                fin = tiempo + 1
                llegada = procesos[idx]["llegada"]
                duracion = procesos[idx]["duracion"]
                espera = fin - llegada - duracion
                retorno = fin - llegada
                respuesta = inicio_dict[procesos[idx]["id"]] - llegada
                resultados.append({"id": procesos[idx]["id"], "inicio": inicio_dict[procesos[idx]["id"]], "fin": fin, "espera": espera, "retorno": retorno, "respuesta": respuesta})
                completados += 1
        else:
            proceso_actual = None
        tiempo += 1
    return resultados, ejecuciones

def diagrama_gantt(etiqueta, resultados, ejecuciones=None):
    fig, gnt = plt.subplots()
    gnt.set_title(f"Diagrama de Gantt - {etiqueta}")
    gnt.set_xlabel("Tiempo")
    gnt.set_ylabel("Procesos")
    gnt.set_yticks(range(10, 10*len(procesos)+1, 10))
    gnt.set_yticklabels([p["id"] for p in procesos])
    gnt.grid(True)

    colores = {
        "P1": "red", "P2": "blue", "P3": "green", "P4": "purple", "P5": "orange"
    }

    if ejecuciones:
        for i in range(len(ejecuciones)):
            t0, pid = ejecuciones[i]
            t1 = ejecuciones[i+1][0] if i+1 < len(ejecuciones) else max([r["fin"] for r in resultados])
            gnt.broken_barh([(t0, t1 - t0)], (10 * (int(pid[1]) - 1), 9), facecolors=colores[pid])
    else:
        for r in resultados:
            gnt.broken_barh([(r["inicio"], r["fin"] - r["inicio"])], (10 * (int(r["id"][1]) - 1), 9), facecolors=colores[r["id"]])
    return fig

def imprimir_resultados(resultados):
    espera_total = retorno_total = respuesta_total = 0
    for r in resultados:
        st.write(f"{r['id']}: Espera={r['espera']} | Retorno={r['retorno']} | Respuesta={r['respuesta']}")
        espera_total += r["espera"]
        retorno_total += r["retorno"]
        respuesta_total += r["respuesta"]
    n = len(resultados)
    st.write(f"**Promedio Espera:** {espera_total/n:.2f}")
    st.write(f"**Promedio Retorno:** {retorno_total/n:.2f}")
    st.write(f"**Promedio Respuesta:** {respuesta_total/n:.2f}")

# Streamlit UI
st.title("Simulación de Planificación de Procesos")
st.write("Algoritmos implementados: **FCFS** y **SRTF**")

# Ejecutar
res_fcfs = fcfs(procesos)
res_srtf, ejec_srtf = srtf(procesos)

# FCFS
st.header("Resultados - FCFS")
imprimir_resultados(res_fcfs)
st.pyplot(diagrama_gantt("FCFS", res_fcfs))

# SRTF
st.header("Resultados - SRTF")
imprimir_resultados(res_srtf)
st.pyplot(diagrama_gantt("SRTF", res_srtf, ejec_srtf))
