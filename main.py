import pygame
pygame.init()


# ---------- Création de la classe "Game" ------------------

class Game:

    def __init__(self):
# -------- Générer notre joueur lors d'une nouvelle partie
        self.player = Player()

# ---------- Création de la classe "Player" ------------------

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500


# ---------- Création de la fenêtre de jeu ------------------

pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1800, 720))

# ---------- Importer et charger background du jeu ------------------

background = pygame.image.load('assets/bg.jpg')

# ---------- Importer et charger background du jeu ------------------

game = Game()


running = True

while running:

    # appliquer l'arrière plan du jeu --------
    screen.blit(background, (0, -200))

    # appliquer l'image du joueur -------- (par dessus le background)
    screen.blit(game.player.image, game.player.rect)



    # mettre à jour l'écran
    pygame.display.flip()

    # verification si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # verification si l'event est : fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()