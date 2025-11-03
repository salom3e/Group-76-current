# 4) მომხმარებელს შემოატანინეთ წინადადება.  
# -> დაუარეთ მას for ლუპით  
# -> გამოტოვეთ ხმოვნები (a, e, i, o, u)  
# -> დაბეჭდეთ მხოლოდ თანხმოვნები და თავისთავათ ყველა სხვა სიმბოლო 

sentence = input("enter some sentence: ")

for i in sentence:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        continue
    print(i)
