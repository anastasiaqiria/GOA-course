# ლოგიკური ოპერატორები არსებობს And, or და not-ი
# for loop-ის შექმნის დროს ჩვენ ვიცით ზუსტი იტერაციის რაოდენობა ხოლო while loop-ის დროს კი არ ვიცით
# თუ იტერაცია  რამდენჯერ განმეორდება სანამ პასუხი true არ იქნება
# def გამოიყენება ფუნქციის შესაქმნელად და ის გვჭირდება და გვეხმარება იმისთვის რომ ერთი და იგივე კოდი ბევრჯერ არ დავწეროთ, 
# ხოლო ფუნქციის შემდეგ შეგვიძლია რომ ის გამოვიძახოთ რამდენჯერაც გვინდა

# 1
correct_name = 'Anastasia'
name = input('enter your name: ')

while name != correct_name :
    print('სახელი არასწორია სცადეთ თავიდან')
    name = input('enter your name again: ')

print('სახელი სწორია')

# 2
list = [20, 'Hello world', 'Dog', 3.14, False, 'GOA']
list.pop(1)
list.append('Goa Best')
print(list)

# 3
def info(Name,Surname,Age):
    print('i am', Name, Surname, 'And i am', Age, 'Years Old')

info('Anastasia','Qiria', 13)