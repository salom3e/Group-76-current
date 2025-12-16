# 4) შექმენით სიტყვებით სავსე სია და ამ სიაში ყველა ისეთ სიტყვას რომელიც იწყება პატარა ასოთი, პირველი ასო გაუხადეთ დიდი. 
# გამოიყენეთ for ციკლი და სტრინგის შესაბამისი ფუნქცია.


words = ["music", "Disco", "ball", "glitter", "Gems", "Stage", "artist", "DJ", "dance"]

for i in range(len(words)):
    if words[i][0] == words[i][0].lower():
        words[i] = words[i].capitalize() 

print(words)
