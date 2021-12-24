SELECT ao.ANIMAL_ID, ao.NAME        -- 보여줄 열
FROM ANIMAL_INS ai, ANIMAL_OUTS ao  -- 조인할 두개의 테이블
WHERE ai.ANIMAL_ID = ao.ANIMAL_ID   -- 두개의 테이블 조인
  AND ai.DATETIME > ao.DATETIME     -- 보호시작일 > 입양일 (입양일이 더 빠른 경우)
ORDER BY ai.DATETIME;               -- 보호시작일 빠른순 조회