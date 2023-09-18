# 데이터 취업 스쿨

# 모든 공지사항을 꼼꼼하게 확인해주시기 바랍니다! 
# https://zerobaseschool.notion.site/DS-Programming-Test-5c508658cde94a359dbff3994733c329?pvs=4

# 파이썬 프로그래밍 테스트
# 내용: 파이썬 활용 능력 평가
# 범위: 파이썬 강의 기반
# 문항: 1 ~ 6번, 총 6문제
# 배점: 총점 100점 
# 1,2번 각 10점 
# 3,4번 각 15점 
# 5,6번 각 25점
 
# 채점 기준 
# 각 문제마다, print() 값의 결과만 나오시게끔 작성하시면 됩니다.
# 코드는 어떻게 작성하셔도 상관없습니다. 
# 코드 정상작동 만점 (각 배점에 맞게 만점)
# 코드 미실행(에러 발생)은 0점
# 부분 점수는 없습니다

# 숙지 사항
# 아래 각 문제에, pass 부분을 지우시고 코드를 작성해주시면 됩니다. 
# 모든 코드를 작성하셨을 때, 코드가 정상적으로 실행되어야 합니다. 
# 모든 문제는 print() 문으로 결과가 출력되어야 합니다. 
# 제출 코드는 실행했을 때 자동으로 실행되게끔 작성해주세요(input 함수 사용 금지). 

# start ! 

# 문제 1 (10점)
# 문제 1번은 함수가 아닌, 변수만 선언해주시면 됩니다. 

print("1번 답안")
tmp = []
print(tmp)


# 문제 2 (10점)
def data_type(v):

    return f'list <{", ".join(map(data_type, v))}>' if isinstance(v, list) else f'tuple <{", ".join(map(data_type, v))}>' if isinstance(v, tuple) else ['int', 'float', 'str','dict'][[int, float, str, dict].index(type(v))] 


print("2번 답안")   
print(data_type(1))
print(data_type(5.))
print(data_type([2, 3, [2, 3], "Hello"]))


# 문제 3 (15점)
def calc_tips(n):

    return int(n) + int(n % 1 > 0)

print("3번 답안")   
print(calc_tips(5.1))

# 문제 4 (15점)
def search_target(sentence, target):

    return sentence.count(target), [i for i in range(len(sentence)) if sentence.startswith(target, i)]
    
print("4번 답안")

sentence = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex."
target = "than"

print(search_target(sentence, target))


# 문제 5 (25점)#
def div_ab(a,b):

    return f'{a} 나누기 {b}의 결과: 몫{divmod(a, b)[0]}, 나머지{divmod(a, b)[1]}' if isinstance(a, int) and isinstance(b, int) else None
    

print("5번 답안")
a = 3
b = 2 
print(div_ab(a, b))


# 문제 6 (25점)

def hanoi_sol(n, from_rod, to_rod):
    
    aux_rod = [x for x in ["A", "B","C"] if x not in [from_rod, to_rod]][0]
    
    if n == 1:
        print(from_rod + " -> " + to_rod)
        return ""
    
    hanoi_sol(n-1, from_rod, aux_rod)
    
    print(from_rod + " -> " + to_rod)
    
    return hanoi_sol(n-1, aux_rod, to_rod) 


print("6번 답안") 
print(hanoi_sol(3, "A", "B"))



print("모든 문제가 끝났습니다")
print("수고하셨습니다 :)")
# end !

# 제출 전 반드시 확인!
# 실행 버튼을 눌러서, 처음부터 끝까지 정상 실행되는지 확인해주세요.

# 시험이 끝난 후에는? 
# 제출 방법: 제공드린 설문지에 파일을 업로드 해주세요 
# 제출 양식: [DS]python_programming_honggildong.py 

# 대괄호 안에 대문자로 [DS] 
# _ 언더바 사용 
# 수강생분 성함(성부터 이름 순으로 모두 소문자 작성)
# 잘못된 예 -> [ds]_HongGilDong.py 또는 [ds]_HongGilDong.py.py 또는 [DS]_Hongggildong.py 등
