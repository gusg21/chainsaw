# chainsaw [![GitHub release](https://img.shields.io/github/release/gusg21/chainsaw.svg)](http://github.com/gusg21/chainsaw) [![Travis branch](https://img.shields.io/travis/rust-lang/rust/master.svg)](http://travis-ci.org/gusg21/chainsaw/) [![GitHub issues](https://img.shields.io/github/issues/gusg21/chainsaw.svg)](https://github.com/gusg21/chainsaw/issues) [![GitHub forks](https://img.shields.io/github/forks/gusg21/chainsaw.svg)](https://github.com/gusg21/chainsaw/network) [![GitHub stars](https://img.shields.io/github/stars/gusg21/chainsaw.svg)](https://github.com/gusg21/chainsaw/stargazers) [![GitHub license](https://img.shields.io/badge/license-Apache%202-blue.svg)](https://raw.githubusercontent.com/gusg21/chainsaw/master/LICENSE) [![Awesomeness](https://img.shields.io/badge/awesomeness-off%20the%20charts-brightgreen.svg)](http://sanger.dk/)
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

That will test three current major functions of chainsaw.

## License

Apache License, Version 2.0

See the LICENSE file
