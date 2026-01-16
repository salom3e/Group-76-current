# 7) შექმენით წინადადების სტრინგის ცვლადი და ცარიელი სია, ცარიელ სიაში ჩაამატეთ სიტყვები ცალ-ცალკე, არა ასოები, 
# არამედ მთლიანი სიტყვები. ამაზე იჭყლიტეთ ტვინი, წარმატებებს გისურვებთ.

sentence = "khinkali is very delicious"
words = []
word = ""

for i in sentence:
    if i != " ":
        word += i
    else:
        words.append(word)
        word = ""
words.append(word)

print(words)

