class Rule():

    rules = {} # All the rules in the object
    CSS = None # The compiled CSS of the object

    def __init__(self, rules): # providing a dictionary as rules (e.g: {"color" : "blue"})
        self.rules = rules
        self.CSS = ""
        self.parseCSS()

    def parseCSS(self): # Parse the CSS from the rules
        index = 0 # For iterating over the rules
        for rule in self.rules:
            index += 1
            type = rule # Type is the key
            value = self.rules[rule] # Value is the key's value
            if index == len(self.rules): # If we're on the last index, don't add a newline at the end
                self.CSS += \
                "\t{}: {};"\
                .format(type, value)
            else: # otherwise add one
                self.CSS += \
                "\t{}: {};\n"\
                .format(type, value)
