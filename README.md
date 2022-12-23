# Image Segmentation using K-means and DBSCAN
![image](https://user-images.githubusercontent.com/29672160/208297729-0bf1eaf9-b4f2-4458-8215-3b09b4d33a31.png)

Two Approaches:<br>
1:Generic Approach(Main) :All Data get Flattened/Reshaped and is fed into the clustering module. Works well with all data.<br>
2:Image Specific approach: Works only for Image data, using following format string (string of 3 dimensional array of size [x,y,n]):

For a local installation, make sure you have pip installed and run:<br>
$ pip install notebook 
# Note: Use conda environment to ease up the setup and future environment setups.
    conda create --name <envname> --file requirements.txt
    conda activate testing
Install the necessary dependencies:<br>
     $ python -m pip install -r requirements.txt

Running in a local installation
Launch with:<br>
     $ jupyter notebook

Then you can navigate into the folder `ImageSegmentation/` and upload ImageSegmentation.ipynb, ImageSegmentationGeneric.ipynb, clustering_algorithms_generic.py and clustering_algorithms.py in to jupyter
Run Each cells in ImageSegmentation.ipynb and ImageSegmentationGeneric.ipynb one by one and observe.

Note: Image feeding is possible with 2 methods in-program feeding and if using google colab file upload is also a given, choose based on context.
>>>
`K-means` and `DBSCAN` are clustering algorithms, which we apply for color segmentation in images.

K-means tries to find a color representatives for a number of classes given, i.e., most average color for each class, which is most similar to the colors within the class but as different as possible from colors in other classes.

![image](https://user-images.githubusercontent.com/29672160/208297759-7c5d0140-25e2-4075-8470-015edd78cf5e.png)

DBSCAN is so called density-based clustering algorithm, which tries to group similar colors into different classes based on how densely they are positioned together.

![image](https://user-images.githubusercontent.com/29672160/208297777-fb7974c8-1172-4d4e-86fd-4be2adf8e24d.png)

`logger.txt` is given to get clustering information, including the computational time information.


# Files
   clustering_algorithms.py - Container for Kmeans and DBScan   
   logger.txt - contains clustering information for pictures<br>
   Images/x.jpg - Images used for segmentation, Custom Image Feeding is possible with browse through.
   Iris.csv - Verification Purpose the clustering methods works with any data

# Dependencies
   All packages/libraries should be included in Python 3.9.13

# Limitations
   # Image Specific Approach
    Image generation with works only for 3 or 4 channel models i.e. RGB (.jpg) or RGBA (.png)


# Format
   # Main Approach
    All Data get Flattened/Reshaped and is fed into the clustering module.
   
   # Image Specific Approach
    k-means and dbscan use following format string (string of 3 dimensional array of size [x,y,n]):
   
    [[[n0,n1,n2,...],[n0,n1,n2,...]],[[n0,n1,n2,...],[n0,n1,n2,...]],...]  



# Copyright
   All the images were taken from internet and therefore belong to their respective owners.

# Some Observations.
Computation Time Depends on size of image and hyperparameter tuning.
 # Image Specific Approach
    * Image with dimension 2000x1500 pixels have a computation time of 50-70 seconds for DBscan and 4-5 mins for k-means.
    * for an image of 300x168 pixels have a computation time of 1-3 seconds for DBscan and 3-8 seconds for k-means.
    * Image file with dimensions 1000x1500 pixels, Time taken for DBScan 17 Seconds, Time taken for Kmeans 221 Seconds
    * Image file with dimensions 2520x1184 pixels, Time taken for DBScan 47 Seconds, Time taken for Kmeans 465 Seconds
Works well with small images, and does cluster other type of data.
