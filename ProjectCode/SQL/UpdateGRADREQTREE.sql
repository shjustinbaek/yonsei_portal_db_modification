SELECT * FROM mydb.gradreqtree;

UPDATE gradreqtree
SET NodeName = '채플'
WHERE `Left` = '2';

UPDATE gradreqtree
SET NodeName = '글쓰기'
WHERE `Left` = '4';

UPDATE gradreqtree
SET NodeName = '대학영어'
WHERE `Left` = '6';

UPDATE gradreqtree
SET NodeName = '기독교의이해'
WHERE `Left` = '8';
