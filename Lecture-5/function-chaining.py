sentence = "I Like Harry Potter book."
prompt = " i like Harry Potter book."
# print(sentence.lower().replace(" ",""),)
"""
sentence.lower().replace(" ","")
"i like harry potter book.".replace(" ","")
"ilikeharrypotterbook."
"""
# If a function returns nothing you cannot perform function chaining 
# to perform function chaining it must return the updated value 
print(sentence.lower().replace(" ","") == prompt.lower().replace(" ",""))