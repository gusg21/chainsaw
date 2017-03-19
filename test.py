from chainsaw import *

import sys

try:
    sys.argv[1]
except:
    input = input("Please enter chainsaw testing command (chainsaw/minify/loader): ")
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

    print("WITHOUT COMMENTS: \n\n" + minify(css))
    print("\n\nWITH COMMENTS: \n\n" + minify(css, removeComments=False))
    print("\n\nKEEP LAYOUT: \n\n" + minify(css, keepLayout=True))

elif input == "loader":

    css = '''\
body {
    font-decoration: underline;
    moo: spam;
    robocop: true;
}

h1, h2 {
    color: red;
    stuff: foo;
    bar: spam;
    font-family: "Font with Spaces", sans-serif;
    /* Comment! */

}
    '''

    style = Chainsaw()
    style.load(css) # Parse and create Rule and Component objects from raw css

    sampleComp = Component("img") # Add some user defined stuff to make sure everything is working
    sampleRule = Rule({"width" : "120%"})
    sampleComp.addRule(sampleRule)
    style.addComponent(sampleComp)

    print(style.minify())

else:
    print("\nUnknown command!\n")
    print('''\
The testing commands are:
- chainsaw (Testing the library)
- minify (Testing the minifier)
- loader (Testing the loader)

The commands can also be provided as arguments:
    python ''' + sys.argv[0] + ''' chainsaw\
''')
