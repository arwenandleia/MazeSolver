from graphics import Window,Line,Point
import time
import random

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
            seed=None,
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
        
        if not seed:
            random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self,i,j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.is_visited=True
        if i==self._num_cols-1 and j==self._num_rows-1:
            return True
        to_visit_list=[]
        self.immediate_cells_to_visit(i,j,to_visit_list)
        for neighbour in to_visit_list:
            new_i=neighbour[0]
            new_j=neighbour[1]
            if self._is_there_no_wall(i,j,new_i,new_j):
                new_cell=self._cells[new_i][new_j]
                current_cell.draw_move(new_cell)
                if self._solve_r(new_i,new_j):
                    return True
                else:
                    current_cell.draw_move(new_cell,undo=True)

        return False


    def _is_there_no_wall(self,i,j,new_i,new_j):
        
        if new_i>i: # to right
            return not self._cells[i][j].has_right_wall
        elif new_i<i: # to left
            return not self._cells[i][j].has_left_wall
        elif new_j>j: # to bottom
            return not self._cells[i][j].has_bottom_wall
        elif new_j<j: #to top
            return not self._cells[i][j].has_top_wall
        else:
            return False


    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].is_visited=False

    def _break_walls_r(self,i,j): # i will represent the column and j the row in that column
        current_cell = self._cells[i][j]
        current_cell.is_visited=True
        
        while True:
            self._to_visit_list=[]
            self.immediate_cells_to_visit(i,j,self._to_visit_list)
            if len(self._to_visit_list)==0:
                self._draw_cell(i,j)
                return
            rnd_choice = random.choice(self._to_visit_list)
            new_i=rnd_choice[0]
            new_j=rnd_choice[1]
            self._knock_down_wals(i,j,new_i,new_j)
            self._break_walls_r(new_i,new_j)


    def _knock_down_wals(self,i,j,new_i,new_j):
        cell_one = self._cells[i][j]
        cell_two = self._cells[new_i][new_j]

        #cell two on the right
        if new_i>i:
            cell_one.has_right_wall=False
            cell_two.has_left_wall=False
            
        #cell two on the left
        if new_i<i:
            cell_one.has_left_wall=False
            cell_two.has_rigt_wall=False
        #cell two on the top
        if new_j<j:
            cell_one.has_top_wall=False
            cell_two.has_bottom_wall=False
        #cell two on the bottom
        if new_j>j:
            cell_one.has_bottom_wall=False
            cell_two.has_top_wall=False

            
    def immediate_cells_to_visit(self,i,j,to_vist):
        #check top
        cell_col=i
        cell_row=j-1
        if cell_col>=0 and cell_col<self._num_cols and cell_row>=0 and cell_row <self._num_rows:
            if not self._cells[cell_col][cell_row].is_visited:
                to_vist.append( (cell_col,cell_row))
        
        #check bottom
        cell_col=i
        cell_row=j+1
        if cell_col>=0 and cell_col<self._num_cols and cell_row>=0 and cell_row <self._num_rows:
            if not self._cells[cell_col][cell_row].is_visited:
                to_vist.append( (cell_col,cell_row))
        
        #check right
        cell_col=i+1
        cell_row=j
        if cell_col>=0 and cell_col<self._num_cols and cell_row>=0 and cell_row <self._num_rows:
            if not self._cells[cell_col][cell_row].is_visited:
                to_vist.append( (cell_col,cell_row))
        
        #check left
        cell_col=i-1
        cell_row=j
        if cell_col>=0 and cell_col<self._num_cols and cell_row>=0 and cell_row <self._num_rows:
            if not self._cells[cell_col][cell_row].is_visited:
                to_vist.append( (cell_col,cell_row))
        

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
        self.is_visited=False
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
        
    