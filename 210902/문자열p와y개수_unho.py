def solution(s):
    cntp, cnty = 0, 0
    
    for i in s:
        if i=='P' or i=='p': cntp+=1
        elif i=='Y' or i=='y': cnty+=1
            
    if cntp != cnty:
        return False

    return True