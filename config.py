import pygame
from button import Button

class Config:
    """
    Classe que armazena configurações e constantes relacionadas ao jogo.
    Contém atributos estáticos com valores específicos.
    """

    pygame.init()

    # Configurações da tela
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    SCREEN_COLOR = '#444444'

    # Configurações dos blocos
    BLOCK_SIZE = 80
    BLOCK_COLOR = "#222222"

    # Configuração do jogador
    PLAYER_COLOR = "purple"

    # Configuração da fonte
    font = pygame.font.SysFont("arialblacomicck", 40)
    COR_FONTE = (255, 255, 255)
    COR_FUNDO_TEXTO = (0, 0, 0)

    # imagens que serão usadas durante o jogo
    menu1_jpg = pygame.image.load("imgs/menu1.jpg")
    menu2_jpg = pygame.image.load("imgs/menu2.jpg")
    leaderboardFUNDO_jpg = pygame.image.load("imgs/leaderboard.jpg")
    
    campanha_jpg = pygame.image.load("imgs/botoes/campanha.png")
    arcade_jpg = pygame.image.load("imgs/botoes/arcade.png")
    leaderboard_jpg = pygame.image.load("imgs/botoes/leaderboard.png")
    sair_jpg = pygame.image.load("imgs/botoes/sair.png")

    campanhaAlt_jpg = pygame.image.load("imgs/botoes/campanhaAlt.png")
    arcadeAlt_jpg = pygame.image.load("imgs/botoes/arcadeAlt.png")
    leaderboardAlt_jpg = pygame.image.load("imgs/botoes/leaderboardAlt.png")
    sairAlt_jpg = pygame.image.load("imgs/botoes/sairAlt.png")

    # Botões que serão usados 
    botao_campanha = Button(254, 280, campanha_jpg, campanhaAlt_jpg, 0.5)
    botao_arcade = Button(254, 100, arcade_jpg, arcadeAlt_jpg, 0.5)
    botao_leaderboard = Button(254, 190, leaderboard_jpg, leaderboardAlt_jpg, 0.5)
    botao_sair = Button(254, 600, sair_jpg, sairAlt_jpg, 0.5)
