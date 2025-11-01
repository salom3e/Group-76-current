# 2) შექმენით სია სხვადასხვა სიტყვებით.  
# -> for loop-ით დაბეჭდეთ მხოლოდ ის სიტყვები, რომელთა სიგრძე ზუსტად იყოფა 15-ზე.

words = ["cinema", "water", "khinkali", "sushi", "guitar", "mitsisqveshagadasasvleli"]
for i in words:
    if len(i) % 15 == 0:
        print(i)
