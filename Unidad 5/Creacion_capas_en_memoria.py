#CAPA DE PUNTOS
mem_layer_ptos =QgsVectorLayer("Point?crs=epsg:4326&field=id:integer""&field=nombre:string&index=yes", "capa_memory_ptos", "memory")
#CAPA DE LINEAS
mem_layer_line =QgsVectorLayer("LineString?crs=epsg:4326&field=id:integer""&field=longitud:double&index=yes", "capa_memory_line", "memory")
#CAPA DE POLIGONOS 
mem_layer_poly =QgsVectorLayer("Polygon?crs=epsg:4326&field=id:integer""&field=area:double&index=yes","capa_memory_polig", "memory")
#CARGA LAS CAPAS EN LA TOC
QgsProject.instance().addMapLayer(mem_layer_ptos)
QgsProject.instance().addMapLayer(mem_layer_line)
QgsProject.instance().addMapLayer(mem_layer_poly) 
# mostrar los atributos de la capa en memoria
layer=qgis.utils.iface.mapCanvas().currentLayer()
layer_dp=layer.dataProvider()
layer_attrib_names = layer_dp.fields()
#CONVIERTE EL GRUPO DE CAMPOS (fields) EN UN LISTADO
attributeList = layer_attrib_names.toList()
print(attributeList)
for field in attributeList:
 print ("Orden: %s, Nombre: %s, Tipo: %s, Longitud: %s" % (
layer.fields().lookupField(field.name()), field.name(),
field.typeName(), field.length()))
