# 3) მომხმარებელს შემოატანინეთ წინადადება.  
# -> დაუარეთ ტექსტს for ციკლით  
# -> გამოტოვეთ ყველა space => ' '
# -> დაბეჭდეთ ყველა დანარჩენი სიმბოლო  


sentence = input("enter some sentence: ")

for i in sentence:
    if i == ' ':
        continue
    print(i)
