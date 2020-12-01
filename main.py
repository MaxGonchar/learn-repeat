from tkinter import Tk

from learn_repeat.ui.mainscreen import MainScreen


def main():
    window = Tk()
    MainScreen(window)
    window.mainloop()


if __name__ == '__main__':
    main()
