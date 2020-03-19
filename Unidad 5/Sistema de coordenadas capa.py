#ACCEDE A LA CAPA ACTIVA
layer=qgis.utils.iface.mapCanvas().currentLayer()
#ACCEDE AL DATA PROVIDER DE LA CAPA
layer_dp=layer.dataProvider()
#METODO crs() SOBRE EL DATA PROVIDER
layer_crs=layer_dp.crs()
#imprime la referencia interna del layer
print(layer_crs)
#TRANSFORMA EL CRS EN UN STRING
layer_crs_str=layer_crs.authid()
print (layer_crs_str)
#OBTIENE EL NUM DEL IDENTIFICADOR EPGS
layer_EPSG_int=int(layer_crs_str[5:])
print (layer_EPSG_int) 