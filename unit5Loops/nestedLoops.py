'''
Program to print all two-letter domain names.

ord('a') --> take a character and return the ASCII #
chr(97) --> take an ASCII # and return the character
'''

print("\n\nTwo-letter domain names: ")

letter1 = "a"
letter2 = "?"
while letter1 <= "z":    # Outer loop
    letter2 = "a"
    while letter2 <= "z":    # Inner loop
        print(f"{letter1}{letter2}.com")
        letter2 = chr(ord(letter2) + 1)    # Protects us from an infinite loop
    letter1 = chr(ord(letter1) + 1)    # Protects us from an infinite loop