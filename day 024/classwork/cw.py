#1
def count_x(word):
    count = 0
    for letter in word:
        if letter == "x":
            count += 1
    
    print(count)

print("xxboxx")


#2
def average(arr):
    total = 0
    count = 0
    for num in arr:
        total += num
        count += 1

    avg = total / count
    print(avg)

average ([1, 2, 4, 5])


#3
def count_odd(arr):
    even_count = 0
    odd_count = 0

    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("ლუწი რიცხვები:", even_count )
    print("კენტი რიცხვები:", odd_count )


count_odd([1, 2, 3, 4, 5, 6, 7, 8, 9])


#4
def multiply(arr):
    for i in arr:
        print(i * 2)

multiply([1, 2, 3, 4, 5]) #5 aura chamomaklo andria maswma







    

