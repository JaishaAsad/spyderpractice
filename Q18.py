print ( '  VOWEL AND COSONANT COUNTER ')
text = input("Please Enter Your Text : ")
vowels = 0
consonants = 0

for i in text:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1
 
print("Total Number of Vowels in this Text = ", vowels)
print("Total Number of Consonants in this Text = ", consonants)
