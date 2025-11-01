# 4) შექმენით სია სხვადასხვა სიტყვებით.  
# -> for loop-ით დაბეჭდეთ მხოლოდ ის სიტყვები, რომელთა სიგრძე ზუსტად 5 სიმბოლოა.

word = ["gvino", "electro", "hollywood", "partygirl", "movie"]
for i in word:
    if len(i) == 5:
        print(i)