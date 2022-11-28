# ImageSegmentation
Image Segmentation Using K-means and DBSCAN.

image.png K-means and DBSCAN are clustering algorithms, which we apply for color segmentation in images. image-3.png K-means tries to find a color representatives for a number of classes given, i.e., most average color for each class, which is most similar to the colors within the class but as different as possible from colors in other classes.

DBSCAN is so called density-based clustering algorithm, which tries to group similar colors into different classes based on how densely they are positioned together.

Format k-means and dbscan use following format string (string of 3 dimensional array of size [x,y,n]):

[[[n0,n1,n2,...],[n0,n1,n2,...]],[[n0,n1,n2,...],[n0,n1,n2,...]],...]
Image Segmentation Using Clustering Algorithm
