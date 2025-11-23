import pygame

def play_backsound(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1)

def stop_backsound():
    pygame.mixer.music.stop()