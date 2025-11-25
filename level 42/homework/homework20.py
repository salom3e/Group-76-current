# 20)შექმენი სია values = [1, 2, 3, 4]. მომხმარებელს შემოატანინე ინდექსი. თუ ინდექსი სიის ფარგლებშია, pop()-ით 
# ამოშალე შესაბამისი ელემენტი; თუ არა, დაბეჭდე "Index out of range". ბოლოს დაბეჭდე სია.


values = [1, 2, 3, 4]
user = int(input("enter index: "))

if 0 <= user < len(values):
    values.pop(user)
else:
    print("Index out of range")

print(values)