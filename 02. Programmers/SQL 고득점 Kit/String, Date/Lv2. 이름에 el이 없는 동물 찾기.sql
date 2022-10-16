-- MySQL 1
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog' and (NAME like '%el%' or NAME like '%EL')
ORDER BY NAME ASC

-- MySQL 2
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog' AND UPPER(NAME) LIKE '%EL%'
ORDER BY UPPER(NAME) ASC