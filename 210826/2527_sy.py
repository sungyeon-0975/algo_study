def find_common_section(s1,e1,s2,e2):
    if s1 <= s2 < e1 or s1 < e2 <= e1:#겹치는 구간 존재
        return 2
    elif s2 == e1 or e2 == s1:#겹치는 선 존재
        return 1
    elif e1 < s2 or e2 < s1:#x가 겹치는 구간/선 아예 없음
        return 0
    else:
        return 2
    
if __name__ == "__main__":
    d = {0:'d', 1:'c', 2:'b', 4:'a'}
    for _ in range(4):
        x1,y1,p1,q1,x2,y2,p2,q2  = map(int, input().split())
        res = find_common_section(x1,p1,x2,p2)* find_common_section(y1,q1,y2,q2)
        print(d[res])