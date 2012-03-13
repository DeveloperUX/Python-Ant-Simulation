#### TO DO ####
# MAKE SPIDER CLASS
# SET A GOAL
from graphics import *
import math, time
from random import *

num_of_ants = 10
num_of_spiders = 1
num_of_food = 15
home_pos = [270,30]

class Spider:
    def __init__(self,x,y, state='explore'):
        self.pos = Point(x, y)
        self.x = None; self.y = None
        self.ant_pos = None
        self.obj = Circle(self.pos, 4); self.obj.setFill('blue')
        self.state = state
        self.counter = 1
    def draw(self, win):
        self.obj.draw(win)
    def move(self, x, y):
        self.obj.move(x, y)
    def current_state(self):
        return self.state
    def explore(self):
        # MOVE RANDOMLY, LINE 2: MAKES IT LOOK NATURAL
        if self.counter == 1:
            self.x, self.y = randint(-2,2)/2, randint(-2,2)/2
        # TURN AFTER 15 STEPS
        if self.counter == 25:
            self.counter = 0
        self.obj.move(self.x, self.y)
        self.counter += 1
        # WALL BOUNDRIES
        # test
        print self.pos.getX()
        if self.pos.getX() < 5:
            self.x = 1
        if self.pos.getX() > 295:
            self.x = -1
        if self.pos.getY() < 5:
            self.y = 1
        if self.pos.getY() > 295:
            self.y = -1
        # UPDATE CURRENT POSITION
        self.pos = self.obj.getCenter()
    def hunt(self):
		# MOVE TOWARDS ANT
        self.obj.setFill(color_rgb(100,100,255))
		# FIND SLOPE BETWEEN FOOD AND ANT
        tempx = self.ant_pos.getX() - self.pos.getX()
        tempy = self.ant_pos.getY() - self.pos.getY()
        # MOVE TOWARDS ANT FAST
        x = tempx/100; y = tempy/100
        self.obj.move(x, y)
        # UPDATE CURRENT POSITION
        self.pos = self.obj.getCenter()
        print "%f %f" % (math.fabs(tempx), tempy) ################################
        if math.fabs(tempx) < .9 and math.fabs(tempy) < .9:
            self.state = 'kill'
    def look_for(self, list_of_ants):
        for ant in list_of_ants:
            if ant.pos.getX() - self.pos.getX() < 20 and \
               ant.pos.getY() - self.pos.getY() < 20:
                self.state = 'hunt'
                self.ant_pos = ant.pos
        return list_of_ants        

class Food:
    def __init__(self,x,y):
        self.pos = Point(x, y)
        self.obj = Circle(self.pos, 1); self.obj.setFill('black')
    def draw(self, win):
        self.obj.draw(win)
    def move(self, x, y):
        self.obj.move(x, y)


class Ant:

    def __init__(self, x, y, state='explore'):
        self.x = None
        self.y = None
        self.pos = Point(x, y)
        self.food_pos = None
        self.obj = Circle(self.pos, 3)
        self.state = state
        self.home_pos = home_pos
        self.counter = 1 
        self.temp = 0 #    
        
    def draw(self, win):
        self.obj.draw(win)
    def current_state(self):
        return self.state

    def explore(self):
        self.obj.setFill(color_rgb(255,0,0))
        # MOVE RANDOMLY, LINE 2: MAKES IT LOOK NATURAL
        if self.counter == 1:
            self.x, self.y = randint(-1,1), randint(-1,1)
        # TURN AFTER 15 STEPS
        if self.counter == 15:
            self.counter = 0
        self.obj.move(self.x, self.y)
        self.counter += 1
        # WALL BOUNDRIES
        if self.pos.getX() < 4:
            self.x = 1
        if self.pos.getX() > 296:
            self.x = -1
        if self.pos.getY() < 4:
            self.y = 1
        if self.pos.getY() > 296:
            self.y = -1
        # UPDATE CURRENT POSITION
        self.pos = self.obj.getCenter()
    
    def seek(self):
		# MOVE TOWARDS FOOD
        self.obj.setFill(color_rgb(255,150,100))
		# FIND SLOPE BETWEEN FOOD AND ANT
        tempx = self.food_pos[0].pos.getX() - self.pos.getX()
        tempy = self.food_pos[0].pos.getY() - self.pos.getY()
        # MOVE TOWARDS FOOD SLOWLY
        x = tempx/20; y = tempy/20
        self.obj.move(x, y)
        # UPDATE CURRENT POSITION
        self.pos = self.obj.getCenter()
        #print "%f %f" % (math.fabs(tempx), tempy) ################################
        if math.fabs(tempx) < .9 and math.fabs(tempy) < .9:
            self.state = 'return'

    def warn(self, list_of_ants):
        pass
#       list_of_food = self.food_pos; dist_from_hill = 15; dist_from_ants = 15
#        # UPDATE CURRENT POSITION
#       self.pos = self.obj.getCenter(); self.obj.setFill('purple')
#       # MOVE TOWARDS HOME
#       tempx = self.home_pos[0] - self.pos.getX(); x = tempx/50
#       tempy = self.home_pos[1] - self.pos.getY(); y = tempy/50
#       self.obj.move(x, y)
#       close_ants = []
#       if math.fabs(tempx) < dist_from_hill and math.fabs(tempy) < dist_from_hill:
#           for ant in list_of_ants:
#                if ant.pos.getX() - self.pos.getX() < dist_from_ants and \
#                  ant.pos.getY() - self.pos.getY() < dist_from_ants:
#                   close_ants.append(ant)
#                    if len(list_of_food) != 0:
#                       ant.food_pos = [list_of_food[0]]
#                        ant.state = 'seek'
#                        list_of_food.pop(0)
#                    else : pass
#            self.state = 'explore'
        
    def escape(self):
        pass
    def return_home(self):
        self.obj.setFill(color_rgb(255,200,0))
        # SETS THE DIRECTION TO MOVE THE FOOD - TO GET HOME
        # IF THE DIRECTION IS ALREADY SET THEN JUST MOVE
        if self.temp != 1:
            tempx = self.home_pos[0]+randint(-9,9) - self.pos.getX()
            tempy = self.home_pos[1]+randint(-9,9) - self.pos.getY()
            self.temp = 1
            self.x = tempx/100; self.y = tempy/100
        # MOVE BOTH THE ANT AND THE FOOD TO ANT-HILL
        self.obj.move(self.x, self.y)
        self.food_pos[0].move(self.x, self.y)
        # UPDATE CURRENT POSITION
        self.pos = self.obj.getCenter()
        # IF ANT IS NEAR THE CIRCLE IT WILL START EXPLORING
        #x = randint(1,10)
        #print self.pos.getX(), self.home_pos[0]
        if math.fabs(self.pos.getX() - self.home_pos[0]) < 10 and \
           math.fabs(self.pos.getY() - self.home_pos[1]) < 10:
            self.state = 'explore' 
            self.temp = 0
 
    def check_for(self, list_of_food):
        close_food = []
        for i in list_of_food:
            #print 'food', i.pos.getX()#
            #print 'ant', self.pos.getX()#
            distx = math.fabs(i.pos.getX() - self.pos.getX())
            disty = math.fabs(i.pos.getY() - self.pos.getY())
            #print distx, disty
            if distx < 40 and disty < 40:     ###############
                close_food.append(i)
        #print len(close_food)
        if len(close_food) > 1:
            self.state = 'warn'
            self.food_pos = close_food
            for i in range(len(close_food)):
                x = list_of_food.index(close_food[i])
                list_of_food.pop(x)
        elif len(close_food) == 1:
            distanceX = math.fabs(close_food[0].pos.getX() - self.pos.getX())
            distanceY = math.fabs(close_food[0].pos.getY() - self.pos.getY())
            if distanceX < 40 and distanceY < 40:
                self.state = 'seek'
                self.food_pos = close_food
                x = list_of_food.index(close_food[0])
                list_of_food.pop(x)
            else : pass
        return list_of_food    

def make_hill(win):
    # makes the ant house
    home = Circle(Point(home_pos[0],home_pos[1]), 25)
    home.setFill('green'); home.setOutline('green2')
    home.draw(win)               
    
def main():
    win = GraphWin('game', 300, 300)
    make_hill(win)
    ants = [];  food = []; spiders = []
    for i in range(num_of_ants):
        r1 = randint(home_pos[0]-20,home_pos[0]+20); r2 = randint(home_pos[1]-20,home_pos[1]+20)
        ants.append(Ant(r1,r2))
        ants[i].draw(win)
    for i in range(num_of_food):
        r1 = randint(50,250); r2 = randint(50,250)
        food.append(Food(r1,r2))
        food[i].draw(win)
    for i in range(num_of_spiders):
        r1 = randint(10,80); r2 = randint(230,290)
        spiders.append(Spider(r1,r2))
        spiders[i].draw(win)
    win = False
    while not win:
        for i in range(num_of_ants):
            #print ants[i].current_stat()
            for s in range(num_of_spiders):
                if spiders[s].current_state() == 'explore':
                    spiders[s].explore()
                    spiders[s].look_for(ants)
                if spiders[s].current_state() == 'hunt':
                    spiders[s].hunt()
                time.sleep(.00001)
            if ants[i].current_state() == 'explore':
                ants[i].explore()
                ants[i].check_for(food)
                if food == []:
                    win = True
            if ants[i].current_state() == 'seek':
                ants[i].seek()
            if ants[i].current_state() == 'return':
                ants[i].return_home()
            if ants[i].current_state() == 'warn':
                ants[i].warn(ants)
            if ants[i].current_state() == 'escape':
                ants[i].escape()
            time.sleep(.0001)
        if food == []:
            win = True
    print 'YOU WIN'

main()
