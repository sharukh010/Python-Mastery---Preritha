"""
I am sitting on a chair 
I am standing on a chair


I am happy to see you
I am sad to see me 

sit -> stand 
sleep -> wake 
sitting -> standing 
sleeping -> waking 
you -> me 
he -> she 
do -> don't 
happy -> sad
"""
sentence = input("Enter a sentence: ").lower().split()
for word in sentence: 
    match word: 
        case "sit": 
            print("stand",end=" ")
        case "sleep": 
            print("wake",end=" ")
        case "sitting": 
            print("standing",end=" ")
        case "sleeping": 
            print("waking",end=" ")
        case "you": 
            print("me",end=" ")
        case "he": 
            print("she",end=" ")
        case "do": 
            print("don't",end=" ")
        case "happy": 
            print("sad",end=" ")
        case "stand": 
            print("sit",end=" ")
        case "wake": 
            print("sleep",end=" ")
        case "standing": 
            print("sitting",end=" ")
        case "waking": 
            print("sleepping",end=" ")
        case "me": 
            print("you",end=" ")
        case "she": 
            print("he",end=" ")
        case "don't": 
            print("do",end=" ")
        case "sad": 
            print("happy",end=" ")
        case _ : 
            print(word,end=" ")