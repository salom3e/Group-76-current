# 3) შექმენით სტრინგებით სავსე სია და ამ სიიდან ამოშალეთ ყველა ის სიტყვა რომელიც არის ან 6-ზე ნაკლები სიგრძეში, 
# ან რომელიც მთავრდება დიდი ასოთი.

words = ["music", "disco", "balL", "glitteR", "gemS", "stagE", "artist", "DJ", "dance"]

for i in range(len(words) - 1, -1, -1):
    if len(words[i]) <= 6 or words[i][-1] == words[i][-1].upper():
        words.pop(i)

print(words)
