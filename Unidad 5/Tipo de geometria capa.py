#ACCEDE A LA CAPA ACTIVA
layer=qgis.utils.iface.mapCanvas().currentLayer()
#CONDICION IF - ELIF QUE EVALUA EL TIPO DE GEOMETRIA
#UTILIZANDO EL METODO .wkbType():
if layer.wkbType()== QgsWkbTypes.Point:
 print ('La capa activa es de tipo punto')
elif layer.wkbType()==QgsWkbTypes.MultiLineString:
 print ('La capa activa es de tipo linea')

elif layer.wkbType()==QgsWkbTypes.MultiPolygon:
 print ('La capa activa es de tipo poligono')

else:
 print ('La capa activa tiene otro formato')