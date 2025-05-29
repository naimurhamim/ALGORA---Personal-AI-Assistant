import os
import pygame



voice2 = 'en-US-AnaNeural'#cartoon
voice3 = 'en-US-RogerNeural'
voice4 = 'en-US-JennyNeural'  #['Friendly', 'Considerate', 'Comfort']}


def speak(data):
    voice1 = 'en-IN-NeerjaNeural'
    command = f'edge-tts --voice "{voice2}" --text "{data}" --write-media "data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()