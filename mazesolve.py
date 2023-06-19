from graphics import Window,Line,Point
from cell import Cell,Maze


def main():
    win = Window(800,600)
    
    num_rows=20
    num_cols=14
    x_size=30
    y_size=30

    m1=Maze(15,15,num_rows,num_cols,x_size,y_size,win,seed=1)

    win.wait_for_close()


if __name__ == "__main__":
    main()

