from src.chainsaw import *
from src.component import *
from src.rule import *
from src.minify import *

import sys

try:
    sys.argv[1]
except:
    input = input("Please enter chainsaw testing command (chainsaw/minify): ")
else:
    input = sys.argv[1]

if input == "chainsaw":
    red = Rule({"font-family" : "'I have spaces'"})
    h1 = Component("h1", "h2", "h3")
    h1.addRule(red)

    style = Chainsaw(h1)

    print(style)

elif input == "minify":
    css = '''\
    body {
        font-decoration: underline;
        moo: spam;
        robocop: true;
    }

    h1 {
        color: red;
        stuff: foo;
        bar: spam;
        font-family: "Font with Spaces", sans-serif;
        /* Comment! */
    }
    '''

    print(minify(css))

else:
    print("\nUnknown command!\n")
    print('''\
The testing commands are:
- chainsaw (Testing the library)
- minify (Testing the minifier)

The commands can also be provided as arguments:
    python ''' + sys.argv[0] + ''' chainsaw\
''')
