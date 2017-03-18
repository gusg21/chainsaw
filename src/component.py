class Component:

    CSS = None
    to = ""
    rules = ""

    def __init__(self, *to):
        self.to = ", ".join(to)

        self.CSS = ""
        self.parseCSS()

    def __repr__(self):
        return "CSS: \"" + self.CSS + "\""

    def parseCSS(self):
        self.CSS = \
        '''\
{} {{
    {}}}\
        '''.format(self.to, self.rules)

    def addRule(self, *rules):
        for rule in rules:
            self.rules += rule.CSS + "\n"
        self.parseCSS()
