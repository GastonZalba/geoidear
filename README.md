# geoidear
API implementada en Python que emula el funcionamiento de la [calculadora online GEOIDE-AR 16](https://www.ign.gob.ar/NuestrasActividades/Geodesia/Geoide-Ar16/calculadora) del Intituto Geográfico Nacional (IGN). Esta aplicación surge ante la falta de una API oficial que permita hacer las conversiones programáticamente sin utilizar el formulario online.

[Visitar el sitio](https://geoidear.herokuapp.com) para ver implementación de la aplicación y su documentación.

Para las conversiones se utiliza [pyproj](https://pypi.org/project/pyproj/) (que interpreta la biblioteca [PROJ](https://proj.org/)), y el geoide Geoide-ar16 convertido a formato gtx a partir de los que ofrece el IGN de manera online [aquí](https://www.ign.gob.ar/NuestrasActividades/Geodesia/Geoide-Ar16/DocumentacionTecnica).

Según el sitio del IGN la herramienta `permite la determinación de ondulaciones geoidales de puntos localizados sobre la superficie de la República Argentina. Estas ondulaciones permitirán transformar alturas elipsoidales referidas al Marco de Referencia Geodésico Nacional POSGAR07 en alturas ortométricas referidas al Sistema de Referencia Vertical Nacional 2016 (SRVN16) exclusivamente.`

También se añade la posibilidad de: 
- convertir las coordenadas suministradas (EPSG:4326) a valores POSGAR07.
- ingresar un tercer parámetro en cada entrada con la elevación, obtienendo como resultado la diferencia de altura aplicada a ese valor. Si la elevación no es suministrada, se devuelve simplemente la diferencia entre la altura elipsoidal y la ortométrica en esas coordenadas.
- diferentes modos de carga en el formulario, pudiéndose separar los campos por espacios, tabs o comas.
- exportar el resultado directamente en un archivo CSV.

## Requerimientos
- Python > 3
- [pyproj](https://pypi.org/project/pyproj/) >= 2
- [numpy](https://pypi.org/project/numpy/)
- [Flask](https://pypi.org/project/Flask/)
- [gunicorn](https://pypi.org/project/gunicorn/)
- [flask-talisman](https://pypi.org/project/flask-talisman-rdil/)