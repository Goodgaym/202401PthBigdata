list = ['one', 'two', 'three']

for i in list:
    print(i)

tuple = [(1,2), (3,4), (5,6)]
for (first, last) in tuple:
    print(first + last)

# python의 for는 다른 프로그래밍 언어의 foreach (javascript, C#), for each (java)의 기능을 함
# 기존 for, while 이 명확한 사용 용도에 맞게 분리가 되었음
# 반복자(Iterator)를 통해 순회할 수 있는 객체를 반복한다.

# 점수를 한명씩 채점해서 합격과 불합격을 출력하는 코드
scores = [90, 67, 12, 85, 52]
number = 0
for score in scores:
    number += 1
    print(f"{number}번 수험생은 {score}점. ", end = '')
    if score >= 70:
        print("합격입니다. ")
    else:
        print("불합격입니다. ")


# continue
number = 0
for score in scores:
    number += 1
    if score < 70:
        continue
    else:
        print(f"{number}번 수험생은 {score}점. 합격입니다.")
    print(" 다음")

# break
number = 0
scores[2] = -1
for score in scores:
    number += 1
    if score < 0 or score > 100:
        print(f"{number}번 수험생은 점수가 잘못되었습니다.")
        break
    print(f"{number} PASS")
    
# range() 함수
sum = 0
for i in range(1, 11):
    sum += i
print(sum)

for number in range(len(scores)):
    if scores[number] < 70:
        continue
    else:
        print(f"{number+1}번 수험생은 {scores[number]}점. 합격입니다.")
    print("다음")


# 다중 루프: range()로 구구단, 별계단 출력 

# 리스트 컴프리헨션
# {표현식} for {항목} in {반복가능객체} if {조건문}