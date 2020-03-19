from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
#IMPORTA EL QVARIANT NECESARIO PARA CREAR UN CAMPO QgsField
from PyQt5.QtCore import QVariant



layer=qgis.utils.iface.mapCanvas().currentLayer() 
# observa los campos de la capa activa y sus elementos
layer_dp=layer.dataProvider()
layer_att_names = layer_dp.fields().toList()
print(layer_att_names)
print ('la capa tiene %s elementos' % (layer.featureCount()))

#ACCEDE AL DATAPROVIDER Y CREA Un CAMPO NUEVO DE TIPO DOUBLE
layer.dataProvider().addAttributes( [ QgsField("ScaleRank2",QVariant.Double) ] )
layer.updateFields()

#OBSERVA QUE SE HA CREADO EL CAMPO (OJO, a pesar de verlo en la lista NO SE GRABA SI NO PONES layer.updateFields() 
layer_dp=layer.dataProvider()
layer_att_names = layer_dp.fields().toList()
print(layer_att_names)
print ('la capa tiene %s elementos' % (layer.featureCount()))

# copia los valores de CADA ELEMENTO DESDE scalerank a scalerank2
features=layer.getFeatures()
n=-1
for feature in features:
    n=n+1
    Valor_n_ScaleRank = feature.attribute('ScaleRank')
    attrs = { 6 : Valor_n_ScaleRank }
#    print(attrs)
#CAMBIA LOS VALORES DE LOS CAMPOS INDICADOS EN EL DICCIONARIO
    layer.dataProvider().changeAttributeValues({ n : attrs }) 
# SI NO LO ACTUALIZA NO TE COPIA LOS VALORES EN LA TABLA.
layer.updateFields()

layer_att_names = layer.dataProvider().fields().toList()
print(layer_att_names)

#BORRA EL SCALE RANK ANTIGUO
layer.dataProvider().deleteAttributes([0])
layer_att_names = layer.dataProvider().fields().toList()
print(layer_att_names)
##ACTUALIZA LA CAPA )ESTO NO SIRVE. AQUI SE ACTUALIZA SOLO!!!!
#layer.updateFields() 

#cambia el nombre a ScaleRank2 to ScaleRank para que sea igual al de la capa Rios
# EN ESTE CASO SI NO HACE START EDITING AND COMMITEDIT NO TE HACE EL CAMBIO PORQUE 
#ES NECESARIO ENTRAR EN MODO EDICCIÓN. 
layer.startEditing()
layer.renameAttribute(5,'ScaleRank')
layer.commitChanges()
layer_att_names = layer.dataProvider().fields().toList()
print(layer_att_names)

#esto sirve para importar las funciones de la Caja de Herramienta de procesado de Qgis
import processing
# si quieres ver el nombre de todos los algoritmos de la Caja de herramienta digita
#for alg in QgsApplication.processingRegistry().algorithms(): print(alg.id()) 
# y aquí buscas los que hacen merge
#for alg in QgsApplication.processingRegistry().algorithms():
#    if 'merge' in alg.id():
#        print(alg.id()) 
#para la sintaxis usa 
#processing.algorithmHelp('saga:mergevectorlayers')
nom_layer_carret = r'C:/CURSO_PYQGIS/CAPAS/carreteras.shp'
nom_layer_rios = r'C:/CURSO_PYQGIS/CAPAS/rios.shp'
nom_resultado =r'C:/CURSO_PYQGIS/CAPAS_PROCESADAS/elementos_lineales.shp'
parameters ={'LAYERS':[nom_layer_carret,nom_layer_rios],'CRS':'EPSG:4326','OUTPUT':nom_resultado}
feedback = QgsProcessingFeedback()
processing.runAndLoadResults('native:mergevectorlayers',parameters,feedback=feedback)




