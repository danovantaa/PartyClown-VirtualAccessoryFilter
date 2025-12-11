import pygame

def play_backsound(path):
    """
    play backsound
    """
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1)

def stop_backsound():
    """
    stop audio
    """
    pygame.mixer.music.stop()