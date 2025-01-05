# Öklit hesaplama
def euclideanDistance(x,y):
    distances = 0
    for i in range(len(x)):
        distances += (x[i] - y[i]) * (x[i] - y[i])
        distances **= 0.5
        return distances
point1 = [1, 1]
point2 = [5, 5]
result = euclideanDistance(point1,point2)
print (result)
