# 5) შექმენით 2 სია, პირველი სია იყოს სავსე 5 ცალი ქალაქის სახელებით, და მეორე სიაში მოთავსებული იყოს 10 ქვეყნის სახელი. თქვენი 
# დავალებაა რომ ქვეყნის სახელებში ჩაამატოთ ყველა ქალაქის სახელები ცალ-ცალკე მენულე ინდექსიდან მეოთხე ინდექსის ჩათვლით. 
# გამოიყენეთ for ციკლი და შესაბამისი ფუნქციები.


cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi", "Telavi"]
countries = ["Georgia", "France", "Italy", "Germany", "Spain", "Japan", "USA", "Brazil", "India", "England"]

for i in range(len(cities)):
    countries.insert(i, cities[i]) 
print(countries)
