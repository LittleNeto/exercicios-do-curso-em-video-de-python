import pygame
pygame.mixer.init()
pygame.mixer.music.load("Taste - TrackTribe.mp3")
pygame.mixer.music.play()
input('Pressione Enter para encerrar...')
pygame.mixer.music.stop()