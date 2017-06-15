import os
import sys
from PIL import Image

rootdir = sys.argv[1]
slicefolders = []
labelfolders = []
#print("label maker started...walking over {} \n".format(rootdir))

#rootdir = raw_input("please input path name.\n")
#print("walking over {}".format(rootdir))

#for root, subdirs, filenames in os.walk(rootdir):
#	print("subdir: {}".format(subdirs))
#	print("files: ".format(filenames))

#creates the folders for the label files

def createLabelFolders():
        print("creating label folders.")
	for root, dirs, files in os.walk(rootdir):
                if not dirs:
                        slicefolders.append(root)

	for folder in slicefolders:
		folderbase = os.path.basename(folder)
                #a,foldername = folderbase.split("segmentation_")
                labelsfolder = os.path.join(folder,folderbase + "_labels")
		if not os.path.exists(labelsfolder):
                        #print("making {}".format(labelsfolder))
                        labelfolders.append(labelsfolder)
                        os.makedirs(labelsfolder)
        print("labelfolders made.")
#        print("SLICEFOLDERS:")
#        for f in slicefolders:
#            print(f)
#        print("LABELFOLDERS SIZE OF {}".format(len(labelfolders)))
#        for f in labelfolders:
#            print(f)


"""
If target-color is equal to replacement-color, return.
 2. If the color of node is not equal to target-color, return.
 3. Set the color of node to replacement-color.
 4. Perform Flood-fill (one step to the south of node, target-color, replacement-color).
    Perform Flood-fill (one step to the north of node, target-color, replacement-color).
    Perform Flood-fill (one step to the west of node, target-color, replacement-color).
    Perform Flood-fill (one step to the east of node, target-color, replacement-color).
 5. Return.
"""
def recFloodFill(pix, fromC, x, y, checkColor, border):
    if(x >= border[0] or x < 0 or y >= border[1] or y < 0):
        return pix
    elif fromC != pix[x,y]:
        return pix
    else:
        #print("{},{}".format(x,y))
        pix[x,y] = checkColor
        recFloodFill(pix, fromC, x, y + 1, checkColor, border)#south
        recFloodFill(pix, fromC, x, y - 1, checkColor, border)#north
        recFloodFill(pix, fromC, x + 1, y, checkColor, border)#east
        recFloodFill(pix, fromC, x - 1, y, checkColor, border)#west
 #pix[x,y] = value # Set the RGBA Value of the image (tuple)
    return pix
"""
1. If target-color is equal to replacement-color, return.
2. If color of node is not equal to target-color, return.
3. Set Q to the empty queue.
4.  Set the color of node to replacement-color.
5. Add node to the end of Q.
6. While Q is not empty:
7.     Set n equal to the first element of Q.
8.     Remove first element from Q.
9.     If the color of the node to the west of n is target-color,
                  set the color of that node to replacement-color and add that node to the end of Q.
10.     If the color of the node to the east of n is target-color,
                 set the color of that node to replacement-color and add that node to the end of Q.
11.    If the color of the node to the north of n is target-color,
                 set the color of that node to replacement-color and add that node to the end of Q.
12.    If the color of the node to the south of n is target-color,
                 set the color of that node to replacement-color and add that node to the end of Q.
13. Return.

#==================================================================================================
"""
# Pure Python, usable speed but over 10x greater runtime than Cython version
def fill(data, fromC, start_coords, fill_value, bounds):
    xsize, ysize = bounds
    orig_value = fromC
    stack = set(((start_coords[0], start_coords[1]),))

    if fill_value == orig_value:
       raise ValueError("Filling region with same value "
                        "already present is unsupported. "
                        "Did you already fill this region?")

    while stack:
        x, y = stack.pop()

        if data[x, y] == orig_value:
            data[x, y] = fill_value
            if x > 0:
                stack.add((x - 1, y))
            if x < (xsize - 1):
                stack.add((x + 1, y))
            if y > 0:
                stack.add((x, y - 1))
            if y < (ysize - 1):
                stack.add((x, y + 1))
    return data
#==================================================================================================
def writeToFile(data, filename):
    f = open(filename,"w+")
    for d in data:
            #print '{} {} {}\n'.format(d[0],d[1],d[2])
            f.write("{} {} {}\n".format(d[0],d[1],d[2]))
    f.close()

""" OLD WRITE TO FILE
def writeToFile(data, filename):
    f = open(filename,"w+")
    #write labelData to file path
    lastRgbInt = -1
    for d in data:
        if lastRgbInt == d[0]:
            f.write("[{}],".format(d))
        else:
            lastRgbInt = d[0]
            f.write("\n[{}],".format(d))
    f.close()
"""


"""
====labelCollector====
labels = []
checkedColor = (255,0,0)
for each pixel in slice
get pixel color
if pixel color not = to check color
    then: add pixel color -> location to labels
    floodfill at (location of pixcolor) on (pixelcolor) with (checkedcolor)

return labels

"""
def getIntFromRGB(rgb):
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    #print red, green, blue
    RGBint = (red<<16) + (green<<8) + blue
    return RGBint

def labelCollector(slice):
    labels = []
    checkColor = (255,0,0)
    img = Image.open(slice)#open slice
    pix = img.load()
    width,height = img.size #Get the width and hight of the image for iterating over
    for x in range(0, width):
        for y in range(0, height):
            color = pix[x,y]
            if color != checkColor:
                labels.append((getIntFromRGB(color), x, y))# RGBINT, x, y
                pix = fill(pix, color, (x,y), checkColor, img.size)
    #img.save("testOutput.png") # Save the modified pixels as png
    return sorted(labels)
"""
====createLabelFiles====
 for each label folder \
 go one directory up \
 get all the files in that directory \
 filter for just pngs \
 run labelcollector on each png
 save the output of labelcollector to labelfolder with the name of the png + labels
"""

#creates the data files for the labels
def createLabelFiles():
        print("create label files.")
        for labelfolder in labelfolders:#for each folder label
            slicefolder,b = labelfolder.rsplit('/', 1)
            potentialslices = []
            for (dirpath, dirnames, filenames) in os.walk(slicefolder): #get all files in above dir
                potentialslices.extend(filenames)
                #print("|")
                break
            slices = []#holds all the pngs
            for s in potentialslices: # filter for pngs
                if s.endswith("png"):
                    slices.append(s)
            #run labelcollector on each slice in slices
            for slice in slices:
                labelfilename,a = slice.split(".png")
                sliceFilePath = os.path.join(dirpath, os.path.basename(dirpath) + "_labels")
                labelFilePath = os.path.join(sliceFilePath, labelfilename + "_labels.txt")
                labelData = labelCollector(os.path.join(dirpath, slice) )#gets label data
                writeToFile(labelData, labelFilePath)
        print("created label files.")
#creates the labels
#def createLabels(root, files):



def main():
        #data = labelCollector("/home/liam/Desktop/test.png")
        #print(data)
        createLabelFolders()
        createLabelFiles()
        print("Done!")

#if __name__== "__main__"
main()
