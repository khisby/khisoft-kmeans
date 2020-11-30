import math
class CalculateDistance:
    def euclidean(data1, data2):
        n = len(data1)
        total = 0
        jarak = 0
        for i in range(n):
            jarak = math.pow(data1[i] - data2[i], 2)
            total = total + jarak
        return math.sqrt(total)


