from src.minify import minify

class Chainsaw:

    # Set all future-use variables to None
    rawCSS = None

    def __init__(self, *components):
        # Initialize the variables
        self.rawCSS = ""
        for component in components:
            self.addComponent(component)

    def __repr__(self):
        return "<Chainsaw Stylesheet content:\"" + self.rawCSS.replace("\n", "")[:20] + "...\">"

    def __str__(self):
        return self.rawCSS

    def addComponent(self, component):
        # Iterate over current components
        self.rawCSS += component.CSS

    def minify(self):
        self.rawCSS = minify(self.rawCSS)
