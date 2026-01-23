# 6) მომხმარებელს შემოატანინეთ წინადადება და დაპრინტეთ ამ წინადადებაში მყოფი ყველაზე გრძელი სიტყვა, 
# გამოიყენეთ while ციკლი, არ გამოიყენოთ max() ფუნქცია.

sentence = input("enter some sentence: ")
word = sentence.split()
i = 0
longest = word[0]

while i < len(word):
    if len(word[i]) > len(longest):
        longest = word[i]
    i += 1
print(longest)
