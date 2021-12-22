-- 코드를 입력하세요
SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.NAME
FROM ANIMAL_INS, ANIMAL_OUTS
WHERE ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
AND ANIMAL_INS.DATETIME >= ANIMAL_OUTS.DATETIME
ORDER BY ANIMAL_INS.DATETIME