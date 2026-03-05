def solution(numbers, target):
    answer = 0
    
    n = len(numbers)
    
    all_calc = []
    
    for i in range(1 << n):
        current_sum = 0 
        
        for j in range(n):
            if (i >> j) & 1:
                current_sum += numbers[j]
            else:
                current_sum -= numbers[j]
        
        all_calc.append(current_sum)
    
    for calc in all_calc:
        if calc == target:
            answer += 1
    return answer