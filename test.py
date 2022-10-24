import tkinter as tk
from tkinter import *
import winsound as win
import random as ran

class Fleet(object):
    def __init__(self):
        self.aliens_lines = 5
        self.aliens_columns = 10
        self.aliens_inner_gap = 20
        self.alien_x_delta = 5
        self.alien_y_delta = 15
        fleet_size = self.aliens_lines * self.aliens_columns
        self.aliens_fleet = [None] * fleet_size
        self.width = 950
        self.defender = Defender()
        self.height = 600
        self.id_tire = None

    def get_dx(self):
        return self.alien_x_delta
    def get_dy(self):
        return self.alien_y_delta
    def set_dx(self,new_dx):
        self.alien_x_delta=new_dx

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_score(self):
        return (self.aliens_lines * self.aliens_columns - len(self.aliens_fleet)) * 100
        
    def install_in(self, canvas):
        self.alien=Alien()
        self.canvas=canvas
        self.x=50   
        self.y=50
        pos = 0
        for i in range(self.aliens_lines):
            for j in range(self.aliens_columns):
                self.aliens_fleet[pos] = self.alien.install_in(self.canvas,self.x,self.y)
                pos= pos+1 
                self.x += self.aliens_inner_gap+70  # distance en largeur entre chaque alien 70
            self.x=50
            self.y += self.aliens_inner_gap+50   # distance en longeur entre les aliens 50 
                 
    
    def move_in(self, canvas): 
        dy = 0
        if len(self.aliens_fleet)!=0:
            all_rect_ids = self.canvas.find_withtag("alien")
            x1,y1,x2,y2 = self.canvas.bbox("alien")
            
            if x2>=self.width:      #déplacement vers la droite sans depassé la fenetre de jeu
                self.set_dx(-self.get_dx())
                dy = self.alien_y_delta
            elif x1<=0:      #déplacement vers la gauche sans depassé la fenetre de jeu
                self.set_dx(-self.get_dx())
                dy = self.alien_y_delta
            elif y2 >= (self.get_height() - self.defender.height) :
                canvas.delete(ALL)
                canvas.create_text(self.width//2,self.height//2,font=('Fixedsys',24),text="Game Over",fill='blue') 
            else:        #centre
                dy=0

            for i in range(0,len(all_rect_ids)):
                self.alien.move_in(self.canvas,all_rect_ids[i],self.alien_x_delta,dy)
    
    def manage_touched_aliens_by(self,canvas,defender):
        self.canvas = canvas
        self.defender=defender
        for i in range(len(self.defender.fired_bullets)):
            cond_sorti=0   
            xb1,yb1,xb2,yb2=self.canvas.bbox(self.defender.fired_bullets[i]) #coordonnée des bullet
            if(len(self.aliens_fleet)==0):
                canvas.delete(ALL)
                canvas.create_text(int(canvas.cget("width"))//2,int(canvas.cget("height"))//2,font=('Fixedsys',24),text="You win",fill='blue')
                break
            else:
                    for j in range(len(self.aliens_fleet)):
                        if self.aliens_fleet[j] != None:
                            #condition si il existe des aliens vivants
                            #si tout les aliens ne sont pas détruis
                            xa1,ya1,xa2,ya2=self.canvas.bbox(self.aliens_fleet[j])
                                #condition pour savoir s'il a collision entre le bullet et les aliens
                            if (xb1>=xa1 or xb2>=xa1) and (xb1<=xa2 or xb2<=xa2) and (yb1<=ya2) and (yb1>=ya1):
                                son_tire = "explosion.wav"
                                win.PlaySound(son_tire, win.SND_FILENAME | win.SND_ASYNC)
                                self.alien.touched_by(self.canvas,self.defender.fired_bullets[i])   #si collision le bullet est détruit
                                canvas.delete(self.defender.fired_bullets[i])  #l'alien meurt
                                    #supression de l'alien
                                canvas.delete(self.aliens_fleet[j])    
                                self.alien.alive = False                      
                                del self.defender.fired_bullets[i]   #supression des valeur de la liste
                                del self.aliens_fleet[j]  
                                cond_sorti=1    #pour sortir de la 2eme boucle
                                break
               
                            
                    if(cond_sorti==1):
                        break

    def tire_alien(self, canvas):
        self.fire_alien = 0
        if(self.fire_alien < 2):
            self.id_tire = 1
            
            





class Bullet_alien(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.fleet = Fleet()
        self.id = None
        self.choix = self.fleet.aliens_fleet[:]
        self.choix_tireur = 0
        self.radius = 8
        self.speed = 10
        

    def install_in_bullet(self, canvas):
        i = 0
        while(i < len(self.choix)):
            if(self.choix_tireur[i] == None):
                del self.choix[i]
            i+=1
        if(len(self.choix == 1)):
            self.choix_tireur = 0
        else:
            self.choix_tireur = ran.randrange(0, len(self.choix),1)
        
        
        if(self.choix != 0):
            alien_x1, alien_y1, alien_x2, alien_y2 = self.canvas.bbox(self.choix[self.choix_tireur])
            self.id = self.canvas.create_oval(alien_x1+20, alien_y1+20, alien_x2+self.radius, alien_y2+self.radius)
            return self.id

    def move_bullet_alien_in(self, canvas):
        canvas.move(self.id, 0, self.speed)



        





   






class Alien(object):
    def __init__(self):
        self.id = None
        self.alive = True
        self.alien = PhotoImage(file="alien.gif")
        self.explosion = PhotoImage(file="explosion.gif")
        
    def install_in(self, canvas, x, y): 
        self.id = canvas.create_image(x, y, image=self.alien, tags="alien") 
        return self.id
    
    def move_in(self, canvas, alien, dx, dy): #déplacement de l'alien sur l'axe des x et sur l'axe des y
        self.id=alien
        canvas.move(self.id, dx, dy)
    
    def touched_by(self,canvas,projectile): #destruction(la mort) de l'alien
        x1,y1,x2,y2=canvas.bbox(projectile)
        explosion = canvas.create_image(x1+(x2-x1)/2, y1+(y2-y1)/2, image=self.explosion, tags="explosion")
        canvas.after(100,canvas.delete,explosion) 


class Defender(object):
    def __init__(self):
        self.width =20
        self.height = 20
        self.move_delta =20
        self.id = None
        self.max_fired_bullets = 8
        self.fired_bullets = []
        self.image_player = PhotoImage(file="player.gif") # image du defender dans la variable self.image_player
        self.nb_vies = 3

    def get_vies(self):
        return self.nb_vies

    def install_in(self, canvas):
        self.canvas = canvas
        self.canvas_width = int(canvas.cget("width")) # largeur de la fenêtre de jeux
        self.canvas_height = int(canvas.cget("height")) # hauteur de la fenêtre de jeux
        x, y = self.canvas_width//2 , (self.canvas_height-30) # definition de sa taille 
        self.id = canvas.create_image(x, y, image=self.image_player) # création du defender avec son image

    # fonction de deplacement du defender avec la valeur dx 
    def move_in(self, canvas, dx):
        canvas.move(self.id, dx, 0) # deplacement du defender avec la valeur dx 

    def fire(self, canvas):
        if(len(self.fired_bullets)< self.max_fired_bullets):
            self.id = 1
            self.newBullet = Bullet(self.id) 
            self.fired_bullets.append(self.newBullet.install_in(self.canvas))
            son_tire = "tire.wav"
            win.PlaySound(son_tire, win.SND_FILENAME | win.SND_ASYNC)
        else:
            son_tire = "recharge.wav"
            win.PlaySound(son_tire, win.SND_FILENAME | win.SND_ASYNC)
    
    def move_bullet(self, canvas):
           for i in range(0,len(self.fired_bullets)):
            x1,y1,x2,y2 = self.canvas.bbox(self.fired_bullets[i]) # position du bullet dans la fenêtre du jeu
            if (y1 < 0) :    # verification du depassement du bullet hors de la fenêtre du jeu
                self.canvas.delete(self.fired_bullets[i]) # destruction du bullet 
                del self.fired_bullets[i]  # diminution du nombre de bullet tiré
                break
            else:
                self.newBullet.move_in(self.canvas, self.fired_bullets[i]) # deplacement du bullet 

class Creation_Abris(object):
    def __init__(self, nb_abris):
        self.liste_abris = []
        self.brique = []
        self.fleet = Fleet()
        self.height = self.fleet.get_height()
        self.width = self.fleet.get_width()
        self.nb_abris = nb_abris

    def get_liste_bris(self):
        return self.liste_abris

    def get_coord_brique(self):
        return self.brique

    def install_brique(self, canvas):
        i=0
        x= 20
        y= self.height - 120
        self.canvas = canvas
        while i < self.nb_abris: 
            limitebloc_x = x + 200
            limitebloc_y = y +60
            depart_bloc_sv = x
            while y  < limitebloc_y:
                while x < limitebloc_x :
                    self.liste_abris.append(self.canvas.create_rectangle(x, y, x+20, y+20, fill = "purple"))
                    x+=20
                x = depart_bloc_sv
                y+= 20
            i+=1
            x+= (self.width / self.nb_abris)
            y-=60

    
        

    
class Bullet(object):
    def __init__(self, shooter):
        self.radius=5
        self.color = "red"
        self.speed = 15
        self.id = None
        self.shooter = shooter
        self.defender = Defender()

    def install_in(self, canvas):
        x1, y1 =canvas.coords(self.shooter) # coordonnées du defender
        self.id=canvas.create_oval(x1+(15/2), y1-(15/2)-1, x1+(15/2)+self.radius, y1-(15/2)+self.radius, fill=self.color, outline=self.color)
        return self.id
   
    def move_in(self, canvas, tire):
        self.circl = tire
        canvas.move(self.circl, 0, -self.speed)  # deplacement du bullet vers le haut de la fenêtre



class Game:
    def __init__(self, frame):
        self.frame=frame # création du frame 
        self.fleet = Fleet()
        self.height = self.fleet.get_height() # longeur du frame
        self.width = self.fleet.get_width() # largeur du frame 
        self.canvas = tk.Canvas(self.frame, width=self.width, height=self.height, bg = "black")
        self.defender = Defender()
        self.abris = Creation_Abris(3)
        self.abris.install_brique(self.canvas)
        self.defender.install_in(self.canvas) # affichage du defender dans la fenêtre du jeux
        self.bullet = Bullet(self.canvas)
        self.fleet.install_in(self.canvas)
        self.canvas.pack()

    # fonction de deplacement du defender
    def keypress(self, event):
        self.gap = self.defender.move_delta # variable du defender en pixel qui se trouve dans la class defender
        x, y,  = self.canvas.coords(self.defender.id)
        if event.keysym == 'Left':
            self.gap = -10
        elif event.keysym == 'Right':
            self.gap = 10  
        elif event.keysym == 'space':
            self.defender.fire(self.canvas)

        if((x+self.gap > 0) and (x+self.gap < self.width and event.keysym == 'Left' or event.keysym == 'Right')) : # limitation du deplacement à l'interieur de la fênetre du jeux
            self.defender.move_in(self.canvas, self.gap) # deplacement du defender vers la droite ou la gauche
            


    def start_animation(self):
        self.texte = StringVar()
        label = Label(self.canvas, textvariable = self.texte, fg = "#000fff000", bg = "#000000")
        self.canvas.create_window(self.width -100 , 15, window = label)
        self.canvas.after(10, self.animation)

    def animation(self):
        self.defender.move_bullet(self.canvas) # animation du bullet
        self.fleet.move_in(self.canvas)
        self.fleet.manage_touched_aliens_by(self.canvas,self.defender)
        self.texte.set("Score : " + str(self.fleet.get_score()) + " " + "Vies restant : " + str(self.defender.get_vies()))
        self.canvas.after(100, self.animation)



class SpaceInvaders(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Space Invaders")
        self.frame=tk.Frame(self.root, width=800, height=500, bg = "green")
        self.frame.pack()
        self.game=Game(self.frame)


    def start(self):
        self.game.start_animation()
        self.root.bind("<Key>", self.game.keypress)
        self.root.mainloop()


        


SpaceInvaders().start()
