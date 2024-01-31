alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"

with open('secret.txt') as f:
    text = f.read()

print(text)
#1. split the text into lines (split by /n)
#2. use a for loop to iterate over the lines
#3. iterate over the vowels and count how many times vowel appear in the line
#4. "decode" the letter on that line by indexing the alphabet with the vowel count
#5. print the decoded letter

lines = text.split("\n")
decoded_text = ("")
print(lines)
for line in lines:
    num_vowels = 0
    # for v in vowel
    # num_vowels += line.count