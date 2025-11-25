# 23)შექმენი სია queue = ["first", "second"].  მომხმარებელს შემოატანინე ახალი ელემენტი და insert()-ით ჩასვი სიის დასაწყისში. 
# შემდეგ if-ით შეამოწმე სიის სიგრძე — თუ უფრო დიდია 5-ზე, pop()-ით ამოშალე ბოლო ელემენტი; ბოლოს დაბეჭდე სია, 
# თუ არ არის 5-ზე მეტი დაბეჭდე შებრუნებული სია.

queue = ["first", "second"]

user = input("enter new element: ")

queue.insert(0, user)

if len(queue) > 5:
    queue.pop(-1)
else:
    queue.reverse()
print(queue)
