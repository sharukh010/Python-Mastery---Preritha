"""
Harry       Potter 
Harry Potter
removing spaces: 
HarryPotter
HarryPotter
"""
word1 = "harry Potter"
word2 = "harry       Potter"
word1 = word1.lower() # we are updating the original string 
word2 = word2.lower()
print(word1.replace(" ",""))
print(word2.replace(" ",""))