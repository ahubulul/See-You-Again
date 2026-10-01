import sys
from time import sleep
import pygame

pygame.mixer.init()
pygame.mixer.music.load("See U Again.mp3")
pygame.mixer.music.play()

def print_lyrics():
    # Danh sách (dòng chữ, thời gian delay giữa các ký tự, thời gian nghỉ sau khi xong dòng)
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
        for char in line:
            print(char, end='', flush=True)
            sleep(char_delay)
        print() # Xuống dòng
        sleep(line_delay)

try:
    print_lyrics()
    # Giữ chương trình chạy nếu nhạc chưa phát xong
    while pygame.mixer.music.get_busy():
        sleep(0.5)
except KeyboardInterrupt:
    pygame.mixer.music.stop()
    sys.exit()