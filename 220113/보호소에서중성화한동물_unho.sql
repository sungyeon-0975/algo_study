SELECT ai.animal_id, ai.animal_type, ai.name                                                              -- 출력 열
FROM animal_ins AS ai
JOIN animal_outs AS ao ON ai.animal_id = ao.animal_id                                                     -- 조인
WHERE ai.SEX_UPON_INTAKE LIKE "Intact%" AND ao.SEX_UPON_OUTCOME IN ("Spayed Female", "Neutered Male")     -- 들어올때 중성화 되지 않았으나 나갈때 중성화 된 동물들
ORDER BY animal_id;                                                                                       -- 아이디순 정렬