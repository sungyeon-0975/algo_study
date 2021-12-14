SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
FROM ANIMAL_OUTS, ANIMAL_INS
WHERE ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
ORDER BY DATEDIFF(ANIMAL_INS.DATETIME, ANIMAL_OUTS.DATETIME)
LIMIT 2;