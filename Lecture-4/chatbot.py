question1 = "What is your name?"
answer1 = "My name is Chatbot AI, nice to meet you!"

question2 = "What is your favourite colour?"
answer2 = "My favourite colour is purple"

question3 = "What do you like to eat?"
answer3 = "Great question but unfortunately I cannot eat as I am an AI and don't have a favorite food"

question4 = "What is the weather today?"
answer4 = "Unknown information"

question5 = "What is your favorite sport?"
answer5 = "I love badminton!"

print("Chatbot:")
while True: # infinite loop 
    prompt = input("Prompt: ")
    if prompt == question1:
        print(f"Response: {answer1}")
    elif prompt == question2: 
        print(f"Response: {answer2}")
    elif prompt == question3:
        print(f"Response: {answer3}")
    elif prompt == question4: 
        print(f"Response: {answer4}")
    elif prompt == question5: 
        print(f"Response: {answer5}")
    else: 
        print("Sorry couldn't answer the question.")