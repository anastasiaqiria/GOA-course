password = 123678

user_password = int(input("შეიყვანეთ პაროლი: "))

while user_password != password:
    print(" პაროლი არასწორია, შეიყვანე თავიდან")
    user_password = int(input("შეიყვანე პაროლი ხელახლა: "))

print("შენი შეყვანილი პაროლი სწორია")
