SELECT animal_id, name                          -- 출력 열
FROM animal_ins     
WHERE animal_type = 'dog' AND name LIKE '%el%'  -- 동물의 종류가 개이고, 이름에 el이 들어가는 경우
ORDER BY name;                                  -- 정렬