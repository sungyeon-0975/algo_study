SELECT *                        -- 모든 열 출력
FROM PLACES                     -- 테이블
WHERE HOST_ID IN (              
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(HOST_ID) >= 2
)                               -- HOST_ID가 서브쿼리 결과에 속해 있는것만 필터링
                                -- 서브쿼리 => HOST_ID 그룹화를 하여 해당 그룹이 2개 이상의 데이터가 있는것만 필터링
ORDER BY ID;                    -- ID 순서대로 정렬