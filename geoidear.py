from pyproj import transform, Proj
import numpy as np
import json

WGS84 = Proj(init="EPSG:4326") #WGS84 datum ellipsoid height

class Geoidear():

    def __init__(self, data, epsg='EPSG:4326'):

        self.targetEPSG = Proj(init=epsg, geoidgrids='./geoidear-16/geoidear16.gtx')
        try:
            data = json.loads(data)
        except:
            data = self.createListFromString(data)
        finally:
            self.dataList = data

    def processList(self):

        _lon, _lat, _elev = transform(WGS84, self.targetEPSG, self.dataList[:,1], self.dataList[:,0], self.dataList[:,2])
        
        # Redondeamos valores igual a la calculadora original
        _elev = np.around(_elev, 3)
        _lat = np.around( _lat, 6)
        _lon = np.around(_lon, 6)

        return np.dstack([_lat,_lon,_elev])[0] 
    
    def createListFromString(self, data):
        data = data.replace(',', ' ')
        data = data.splitlines()
        dataList = []
        for line in data:
            values = line.split()
            if len(values) < 3:
                #si no hay elevación, la establecemos como 0
                values.append(0)
            dataList.append(values)
        return np.array(dataList)
