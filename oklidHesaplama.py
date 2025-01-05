# Öklit hesaplama
def euclideanDistance(x,y):
    distances = 0
    distances = ((x[0] - y[0]) * (x[0] - y[0]) + (x[1] - y[1]) * (x[1] - y[1]))
    distances **= 0.5
    return distances
point1 = [1, 1]
point2 = [4, 5]
result = euclideanDistance(point1,point2)
print (result)
