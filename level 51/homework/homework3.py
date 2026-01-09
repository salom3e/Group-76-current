# 3) შექმენით string წინადადების ცვლადი, ამ წინადადებიდან დაპრინტეთ მხოლოდ ხმოვანი ასოები.

sent = "pop music will never be low brow"
empty = ""

for i in sent:
    if i in "aeiou":
       empty += i
print(empty)

