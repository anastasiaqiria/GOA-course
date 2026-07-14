# 1) კომენტარებით ახსენით რა არის mutable და imutable

# immutable-არის როდესაც არ შეგიძლია იმის შეცვლა რასაც შექმნი, მაგ: თუ შექმენი ცვლადი ის უცვლელია და ვეღარ შეცვლი.
# mutable-არის ისეთი რამ რაც შეგიძლია რომ შეცვალო, მაგ: თუ სიას შეცვლი შეგიძლია შენ რომ ის შცვალო.


# 2) კომენტარებით ახსენით რას გამოიტანს ეს კოდი
# name = "luka"
# name[2] = "l"
# print(name)

# ეს კოდი ერორს გამოიტანს რადგან სტრინგი immutable არის და არ შეგვიძლია მისი შეცვლა


# 3) შექმენი სია groups = ['group75', 'group76', 'group77', 'group79']
# და შემდეგ შეცვალე ბოლო ინდექსი 'group78'-ით გამოიყენეთ მინუს ინდექსინგი


groups = ['group75', 'group76', 'group77', 'group79']
groups[-1] = 'group78'

print(groups)


# 4) შექმენი სია fruits = ["apple", "banana", "orange", "strawberry", "grape", "mango", "pineapple"]
# და პირველი სამი ელემენტი შეცვალე ამით ["carrot", "broccoli", "spinach"]


fruits = ["apple", "banana", "orange", "strawberry", "grape", "mango", "pineapple"]
fruits[0] = 'carrot'
fruits[1] = 'broccoli'
fruits[2] = 'spinach'

print(fruits)

