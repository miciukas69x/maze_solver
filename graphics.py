from tkinter import Tk, BOTH, Canvas

Class Window:
    def __init__(self, width, height):
            self.width = width
            self.height = height
            self.__root = Tk()
            self.__root.title("Maze Solver")
            self.__canvas = Canvas(self.__root, width=self.width, height=self.height)
            self.__canvas.pack(fill=BOTH)
            self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()