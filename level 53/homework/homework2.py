# 2) შექმენით სიტყვებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა და პირველი ასო არის g, მაშინ ახალ სიაში ჩაამატეთ სახელი "Goga", 
# თუ სიტყვის ყველა ასო არის დიდი ან იწყება ასო N-თი, მაშინ სიაში ჩაამატეთ სახელი "Nika", სხვა შემთხვევაში სიაში ჩაამატეთ 
# სიტყვა "ლიდერი". დაპრინტეთ მიღებული სია.

words = ["MUSIC", "disco", "gems", "Neon", "ball", "glitter", "Stage", "artist", "DJ", "dance", "Nightlife"]
new = []

for i in words:
    if i == i.lower() and i[0] == "g":
        new.append("Goga")
    elif i == i.upper() or i[0] == "N":
        new.append("Nika")
    else:
        new.append("Leader")
print(new)
