from chainsaw.minify import minify
from chainsaw.load import load

class Chainsaw:

    # Set all future-use variables to None
    rawCSS = None

    def __init__(self, *components):
        # Initialize the variables
        self.rawCSS = "" # The actual CSS the object contains
        for component in components: # Add all components given as arguments
            self.addComponent(component)

    def __repr__(self): # String representing the object
        return "<Chainsaw Stylesheet content:\"" + self.rawCSS.replace("\n", "")[:20] + "...\">"

    def __str__(self): # printed by print(ChainsawObject)
        return self.rawCSS

    def addComponent(self, *components): # Adding given component's CSS
        # Iterate over given components
        for component in components:
            self.rawCSS += component.CSS

    def minify(self):
        # Minify the rawCSS variable
        self.rawCSS = minify(self.rawCSS)
        return self.rawCSS # return for use in-line

    def load(self, string): # Load objects from a string (SEE: load.py)
        components = load(string)
        for component in components: # Add returned components
            self.addComponent(component)
