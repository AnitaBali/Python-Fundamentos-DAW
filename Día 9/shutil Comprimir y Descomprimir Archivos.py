import shutil

#Comprimir
"""carpeta_origen= 'C:\\Users\\LENOVO\\OneDrive\\Escritorio\\Carpeta Superior'

archivo_destino='Todo_Comprimido'

shutil.make_archive(archivo_destino,'zip',carpeta_origen)
"""
#Descomprimir
shutil.unpack_archive('Todo_Comprimido.zip','Extracción_Terminada','zip')
