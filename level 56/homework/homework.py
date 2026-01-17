# 1) შექმენით წინადადების სტრინგის ცვლადი, ამ ცვლადში დაითვალეთ ხმოვანი ასოების რაოდენობა. გამოიყენეთ for ციკლი.

sentence = "i like red nail polish"
count = 0

for i in sentence:
    if i in "aeiou":
        count += 1
print(count)







