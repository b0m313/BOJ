inputs = input()
stack = []
while inputs != '고무오리 디버깅 끝' :
    if inputs == '문제' :
        stack.append(inputs)
    elif inputs == '고무오리' :
        if stack:
            stack.pop()
        else :
            stack.append('문제')
            stack.append('문제')
    # print(stack)
    inputs = input()
if stack:
    print('힝구')
else :
    print('고무오리야 사랑해')