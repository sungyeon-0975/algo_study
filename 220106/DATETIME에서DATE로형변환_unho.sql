SELECT animal_id, name, DATE_FORMAT(datetime, '%Y-%m-%d')   -- 데이터 타입 형 변환을 위해서 DATE_FORMAT 함수 사용
FROM animal_ins
ORDER BY animal_id;                                         -- 정렬