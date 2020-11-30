import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import streamlit as st
style.use('ggplot')

class Visualization:
    color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

    def plot(data=[],cluster=[], title=""):
        data = np.array(data, dtype=np.ndarray)
        cluster = np.array(cluster, dtype=np.ndarray)
        max_number = np.max(np.max(data))+3
        plt.gca().set_xlim([0, max_number])
        plt.gca().set_ylim([0, max_number])

        for index, i in enumerate(data):
            arr = np.asarray(i)
            d = plt.scatter(arr[:,0], arr[:,1], s=150, color=Visualization.color[index])

        for i in cluster:
            arr = np.asarray(i)
            c = plt.scatter(arr[0], arr[1], s=150, marker="x", edgecolors="black", linewidths=3)

        plt.legend((d, c), ("Data", "Centroid"))
        plt.title(title)
        plt.show()

    def plot_sse(sse, title=""):
        plt.plot(sse)
        plt.title(title)
        plt.show()

    def plot_web(data=[],cluster=[], title=""):
        data = np.array(data, dtype=np.ndarray)
        cluster = np.array(cluster, dtype=np.ndarray)
        Visualization.max_number = np.max(np.max(data))+5
        plt.gca().set_xlim([0, Visualization.max_number])
        plt.gca().set_ylim([0, Visualization.max_number])

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        for index, i in enumerate(data):
            arr = np.asarray(i)
            d = ax.scatter(arr[:,0], arr[:,1], s=150, color=Visualization.color[index])

        for i in cluster:
            arr = np.asarray(i)
            c = ax.scatter(arr[0], arr[1], s=150, marker="x", edgecolors="black", linewidths=3)

        ax.legend((d, c), ("Data", "Centroid"))
        fig.suptitle(title, y=.995)
        fig.show()
        st.write(fig)

    def plot_sse_web(sse, title=""):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(sse)
        fig.suptitle(title)
        fig.suptitle(title, y=.995)
        fig.show()
        st.write(fig)