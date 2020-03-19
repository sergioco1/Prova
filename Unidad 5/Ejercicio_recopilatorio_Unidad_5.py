#ACCEDE A LA CAPA ACTIVA
layer=qgis.utils.iface.mapCanvas().currentLayer()

#EVALUA EL TIPO DE GEOMETRIA TILIZANDO EL METODO .wkbType():
if layer.wkbType()== 1:
 print ('La capa activa es de tipo punto')
 tipoCapa='Point?'
 
elif layer.wkbType()== 5:
 print ('La capa activa es de tipo linea')
 tipoCapa='LineString?'
elif layer.wkbType()== 6:
 print ('La capa activa es de tipo poligono')
 tipoCapa='Polygon?'
else:
 print ('La capa activa tiene otro formato')
 
# obtener información sobre el data provider  para luego con crs()obtener sistema coordenadas
layer_dp=layer.dataProvider()
layer_crs=layer_dp.crs()
#TRANSFORMA EL CRS EN UN STRING
layer_crs_str=layer_crs.authid()
print (layer_crs_str)
#OBTIENE EL NUM DEL IDENTIFICADOR EPGS
layer_EPSG_int=int(layer_crs_str[5:])
print (layer_EPSG_int)

EPGS_code=str(layer_EPSG_int)
print(EPSG_code)
#Esta linea viene en la resolución de Antoni. Claramente hace lo mismo pero más eficientemente
#EPSG_code =int(layer.dataProvider().crs().authid().split(":")[1])

#CREA UNA CAPA EN MEMORIA CON LOS VALORES DE GEOMETRIA Y PROYECCION CAPTURADOS (con el + se concatenan stingas)
destination_layer =QgsVectorLayer(tipoCapa+'crs=epsg:'+str(EPSG_code)+'&index=yes','memory layer','memory') 

layer_attrib_names = layer_dp.fields()
attributeList = layer_attrib_names.toList()
print(attributeList)
#oldattributeList = layer.dataProvider().fields().toList() (es más corto así)
newattributeList=[]
for attrib in attributeList:
    if destination_layer.fields().lookupField(attrib.name())==-1:

        newattributeList.append(QgsField(attrib.name(),attrib.type())) 

#PON EL LISTADO DE CAMPOS EN LA CAPA DESTINO
destination_layer.dataProvider().addAttributes(newattributeList)
destination_layer.updateFields() 
destination_layer_attrib_names = destination_layer.fields()
destination_layer_attributeList = destination_layer_attrib_names.toList()
print(destination_layer_attributeList)

QgsProject.instance().addMapLayer(destination_layer)
print ("HECHO") 

    
    

