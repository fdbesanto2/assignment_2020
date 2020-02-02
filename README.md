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

The elevations can be set on reading:

   xlvisData(filename,seteElev=True)



Where (x0,y0) is the bottom left coordinate of the area of interest and (x1,y1) is the top right.


The class includes the methods:

* setElevations(): converts the compressed elevations in to arrays of elevation, z.
* getOneWave(ind): returns the 
* 

### Usage example

