# 7) \<.BOSS.>/ 
# მომხმარებელს შემოაყვანით ორი რიცხვი
# --> დაუარეთ ყველა რიცვს ამ დიაპაზონში
# --> დაბეჭდეთ მხოლოდ რიგით მესამე რიცხვი ამ შუალედში რომელიც იყოფა 3-ზე(შეწყვიტეთ ციკლი თუ არის ეგეთი)

first = int(input("enter first number: "))
second = int(input("enter second number: "))

num = 0

for i in range(first, second, + 1):
    if i % 3 == 0:
        num += 1
        if num == 3:
            print(i)
            break
