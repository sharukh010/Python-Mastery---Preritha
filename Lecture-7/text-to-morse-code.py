text = input("Text: ").upper()
morse_code = ""

for character in text: 
    match character: 
        case "A": 
            morse_code += ".-"
            # morse_code = morse_code + ".-"
        case "B": 
            morse_code += "-..."
        case "C": 
            morse_code += "-.-."
        case "D": 
            morse_code += "-.."
        case "E": 
            morse_code += "."
        case "F": 
            morse_code += "..-."
        case "G": 
            morse_code += "--."
        case "H": 
            morse_code += "...."
        case "I": 
            morse_code += ".."
        case "J": 
            morse_code += ".---"
        case "K": 
            morse_code += "-.-"
        case "L": 
            morse_code += ".-.."
        case "M": 
            morse_code += "--"
        case "N": 
            morse_code += "-."
        case "O": 
            morse_code += "---"
        case "P": 
            morse_code += ".--."
        case "Q": 
            morse_code += "--.-"
        case "R": 
            morse_code += ".-."
        case "S": 
            morse_code += "..."
        case "T": 
            morse_code += "-"
        case "U":
            morse_code += "..-" 
        case "V":
            morse_code += "...-" 
        case "W": 
            morse_code += ".--"
        case "X": 
            morse_code += "-..-"
        case "Y": 
            morse_code += "-.--"
        case "Z": 
            morse_code += "--.."
        case "0": 
            morse_code += "-----"
        case "1": 
            morse_code += ".----"
        case "2": 
            morse_code += "..---"
        case "3": 
            morse_code += "...--"
        case "4": 
            morse_code += "....-"
        case "5": 
            morse_code += "....."
        case "6": 
            morse_code += "-...."
        case "7": 
            morse_code += "--..."
        case "8": 
            morse_code += "---.."
        case "9": 
            morse_code += "----."
        case " ": 
            morse_code += "/"
    morse_code += " "
print(morse_code)