-- ORACLE
SELECT P.MEMBER_NAME AS MEMBER_NAME, R.REVIEW_TEXT AS REVIEW_TEXT, TO_CHAR(R.REVIEW_DATE, 'YYYY-MM-DD') AS REVIEW_DATE
FROM MEMBER_PROFILE P INNER JOIN REST_REVIEW R ON P.MEMBER_ID = R.MEMBER_ID
WHERE R.MEMBER_ID IN (SELECT MEMBER_ID -- 리뷰 쓴 개수가 COUNT(*)인 경우에 대해 GROUP BY후 사람들 ID 출력
                       FROM REST_REVIEW
                       GROUP BY MEMBER_ID -- 사람들이 리뷰 쓴 개수가 COUNT(*)인 경우에 대해 GROUP BY. 
                       HAVING COUNT(*) = (SELECT MAX(COUNT(*)) -- 최대 리뷰 쓴 사람들의 개수를 구함
                                          FROM REST_REVIEW
                                          GROUP BY MEMBER_ID)
                        )
ORDER BY R.REVIEW_DATE