def change_info(m):
    if 'A#' in m:
        m = m.replace('A#', 'a')
    if 'C#' in m:
        m = m.replace('C#', 'c')
    if 'D#' in m:
        m = m.replace('D#', 'd')
    if 'F#' in m:
        m = m.replace('F#', 'f')
    if 'G#' in m:
        m = m.replace('G#', 'g')

    return m


def solution(m, musicinfos):
    answer = ''
    musicdict = {}
    answerlist = []

    m = change_info(m)

    for musicinfo in musicinfos:
        music = musicinfo.split(",")

        end = list(map(int, music[1].split(":")))
        start = list(map(int, music[0].split(":")))
        duration = (end[0]-start[0])*60 + end[1] - start[1]

        song = music[3]*duration
        song = change_info(song)
        musicdict[music[2]] = song[:duration]

    for key, value in musicdict.items():
        if m in value:
            answerlist.append(key)

    if answerlist:
        for ans in answerlist:
            if len(ans) > len(answer):
                answer = ans
        return answer
    else:
        return None
