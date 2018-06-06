from tkinter import *
from random import randint

class RandomBall:
    def __init__(self,canvas,swidth,sheight):
        self.canvas=canvas
        self.radius=randint(30,70)
        self.xpos=randint(self.radius,int(swidth)-self.radius)
        self.ypos=randint(self.radius,int(sheight)-self.radius)
        self.xv=randint(6,12)
        self.yv=randint(6,12)
        self.swidth=swidth
        self.sheight=sheight
        
        r=lambda :randint(0,255)
        self.color='#%02x%02x%02x' % (r(),r(),r())
    
    def create_ball(self):
        x1=self.xpos-self.radius
        y1=self.ypos-self.radius
        x2=self.xpos+self.radius
        y2=self.ypos+self.radius
        self.itm=self.canvas.create_oval(x1,y1,x2,y2,fill=self.color,outline=self.color)
    
    def move_ball(self):
        self.xpos+=self.xv
        self.ypos+=self.yv
        if self.ypos>=self.sheight-self.radius:self.yv=-self.yv
        if self.ypos<=self.radius:self.yv=-self.yv
        if self.xpos>=self.swidth-self.radius:self.xv=-self.xv
        if self.xpos<=self.radius:self.xv=-self.xv
        self.canvas.move(self.itm,self.xv,self.yv)
        
class ScreenSaver:
    
    def __init__(self,num_balls=1):
        self.root=Tk()
        self.root.bind('<Any-KeyPress>',self.myquit)
        self.root.bind('<Motion>',self.myquit)
        self.root.bind('<Escape>',lambda e:exit())
        self.root.overrideredirect(1)
        # self.root.attributes('-alpha',0.1)
        w,h=self.root.winfo_screenwidth(),self.root.winfo_screenheight()
        print(w,h)
        self.canvas=Canvas(self.root,width=w,height=h)
        self.balls=[]
        for i in range(num_balls):
            ball=RandomBall(self.canvas,w,h)
            ball.create_ball()
            self.balls.append(ball)
        self.canvas.pack()
        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()
        if self.canvas:
            self.canvas.after(20,self.run_screen_saver)
                 
    def myquit(self,e):
        self.root.destroy()

if __name__=='__main__':
    ScreenSaver(1)
    ScreenSaver(10)