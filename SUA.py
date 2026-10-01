import sys
import threading
import tkinter as tk
from time import sleep
import pygame

pygame.mixer.init()
try:
    pygame.mixer.music.load("See U Again.mp3")
except Exception as e:
    print(
        f"Lỗi tải nhạc: {e}. Vui lòng kiểm tra lại tên file See U Again.mp3'"
    )

root = tk.Tk()
root.title("Lyrics Player")
root.geometry("600x400")
root.configure(bg="#1e1e1e")  

label = tk.Label(
    root,
    text="",
    font=("Segoe UI", 16, "bold"),
    fg="#ffffff",
    bg="#1e1e1e",
    wraplength=550,
    justify="center",
)
label.pack(expand=True)

def animate_lyrics():
    if pygame.mixer.music.get_busy() or True:
        pygame.mixer.music.play()

    lines = [
                ("20/20, 20/20 vision", 0.08, 0.9),
                ("Cupid hit me, cupid hit me with precision", 0.04, 1.2),
                ("I wonder if you look both ways", 0.07, 0.4),
                ("When you cross my mind, ", 0.06, 0.7),
                ("I said, I said",0.1, 0.08),
                ("I'm sick of, sick of, sick of, sick of chasing", 0.04, 1.1),
                ("You're the one that's always running through my daydream", 0.05, 0.5),
                ("I can only see your face when I close my eyes", 0.08, 1.4),
                ("So ", 0.07, 0.3),
                ("Can I get a kiss? (Can I get a kiss?)", 0.05, 0.5),
                ("And can you make it last forever? (Oh, forever)", 0.05, 0.5),
                ("I said I'm 'bout to go to war (Go to war)", 0.05, 1.0),
                ("I don't know if I'ma see you again (See you again)", 0.05, 1.0),
                ("Can I get a kiss? (Can I)", 0.05, 1.0),
                ("And can you make it last forever? (Can you)", 0.06, 0.7),
                ("I said I'm 'bout to go to war ('Bout to)", 0.05, 0.7),
                ("And I don't know if I'ma see you again ", 0.06, 1.9),
                ("Okay, okay, okay, okay, okay, okay, okay, oh ", 0.05, 0.9),
                ("Okay, okay, okay, okay, okay, okay, okay, oh ", 0.05, 0.9),
                ("Okay, okay, okay, okay, okay, okay, okay, oh ", 0.05, 0.9),
                ("Okay, okay, okay, okay, okay, oh ", 0.05, 0.9),
    ]

    sleep(0.5)

    for line, char_delay, line_delay in lines:
        current_text = ""
        for char in line:
            current_text += char
            label.config(text=current_text)
            sleep(char_delay)
        sleep(line_delay)

def start_app():
    threading.Thread(target=animate_lyrics, daemon=True).start()

def on_closing():
    pygame.mixer.music.stop()
    root.destroy()
    sys.exit()


root.protocol("WM_DELETE_WINDOW", on_closing)

root.after(500, start_app)
root.mainloop()