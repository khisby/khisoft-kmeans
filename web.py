import streamlit as st
import khisoft as khisoft
import numpy as np
import pandas as pd

d_data = [[1,2],
        [3,4],
        [2,3],
        [9,2],
        [8,9],
        [2,6],
        [8,1],
        [9,5],
        [8,9],
        [5,8],
        [8,8]]

d_centroid_awal = [[3,3],[0,1],[1,5],[4,8],[7,3]]
st.write(""" Selamat Datang - Khisoft K-Means """)
st.sidebar.header("K-Means")
st.sidebar.header("User Input")
data = eval(st.sidebar.text_area("Input Data",str(d_data)))
centroid_awal = eval(st.sidebar.text_area("Centroid Awal",str(d_centroid_awal)))
btn = st.sidebar.button("Hitung")

if btn:
    khisoft.Visualization.plot_web([data], [centroid_awal], title="Data Awal")
    kmeans = khisoft.Kmeans(data, centroid_awal)
    kmeans.train()
    kmeans.plot()