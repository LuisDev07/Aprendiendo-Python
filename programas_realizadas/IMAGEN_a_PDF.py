import aspose.words as aw
from tkinter import filedialog
from PIL import Image



docu =filedialog.askopenfilename(
     title="Seleccionar imágenes",
    filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg;*.gif"), ("Todos los archivos", "*.*")],
    initialdir="/"
    
    
    )


imagen = Image.open(docu)
imagen = imagen.convert('RGB')

imagen.save(filedialog.asksaveasfilename ( 
        title="guardar como ",
        defaultextension=".PDF",
        initialdir="/",
        initialfile="NewImagePDF"

        
        ))
print("____________transaccion realizada__________")
