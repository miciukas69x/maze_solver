from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    p1 = Point(50, 50)
    p2 = Point(200, 150)
    line = Line(p1, p2)

    win.draw_line(line, "red")
    win.wait_for_close()



if __name__ == "__main__":
    main()