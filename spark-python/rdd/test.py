
import enchant
word = "hello"
#ascii A-Z (65-90), a-z (97-122)
ascii_word = ord(word[0])
if ascii_word > 65 and ascii_word < 90:
    print ("A-Z")
elif ascii_word > 97 and ascii_word < 122:
    print("a-z")