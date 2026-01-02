# 2) შექმენით სახელებით სავსე სია, მომხმარებელს შემოატანინეთ რაიმე რიცხვი, 
# და ამ რიცხვის ინდექსზე ჩაამატეთ სახელი "ნიკა" თქვენს სიაში.

names = ["Meryl", "Julia", "Audrey", "Marilyn", "Monica", "Nicole", "Gabrielle", "Anne", "Scarlett"]
num = int((input("enter some number: ")))

names.insert(num, "ნიკა")
print(names)