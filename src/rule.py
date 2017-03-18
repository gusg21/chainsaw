class Rule():

    rules = {}
    CSS = None

    def __init__(self, rules):
        self.rules = rules
        self.CSS = ""
        self.parseCSS()

    def parseCSS(self):
        index = 0
        for rule in self.rules:
            index += 1
            type = rule
            value = self.rules[rule]
            if index == len(self.rules):
                self.CSS += \
                "\t{}: {};"\
                .format(type, value)
            else:
                self.CSS += \
                "\t{}: {};\n"\
                .format(type, value)
