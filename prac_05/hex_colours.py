HEX_TO_COLOUR = {}

NAME_TO_HEX = {'Absolute Zero': '#0048ba', 'Acid Green': '#b0bf1a', 'AliceBlue': '#f0f8ff',
               'Alizarin crimson': '#e32636', 'Amaranth': '#e52b50', 'Amber': '#ffbf00'}

hex_name = input("Enter hex name: ").title()
while hex_name != "":
    try:
        print(hex_name, "is", NAME_TO_HEX[hex_name])
    except KeyError:
        print("Invalid hex name")
    hex_name = input("Enter hex name: ").title()
