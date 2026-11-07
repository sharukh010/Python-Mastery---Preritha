word1 = "Preritha" # title case 
word2 = "PRERITHA" # capital case 
word3 = "harry potter"
print(word1.lower())# this will not make any changes in original 
print(word2.lower())
print(word1.lower() == word2.lower())
print(word3.title()) # harry potter -> Harry Potter 
print(word3.capitalize())# harry potter -> Harry potter
print(word3.upper())