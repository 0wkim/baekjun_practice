import math

def solution(progresses, speeds):
    answer = []
    
    do_pro = []
    for num in progresses:
        do_pro.append(100 - num)

    day_count = []
    for i in range(len(do_pro)):
        day_count.append(math.ceil(do_pro[i]/speeds[i]))
        
    count = 1
    front = 0
    for i in range(1, len(day_count)):
        if day_count[i] <= day_count[front]:
            count += 1
        else:
            answer.append(count)    
            count = 1
            front = i
    answer.append(count)
    
    return answer