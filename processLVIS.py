
'''
Some example functions for processing LVIS data
'''

#######################################

import numpy as np
from lvisClass import lvisData
from pyproj import Proj, transform


#######################################

class proLVIS(lvisData):
  '''
  LVIS class with extra processing steps
  '''

  def __init__(self,filename,nRead=-1,sInd=0,setElev=1):
    '''
    For now, only calls the inherited initialiser
    class lvisData:
    Class initialiser. Calls a function
    to read "nRead" waveforms, starting 
    at "sInd" from the file, filename
    setElev=1 converts LVIS's stop and start
    elevations to arrays of elevation.
    '''
    super().__init__(filename,nRead=nRead,sInd=sInd,setElev=setElev)


  def meanNoises(self,noiseBins):
    '''
    Calculates mean noise per waveform.
    noiseBins gives the number of bins 
    known to be filled with noise
    '''
    meanNoise=np.zeros((self.nWaves))
    for i in range(0,self.nWaves):          # loop over all waveforms
      z,wave=proLVIS.getOneWave(self,i)     # read waveform
      meanNoise[i]=np.mean(wave[0:noiseBins])  # add mean from slice
    return(meanNoise)


  def reproject(self,inEPSG,outEPSG):
    '''
    Reproject footprint coordinates
    '''
    # set projections
    inProj=Proj(init="epsg:"+str(inEPSG))
    outProj=Proj(init="epsg:"+str(outEPSG))
    # reproject data
    x,y=transform(inProj,outProj,self.lon,self.lat)
    self.lon=x
    self.lat=y
    return

#############################################################
