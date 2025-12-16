# 3) შექმენით სახელებით სავსე სია და ამ სიიდან ამოშალეთ ყოველი ის სიტყვა რომელიც იწყება ასო გ-თი და მთავრდება ასო ი-თი, 
# გამოიყენეთ for ციკლი, დაწერეთ ორივე ხერხით, pop() ფუნქციითაც და remove() ფუნქციითაც.


names = ["meryl", "julia", "audrey", "gwen", "marilyn", "gemma", "monica", "nicole", "gabrielle", "anne", "scarlett"]


for i in range(len(names) - 1, -1, -1):
    if names[i][0] == "g":
        names.pop(i)

print(names)


