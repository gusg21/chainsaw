import re
from src.component import *
from src.rule import *

def load(string):
    components = []
    scanning = False

    for line in string.splitlines(): # Iterate over each line
        pLine = line.strip() # pLine is the processed line

        if matchesAll(r"}", pLine):
            scanning = False
            components.append(currentComp)
            currentComp = None

        if scanning:
            try: part1 = pLine[:pLine.index(':')].strip()
            except: part1 = None
            try: part2 = pLine[pLine.index(':') + 1:pLine.index(';')].strip()
            except: part2 = None

            if part1 != None and part2 != None:
                rule = Rule({part1 : part2})
                currentComp.addRule(rule)

        if matchesAll(r"(.*)(\s*){", pLine): # If we're at the start of a component
            scanning = True
            argsString = pLine[:pLine.rfind(" ")]
            args = argsString.split(", ")
            currentComp = Component(*args)

    return components

def matchesAll(regex, str):
    cReg = re.compile(regex)
    try: found = cReg.search(str).group()
    except: found = str + "moo" # To make sure we aren't matching the original string
    if found == str:
        return True
    else:
        return False
