SELECT ai.NAME, ai.DATETIME           -- 출력 열
FROM ANIMAL_INS AS ai                 -- 기준 테이블
LEFT JOIN ANIMAL_OUTS AS ao           -- 조인할 테이블
   ON ai.ANIMAL_ID = ao.ANIMAL_ID     -- 조인 조건
WHERE ao.DATETIME IS NULL             -- 입양 데이터가 없는 데이터들만
ORDER BY ai.DATETIME                  -- 가장 오래 보호소에 있었던 순서대로 정렬
LIMIT 3;                              -- 상위 세개의 데이터만 출력