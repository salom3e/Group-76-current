# 4) შექმენით სტრინგებით სავსე სია, და ამ სიიდის ყველა ის სიტყვა რომლის პირველი ასო არის Uppercase-ში და რომელიც ამავდროულად 
# დგას კენტ ინდექსზე სიაში, გაუხადეთ ასეთ სიტყვებს ყველა ასო პატარა - lowercase, ხოლო ყველა ის სიტყვა რომლის პირველი ასო 
# არის Uppercase-ში და თან ეს სიტყვა დგას ლუწ ინდექსზე სიაში, ამოშალეთ სიიდან. დაპრინტეთ შეცვლილი სია.

words = ["music", "Disco", "ball", "glitter", "Gems", "Stage", "artist", "DJ", "dance"]

for i in range(len(words) - 1, -1, -1): 
    if words[i][0] == words[i][0].upper(): 
        if i % 2 == 1:      
            words[i] = words[i].lower()
        else:                
            words.pop(i)

print(words)
