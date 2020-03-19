
#IMPORTA EL MODULO re PARA OPERAR CON LA CADENA DE TEXTO
import re
n = -1
#CAPTURA COMO LAYER LA CAPA ACTIVA
layer=qgis.utils.iface.mapCanvas().currentLayer() 
#OBTIENE LA COLECCION DE FEATURES
features=layer.getFeatures()
#RECORRE CADA ELEMENTO DE LA COLECCION
for feature in features:
 n = n + 1 

#CAPTURA LOS EL VALOR DEL CAMPO NAME EN DOS VARIABLES
 nomRio = feature.attribute('NAME')
 numRio = feature.attribute('NAME')
 print (nomRio)
 #RECALCULA LOS VALORES DE NOMBRE Y DE NUMERO A PARTIR DEL CAMPO
 nomRio = re.sub("\d", '', nomRio)
 print (nomRio)
 numRio = re.sub("\D", "", numRio)
 print (numRio)
 #INTRODUCE LOS VALORES NUEVOS EN UN DICCIONARIO ORDEN_CAMPO:VALOR
 attrs = { 4 : nomRio, 5 : numRio }
#CAMBIA LOS VALORES DE LOS CAMPOS INDICADOS EN EL DICCIONARIO
 layer.dataProvider().changeAttributeValues({ n : attrs }) 
 
layer_dp=layer.dataProvider()
layer_att_names = layer_dp.fields().toList()
print(layer_att_names)

