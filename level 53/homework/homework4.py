# 4) შექმენით სიტყვებით სავსე სია, თუ სიტყვის სიგრძე არის 6-ზე მეტი ან მისი ყველა ასო არის დიდი, ამ სიტყვის ყველა ასო გახადეთ 
# პატარა და ჩაამატეთ ახალ სიაში. ყველა სხვა შემთხვევაში ახალ სიაში ჩაამატეთ შეუცვლელი სიტყვა ოღონდ გადაბმულად ორჯერ, 
# მაგალითად თუ მოცემული იქნება სიტყვა "Nika", ჩაამატეთ "NikaNika". გამოიყენეთ while ციკლი.

words = ["MUSIC", "DISCO", "gems", "neon", "ball", "GLITTER", "stage", "ARTIST", "DJ", "dance", "NIGHTLIFE"]
new = []

i = 0
while i < len(words):
    if len(words[i]) > 6 or words[i] == words[i].upper():
        new.append(words[i].lower())
    else:
        new.append(words[i] + words[i])
    i += 1
print(new)