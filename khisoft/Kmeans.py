from .CalculateDistance import CalculateDistance
from .Visualization import Visualization
import numpy as np

class Kmeans:
    def __init__(self, data, centroid_awal):
        self.data = data
        self.n_cluster = len(centroid_awal)
        self.n_data = len(data)
        self.centroid_sebelumnya = centroid_awal
        self.centroid = centroid_awal
        self.sse = []
        self.log = []

    def train(self):
        iterasi = 1
        while True:
            if self.centroid == self.centroid_sebelumnya and iterasi != 1:
                break

            jarak_cluster, jarak_terdekat_seluruhnya = self.getDistMin()
            self.sse.append(np.sum(jarak_cluster))
            cluster_baru, anggota = self.new_cluster(jarak_terdekat_seluruhnya)

            self.centroid_sebelumnya = self.centroid
            self.centroid = cluster_baru

            self.log.append([cluster_baru,anggota])

            iterasi = iterasi + 1

    def cari_anggota(self,data, jarak_terdekat_seluruhnya, index_data):
        arr = []
        for index, i in enumerate(data):
            if jarak_terdekat_seluruhnya[index] == index_data:
               arr.append(i)
        return arr

    def new_cluster(self, jarak_terdekat_seluruhnya):
        arr = []
        anggotas = []
        for i in range(self.n_cluster):
            anggota = self.cari_anggota(self.data, jarak_terdekat_seluruhnya, i)
            anggotas.append(anggota)
            arr.append(np.asarray(np.average(anggota, axis=0)).tolist())
        return arr, anggotas

    def getDistMin(self):
        jarak_seluruhnya = []
        for i in self.data:
            jarak_perbaris = []
            for j in self.centroid:
                jarak = CalculateDistance.euclidean(i, j)
                jarak_perbaris.append(jarak)
            jarak_seluruhnya.append(jarak_perbaris)

        jarak_terdekat_seluruhnya = []
        for i in jarak_seluruhnya:
            jarak_terdekat = np.argmin(i)
            jarak_terdekat_seluruhnya.append(jarak_terdekat)


        jarak_cluster = [jarak_seluruhnya[index][i] for index, i in [(index, i) for index, i in enumerate(jarak_terdekat_seluruhnya)]]
        return jarak_cluster, jarak_terdekat_seluruhnya

    def plot(self):
        for index, (centroid, data) in enumerate(self.log):
            Visualization.plot_web(data, centroid, title="Iterasi Ke - " + str(index+1))

        Visualization.plot_sse_web(self.sse, title="Plot SSE - " + str(self.n_cluster) + " Cluster")
