def solution(code):
    answer = ''
    mode = 0
    for idx in range(len(code)):
        if code[idx] == '1':
            mode = (mode + 1)%2
            continue
            
        if mode == 0:
            if idx % 2 == 0:
                answer += code[idx]
        else:
            if idx % 2 == 1:
                answer += code[idx]
        
    if answer == '':
        answer += 'EMPTY'
        
    return answer