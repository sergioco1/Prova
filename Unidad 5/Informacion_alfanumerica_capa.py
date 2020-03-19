#ACCEDE A LA CAPA ACTIVA
layer=qgis.utils.iface.mapCanvas().currentLayer()
#CUENTA Y MUESTRA EL NUMERO DE ELEMENTOS DE LA CAPA
print ('la capa tiene %s elementos' % (layer.featureCount()))
#ACCEDE AL DATA PROVIDER DE LA CAPA Y OBTIENE CON EL LOS CAMPOS DE LA CAPA
layer_dp=layer.dataProvider()
layer_attrib_names = layer_dp.fields()
# imprime el objeto creado. NOTA BIEN. ES UN OBJETO DE LA CLASE QgsField ya que field() es un METODO
#de esta clase ES IMPORTANTE QUE VEAS QUE ESTE VALOR SE GRABA CON SU REFERENCIA 
print(layer_attrib_names)
#CONVIERTE EL GRUPO DE CAMPOS (fields) EN UN LISTADO
attributeList = layer_attrib_names.toList()
print(attributeList)
#RECORRE EL LISTADO DE CAMPOS Y PARA CADA UNO MUESTRA SU INFORMACION CON UN BUCLE FOR
for field in attributeList:
 print ("Orden: %s, Nombre: %s, Tipo: %s, Longitud: %s" % (
layer.fields().lookupField(field.name()), field.name(),
field.typeName(), field.length()))
 #EVALUA EL TIPO DE CAMPO,SI ES ENTERO MUESTRA SU MAXIMO VALOR
 if field.typeName() == 'Integer':
    print (layer.maximumValue(layer.fields().lookupField(field.name()))) 