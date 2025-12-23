# 1) შექმენით სახელებით სავსე სია და ასევე ცარიელი სია: Upper_name = [].  სახელების სიიდან ცარიელ სიაში ჩაამატეთ ყველა ის სახელი 
# რომელიც იწყება დიდი ასოთი, გამოიყენეთ for ციკლი და შესაფერისი სიის და სტრინგის ფუნქციები.

names = ["Meryl", "Julia", "Audrey", "gwen", "marilyn", "gemma", "Monica", "nicole", "gabrielle", "anne", "scarlett"]
upper_name = []

for name in names:
    if name[0] == name[0].upper():
        upper_name.append(name) 

print(upper_name)
