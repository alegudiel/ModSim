""" --------Documentacion del modulo game.py--------
https://www.pygame.org/docs/ref/rect.html
"""
from multiprocessing.connection import wait
from time import sleep
from marshmallow import missing
import pygame
from skfuzzy import control as ctrl
import skfuzzy as fuzz
from sympy import re
from FuzzyForce import Shooting
import fuzzyMove as fm
import random
import numpy as np



# To see variables, select in menu
def seeGraphsOfVariables():
    fm.seeGraphsOfVariables()

class Game():
    # definimos los colores, el tamaño de la ventana y coordenadas iniciales del jugador
    def __init__(self):

        pygame.init()
        self.currentGoals = 0

        # Field
        self.field = (26, 189, 83)
        self.windowW = 800
        self.windowH = 400
        self.window = pygame.display.set_mode((self.windowW, self.windowH))
        self.goal = (227, 230, 2285)
        pygame.display.set_caption('Robots para el mundial de soccer')
        
        # Player
        self.playerCoordX = random.randint(10,500)
        self.playerCoordY = random.randint(10,400)
        self.playerVelocity = 2
        self.playerWidth = 15
        self.playerHeight = 15
        self.playerCurrentDirection = (0,0)
        self.playerInitCord = (self.playerCoordX, self.playerCoordY)

        # Ball  
        self.ballCoordX = random.randint(10,500)
        self.ballCoordY = random.randint(50,250)
        self.ballVelocity = 4
        self.ballWidth = 10
        self.ballInitCord = (self.ballCoordX, self.ballCoordY)

        self.updateScene()

    def playerMovement(self):
        # find the position of the ball
        currentPositionBall = (self.ballCoordX, self.ballCoordY)
        # find the position of the player
        currentPositionPlayer = (self.playerCoordX, self.playerCoordY)
        # calculate the distance between the ball and the player
        distance = np.sqrt((currentPositionBall[0] - currentPositionPlayer[0])**2 + (currentPositionBall[1] - currentPositionPlayer[1])**2)

        # using fuzzy logic to calculate the direction of the player
        fm.makeDecisionMovement(self.playerCoordY, self.playerCoordX)
        fm.returnValueOfDecision()
        
        if fm.returnValueOfDecision() < 5:
                if currentPositionBall[0] < self.playerCoordX:
                    self.playerCoordX -= self.playerVelocity+2
                elif currentPositionBall[0] > self.playerCoordX:
                    self.playerCoordX += self.playerVelocity+2
                if currentPositionBall[1] < self.playerCoordY:
                    self.playerCoordY -= self.playerVelocity+2
                elif currentPositionBall[1] > self.playerCoordY:
                    self.playerCoordY += self.playerVelocity+2

                elif currentPositionBall[0] > self.playerCoordX and currentPositionBall[1] > self.playerCoordY:
                    self.playerCoordX += self.playerVelocity+2
                    self.playerCoordY += self.playerVelocity+2

                elif currentPositionBall[0] < self.playerCoordX and currentPositionBall[1] > self.playerCoordY:
                    self.playerCoordX -= self.playerVelocity+2
                    self.playerCoordY += self.playerVelocity+2
                
                elif currentPositionBall[0] > self.playerCoordX and currentPositionBall[1] < self.playerCoordY:
                    self.playerCoordX += self.playerVelocity+2
                    self.playerCoordY -= self.playerVelocity+2

                elif currentPositionBall[0] < self.playerCoordX and currentPositionBall[1] < self.playerCoordY:
                    self.playerCoordX -= self.playerVelocity+2
                    self.playerCoordY -= self.playerVelocity+2
                
                if distance <= 25:
                    self.ballMovement()

        elif fm.returnValueOfDecision() >= 5:
                if currentPositionBall[0] < self.playerCoordX:
                    self.playerCoordX -= self.playerVelocity*2
                elif currentPositionBall[0] > self.playerCoordX:
                    self.playerCoordX += self.playerVelocity*2
                if currentPositionBall[1] < self.playerCoordY:
                    self.playerCoordY -= self.playerVelocity*2
                elif currentPositionBall[1] > self.playerCoordY:
                    self.playerCoordY += self.playerVelocity*2
                
                elif currentPositionBall[0] > self.playerCoordX and currentPositionBall[1] > self.playerCoordY:
                    self.playerCoordX += self.playerVelocity*2
                    self.playerCoordY += self.playerVelocity*2

                elif currentPositionBall[0] < self.playerCoordX and currentPositionBall[1] > self.playerCoordY:
                    self.playerCoordX -= self.playerVelocity*2
                    self.playerCoordY += self.playerVelocity*2
                
                elif currentPositionBall[0] > self.playerCoordX and currentPositionBall[1] < self.playerCoordY:
                    self.playerCoordX += self.playerVelocity*2
                    self.playerCoordY -= self.playerVelocity*2

                elif currentPositionBall[0] < self.playerCoordX and currentPositionBall[1] < self.playerCoordY:
                    self.playerCoordX -= self.playerVelocity*2
                    self.playerCoordY -= self.playerVelocity*2


                if distance <= 25:
                    self.ballMovement()

    def ballMovement(self):
        Shot = Shooting()
        finalforce = Shot.fuzzyForce([self.playerCoordX, self.playerCoordY], 5)
        currentPositionBall = (self.ballCoordX, self.ballCoordY)
        currentPositionBall += finalforce
        self.ballCoordX = currentPositionBall[0] + self.ballVelocity
        self.scoreGoal()

        if self.ballCoordX > self.windowW:
            self.respawnBall()
        

    def respawnBall(self):
        self.ballCoordX =  random.randint(10,500)
        self.ballCoordY = random.randint(50,250)

    def scoreGoal(self):
        if self.ball.colliderect(self.fieldArea):
            self.currentGoals += 1
            self.respawnBall()

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
        self.fieldArea = pygame.draw.rect(self.window, (227,230,228), (780, self.windowH/2-100, 15, 200))

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
            self.updateScene()

            if self.currentGoals == 3:
                print("--------------GAME OVER--------------")
                pygame.quit()

    def Menu():
        print("¿Qué desea hacer?")
        print("1. Ver gráficas de las variables")
        print("2. Jugar")
        print("3. Salir")
        option = int(input("Opción: "))
        if option == 1:
            fm.seeGraphsOfVariables()
        elif option == 2:
            game = Game()
            game.run()
        elif option == 3:
            quit()
        
if __name__ == '__main__':
    Game.Menu()
    # game = Game()
    # game.run()
    