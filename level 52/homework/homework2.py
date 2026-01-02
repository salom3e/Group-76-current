# 2) შექმენით სტრინგის ცვლადი და ცარიელი სია. სტრინგში მყოფი დიდი ასოები გახადეთ პატარა და ამ სიაში ჩაამატეთ, ხოლო სტრინგში 
# მყოფი პატარა ასოები გახადეთ დიდი და ასევე ჩააგდეთ ამ სიაში. დაპრინტეთ საბოლოო სია, გამოიყენეთ while ციკლი.

word = "MuSiC Is TiMe MachiNe"
empty = []

i = 0
while i < len(word):
    if word[i] == word[i].upper() and word[i] != word[i].lower():
        empty.append(word[i].lower())
        
    elif word[i] == word[i].lower() and word[i] != word[i].upper():
        empty.append(word[i].upper())
    i += 1
print(empty)
