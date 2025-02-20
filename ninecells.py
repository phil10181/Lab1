"""
Author: Philip Kwan
Project 1
File: ninecells.py 

"""

from breezypythongui import EasyFrame

class LayoutDemo(EasyFrame):
    """Displays labels in the window's quadrants."""

    def __init__(self):
        """Sets up the window and the labels."""
        EasyFrame.__init__(self)
        for r in range(3): #loop accross rows
            for c in range(3): #loop columns within rows
                self.addLabel(text = f"({r}, {c})", row = r, column = c, sticky="we")

def main():
    """The starting point for launching the program."""
    LayoutDemo().mainloop()

# Instantiates and pops up the window.
if __name__ == "__main__":
    main()
