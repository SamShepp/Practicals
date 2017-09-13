COLOUR_CODES = {"AliceBlue": "#f0f8ff", "Azure4" : "#838b8b",
                "Bisque": "#8b7d6b", "Blue1": "#0000ee", "Black": "#000000",
                "Chartreuse3": "#66cd00", "Chocolate": "#d2691e",
                "Coral": "#ff7f50", "CornflowerBlue": "#6495ed",
                "DarkGoldenrod": "#b8860b"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for {} is {}".format(colour_name,COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")