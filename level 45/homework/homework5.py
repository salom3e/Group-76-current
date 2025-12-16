# 5) შექმენით სიტყვებით სავსე სია, ამ სიიდან ამოშალეთ ყველა სიტყვა რომელიც იწყება Uppercase დიდი ასო G-თი და რომლის ბოლო 2 ასო 
# არის ასევე Uppercase. ხოლო ყველა სიტყვა რომლის თითოეული ასო არის Lowercase-ში, აიყვანეთ Uppercase-ში შესაბამისი სტრინგის 
# ფუნქციის გამოყენებით. დაპრინტეთ მიღებული სია.


words = ["GorilLA", "monkey", "GorgasaLI", "snake", "ROCK", "gaga", "madonna", "club"]

for i in range(len(words) - 1, -1, -1):
    if words[i][0] == "G" and words[i][-2:] == words[i][-2:].upper():
        words.pop(i)

    elif words[i] == words[i].lower():
        words[i] = words[i].upper()

print(words)
