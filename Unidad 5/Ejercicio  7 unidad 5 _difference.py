for alg in QgsApplication.processingRegistry().algorithms():
    if 'difference' in alg.id():
        print(alg.id()) 
#para la sintaxis usa 
processing.algorithmHelp('native:difference')

import processing
#CAPAS DE ENTRADA
layer_ciudades = r'C:\CURSO_PYQGIS\CAPAS\ciudades.shp'
layer_z_estudio = r'C:\CURSO_PYQGIS\CAPAS\zona_estudio.shp'
layer_ciudades_fuera = r'C:\CURSO_PYQGIS\CAPAS_PROCESADAS\ciudades_fuera_03.shp'
#PARAMETROS 
parameters = {'INPUT': layer_ciudades, 'OVERLAY': layer_z_estudio,'OUTPUT': layer_ciudades_fuera}
feedback = QgsProcessingFeedback()
#PROCESO
processing.runAndLoadResults('native:difference', parameters, 
feedback=feedback) 
