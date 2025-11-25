# 1) შექმენით ორი სია ერთი სახელების მეორე float ენის,შენი დავალებაა რომ გააერთიანო ეს ორი სია 
# ერთმანეთშდ ა დაპრინტო განახლებული სია


strings = ["moda", "mediana", "diapazoni", "sashualo aritmetikuli", "fardobiti sixshire"]

floats = [1.2, 2.3, 9.8, 6.7, 4.69]

strings.extend(floats)
print(strings)


floats.extend(strings)
print(floats)