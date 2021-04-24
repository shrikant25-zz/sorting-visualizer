import pygame
import random
import threading
import algorithms

pygame.init()  # creates pygame instance
screen = pygame.display.set_mode((1200, 600))  # sets the size of window
pygame.display.set_caption("Sorting Visualizer")  # sets the title

# following is the dictionary containing colors
color = {1: [0, 128, 0],  # green
         2: [255, 0, 0],  # red
         3: [0, 0, 0],  # black
         4: [250, 250, 250],  # white
         5: [0, 0, 128],  # blue
         6: [42, 53, 61],  # dark-gray
         7: [200, 200, 200],  # silver
         8: [255, 255, 0]}  # yellow

numoflines = 75

screen.fill(color[3])  # fills the screen background with color from dictionary


class Game:
    def __init__(self):
        self.quicksortbutton = Button(240, 550, 80, 30, 'arial', 20, 'QuickSort', 6, 7)
        self.mergesortbutton = Button(330, 550, 85, 30, 'arial', 20, 'MergeSort', 6, 7)
        self.bubblesortbutton = Button(425, 550, 85, 30, 'arial', 20, 'BubbleSort', 6, 7)
        self.heapsortbutton = Button(520, 550, 80, 30, 'arial', 20, 'HeapSort', 6, 7)
        self.insertionsortbutton = Button(610, 550, 100, 30, 'arial', 20, 'InsertionSort', 6, 7)
        self.newlistbutton = Button(720, 550, 70, 30, 'arial', 20, 'New List', 6, 7)
        self.list = []
        self.isalgorunning = False  # flag to checks if the particular part is running
        self.runningthreadname = None  # stores the name of the thread

    def createlist(self):
        if self.list:
            self.clearlist()
        for i in range(1, numoflines):
            randnum = random.randint(10, 300)
            node = Node(i, randnum)
            self.list.append(node)

    def clearlist(self):
        for node in self.list:
            node.drawrect(3)
        self.list.clear()

    def rungame(self):
        self.createlist()
        running = True  # variable is used to keep loop running
        while running:
            for event in pygame.event.get():  # checks for the event
                if event.type == pygame.QUIT:  # if event type is quit, then proceed to quit the window
                    pygame.quit()  # end the pygame instance
                    quit()  # close the window

                #  checks if thread exists and is it dead or not
                if self.runningthreadname is not None and self.runningthreadname.is_alive() is False:
                        self.isalgorunning = False
                        self.runningthreadname = None

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (
                        self.isalgorunning is False):  # checks if mouse button is pressed

                    if self.newlistbutton.chechkifclicked():
                        pygame.display.flip()
                        self.createlist()

                    elif self.bubblesortbutton.chechkifclicked():
                        self.isalgorunning = True
                        bubblesort = algorithms.Bubble(self.list)
                        t1 = threading.Thread(target=bubblesort.bubble)
                        self.runningthreadname = t1
                        t1.start()

                    elif self.insertionsortbutton.chechkifclicked():
                        self.isalgorunning = True
                        insertionsort = algorithms.Insertion(self.list)
                        t1 = threading.Thread(target=insertionsort.insertion)
                        self.runningthreadname = t1
                        t1.start()

                    elif self.heapsortbutton.chechkifclicked():
                        self.isalgorunning = True
                        heapsort = algorithms.Heap(self.list)
                        t1 = threading.Thread(target=heapsort.heap)
                        self.runningthreadname = t1
                        t1.start()

                    elif self.mergesortbutton.chechkifclicked():
                        self.isalgorunning = True
                        mergesort = algorithms.Merge(self.list)
                        t1 = threading.Thread(target=mergesort.merge)
                        self.runningthreadname = t1
                        t1.start()

                    elif self.quicksortbutton.chechkifclicked():
                        self.isalgorunning = True
                        quicksort = algorithms.Quick(self.list)
                        t1 = threading.Thread(target=quicksort.quick)
                        self.runningthreadname = t1
                        t1.start()


class Node:
    def __init__(self, xcoord, height):
        self.xcoord = (xcoord * 12) + 100
        self.ycoord = 100
        self.height = height
        self.width = 8
        self.drawrect()

    def drawrect(self, flag=4,
                 wait=False):  # function to draw rectangle, excepts color-code, x-coordinate and y-coordinate
        pygame.draw.rect(screen, color[flag], [self.xcoord, self.ycoord, self.width,
                                               self.height])  # inbuilt pygame function to create rectangles
        pygame.display.update()  # updates the screen
        if wait is True:
            pygame.time.wait(1)


class Button:  # class use to create buttons
    def __init__(self, bxcoord, bycoord, bwidth, bheight, bfontname, bfontsize, btext, bcolorcode, btextcolor):
        self.bxcoord = bxcoord  # x-coordinate
        self.bycoord = bycoord  # y-coordinate
        self.bwidth = bwidth  # width
        self.bheight = bheight  # height
        self.bfontname = bfontname  # fontname
        self.bfontsize = bfontsize  # fontsize
        self.btext = btext  # text on button
        self.bcolorcode = bcolorcode  # backgroundcolor
        self.btextcolor = btextcolor  # text color
        self.createbutton()  # calls the create button function

    def createbutton(self):  # function to create button
        pygame.draw.rect(screen, color[self.bcolorcode], [self.bxcoord, self.bycoord, self.bwidth, self.bheight])
        # create an instance for font object
        smalltext = pygame.font.SysFont(self.bfontname, self.bfontsize)
        # get the surface and and rectangle to store the text
        textsurf, textrect = self.text_objects(self.btext, smalltext)
        # align the rectangle
        textrect.center = (int(self.bxcoord + (self.bwidth / 2)), int(self.bycoord + (self.bheight / 2)))
        # blit draws one thing on another
        # here it draws the textsurface on textrect
        screen.blit(textsurf, textrect)
        pygame.display.flip()

    # this function returns the surface fo text and a rectangle to hold text on surface
    def text_objects(self, text, font):
        # renders text on surface and returns the surface
        # the returned surface will be the dimensions required to hold the surface
        textsurface = font.render(text, True, color[self.btextcolor])
        # textsurface provides the dimensions
        # while textsurface.get_rect() provides the rectangle to store
        # finally returns the surface (variable = textsurface)
        # textsurface.get_rect() creates returns a new rectangle covering the surface
        return textsurface, textsurface.get_rect()

    def chechkifclicked(self):  # checks if the button is clicked
        mousex, mousey = pygame.mouse.get_pos()  # gets the x and y coordinates of mouse's current position
        # if the position of mouse is within the button does the stuff and returns 1 else returns 0
        if self.bxcoord <= mousex <= self.bxcoord + self.bwidth and self.bycoord <= mousey <= self.bycoord + self.bheight:
            self.bcolorcode = 1  # colorcode is changed
            self.createbutton()  # button is recreated with new color
            pygame.display.flip()
            pygame.time.wait(50)
            self.bcolorcode = 6  # colorcode is changed
            self.createbutton()  # button is recreated with new color
            return 1
        return 0


if __name__ == '__main__':
    game = Game()
    game.rungame()
