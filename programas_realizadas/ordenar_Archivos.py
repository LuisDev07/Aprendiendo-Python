from PIL import Image 
import os

rutaactual = os.path.dirname(os.path.abspath(__file__))

def formatruta(ruta):
    clean =""
    for caracter in ruta:
        if caracter == '\\':
            clean = clean + '/'
        
        else:
            clean =clean + caracter
    return clean


descargasfolder= formatruta(rutaactual)+  "/"

carpeta_padre = descargasfolder + '/archivos_Organizados'
carpeta_imagenes = descargasfolder + '/archivos_Organizados/IMAGENES'
carpeta_audios = descargasfolder + '/archivos_Organizados/AUDIO'
carpeta_videos = descargasfolder + '/archivos_Organizados/VIDEO'

carpeta_exel = descargasfolder + '/archivos_Organizados/PROGRAMAS'
carpetar_rar = descargasfolder + '/archivos_Organizados/ARCHIVOS RAR ZIP'
carpeta_word = descargasfolder +'/archivos_Organizados/DOCUMENTOS WORD'

carpeta_pdf = descargasfolder + '/archivos_Organizados/ARCHIVOS PDF'


os.mkdir(carpeta_padre)
os.mkdir(carpeta_imagenes)
os.mkdir(carpeta_audios)
os.mkdir(carpeta_videos)

os.mkdir(carpeta_exel )
os.mkdir(carpetar_rar)
os.mkdir(carpeta_word)

os.mkdir(carpeta_pdf)

if __name__ =="__main__":
    for filename in os.listdir(descargasfolder):
        name,extensiones = os.path.splitext(descargasfolder + filename)

        if extensiones in [".jpg", ".png"]:
            pictures = Image.open(descargasfolder + filename)
            pictures.save(carpeta_imagenes + '/' + "cinoressed_" + filename, optimized = True,  quality = 60 )
            os.remove(descargasfolder + filename)

        if extensiones in [".mp3"]:
            os.rename (descargasfolder +  filename , carpeta_audios + "/" + filename)

        if extensiones in [".mp4"]:
            os.rename (descargasfolder +  filename , carpeta_videos + "/" + filename)
           

        if extensiones in [".exe"]:
            os.rename (descargasfolder +  filename , carpeta_exel + "/" + filename)

        if extensiones in [".rar", ".zip" ]:
            os.rename (descargasfolder +  filename , carpetar_rar + "/" + filename)

        if extensiones in [".docx"]:
            os.rename (descargasfolder +  filename , carpeta_word + "/" + filename)

    
        if extensiones in [".pdf" ]:
            os.rename (descargasfolder +  filename , carpeta_pdf + "/" + filename)