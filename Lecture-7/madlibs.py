story = """In a quiet -(1)-, an old clockmaker named -(2)- lived surrounded by hundreds of ticking clocks. Some ticked fast, like nervous birds. Others ticked slow, like deep-sea breath. -(2)- believed every person carried an invisible clock inside their chest, and it was his job to listen.
-(3)-, a small boy named -(4)- pushed open the shop door. -(4)- did not want a watch fixed. He placed a tiny, silent silver pocket watch on the glass counter.
"It stopped when my grandfather went away," -(4)- whispered.
-(2)- picked up his jeweler's loupe, peered into the tiny brass gears, and smiled. He did not touch a screwdriver. Instead, he pulled a small bronze key from his pocket and handed it to the boy.
"Your grandfather didn't lose time, -(4)-," -(2)- said gently. "He just left it with you to keep wound up with your own laughter."
-(4)- turned the key once against the back of the silent watch. A soft, clear tick broke the quiet room, followed by another. Outside, the rain stopped, and a single ray of sunlight pierced through the misty glass of the shop window."""
count = 0 
while True: 
    print(story)
    if count == 4:
        print("Story completed")
        break 
    blank_number = int(input("Blank Number: "))
    if blank_number > 0 and blank_number <= 4: 
        count += 1 
    content = input("Content: ")
    story = story.replace(f"-({blank_number})-",content)