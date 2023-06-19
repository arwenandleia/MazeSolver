from graphics import Window,Line,Point
import time

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
        ):
        self._x1=x1
        self._y1=y1
        self._num_rows=num_rows
        self._num_cols=num_cols
        self._cell_size_x=cell_size_x
        self._cell_size_y=cell_size_y
        if win:
            self._win=win
        else:
            self._win = None
        self._create_cells()
        self._break_entrance_and_exit()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall=False
        self._draw_cell(0,0)

        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall=False
        self._draw_cell(self._num_cols-1,self._num_rows-1)

    def _create_cells(self):
        self._cells=[]
        
        for i in range(self._num_cols):
            col_cells=[]
            for j in range(self._num_rows):
                curr_x1 = self._x1 + i*self._cell_size_x
                curr_x2 = curr_x1 + self._cell_size_x
                curr_y1 = self._y1 + j*self._cell_size_y
                curr_y2 = curr_y1 + self._cell_size_y
                new_cell = Cell(self._win, curr_x1,curr_y1,curr_x2,curr_y2)
                if self._win:
                    new_cell.draw()
                col_cells.append(new_cell)
                
            self._cells.append(col_cells)
    
    def _draw_cell(self,i,j):
        cell_in_use = self._cells[i][j]
        
        curr_x1 = self._x1 + i*self._cell_size_x
        curr_x2 = curr_x1 + self._cell_size_x
        curr_y1 = self._y1 + j*self._cell_size_y
        curr_y2 = curr_y1 + self._cell_size_y

        cell_in_use.draw(curr_x1,curr_y1,curr_x2,curr_y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.1)
        



class Cell():
    def __init__(self,win=None,x1=0,y1=0,x2=0,y2=0):
        self.has_left_wall=True
        self.has_right_wall=True
        self.has_top_wall=True
        self.has_bottom_wall=True
        if win:
            self._win = win
        else:
            self._win = None
        self._x1=x1
        self._x2=x2
        self._y1=y1
        self._y2=y2
    
    def draw(self,x1=None,y1=None,x2=None,y2=None):
        if x1:
            self._x1=x1
        if x2:
            self._x2=x2
        if y1:
            self._y1=y1
        if y2:
            self._y2=y2
    
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x1,self._y2)))
        else:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x1,self._y2)),"white")

        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2,self._y1),Point(self._x2,self._y2)))
        else:
            self._win.draw_line(Line(Point(self._x2,self._y1),Point(self._x2,self._y2)),"white")
        
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x2,self._y1)))
        else:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x2,self._y1)),"white")

        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1,self._y2),Point(self._x2,self._y2)))
        else:
            self._win.draw_line(Line(Point(self._x1,self._y2),Point(self._x2,self._y2)),"white")

    def draw_move(self,to_cell,undo=False):
        centre_of_self = Point((self._x1+self._x2)/2,  (self._y1+self._y2)/2 )
        center_of_other = Point((to_cell._x1+to_cell._x2)/2,  (to_cell._y1+to_cell._y2)/2 )
        color_to_fill="red"
        
        if undo:
            color_to_fill="gray"

        self._win.draw_line(Line(centre_of_self,center_of_other),color_to_fill)
        
    