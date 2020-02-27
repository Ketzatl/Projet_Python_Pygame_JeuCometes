import pygame
from player import Player

# ---------- Création de la classe "Game" ------------------

class Game:

    def __init__(self):
# -------- Générer notre joueur lors d'une nouvelle partie
        self.player = Player()
