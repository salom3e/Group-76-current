# 2) შექმენი ფუნქცია სახელად check_even()

# ფუნქციის შიგნით შექმენი ცვლადი სადაც შიინახავ რაიმე რიცხვს

# შემდეგ შეამოწმე-->

# თუ ცვლადში შენახული რიცხვი არის ლუწი --- ფუნქციამ დააბრუნოს ==> "this number is even"

# სხვა შემთხვევაში --- ფუნქციამდ ააბრუნოს ==> "this number is odd"

def check_even():

    num = 26
    if num % 2 == 0:
        return "this number is even"
    else:
        return "this number is odd"

print(check_even())
    