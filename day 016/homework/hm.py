#დაწერე პროგრამა, რომელიც მომხმარებლისგან შეიტანს სტუდენტის მიღებულ ქულას (0-დან 100-მდე)
#და if-else პირობით გამოიტანს შესაბამის ნიშანს შემდეგი წესით:

score = int(input("Enter Your score: "))
if 90 <= score <= 100:
     print("A")
elif 80 <= score <= 89:
     print("B")
elif 70 <= score <= 79:
     print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F")


#მომხმარებელს შემოატანინეთ რიცხვი და if else თი შეამოწმეთ არის თუ არა რიცხვი უარყოფითი ან დადებითი

number = float(input("Enter a number: "))
if number > 0:
     print("შენი რიცხვი დადებითია")
elif number < 0:
     print("შენი რიცხვი უარყოფითია")
else:
     print("შენი რიცხვი ნულია")


#შემოატანინეთ მომხმარებელს ორი რიცხვი, და შეამოწმეთ, თუ პირველი რიცხვი მეორეზე მეტია, 
#მაშინ დაპრინტეთ "First Number is Greater than second one", სხვა შემთხვევაში, 
#"Second Number is Greater than first one"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("First Number is Greater than second one")
else:
    print("Second Number is Greater than first one")


#მომხმარებელს შემოატანინეთ ერთი რიცხვი და შეამოწმეთ არის თუ არა რიცხვი ლუწი ან კენტი

number = int(input("შეიყვანეთ რიცხვი: "))

if number % 2 == 0:
    print("რიცხვი ლუწია")
else:
    print("რიცხვი კენტია")

#მომხმარებელს შემოატანინეთ ტემპერატურა ცელსიუსში.
# ტემპერატურა 0-ზე ნაკლებია → დაპრინტეთ “Cold ❄️”,
#თუ 0–30 შორისაა → დაპრინტეთ “Normal 🌤️”,
#თუ 30-ზე მეტია → დაპრინტეთ “Hot ☀️”.

temperature = float(input("Enter Your Temperature: "))
if temperature < 0:
     print("Cold ❄️")
elif 0 <= temperature <= 30:
     print("“Normal 🌤️")
else:
     print("Hot ☀️")






