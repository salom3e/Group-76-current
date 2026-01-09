# 5) მოცემული გაქვთ სტრინგის ცვლადი: numbers = "0123456789", ამ სტრინგიდან ახალ სიაში ჩაამატეთ ყველა ის რიცხვი რომელიც დგას 
# ამ სტრინგის ლუწ ინდექსზე ან არის 7-ზე მეტი, სიაში ეს რიცხვები იყოს როგორც integer ტიპის მონაცემები და არა სტრინგები. 
# დაწერეთ ორივე ხერხით, for ციკლით და while ციკლით.

numbers = "0123456789"
new = []

for i in range(len(numbers)):
    if i % 2 == 0 or int(numbers[i]) > 7:
        new.append(int(numbers[i]))
print(new)

numbers = "0123456789"
new = []

i = 0
while i < len(numbers):
    if i % 2 == 0 or int(numbers[i]) > 7:
        new.append(int(numbers[i]))
    i += 1
print(new)
