print (' PALINDROME TESTER  ')
original_string = input("Enter a string\n")
# reverse the string
reversed_string = original_string[::-1]
# compare original and reversed string
if(original_string == reversed_string):
    print("String is palindrome")
else:
    print("String is not palindrome")


# palindrome mean a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run.
