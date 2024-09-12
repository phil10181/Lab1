"""
File: countergui.py
"""

from breezypythongui import EasyFrame

class NumberGuessGUI(EasyFrame):
    """View for a counter."""
    def __init__(self, model):
        self.model= model
        self.commands=0

        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self, title = "Guessing game")

        # Instance variable to track the count.
        #self.counter = counter

        self.label = self.addLabel(text = "my guess is " + str(model.guess()) + " for " + str(self.commands), #what does guess do? 
                                  row = 0, column = 0,
                                  sticky = "NSEW",
                                  columnspan = 3)

        # Three command buttons.
        self.addButton(text = "Too low",
                       row = 1, column = 0,
                       command = self.low)

        self.addButton(text = "Too high",
                       row = 1, column = 1,
                       command = self.high)

        self.addButton(text = "Correct",
                       row = 1, column = 2,
                       command = self.correct)


    # Methods to handle user events.
    def high(self):
        """Increments the counter and updates the display."""
        self.model.high()
        self.commands+=1
        self.label["text"] = "my guess is " + str(self.model.guess()) + " for " +  str(self.commands)
 
    def low(self):
        """Decrements the counter and updates the display."""
        self.model.low()
        self.commands+=1
        self.label["text"] = "my guess is " + str(self.model.guess()) + " for " +  str(self.commands)

    def correct(self):
        """Resets the counter and updates the display."""
        self.model.correct()
        self.commands+=1
        self.label["text"] = "yay I win!"
