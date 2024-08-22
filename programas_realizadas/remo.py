
from rembg import remove # descargas la libreria 
from PIL import Image # te permite manipular la imagen 
from tkinter import filedialog



image_input= Image.open(filedialog.askopenfilename(
    filetypes=[("Archivos de imagen ", "*.jpg*")]
    
    )) #ingresas la direccion de imagen que deseas quitar le fondo 
output = remove(image_input)
output.save(filedialog.asksaveasfilename( 
        title="guardar como ",
        defaultextension=".png"
        ) ) 
print("realizado") # ingresas el nombre de como deseas aguardarlo  