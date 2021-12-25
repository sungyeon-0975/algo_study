SELECT CART_ID                          -- 출력 열
FROM (                                  
    SELECT DISTINCT CART_ID, NAME       -- 서브쿼리
    FROM CART_PRODUCTS                  
    WHERE NAME IN ('Milk', 'Yogurt')    -- 우유와 요거트를 구입한 장바구나 아이디 보여줌
) AS cp                                 
GROUP BY CART_ID                        -- 장바구니 아이디로 묶음
HAVING COUNT(CART_ID) >= 2              -- 종류가 두개 이상인 조건
ORDER BY CART_ID;                       -- 장바구니 아이디 순서대로 정렬