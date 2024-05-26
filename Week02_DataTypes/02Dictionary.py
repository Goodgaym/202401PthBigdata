a = {}
b = {0:1}   # 0이 키값 1 밸류값
c = {3: 'Name'}
d = {'list': [1, 2, 'a'], 'dic': {'phone':'01012341234'}}

print(a, b, c)

# 딕셔너리는 요소는 Key:Value 의 형태를 가지고 있음
dic = {'name':'jun', 'phone':'010-1010-1010', 'birth':'0311'} # 딕셔너리 선언

dic['name'] = 'hyun'    # 수정
dic['address'] = 'anseong'  # 추가
del dic['phone']

dic['list'] = [1, 2, 3, 4]
print(dic)

del dic['list'][2]
print(dic)

# Key 리스트 만들기
#keys 3.0 이전에선 리스트 리턴. 이후에선 dict_keys 객체 리턴
keys = list(dic.keys())
print(keys)

# Value 리스트 만들기
dic.values()

# Key, Value 쌍 얻기 (쌍을 튜플로 묶은 리스트 반환)
dic.items()

# Key로 Value 얻기 (None 리턴 / 배열 접근은 에러)
dic.get('name')
dic.get('tele', 'blank')    # get(key, default) / tele 없으면 blank 리턴

# Key가 있는지 조사
'name' in dic       # True 리턴
'email' in dic      # False 리턴

r = dic.pop('name')
print(r)