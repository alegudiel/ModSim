""" --------Documentacion del modulo game.py--------
https://www.pygame.org/docs/ref/rect.html
"""
import pygame
from skfuzzy import control as ctrl
import skfuzzy as fuzz
from FuzzyForce import Shooting as sh
import fuzzyMove 
import random
import numpy as np

# Sequence for initialize values
# fuzzyMove.makeDecisionMovement(103, 155)
# fuzzyMove.seeGraphsOfVariables()
# print(fuzzyMove.returnValueOfDecision())

class Game():

    # To see variables, select in menu
    def seeGraphsOfVariables():
        fuzzyMove.seeGraphsOfVariables()

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
        self.goalAngle = (0,0)
        pygame.display.set_caption('Robots para el mundial de soccer')
        
        # Player
        self.playerCoordX = 500
        self.playerCoordY = 400
        self.playerVelocity = 5
        self.playerWidth = 30
        self.playerHeight = 15
        self.playerCurrentDirection = (0,0)
        self.playerInitCord = (random.randint(10,750), random.randint(10,300))

        # Ball  
        self.ballCoordX = random.randint(10,500)
        self.ballCoordY = random.randint(10,400)
        self.ballVelocity = 4
        self.ballWidth = 10
        self.ballInitCord = (self.ballCoordX, self.ballCoordY)

        self.updateScene()

    # with the decision of the fuzzy move, move the player
    # find a way to move the player in the direction of the ball
    def playerMovement(self, newMov):
        playerPosition = (self.playerCoordX, self.playerCoordY)
        ballPosition = (self.ballCoordX, self.ballCoordY)
        distance = self.calcBallProximity(playerPosition, ballPosition)
        forceBall = sh.fuzzyForce(distance)
        self.findGoal()
        self.kickGoal(self.goalAngle, forceBall*self.ballVelocity)

    def playerStep(self):
        self.playerCoordX += self.playerCurrentDirection[0] * self.playerVelocity
        self.playerCoordY += self.playerCurrentDirection[1] * self.playerVelocity

    def calcBallProximity(self):
        playerCurrentPos = (self.playerCoordX, self.playerCoordY)
        ballCurrentPos = (self.ballCoordX, self.ballCoordY)
        distanceX = abs(playerCurrentPos[0] - ballCurrentPos[0])
        distanceY = abs(playerCurrentPos[1] - ballCurrentPos[1])

        if distanceX < 0:
            self.playerCurrentDirection = (1, self.playerCurrentDirection[1])
        elif distanceX > 0:
            self.playerCurrentDirection = (-1, self.playerCurrentDirection[1])

        if distanceY < 0:
            self.playerCurrentDirection = (self.playerCurrentDirection[0], 1)
        elif distanceY > 0:
            self.playerCurrentDirection = (self.playerCurrentDirection[0], -1)
        
        self.playerStep()

    def scoreGoal(self):
        if self.ball.colliderect(self.fieldGoal):
            self.currentGoals += 1
            self.respawnBall()
            print(self.currentGoals)

    def kickGoal(self, direction, force):
        directionX, directionY = direction[0], direction[1]

        if directionX == 1 and directionY == 1:
            if self.ballCoordX + force > self.windowW:
                self.kickGoal((-directionX, -directionY), force)
            else:
                self.ballCoordX += force
                self.ballCoordY += force
        
        elif directionX == -1 and directionY == -1:
            if self.ballCoordX - force < 0:
                self.kickGoal((-directionX, -directionY), force)
            else:
                self.ballCoordX -= force
                self.ballCoordY -= force

    def respawnBall(self):
        self.ballCoordX =  random.randint(10,500)
        self.ballCoordY = random.randint(10,400)

    def findGoal(self):
        ballPosX = self.ballCoordX
        ballPosY = self.ballCoordY
        goal = self.fieldGoal
        
        if ballPosX < goal[0]:
            self.kickGoal(1, self.goalAngle[1])
        elif ballPosX > goal[0]:
            self.kickGoal(-1, self.goalAngle[1])
        elif ballPosY < goal[1]:
            self.kickGoal(self.goalAngle[0], 1)
        elif ballPosY > goal[1]:
            self.kickGoal(self.goalAngle[0], -1)

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
        self.fieldGoal = pygame.draw.rect(self.window, (227,230,228), (780, self.windowH/2 - 50, 10, 100))

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

            self.calcBallProximity()
            self.scoreGoal()
            self.updateScene()

    def Menu():
        print("¿Qué desea hacer?")
        print("1. Ver gráficas de las variables")
        print("2. Jugar")
        print("3. Salir")
        option = int(input("Opción: "))
        if option == 1:
            Game.seeGraphsOfVariables()
        elif option == 2:
            game = Game()
            game.run()
        elif option == 3:
            quit()
        
if __name__ == '__main__':
    Game.Menu()
    # game = Game()
    # game.run()