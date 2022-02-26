def solution(m, musicinfos):
    music = []
    for musicinfo in musicinfos:
        musicinfo = musicinfo.split(',')
        print(musicinfo)
        start = int(musicinfo[0][:2]) * 60 + int(musicinfo[0][3:5])
        end = int(musicinfo[1][:2]) * 60 + int(musicinfo[1][3:5])
        duration = end - start

    answer = ''
    return answer

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))