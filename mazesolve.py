from graphics import Window,Line,Point
from cell import Cell,Maze


def main():
    win = Window(800,600)
    
    num_rows=10
    num_cols=15
    x_size=25
    y_size=25

    m1=Maze(15,15,num_rows,num_cols,x_size,y_size,win)

    win.wait_for_close()


if __name__ == "__main__":
    main()

