# 8) შექმენით სტრინგის ცვლადი და შემოაბრუნეთ ეს სტრინგი. არ გამოიყენოთ slicing. და ყველა ასო გაუხადეთ დიდი. 
# დაპრინტეთ საბოლოო სტრინგი.

word = "sacivi"
reverse = ""

for i in word:
    reverse = i.upper() + reverse
print(reverse)
