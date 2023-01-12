# Code concept by Rahul Ramakrishnan
import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy
import random


# DbScan Helpers
def expand_cluster(neigbouring_points,min_pts,epilson,visited_index,DistanceMatrix,cluster_index,cluster_count):
    neigbouring_points = list(neigbouring_points)
    for i in neigbouring_points:
        if visited_index[i]==0 or visited_index[i]==-1:
            visited_index[i]=1
            neighbours = np.where(DistanceMatrix[i]<epilson)[0]
            if len(neighbours)>=min_pts:
                for j in neighbours:
                    # try inserting to array if element does exist we wont continue 
                    # else wil will add
                    try:
                        neigbouring_points.index(j)
                    except:
                        neigbouring_points.append(j)
            # we have to change here
            
            if cluster_index[i] == -1:
                cluster_index[i]=cluster_count
    return cluster_index,visited_index

def dbscan(vectors,epilson,min_pts):
    
    DistanceMatrix = scipy.spatial.distance.squareform(scipy.spatial.distance.pdist(vectors, 'euclidean'))
    new_shape = len(vectors)
    # let us mark 0 for unvisited
    # 1 - visited
    # -1 for noise
    visited_index = np.zeros((new_shape))
    cluster_index = np.empty((new_shape))
    cluster_index.fill(-1)
    cluster_count=-1
    for i in range(new_shape):
        if visited_index[i] ==0:
            visited_index[i]=1
            # find neigbours
            core_neigbouring_points = np.where(DistanceMatrix[i]<epilson)[0]
            
            if len(core_neigbouring_points)<min_pts:
                visited_index[i]=-1

            else:
                #pop all elements in cluster for new core point
                cluster_count+=1
                cluster_index[i]= cluster_count
                cluster_index,visited_index = expand_cluster(core_neigbouring_points,min_pts,epilson,visited_index,DistanceMatrix,cluster_index,cluster_count)

    
    return cluster_index

# K-Means Helpers

def find_cluster_points(centerPoints,vectors):
    
    distance_mapping = None
    for count,centre_point in enumerate(centerPoints):
        #get distance array
        if distance_mapping is None:
            
            distance_mapping = np.array([np.sum(abs(vectors - centre_point)**2,axis=1)])
        else:
            distance_mapping = np.concatenate((distance_mapping,np.array([np.sum(abs(vectors - centre_point)**2,axis=1)])))

    return np.argmin(distance_mapping,axis=0)

def get_new_centerPoints(vectors,cluster_mapping,centerPoints):
    len_centerPoints = len(centerPoints)
    cluster_centroid={}
    for i in range(len_centerPoints):
        cluster_centroid[i]=[]

    no_of_ele, = cluster_mapping.shape
    for r in range(no_of_ele):
        cluster_centroid[cluster_mapping[r]].append(vectors[r])

    new_centerPoints=[]
    for i in range(len_centerPoints):
        temp_arr = np.array(cluster_centroid[i])
        var = np.mean(temp_arr,axis=0,dtype=np.int32)
        new_centerPoints.append(var)
    return np.array(new_centerPoints)


def run_kmeans(vectors: list, kVal:int) -> list:
    #choose k initial random unequal points
    centerPoints = np.array([random.choice(vectors)],dtype=np.int32)
    row,depth = centerPoints.shape
    while len(centerPoints) != kVal:
        candidate = random.choice(vectors)
        if not np.isin(candidate,centerPoints).all() :
            #change here for n-dimensional data
            centerPoints = np.concatenate((centerPoints.reshape(-1,depth,),candidate.reshape(1,depth,)))

    while True:
        #get cluster of each pixel
        cluster_mapping = find_cluster_points(centerPoints,vectors)
        #find new clusters
        new_centerPoints = get_new_centerPoints(vectors,cluster_mapping,centerPoints)
        if np.isin(new_centerPoints,centerPoints).all() :
            break
        centerPoints = new_centerPoints    
    return cluster_mapping
