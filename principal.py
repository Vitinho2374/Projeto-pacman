import pygame
import constantes
import sprites

class Game:
    def __init__(self):
        # Criando a tela do jogo
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        pygame.display.set_caption(constantes.TITULO_JOGO)
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True

    def novo_jogo(self):
        # Instancia as classes das sprites do jogo
        self.todas_as_sprites = pygame.sprite.Group()
        self.rodar()

    def rodar(self):
        # Loop do jogo
        self.jogando = True
        while self.jogando:
            self.relogio.tick(constantes.FPS)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()

    def eventos(self):
        # Define os eventos do jogo
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.jogando = False
                self.esta_rodando = False

    def atualizar_sprites(self):
        # Atualizar sprites
        self.todas_as_sprites.update()

    def desenhar_sprites(self):
        # Desenhar sprites
        self.tela.fill(constantes.PRETO)  # Limpando a tela
        self.todas_as_sprites.draw(self.tela)  # Desenhando as sprites
        pygame.display.flip()

    def mostrar_tela_start(self):
        pass

    def mostrar_tela_game_over(self):
        pass

g = Game()
g.mostrar_tela_start()

while g.esta_rodando:
    g.novo_jogo()
    g.mostrar_tela_game_over()