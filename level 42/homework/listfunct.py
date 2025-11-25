# extend() - სიის გაერთიანება

# აერთიანებს 2 სიას

name = ["salome", "qeti", "anano", "taso", "tina"]

nums = [4, 55, 6, 67, 26]

name.extend(nums)
print(name)


nums.extend(name)
print(nums)

# ჯერ ვწერთ იმ ცვლადის სახელს, რომელშიც უნდა გაერთიანდეს, ხოლო extend-ს ეძლევა არგუმენტად იმ ცვლადის სახელი, რომელიც
# პირველ ცვლადშ უნდა გაერთანდეს



# clear() - შლის ყველა ელემენტს სიიდან

list = ["rara", "lala", "baba", "papa"]

list.clear()
print(list)


# index() - გვიბრუნებს არგუმენტად გადაცემული ელემენტის ინდექსს.

name = ["salome", "qeti", "anano", "taso", "tina", "qeti"]

name.remove("qeti")

print(name.index("taso"))



# count() - ითვლის ფრჩხილებში გადაცემული ელემენტის რაოდენობას სიაში.

name = ["salome", "qeti", "anano", "taso", "tina", "qeti"]

print(name.count("qeti"))



# reverse() - ატრიალებს სიას უკუღმა

name = ["salome", "qeti", "anano", "taso", "tina", "qeti"]
name.reverse()
print(name)