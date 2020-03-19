layer=QgsVectorLayer(r'C:\CURSO_PYQGIS\CAPAS\urbano.shp','urbano','ogr')
#QgsProject.instance().addMapLayer(layer)

##Con dataProvider().subLayers() puedes ver la estructura que usa Qgis para guardar la info de la capa
##En el ejemplo la capa urbano tiene 1 capa (si fuera un geopackage podría tener más como ves abajo), 
##de nombre urbano, con 403 elementos y es de tipo Poligon.

subcapa= layer.dataProvider().subLayers()
print(subcapa)
###################['0!!::!!urbano!!::!!403!!::!!Polygon!!::!!']
## te devuelve una LISTA (mira las parentesis) así si quieres seleccionar parte de la información de la capa puede usar split 
for capa in subcapa:
    name= capa.split('!!::!!')[2]
    print(name)    
#Con el split el sistema te coge todo lo que hay entre los caracteres especificados en las comillas !!::!! en este caso
# y [2] es el segundo elemento de la lista (empieza en 0) 
## Ejemplo: name= '89aa!!::!!aacasaaa!!::!!aa3aa!!::!!aaventaaa!!::!!aamiio'
##namesplit=name.split('aa!!::!!aa')[2]
##print (namesplit)..te devolvería 2 ya que el 0 es 89, el 1 es casa el 2 es 3...etc
#Ojo, si usas cadenas puede usar directamente el split. Si son lista tiene que recorrerla con el for

## LO MISMO SE PUEDE OBTENER CON EL METODO mapCanvas()  (te da algo más de info)
layer=qgis.utils.iface.mapCanvas().currentLayer()
subcapa = layer.dataProvider().subLayers()
print(subcapa)
for capa in subcapa:
    name= capa.split('!!::!!')[4]
    print(name)
# o mapcanvases()
layer2=qgis.utils.iface.mapCanvases()
subcapa2= layer.dataProvider().subLayers()
print(subcapa2)
for capa2 in subcapa2:
    name2= capa2.split('!!::!!')[3]
    print(name2)

#EJEMPLO EN EL CASO DE UN GEOPACKAGE y usos de caracter especial %s

#fileName = 'C:\CURSO_PYQGIS\CAPAS\capas.gpkg'
#layer = QgsVectorLayer(fileName,'carreteras','ogr')
#subcapa = layer.dataProvider().subLayers()
#print(subcapa)
#for capa in subcapa:
#    name = capa.split('!!::!!')[1]
#    print (name)
#    uri = "%s|layername=%s" % (fileName, name,)
#    print (uri)
#    sub_vlayer = QgsVectorLayer(uri, name, 'ogr')
#    QgsProject.instance().addMapLayer(sub_vlayer)

# TAMBIEN SE PUEDE PEDIR el nombre DE LOS CAMPOS O SUBCAPAS CON FIELDS() pero hay que decir de ponerlo en una lista
#sino te da la referencia interna del objeto
layer_attrib_name=layer.dataProvider().fields().toList()
print(layer_attrib_name)


