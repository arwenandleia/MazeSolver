from tkinter import Tk,BOTH,Canvas


class Window():
    def __init__(self,window_height,window_width):
        self.root = Tk() #initializing new root widget
        self.root.title = "MyWindow" #setting a title for root
        self.canvas = Canvas(self.root,width=window_width,height=window_height)     #creating a canvas with height and width 
                                                                                    #make sure that width and heigh positoin is okay
        self.canvas.pack(fill=BOTH,expand=1) # packing the canvas 
        self.is_window_running=False
        self.root.protocol("WM_DELETE_WINDOW",self.close)
    
    def redraw(self): #redraw method for the window
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.is_window_running=True
        
        while self.is_window_running:
            self.redraw()
    
    def close(self):
        self.is_window_running=False

    def draw_line(self,line_instance,fill_colour="black"):
        line_instance.draw(self.canvas,fill_colour)


class Point():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
class Line():
    def __init__(self,point_1,point_2) :
        self.point_1=point_1
        self.point_2=point_2
    
    def draw(self,canvas_to_draw,fill_colour):
        x1,y1=self.point_1.x,self.point_1.y
        x2,y2=self.point_2.x,self.point_2.y
        canvas_to_draw.create_line(x1,y1,x2,y2,fill=fill_colour,width=2)
        canvas_to_draw.pack(fill=BOTH,expand=1)
