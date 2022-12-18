import sys
import random
import math
from ast import literal_eval
import time

# DMindYR
xk,yk=0,0


# Kmeans Implementation
# Input : Array List (vectors), K value (kVal)
# Output : Clustered vector (clusteredVectors)
def kmeans(vectors: list, kVal:int) -> list:
    #choose k initial random unequal points
    start = time.time()
    centerPoints = []
    while len(centerPoints) != kVal:
        candidate = random.choice(random.choice(vectors))
        if candidate not in centerPoints:
            centerPoints.append(candidate)
    #clustering
    testPrev = []
    iterationCounter = 0
    while True:
        clusteringTable = []
        for y in range(len(vectors)):
            clusteringTable.append([])
            for x in range(len(vectors[0])):
                temp = []
                temp.append(vectors[y][x])
                for k in range(kVal):
                    #distance from center point
                    distance = 0
                    for l in range(len(centerPoints[0])):
                        distance = distance + abs(centerPoints[k][l]-vectors[y][x][l])
                    temp.append(distance)
                #assign cluster centroid with min distance
                temp.append(temp[1:].index(min(temp[1:])))
                clusteringTable[y].append(temp)

        #check if cluster values changed, exit otherwise
        test = []
        for k in range(kVal):
            test.append(0)
            for itemY in clusteringTable:
                for itemX in itemY:
                    if itemX[-1] == k:
                        test[k] = test[k] + 1
        if testPrev == test:
            break
        testPrev = test

        #update centroids
        for k in range(kVal):
            n = 0
            vectorTemps = [0]*len(clusteringTable[0][0][0])
            for itemY in clusteringTable:
                for itemX in itemY:
                    if itemX[-1] == k:
                        for valCounter in range(len(itemX[0])):
                            vectorTemps[valCounter] = vectorTemps[valCounter] + itemX[0][valCounter]
                        n = n + 1
            #check for 0 division
            for valCounter in range(len(vectorTemps)):
                if vectorTemps[valCounter] != 0:
                    vectorTemps[valCounter] = vectorTemps[valCounter]/n
            centerPoints[k] = vectorTemps
        iterationCounter = iterationCounter + 1

    #Build clustered array
    clusteredVectors = []
    for y in range(len(clusteringTable)):
        clusteredVectors.append([])
        for x in range(len(clusteringTable[0])):
            clusteredVectors[y].append(centerPoints[clusteringTable[y][x][-1]])
    end = time.time()
    #Log info
    with open('logger.txt', 'a+') as out:
        out.write(f"""**K-MEANS RESULTS**\n""")
        out.write(f"""Array size: {len(vectors)}x{len(vectors[0])}x{len(vectors[0][0])}\n""")
        out.write(f"""Parameters: kVal: {kVal}\n""")
        out.write(f"""Centroid averages: {str(centerPoints)}\n""")
        out.write(f"""Time taken: {round(end - start)} seconds\n""")
    return clusteredVectors







#DBScan Implementation
#Distance functions
def EuclideanDistance(P,Q):
    intermediateValues = []
    for i in range(len(P[2])):
        intermediateValues.append(math.pow(Q[2][i]-P[2][i],2))
    return math.sqrt(sum(intermediateValues))

"""
#If using this then correct dbscan and FindNeighbours to have a param to differentiate the distance methods.
def MaximumDistance(P,Q):
    intermediateValues = []
    for i in range(len(P[2])):
        intermediateValues.append(abs(Q[2][i]-P[2][i]))
    return max(intermediateValues)
    
"""
mp = {}
#Finds all neighbor points for a chosen point
def FindNeighbours(Point, Points, eps):
    tempNeighbours = []
    for y in range(len(Points)):
        for x in range(len(Points[0])):
            if EuclideanDistance(Point, Points[y][x]) <= eps:
                    tempNeighbours.append(Points[y][x])
#Note: use Max Distance if required 
    return tempNeighbours

#reads vector array, performs dbscan and outputs vector array
def dbscan(vectors: list, minpts: int, epsilon: int) -> list:
    #Initialization
    start = time.time()
    mp = {}
    pointsArray = []
    for y in range(len(vectors)):
        pointsArray.append([])
        for x in range(len(vectors[0])):
            pointsArray[y].append([y,x,vectors[y][x],"Undefined"])
            
    #DBSCAN clustering
    clusterCounter = 0
    for y in range(len(vectors)):
        for x in range(len(vectors[0])):
            if pointsArray[y][x][-1] != "Undefined":
                continue
            xk,yk=x,y
            if (xk,yk) in mp.keys():
                Neighbours=mp[(yk,xk)]
            else:
                Neighbours = FindNeighbours(pointsArray[y][x], pointsArray, epsilon)
                mp[(yk,xk)]=Neighbours
            if len(Neighbours) < minpts:
                pointsArray[y][x][-1] = "Noise"
                continue

            clusterCounter = clusterCounter + 1
            pointsArray[y][x][-1] = str(clusterCounter)
            if pointsArray[y][x] in Neighbours:
                Neighbours.remove(pointsArray[y][x])

            for innerPoint in Neighbours:
                if innerPoint[-1] == "Noise":
                    pointsArray[innerPoint[0]][innerPoint[1]][-1] = str(clusterCounter)
                if innerPoint[-1] != "Undefined":
                    continue
                pointsArray[innerPoint[0]][innerPoint[1]][-1] = str(clusterCounter)
                   
    #Get distinct clusters
    clusterNumbers = []
    for y in range(len(vectors)):
        for x in range(len(vectors[0])):
            if pointsArray[y][x][-1] not in clusterNumbers:
                clusterNumbers.append(pointsArray[y][x][-1])
    #Map cluster's averages
    averagesForClusters = []
    for item in clusterNumbers:
        n = 0
        vectorTemps = [0]*len(pointsArray[0][0][2])
        for y in range(len(vectors)):
            for x in range(len(vectors[0])):
                if pointsArray[y][x][-1] == item:
                    for i in range(len(pointsArray[y][x][2])):
                        vectorTemps[i] = vectorTemps[i] + pointsArray[y][x][2][i]
                    n = n + 1
        #Check Zero division
        for i in range(len(vectorTemps)):
            if vectorTemps[i] != 0:
                vectorTemps[i] = vectorTemps[i]/n
        averagesForClusters.append(vectorTemps)
    #Build clustered array and change cluster averages with initial values
    clusteredVectors = []
    for y in range(len(pointsArray)):
        clusteredVectors.append([])
        for x in range(len(pointsArray[0])):
            clusteredVectors[y].append(averagesForClusters[clusterNumbers.index(pointsArray[y][x][-1])])
    end = time.time()
    #Log info
    with open('logger.txt', 'a+') as out:
        out.write(f"""**DBSCAN RESULTS**\n""")
        out.write(f"""Array size: {len(vectors)}x{len(vectors[0])}x{len(vectors[0][0])}\n""")
        out.write(f"""Parameters: Eps: {epsilon}, minPts: {minpts}\n""")
        out.write(f"""Number of identified clusters: {len(clusterNumbers)}\n""")
        out.write(f"""Cluster averages: {str(averagesForClusters)}\n""")
        out.write(f"""Time taken: {round(end - start)} seconds\n""")
            
    return clusteredVectors
