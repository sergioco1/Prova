#CAPTURA COMO LAYER LA CAPA ACTIVA LA PREPARA PARA EDITAR
layer=qgis.utils.iface.mapCanvas().currentLayer()
layer.startEditing() 
#CREA UN FEATURE
feat = QgsFeature()
#APORTA LA GEOMETRIA AL FEATURE A TRAVES DE UN QGSPOINT
feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(-92,37)))
#APORTA LOS ATRIBUROS DE LA LISTA AL FEATURE
feat.setAttributes(["MiCiudad","Estados Unidos"])
#INTRODUCE EL FEATURE DENTRO DE LA CAPA A TRAVES DEL DATAPROVIDER
layer.dataProvider().addFeatures( [ feat ] )
#CIERRA EDICION GUARDANDO CAMBIOS
layer.commitChanges() 