# chainsaw
CSS Stylesheet creator made in pure Python

## How to

```python
    from src.chainsaw import *
    from src.component import *
    from src.rule import *
    from src.minify import *

    boldRed = Rule({"color" : "red", "font-weight" : "bold"}) # Define the styles in the rule
    h1 = Component("h1") # Create a component to hold the Rules, and make it apply to the HTML tag h1
    h1.addRule(boldRed) # Apply the rule to the component
    style = Chainsaw(h1) # Create the stylesheet and give it h1

    print(style) # You can get the raw CSS by using the Chainsaw object like a string
```

## Installing

To setup/install the requirements for chainsaw:

    $ make install

Then, to make sure everything's going well:

    $ make
    -- snip --
    $ make minify
    -- snip --
    $ make loader
    -- snip --

That will test two current major functions of chainsaw.

## License

Apache License, Version 2.0

See the LICENSE file
