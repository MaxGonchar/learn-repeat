from tkinter import Tk

from learn_repeat.errors import error_logger
from learn_repeat.ui.mainscreen import MainScreen


@error_logger
def main():
    window = Tk()
    MainScreen(window)
    window.mainloop()


if __name__ == '__main__':
    main()
