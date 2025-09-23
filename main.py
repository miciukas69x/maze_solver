from graphics import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)

    c1 = Cell(win)
    c1.draw(50, 50, 200, 200)

    c2 = Cell(win)
    c2.draw(200, 50, 350, 200)

    c2.draw_move(c1, undo=True)
    c1.draw_move(c2)


    win.wait_for_close()



if __name__ == "__main__":
    main()