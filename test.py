from geoidear import Geoidear
import json

with open('test/data.json') as f:
    data = json.load(f)
    geoidear = Geoidear(data, 'EPSG:5348')
    print(geoidear.processList())


# Valores de Ejemplo que aparecen en IGN
# Latitud    Longitud   N (m)
# -35.41433	-60.14175	17.699
# -35.40661	-60.77244	17.817
# -37.87528	-62.88564	16.720
# -34.43196	-61.07527	18.048
# -35.43826	-62.98717	18.748
# -36.58201	-62.11748	17.483