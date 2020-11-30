import khisoft as khisoft
import numpy as np

data = [[1,2],
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


x_min = np.min(np.asarray(data)[:,0])
x_max = np.max(np.asarray(data)[:,0])
y_min = np.min(np.asarray(data)[:,1])
y_max = np.max(np.asarray(data)[:,1])
# print(x_min, x_max, y_min, y_max)

# x_min = 4
# x_max = 6
# y_min = 4
# y_max = 6


centroid_awal = [[3,3],[0,1],[1,5]]
# centroid_awal = []
# for i in range(centroid):
#         centroid_awal.append([randrange(x_min,x_max),randrange(x_min,x_max)])

khisoft.Visualization.plot([data], [centroid_awal], title="Data Awal")


kmeans = khisoft.Kmeans(data, centroid_awal)
kmeans.train()
kmeans.plot()