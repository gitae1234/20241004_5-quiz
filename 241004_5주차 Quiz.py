#1
def add(a, b, c, d):
    result = a + b + c + d
    return result

def multiply(a, b, c, d):
    result = a * b * c * d
    return result

sum_result = add(1, 2, 3, 4)
multiply_result = multiply(1, 2, 3, 4)

print("합: {sum_result}")
print("곱: {multiply_result}")


#2
def check_odd(number):
    if number % 2 == 0:
        return "짝수"
    else:
        return "홀수"

result1 = check_odd(5)
result2 = check_odd(8)

print(result_1)
print(result_2)


#3
def average(list_numbers):
    if len(list_numbers) == 0:
        return 0
    total = 0
    for numbers in list_numbers:
        total += numbers
    return total / len(list_numbers)
print(average)


#4
class GameCharacter:
    def __init__(self, id, gender, job):
        self.id = id
        self.gender = gender
        self.job = job

    def attack(self):
        print("공격!")

character1 = GameCharacter("gitae1234", "남성", "마법사")

print("아이디: {character1.id}, 성별: {character1.gender}, 직업: {character1.job}")

character1.attack()


#5
class realestate:
    def __init__(self, location, size, building_type, price, year_built):
        self.location = location
        self.size = size
        self.building_type = building_type
        self.price = price
        self.year_built = year_built

    def information(self):
        print("위치: {self.location}")
        print("평수: {self.size}평")
        print("건물 종류: {self.building_type}")
        print("가격: {self.price}원")
        print("건축 연도: {self.year_built}년")

property1 = realestate("경기 수원", 32, "아파트", 100000000, 2024)
property1.information()
print()