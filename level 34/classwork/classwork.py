# 1) მომხმარებელს შემოატანინე სიტყვა ანდა ტექსტი.  
# გაიგე ამ სიტყვის/ტექსტის სიგრძე და დაპრინტე 
# for ციკლით დაბეჭდე ამ სიტყვის თითოეული ასო ცალცალკე.

text = input("enter any word or text: ")
print(len(text))

for i in range(len(text)):
    print(text[i])