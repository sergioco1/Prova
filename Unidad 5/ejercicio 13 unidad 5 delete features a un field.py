# CAPTURA COMO LAYER LA CAPA ACTIVA Y LA PREPARA PARA EDITAR
layer=qgis.utils.iface.mapCanvas().currentLayer()
layer.startEditing()
#CREA UNA LISTA DE LAS CIUDADES A ELMINAR 
ListaBorra = ["Topeka","Tulsa","Tupelo"]
#ACCEDE AL CONJUNTO DE FEATURES Y LOS RECORRE UNO A UNO
for feature in layer.getFeatures():
#COMPARA EL NOMBRE DEL FEATURE CON EL DE LA LISTA
   if feature['NAME'] in ListaBorra:
 #BORRA EL FEATURE COINCIDENTE
        layer.deleteFeature(feature.id())
#CIERRA EDICION GUARDANDO CAMBIOS
layer.commitChanges() 