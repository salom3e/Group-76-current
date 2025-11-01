# 5) მომხმარებელს შემოატანინე წინადადება.  
# -> გაიგე რამდენი სიმბოლოა წინადადებაში.  
# -> for ციკლით დათვალე რამდენი აso "a" ან "A" არის ტექსტში.

sentence = input("enter some sentence: ")
print(len(sentence))

count = 0
for i in sentence:
    if i == "a" or i == "A":
        count += 1
print(count)
