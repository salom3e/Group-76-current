# 5) მომხმარებელს შემოაყვანით ორი რიცხვი
# --> დაუარეთ ყველა რიცვს ამ დიაპაზონში
# --> დაბეჭდეთ მხოლოდ რიგით პირველი რიცხვი ამ შუალედში რომელიც იყოფა 15-ზე(შეწყვიტეთ ციკლი თუ არის ეგეთი)

first = int(input("enter first number: "))
second = int(input("enter second number: "))


for i in range(first, second, + 1):
    if i % 15 == 0:
        print(i)
        break