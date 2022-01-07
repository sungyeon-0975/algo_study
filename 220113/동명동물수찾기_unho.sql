SELECT name, COUNT(animal_id) AS cnt    -- 출력 열
FROM animal_ins
WHERE name IS NOT NULL                  -- 이름이 없는 경우는 필요 없으므로
GROUP BY name                           -- 이름을 그룹화
HAVING COUNT(animal_id) >= 2            -- 이름이 나온 횟수가 2회 이상을때
ORDER BY name;