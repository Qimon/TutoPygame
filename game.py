import pygame
import pytmx
import pyscroll

from player import Player

GAME_RESOLUTION: tuple = (800, 600)
GAME_NAME: str = 'MyGame'


class Game:

    def __init__(self) -> None:
        # Créer la fenêtre du jeu.
        # Résolution de l'écran:
        self.screen = pygame.display.set_mode(GAME_RESOLUTION)
        # Nom de la fenêtre
        pygame.display.set_caption(GAME_NAME)
        # Chargement de la carte
    # Chargement du fichier tmx
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        print(type(tmx_data))
        # Extraction des donnees du fichier tmx
        map_data = pyscroll.data.TiledMapData(tmx_data)
        print(type(map_data))
    # Chargement des calques contenus dans les datas
        map_layer = pyscroll.orthographic.BufferedRenderer(
            map_data, self.screen.get_size())
        print(type(map_layer))
        
        # Pour faire un zoom
        map_layer.zoom = 2
        
        # Génerer un joueur
        self.player = Player()
        
        # Varibilisation du groupe de calques depuis les donnes tmx
        self.group = pyscroll.PyscrollGroup(
            map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

    def run(self):
		
        # Boucle pour faire continuer le jeu
        running: bool = True

        while running:
            # Ordonner de dessiner les calques
            self.group.draw(self.screen)
            # Actualisation de la carte
            pygame.display.flip()

            for event in pygame.event.get():
                # declaration d'un evenement pour fermer la fenêtre de jeu
                if event.type == pygame.QUIT:
                    # On sort de la boucle
                    running = False

        pygame.quit()
