--SELECT A.CART_ID
--FROM CART_PRODUCTS as A
--INNER JOIN CART_PRODUCTS as B
--ON A.CART_ID = B.CART_ID
--WHERE A.NAME = 'Milk' AND B.NAME = 'Yogurt'
--GROUP BY A.CART_ID

SELECT DISTINCT A.CART_ID
FROM CART_PRODUCTS as A
INNER JOIN CART_PRODUCTS as B
ON A.CART_ID = B.CART_ID
WHERE A.NAME = 'Milk' AND B.NAME = 'Yogurt'