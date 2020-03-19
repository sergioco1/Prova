#IMPORTA EL QVARIANT NECESARIO PARA CREAR UN CAMPO QgsField
from PyQt5.QtCore import QVariant
#CAPTURA COMO LAYER LA CAPA ACTIVA
layer = qgis.utils.iface.mapCanvas().currentLayer()
#ACCEDE AL DATAPROVIDER Y CREA LOS CAMPOS DE LA LISTA
layer.dataProvider().addAttributes( [ QgsField("NOMBRE",
QVariant.String), QgsField("NUMERO", QVariant.Int) ] )
#ACTUALIZA LA CAPA
layer.updateFields()
