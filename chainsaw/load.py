import re
from chainsaw.component import *
from chainsaw.rule import *

def load(string):
    components = [] # The returned components
    scanning = False # Whether we're scanning the inside of a component or not
    currentComp = None # When we're scanning a component, add the found rules to this temporary component

    for line in string.splitlines(): # Iterate over each line
        pLine = line.strip() # pLine is the processed line

        if matchesAll(r"}", pLine): # If we're at the end of a Component
            scanning = False # Stop scanning
            components.append(currentComp) # Add the current component
            currentComp = None # Clear the current component

        if scanning: # If we're scanning
            try: part1 = pLine[:pLine.index(':')].strip() # Get the text up to the ":"
            except: part1 = None # If it's not there ignore this line
            try: part2 = pLine[pLine.index(':') + 1:pLine.index(';')].strip() # Get the text from the ":" to the ";"
            except: part2 = None # Again, ignore if not there

            if part1 != None and part2 != None: # If we found both
                rule = Rule({part1 : part2}) # Make a rule out of what we found
                currentComp.addRule(rule) # Add the rule to the current component

        if matchesAll(r"(.*)(\s*){", pLine): # If we're at the start of a component
            scanning = True # Start scanning this component
            argsString = pLine[:pLine.rfind(" ")] # Isolate the HTML tags it applies to
            args = argsString.split(", ") # Turn that string into a list
            currentComp = Component(*args) # Pass the list as a new component

    return components # Return the components

def matchesAll(regex, str):  # A small function to check if the regex is the
    cReg = re.compile(regex) # entire string, no more, no less
    try: found = cReg.search(str).group() # Get what the regex found
    except: found = str + "moo" # To make sure we aren't matching the original string
    if found == str: # Check if it is the same as the string
        return True
    else:
        return False
