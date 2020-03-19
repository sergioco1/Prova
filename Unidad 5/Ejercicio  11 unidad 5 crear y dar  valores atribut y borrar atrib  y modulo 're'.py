#IMPORTA EL QVARIANT NECESARIO PARA CREAR UN CAMPO QgsField
from PyQt5.QtCore import QVariant
#CAPTURA COMO LAYER LA CAPA ACTIVA
layer = qgis.utils.iface.mapCanvas().currentLayer()
#ACCEDE AL DATAPROVIDER Y CREA LOS CAMPOS DE LA LISTA
layer.dataProvider().addAttributes( [ QgsField("NOMBRE",
QVariant.String), QgsField("NUMERO", QVariant.Int) ] )
#ACTUALIZA LA CAPA
layer.updateFields()

#IMPORTA EL MODULO re PARA OPERAR CON LA CADENA DE TEXTO
import re
n = -1
#CAPTURA COMO LAYER LA CAPA ACTIVA
layer=qgis.utils.iface.mapCanvas().currentLayer()
#OBTIENE LA COLECCION DE FEATURES
features = layer.getFeatures()
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
# OJO, RECORRE LA LISTA UNO A UNO. SI NO LO PONES TODOS INDEXADO NO PEGA LOS VALORES YA
# QUE TE SALES DEL BUCLE FOR. NO ES NECESARIO PONER EL MÉTODO updateFeature()
layer.dataProvider().deleteAttributes([1,2])
## si lanza este te borra los valores del campo pero no los atributos. con el de abajo borras los atributos
layer.updateFields()