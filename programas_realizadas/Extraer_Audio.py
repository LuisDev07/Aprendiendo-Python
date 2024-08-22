import moviepy.editor as mp
from tkinter import filedialog



    
video = mp.VideoFileClip(filedialog.askopenfilename(
    filetypes=[("Archivos de video", "*.mp4*")]
    
    ))
video.audio.write_audiofile(filedialog.asksaveasfilename( 
        title="guardar como ",
        defaultextension=".mp3"
        ))
print("realizado")


    