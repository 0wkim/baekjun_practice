-- 코드를 작성해주세요
# NTILE(등급) OVER(등급을 나누는 기준(오름차순, 내림차순))
SELECT ID, CASE NTILE(4) OVER(ORDER BY SIZE_OF_COLONY DESC)
                WHEN 1 THEN 'CRITICAL'
                WHEN 2 THEN 'HIGH'
                WHEN 3 THEN 'MEDIUM'
                ELSE 'LOW'
            END AS COLONY_NAME
FROM ECOLI_DATA
ORDER BY ID ASC;