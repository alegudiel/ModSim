from fuzzylogic.classes import Domain, Set, Rule
from matplotlib import pyplot
from fuzzylogic.hedges import very
from fuzzylogic.functions import R, S
from fuzzylogic.functions import gauss
import math
pyplot.rc("figure", figsize=(10, 10))

class Shooting(object):

    def __init__(self):

        self.field = [200,200]
        self.x_goal = 0
        self.y_goal = self.field[0]/2
        self.ball_mass = 0.45
        self.maximum_dist = self.field[1]
        self.minimum_time = 1
        self.maximum_time = 10
        self.maximum_force = self.maximumForce(self.maximum_dist)

    def maximumForce(self, maximum_dist):

        acc = (2*maximum_dist)/self.minimum_time**2
        force = acc*self.ball_mass
        return force

    def distanceGen(self, x, y):

        distance = math.sqrt(
            ((self.x_goal - x)**2) + ((self.y_goal - y)**2)
            )
        
        return distance

    def fuzzyForce(self, coords, time):
        x_robot, y_robot = coords
        distance = self.distanceGen(x_robot, y_robot)

        maximum_dist = self.maximum_dist
        maximum_force = self.maximum_force

        dist_shooting = Domain("Distance", 0, maximum_dist)
        timing = Domain("Time", self.minimum_time, self.maximum_time)
        force = Domain("Force", 0, maximum_force)

        dist_shooting.close = S(0,2*maximum_dist/5)
        dist_shooting.far = R(maximum_dist/5, maximum_dist)

        timing.short = S(0, self.maximum_time/4)
        timing.long = R(self.maximum_time/5, self.maximum_time)

        force.few = S(0,maximum_force/3)
        force.huge = R(maximum_force/4, maximum_force)

        # dist_shooting.close.plot()
        # dist_shooting.far.plot()

        # timing.short.plot()
        # timing.long.plot()

        force.few.plot()
        force.huge.plot()

        pyplot.show()



        R1 = Rule({(dist_shooting.close,timing.short): force.huge})
        R2 = Rule({(dist_shooting.close, timing.long): force.few})
        R3 = Rule({(dist_shooting.far, timing.short): force.huge})
        R4 = Rule({(dist_shooting.far, timing.long): force.few})



        rules = Rule({(dist_shooting.close,timing.short): force.huge,
                (dist_shooting.close, timing.long): force.few,
                (dist_shooting.far, timing.short): force.huge,
                (dist_shooting.far, timing.long): force.few
                })

        # rules(values)
        rules == R1 | R2 | R3 | R4 == sum([R1, R2, R3, R4])
        values = {dist_shooting: distance, timing: time}
        # print("distance ->", distance)
        # print("time ->", time)

        return rules(values)
        

Shot = Shooting()
# PARAMETROS: Ingresan coordenadas [x, y] del balon / robot
# y tiempo t que tarda el disparo en alcanzar la porteria
finalForce = Shot.fuzzyForce([64,60], 5)
print(finalForce)

