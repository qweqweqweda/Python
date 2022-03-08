#함수정의 한 후 반드시 함수 호출
#더하기 함수 정의
def add(a, b):
    c = a + b
    return c
#빼기 함수 정의
def minus(a, b):
    c = a - b
    return c
#곱하기 함수 정의
def multi(a, b):
    c = a * b
    return c
#나누기 함수 정의
def divide(a, b):
    c = a / b
    return c

#반복문 선언 (앞에 똑같이 띄어서 입력해야 정상작동함)
while True:
#a에 값을 입력
 a = input("1st input? ")

#반복 종료 조건
 if a== "0000":
  break
#b에 값을 입력
 b = int (input("2nd input? "))
 a= int(a);

 #a+b의 값과 결과텍스트
 result = add(a,b)
 print(a, "+", b,"=", result)

#a-b의 값과 결과텍스트
 result = minus(a,b)
 print(a, "-", b,"=", result)

#a*b의 값과 결과텍스트
 result = multi(a,b)
 print(a, "*", b,"=", result)

#a/b의 값과 결과텍스트
 result = divide(a,b)
 print(a, "/", b,"=", result)

 print("\n")
 
#반복문 종료시 나오는 텍스트
print("exit")
