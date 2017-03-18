def minify(css, removeComments=True, keepLayout=False):

    index = -1
    string = False
    comment = False
    finalCSS = ""

    if not keepLayout:
        remove = { # remove no matter what
            "\n",
            "\t"
        }
    else:
        remove = {}

    removeNotString = { # remove if we aren't in a string
        " "
    }

    stringChars = { # characters that start AND END a string
        "\"",
        "\'"
    }

    for char in css:
        index += 1
        if char in stringChars: # check if we're starting a string
            string = not string

        if removeComments: # In case you don't want to remove comments
            if char == "/" and css[index + 1] == "*": # if the current char is / and the next is * turn on comment
                comment = True

            if css[index - 1] == "/" and css[index - 2] == "*": # Same as above, but look back on it to ensure
                comment = False                                 # we've passed the the */ and that has been removed

        if char in remove: # don't add char if on remove list
            continue

        if char in removeNotString and not string: # don't add if on non-string remove list
            continue

        if comment:
            continue

        finalCSS += char

    return finalCSS
