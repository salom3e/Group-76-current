# 2) მომხმარებელს შემოატანინეთ წინადადება და დაითვალეთ თუ ამ წინადადებაში რამდენი სიტყვის სიგრძე არის 4-ზე მეტი, 
# დაპრინტეთ ასეთი სიტყვების რაოდენობა, მაგალითად 4. გამოიყენეთ while ციკლი.

sentence = input("enter some sentence: ")
i = 0
count = 0
word = sentence.split()

while i < len(word):
    if len(word[i]) > 4:
        count += 1
    i += 1
print(count)
