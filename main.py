import pygame

pygame.init

GAME_RESOLUTION: tuple = (800, 600)
GAME_NAME: str = "MyGame"

# Créer la fenêtre du jeu.
# Résolution de l'écran:
pygame.display.set_mode(GAME_RESOLUTION)
# Nom de la fenêtre
pygame.display.set_caption(GAME_NAME)

# Boucle pour faire continuer le jeu
running: bool = True
while running:
    for event in pygame.event.get():
        # declaration d'un evenement pour fermer la fenêtre de jeu
        if event.type == pygame.QUIT:
            # On sort de la boucle
            running = False

pygame.quit()