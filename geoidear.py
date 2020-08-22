from pyproj import transform, Proj
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
        converted = []
        for i in self.dataList: 
            converted.append(self.convert(i))
        return converted

    def convert(self, dlist):

        lat = dlist[0]
        lon = dlist[1]

        # Si no hay elevación como parámetro, lo establecemos como 0
        elev = dlist[2] if len(dlist) > 2 else 0

        _lon, _lat, _elev = transform(WGS84, self.targetEPSG, lon, lat, elev)
        
        # Redondeamos elevación en el tercer decimal igual que en la calculadora original
        _elev = round(_elev,3)

        return [round(_lat,6), round(_lon,6), _elev] 
    
    def createListFromString(self, data):
        data = data.replace(',', ' ')
        data = data.splitlines()
        dataList = []
        for line in data:
            dataList.append(line.split())
        return dataList
