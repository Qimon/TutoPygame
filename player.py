import pygame

# Super Class Sprite pour les éléments animés. Depuis Pygame


class Player(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        # Chargement de l'image du joueur
        self.sprite_sheet = pygame.image.load('player.png')
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()

    def get_image(self, x: int, y: int):
        
        image = pygame.Surface([32, 32])
        print("---------------------------------")
        print(type(image))
        image.blit(
            source=self.sprite_sheet, dest=(0, 0), area=(x, y, 32, 32))
        return image
