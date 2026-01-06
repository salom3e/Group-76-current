# 4) შექმენით ქალაქების სია, წაშალეთ pop() ან remove() ფუნქციით ყველა ის სიტყვა რომლის ყველა ასო არის დიდი, ხოლო ყველა სხვა 
# სიტყვას ყველა ასო გაუხადეთ დიდი. დაპრინტეთ საბოლოო შედეგი. გამოიყენეთ while ციკლი.

cities = ["PARIS", "London", "BERLIN", "Telavi", "ROME", "Tbilisi"]
i = 0

while i < len(cities):
    if cities[i] == cities[i].upper():
        cities.remove(cities[i])
    else:
        cities[i] = cities[i].upper()
        i += 1                           
print(cities)



# while i < len(cities):
#     if cities[i] == cities[i].upper():
#         cities.pop(i)
#     else:
#         cities[i] = cities[i].upper()
#         i += 1
# print(cities)
