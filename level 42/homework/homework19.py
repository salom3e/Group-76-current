# 19)შექმენი სია letters = ["a", "b", "c"]. მომხმარებელს შემოატანინე ასო, შემდეგ insert()-ით ჩასვი ის სიის შუაში 
# (ცენტრალურ ინდექსზე). დაბეჭდე სია.

letters = ["a", "b", "c"]

user = input("enter some letter: ")

letters.insert(1, user)
print(letters)