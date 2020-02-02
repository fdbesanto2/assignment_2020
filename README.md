# OOSA Assignment 2020

This contains the files needed for the 2020 OOSA assignment. LVIS data can be downloaded from [here](https://lvis.gsfc.nasa.gov/Data/Data_Download.html).  We will be using files from [Operation IceBridge](https://www.nasa.gov/mission_pages/icebridge/index.html), which bridged the gap between ICESat and ICESat-2 using aircraft.


## lvisClass.py

A class to handle LVIS data. This class reads in LVIS data from a HDF5 file, stores it within the class, converts from the compressed elevation format and can return a selected waveform as a numpy array. Note that LVIS data is stored in WGS84 (EPSG:4326).

The class is:

**lvisData**

The data is stored as the variables:

    waves:   Lidar waveforms as a 2D numpy array
    lon:     Longitude as a 1D numpy array
    lat:     Latitude as a 1D numpy array
    nWaves:  Number of waveforms in this file as an integer
    nBins:   Number of bins per waveform as an integer
    lZN:     Elevation of the bottom waveform bin
    lZ0:     Elevation of the top waveform bin
    lfid:    LVIS flight ID integer
    shotN:   LVIS shot number for this flight


The data should be read as:

    from lvisClass import lvisData
    x=lvisData(filename)


There is an optional spatial subsetter for when dealing with large datasets.

    x=lvisData(filename,minX=x0,minY=y0,maxX=x1,maxX=x1)

Where (x0,y0) is the bottom left coordinate of the area of interest and (x1,y1) is the top right.

To help choose the bounds, the bounds only can be read from tbe file to save time and RAM:

    lvisData(filename,onlyBounds=True)


The elevations can be set on reading:

    x=lvisData(filename,seteElev=True)

Or later by calling the method:

    x.setElevations()




The class includes the methods:

* setElevations(): converts the compressed elevations in to arrays of elevation, z.
* getOneWave(ind): returns one waveform as an array
* dumpCoords():    returns all coordinates as two numpy arrays
* dumpBounds():    returns the minX,minY,maxX,maxY


### Usage example

    # import and read bounds
    from lvisClass import lvisData
    bounds=lvisData(filename,onlyBounds=True)
    # set bounds
    x0=bounds[0]
    y0=bounds[1]
    x1=(bounds[2]-minX)/2+minX
    y1=(bounds[3]-minY)/2+minY
    # read data
    x=lvisData(filename,minX=x0,minY=y0,maxX=x1,maxY=y1)
    x.setElevations()

This will find the data's bounds, read the bottom left quarter of it in to RAM, then set the elevation arrays. The data is now ready to be processed


## processLVIS.py

Includes a class with methods to process LVIS data.

