""" --------Documentacion del modulo game.py--------
https://www.pygame.org/docs/ref/rect.html
"""

import pygame
import fuzzyMove 

# Sequence for initialize values
fuzzyMove.makeDecisionMovement(103, 155)
fuzzyMove.seeGraphsOfVariables()
print(fuzzyMove.returnValueOfDecision())

class Game():

    # definimos los colores, el tamaño de la ventana y coordenadas iniciales del jugador
    def __init__(self):
        pygame.init()
        self.currentGoals = 0

        # Field
        self.field = (26, 189, 83)
        self.windowW = 800
        self.windowH = 600
        self.window = pygame.display.set_mode((self.windowW, self.windowH))
        self.goal = (227, 230, 2285)
        pygame.display.set_caption('Robots para el mundial de soccer')
        
        # Player
        self.playerCoordX = 650
        self.playerCoordY = 300
        self.playerVelocity = 5
        self.playerWidth = 30
        self.playerHeight = 15
        self.playerCurrentDirection = (0,0)
        self.playerInitCord = (self.playerCoordX, self.playerCoordY)

        # Ball  
        self.ballCoordX = 400
        self.ballCoordY = 300
        self.ballVelocity = 4
        self.ballWidth = 10
        self.ballInitCord = (self.ballCoordX, self.ballCoordY)
        self.updateScene()

    def seeGraphsOfVariables():
        # To see variables, add a menu
        fuzzyMove.seeGraphsOfVariables()

    def playerMovement(self):
        playerKey = pygame.key.get_pressed()

        # Basic movement
        if playerKey[pygame.K_LEFT]:
            self.playerCoordX -= self.playerVelocity
            self.playerCurrentDirection = (-1,0)

        elif playerKey[pygame.K_RIGHT]:
            self.playerCoordX += self.playerVelocity
            self.playerCurrentDirection = (1,0)

        elif playerKey[pygame.K_UP]:
            self.playerCoordY -= self.playerVelocity
            self.playerCurrentDirection = (0,-1)

        elif playerKey[pygame.K_DOWN]:
            self.playerCoordY += self.playerVelocity
            self.playerCurrentDirection = (0,1)

    def ballMovement(self):
        pass

    def scoreGoal(self):
        if self.ball.colliderect(self.fieldGoal):
            self.currentGoals += 1
            self.respawnBall()
            print(self.currentGoals)

    def respawnBall(self):
        self.ballCoordX = self.ballInitCord[0]
        self.ballCoordY = self.ballInitCord[1]

    def updateScene(self):
        # Field
        self.window.fill(self.field)
        pygame.draw.circle(self.window, (227, 230, 228), (self.windowW/2, self.windowH/2), 50, 10)
        pygame.draw.rect(self.window, (227, 230, 228), (self.windowW/2, 0, 10, self.windowH))

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Score: ' + str(self.currentGoals), True, (255, 255, 255))
        textRect = text.get_rect()
        self.window.blit(text, textRect)

        # Goal area
        self.fieldGoal = pygame.draw.rect(self.window, (227,230,228), (0, self.windowH/2 - 50, 10, 100))

        # Player
        self.player = pygame.draw.rect(self.window, (58, 83, 112), (self.playerCoordX, self.playerCoordY, self.playerHeight, self.playerWidth))

        # Ball
        self.ball = pygame.draw.circle(self.window, (122, 122, 122), (self.ballCoordX, self.ballCoordY), self.ballWidth)

        pygame.display.update()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.playerMovement()
            self.scoreGoal()
            self.updateScene()

if __name__ == '__main__':
    game = Game()
    game.run()
