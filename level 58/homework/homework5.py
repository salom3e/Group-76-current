# 5) შექმენით ყველანაირი მონაცემთა ტიპების ელემენტებით სავსე სია, ამოშალეთ ყველა დუპლიკატები - ყველაფერი რაც მეორდება 
# 2-ზე მეტჯერ, გამოიყენეთ remove() ფუნქცია და while ციკლი.

datas = [1, "lala", 2.5, True, "nana", 1, 26, 2.5, False, 1, "wori", "jori", "jori"]
i = 0

while i < len(datas):
    if datas.count(datas[i]) > 1:
        datas.remove(datas[i])
    else:
        i += 1
print(datas)
