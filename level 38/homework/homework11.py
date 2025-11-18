# 11)მომხმარებელს შემოაყვანინე ორი რიცხვი start , end და step , თქვენი დავალებაა დაატრიალოთ 
# ფორ ციკლი start იდან end ამდე და სტეპი იყოს step,ამ დიაპაზონში გამოიტანეთ ტერმინალში მხოლოდ ლუწი რიცხვები

start = int(input("enter start number: "))
end = int(input("enter end number: "))
step = int(input("enter step number: "))

for i in range(start, end, step):
    if i % 2 == 0:
        print(i)