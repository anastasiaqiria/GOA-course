# for loop & while loop-ს შორის განსხვავება ის არის რომ for loop-ით ვიცით ზუსტი იტერაციის რაოდენობა ხოლო while loop-ზე არა სანამ პირობა true-ს არ გამოიტანს
# for loop-ს ვიყინებთ როდესაც ვიცით იტერაციის ზუსტი რაოდენობა
# while loop-ს ვიყენებთ როდესაც წინასწარ არ ვიცით რამდენი იტერაცია დაგვჭირდება

# შემქნით passowrd ცვლადი და შეინახეთ პაროლი, შემდგომ მომხმარებელს შემოატანინეთ პაროლი და
# შეამომწე სანამ მომხმარებლის მიერ შემოყვანილი პაროლი არ უდრის password - ს იქამდე შემოაყვანინე მომხმარებელს პაროლი

password = "091322"

user_password = input("Enter your password: ")

while user_password != password:
    print("Your password is inncorrect, try again")
    user_password = input("Enter your password again: ")

print("Your password is correct!")

# while loop ის მშევეობით გამოითანე 1 დან 10 ის ჩათვლით რიცხვები

a = 1

while a <= 10:
    print(a)
    a += 1

# while loop ის მეშვეობით გამოიტანეთ 20 მდე მხოლო ლუწი რიცხვები

i = 2

while i <= 20:
    print(i)
    i += 2




