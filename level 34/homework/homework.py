# 1) შექმენით სია სადაც შეინახავთ სხვადასხვა ქალაქების სახელებს.  
#    for loop ით დაბეჭდეთ მხოლოდ ის ქალაქები, რომელთა სახელის სიგრძე მეტია 6-ზე.

cities = ["Tbilisi", "Telavi", "London", "Berlin", "Brasília", "New York", "Tokyo"]

for i in cities:
    if len(i) > 6:
        print(i)
        