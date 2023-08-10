import streamlit as st
import numpy as np


def sucesion_aritmetica(primer_termino, diferencia, posicion):
    try:
        a = np.array([primer_termino])
        for i in range(1, posicion):
            a = np.append(a, a[i-1] + diferencia)
        return a
    except Exception as e:
        st.error(f"Error: {e}")
        return None

def sucesion_geometrica(primer_termino, razon, posicion):
    try:
        a = np.array([primer_termino])
        for i in range(1, posicion):
            a = np.append(a, a[i-1] * razon)
        return a
    except Exception as e:
        st.error(f"Error: {e}")
        return None
    
def pertenece_a_la_sucesion(sucesion, numero):
    try:
        return numero in sucesion
    except Exception as e:
        st.error(f"Error: {e}")
        return None

st.title("Sucesiones")
st.image("https://www.matesfacil.com/ESO/progresiones/aritmeticas/P14-2.png", width=200)
st.write("Una sucesión (o progresión) es un conjunto de números ordenados. Cada número ocupa una posición y recibe el nombre de término. El término que ocupa la posición n se denota por an y se denomina término general o término n-ésimo.")
st.write("Una sucesión aritmética es una sucesión de números tales que la diferencia de dos términos consecutivos es constante. Por ejemplo, la sucesión de los números naturales:")
st.latex(r"a_0, a_1, a_2, \dots, a_n = a_0 + n \cdot d")
st.write("donde a0 es el primer término, d es la diferencia común y n es el número de términos.")
st.write("Una sucesión geométrica es una sucesión de números tales que el cociente de dos términos consecutivos es constante. Por ejemplo, la sucesión de los números naturales:")
st.latex(r"a_0, a_1, a_2, \dots, a_n = a_0 \cdot r^n")
st.write("donde a0 es el primer término, r es la razón común y n es el número de términos.")
st.write("Elige una sucesión:")
sucesion = st.selectbox("Sucesión", ["Aritmética", "Geométrica"])
primer_termino = st.number_input("Primer término", value=1)
if sucesion == "Aritmética":
    diferencia = st.number_input("Diferencia", value=1, key="aritmetica")
    posicion = st.number_input("Posición en la sucesión", value=1, min_value=1, step=1, key="aritmetica_posicion")
    sucesion = sucesion_aritmetica(primer_termino, diferencia, posicion)
    st.latex(rf"{', '.join(str(x) for x in sucesion)}")
else:
    razon = st.number_input("Razón", value=2, key="geometrica")
    posicion = st.number_input("Posición en la sucesión", value=1, min_value=1, step=1, key="geometrica_posicion")
    sucesion = sucesion_geometrica(primer_termino, razon, posicion)
    st.latex(rf"{', '.join(str(x) for x in sucesion)}")

st.write("¿Pertenece un número a la sucesión?")
numero = st.number_input("Número", value=1, key="pertenece")
if pertenece_a_la_sucesion(sucesion, numero):
    st.write("Sí pertenece")
    st.latex(f"{', '.join(str(x) for x in sucesion)}")
    
else:
    st.write("No pertenece")
    st.latex(f"{', '.join(str(x) for x in sucesion)}")
    
st.write("¿Cuál es el término n-ésimo?")
posicion = st.number_input("Posición en la sucesión", value=1, min_value=1, step=1, key="nesimo")
st.latex(rf"{sucesion[posicion-1]}")
