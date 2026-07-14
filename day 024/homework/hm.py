# დაწერე ფუნქცია, რომელიც პრინტავს :
# "Hello, World!"


def greeting():
    print("Hello, World!")

greeting()


# დაწერე ფუნქცია, რომელიც იღებს სახელს და პრინტავს :
# "Hello, <სახელი>"
# მაგალითი: "Hello, Nika"

def greet():
    name = input('Enter your name: ')
    print("Hello," + name)

greet()



# დაწერე ფუნქცია, რომელიც იღებს ორ რიცხვს და პრინტავს მათ ჯამს.


def sum_numbers():
    a = int(input('Enter first number: '))
    b = int(input('Enter Second number: '))
    print(a + b)

sum_numbers()


# დაწერე ფუნქცია, რომელიც იღებს ერთ რიცხვს და პრინტავს :

# "ლუწი" თუ ლუწია
# "კენტი" თუ კენტია



def evenodd():
    num = int(input('Enter any number: '))
    if num % 2 == 0:
        print('ლუწი')
    else:
        print('კენტი')

evenodd()


# დაწერე ფუნქცია, რომელიც იღებს რიცხვს და პრინტავს მის გაორმაგებულ მნიშვნელობას.


def number():
    num = int(input('Enter Your number: '))
    print(num * 2)

number()



