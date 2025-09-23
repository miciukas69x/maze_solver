from graphics import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)

    c1 = Cell(win)
    c1.draw(50, 50, 200, 200)

    win.wait_for_close()



if __name__ == "__main__":
    main()