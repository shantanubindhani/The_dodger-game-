#this is tthe pygame tutorrisl program

#imports
import pygame as pg
from random import randint

##================================================== classes =======================================================================================
class img_load(object):
      def __init__(self,imgs):
            self.imgs = imgs
      def image(self):
            images = []
            for img in self.imgs:
                  images.append(pg.image.load(img))

            return images
      
      

class player(object):
      def __init__(self,x,y,width,height):
            self.displaywidth =  800
            self.displayheight = 480
            # charatar attributes. : (x,y),width, height, velocity
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.velocity = 3
            self.isjump = False
            self.jumpcount = 10
            self.left = False
            self.right = False
            self.walkcount = 0
            self.standing = True
            # other variables
            self.screenwidth, self.screenwidth_ = self.displaywidth - self.width - self.velocity, self.displayheight - self.height - self.velocity

            self.heal = 100
            self.visible = True
            

      def draw(self,wn):
            if (self.walkcount+1) >= 27:
                  self.walkcount = 0
            if self.visible:
                  if not(self.standing):      
                        if self.left:
                              wn.blit(walkleft[(self.walkcount//3)], (self.x, self.y))
                              self.walkcount +=1
                        elif self.right:
                              wn.blit(walkright[(self.walkcount//3)], (self.x, self.y))
                              self.walkcount +=1
                  else:
                        if self.left:
                              wn.blit(walkleft[0],(self.x,self.y))
                        else:
                              wn.blit(walkright[0],(self.x,self.y))
                  self.hitbox = (self.x+17, self.y+10, 28, 54)  # (x, y, width, height)
                  #creating health bar
                  pg.draw.rect(wn,(255,0,0), (self.hitbox[0],self.y-20, 50, 10),)
                  pg.draw.rect(wn,(0,0,255), (self.hitbox[0],self.y-20, 50*(self.heal/100), 10),)
                  #pg.draw.rect(wn,(255, 0, 0), self.hitbox,2)
                  #wn.blit(char, (self.x, self.y))
      def hit(self):
            if self.heal > 0:
                  self.heal -= 4.2
            else:
                  self.visible = False
                  print("game over!")

class  projectile(object):
      def __init__(self, x, y, rad, colr, facing):
            self.x = x
            self.y = y
            self.rad = rad
            self.colr = colr
            self.facing = facing
            self.vel = 8*facing
      def draw(self, wn):
            pg.draw.circle(wn,self.colr, (self.x, self.y), self.rad) #,1)  # used to draw only the cirlcle outline

            self.hitbox = (self.x-6, self.y-6, 12, 12)  # (x, y, width, height)
            #pg.draw.rect(wn,(255, 0, 0), self.hitbox,1)

class enemy(object):
      Eright_imgs = ["R1E.png", "R2E.png", "R3E.png", "R4E.png", "R5E.png", "R6E.png", "R7E.png", "R8E.png", "R9E.png", "R10E.png","R11E.png"]
      Eleft_imgs = ["L1E.png", "L2E.png", "L3E.png", "L4E.png", "L5E.png", "L6E.png", "L7E.png", "L8E.png", "L9E.png", "L10E.png","L11E.png"]
      walkright = img_load(Eright_imgs).image()
      walkleft = img_load(Eleft_imgs).image()
      def __init__(self,x,y,width,height,end):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.end = end
            self.path = (self.x, self.end)
            self.walkcount = 0
            self.vel = randint(7,12)
            self.heal = 100
            self.visible = True

      def draw(self,wn):
            self.move()
            if self.visible:
                  if self.walkcount >= 33:
                        self.walkcount = 0
                  if self.vel > 0:
                        wn.blit(self.walkright[self.walkcount//3], (self.x, self.y))
                        self.walkcount += 1
                  else:
                        wn.blit(self.walkleft[self.walkcount//3], (self.x, self.y))
                        self.walkcount += 1

                  self.hitbox = (self.x+10, self.y, 44, 57)  # (x, y, width, height)
                  #creating health bar
                  pg.draw.rect(wn,(255,0,0), (self.hitbox[0],self.y-20, 50, 10),)
                  pg.draw.rect(wn,(255,255,0), (self.hitbox[0],self.y-20, (self.heal/100)*50, 10),)
                  #creating hitbox      
                  #pg.draw.rect(wn,(255, 0, 0), self.hitbox,2)
                  
      def move(self):
            if self.vel > 0:
                  if self.x + self.vel < self.path[1]:
                        self.x+=self.vel
                  else:
                        self.vel = self.vel*(-1)
                        self.wakcount = 0
            else:
                  if self.x - self.vel > self.path[0]:
                        self.x += self.vel
                  else:
                        self.vel = self.vel*(-1)
                        self.wakcount = 0

      def hit(self):
            if self.heal > 0:
                  self.heal -= 3
            else:
                  self.visible = False
            
#===============================================================================================================================================
pg.init() #initiating the pygame window

# creating player object
man = player(300,410,64,64)
wn = pg.display.set_mode((man.displaywidth,man.displayheight)) # used for display initiqlisation and customisation
pg.display.set_caption("quarantine game") # used for giving the window a propeer name

#importing images
right_imgs = ["R1.png", "R2.png", "R3.png", "R4.png", "R5.png", "R6.png", "R7.png", "R8.png", "R9.png"]
left_imgs = ["L1.png", "L2.png", "L3.png", "L4.png", "L5.png", "L6.png", "L7.png", "L8.png", "L9.png"]
bg = pg.image.load("bg.jpg")
char = pg.image.load("standing.png")

##creating enemies
goblin = enemy(100,415,64,64,450)


#===============================================================================================================================================
#loading images

      
clock = pg.time.Clock() # setting up the clock speed
      
walkright = img_load(right_imgs).image()
walkleft = img_load(left_imgs).image()
bg = pg.image.load("bg.jpg")
char = pg.image.load("standing.png")

#===============================================================================================================================================

def redrawgamewindow():
      #wn.fill((0,0,0))
      wn.blit(bg, (0, 0))
      text = font.render("score : "+str(score)+"| bullets used :"+ str(len(bullets))+"/5", 1, (0,0,0) ) # rendering the font to display mode
      wn.blit(text, (350,10))

      if not(man.visible):
            font_go = pg.font.SysFont("comicsans",80,True, False)  # (font type, size, bold, itallic)
            text_GO = font_go.render("GAME OVER!!", 1, (0,0,0) ) # rendering the font to display mode
            wn.blit(text_GO, (200,200))
                  
      #pg.draw.rect(wn, (255,0,0,), (x, y, width, height))
      man.draw(wn) # callin th draw class function  
      goblin.draw(wn)
      
      #draw bullets
      for bullet in bullets:
            bullet.draw(wn)

      pg.display.update()  #refreshing the window...or updating the window

# ========================================== MAIN LOOP ========================================================================================
font = pg.font.SysFont("comicsans",30,True, False)  # (font type, size, bold, itallic)
shootloop = 0
run  = True
bullets = []
gobs = []
score = 0
while  run:
      #pg.time.delay(100) # this is used for the time delay...initialised in pygame
      clock.tick(27)
      # checking for events

      #creating enemies
      if not(goblin.visible):
            goblin_start = randint(0,200)
            goblin_end = randint(600,800)
            goblin = enemy(goblin_start,415,64,64,goblin_end)
            
      if shootloop >0:
            shootloop+=1
      if shootloop > 3:
            shootloop = 0
      for event in pg.event.get():
            if event.type == pg.QUIT: # used for quiting the application.
                  run = False
      #self.hitbox = (self.x+17, self.y+10, 28, 54)
      if man.x+17 >= goblin.x+10 and man.x+17 <= goblin.x+54:
                  if man.y+10 >= goblin.y and man.y+10 <= goblin.y+57 and goblin.visible and man.visible:
                        man.hit()
                        
                        
      for bullet in bullets:
            if bullet.x+bullet.rad >= goblin.x+10 and bullet.x+bullet.rad <= goblin.x+54:
                  if bullet.y+bullet.rad >= goblin.y and bullet.y+bullet.rad <= goblin.y+57 and goblin.visible:
                        goblin.hit()
                        score += 1
                        bullets.pop(bullets.index(bullet))
            if bullet.x < man.displaywidth and bullet.x > 0:
                  bullet.x += bullet.vel
            else:
                  bullets.pop(bullets.index(bullet))

      keys = pg.key.get_pressed()
      #move/shoot the bullets
      if keys[pg.K_SPACE] and shootloop == 0 and man.visible:
            if man.left:
                  facin = -1
            else:
                  facin = 1
            if len(bullets) < 5:
                  bullets.append(projectile(round(man.x + man.width//2), round(man.y + man.height//2), 6, (0, 0, 0),  facin))
            shootloop = 1

      #move the character
      if keys[pg.K_LEFT] and man.x > man.velocity:
            man.x -= man.velocity
            man.left = True
            man.right = False
            man.standing = False
      elif keys[pg.K_RIGHT] and man.x < man.screenwidth:
            man.x+= man.velocity
            man.right = True
            man.left = False
            man.standing = False
      else:
            man.standing = True
            man.walkcount = 0
                  
      if not(man.isjump):
            if keys[pg.K_UP]:
                  man.isjump = True
                  man.right = False
                  man.left = False
                  man.walkcount = 0
      else:
            if man.jumpcount >=-10:
                  neg = 1
                  if man.jumpcount < 0:
                        neg = -1
                  man.y -= man.jumpcount ** 2 *0.5 * neg # jumping quadratic equation
                  man.jumpcount -= 1
            else:
                  man.isjump = False
                  man.jumpcount = 10

      redrawgamewindow()
      

pg.quit()
      
