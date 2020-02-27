import pygame
from game import Game
pygame.init()




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

    # véfifier si le joueur veut aller à gauche ou à droite

    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()

    elif game.pressed.get(pygame.K_LEFT):
        game.player.move_left()


    # mettre à jour l'écran
    pygame.display.flip()

    # verification si le joueur ferme cette fenêtre
    for event in pygame.event.get():

        # verification si l'event est : fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fin de Partie")

        # détecter si le joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:

            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:

            game.pressed[event.key] = False


