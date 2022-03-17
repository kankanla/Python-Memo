import csv
import pathlib
import sqlite3
import sys
import os

# s1=1-31
# s2=(s1-1)-32
# s3=(s2-1)-33
# s4=(s3-1)-34
# s5=(s4-1)-35
# s6=(s5-1)-36
# s7=(s6-1)-37

"""
.mode csv
delete from loto7;
.import loto7.csv loto7
.mode table

+----------+
| count(*) |
+----------+
| 10295472 |
+----------+


1, select * from loto7,alll7 where loto7.s1=alll7.s1 and loto7.s2=alll7.s2 and loto7.s3=alll7.s3 and loto7.s4=alll7.s4 and loto7.s5=alll7.s5 and loto7.s6=alll7.s6 and loto7.s7=alll7.s7;
2, select * from loto7,alll7 where loto7.s1=alll7.s1 and loto7.s2=alll7.s2 and loto7.s3=alll7.s3 and loto7.s4=alll7.s4 and loto7.s5=alll7.s5 and loto7.s6=alll7.s6 and loto7.s7=alll7.s7 order by loto7.t1 desc;
3, update alll7 set n1=(select t1 from loto7 where z1=10274228) where id = 10274228
4, select "update alll7 set n1=(select t1 from loto7 where z2=",z2,") where id=",z2,";" from loto7;
5, select "update alll7 set b1=(select b1 from loto7 where b1=",b1,") where id=",z2,";" from loto7;
5, select "update alll7 set b2=(select b2 from loto7 where b2=",b2,") where id=",z2,";" from loto7;


1,  結果例
+-----+------------+----+----+----+----+----+----+----+----+----+----+------+-----+----+---------+---------+----+----+----+----+----+----+----+----+----+-----+
| t1  |     d1     | s1 | s2 | s3 | s4 | s5 | s6 | s7 | b1 | b2 | n1 |  n2  | n3  | z2 |   z1    |   id    | s1 | s2 | s3 | s4 | s5 | s6 | s7 | b1 | b2 | t1  |
+-----+------------+----+----+----+----+----+----+----+----+----+----+------+-----+----+---------+---------+----+----+----+----+----+----+----+----+----+-----+
| 454 | 2022/1/21  | 8  | 17 | 21 | 26 | 27 | 29 | 31 | 1  | 33 | 2  | 1 g  | -   | H  | 8691080 | 8691080 | 8  | 17 | 21 | 26 | 27 | 29 | 31 | 1  | 33 | 454 |
| 453 | 2022/1/14  | 2  | 8  | 10 | 21 | 24 | 26 | 35 | 9  | 13 | 1  | 3 g  | -   | C  | 3013039 | 3013039 | 2  | 8  | 10 | 21 | 24 | 26 | 35 | 9  | 13 | 453 |
| 452 | 2022/1/7   | 5  | 17 | 20 | 21 | 31 | 34 | 35 | 8  | 27 | 3  | 1 g  | -   | E  | 6882823 | 6882823 | 5  | 17 | 20 | 21 | 31 | 34 | 35 | 8  | 27 | 452 |
| 451 | 2021/12/24 | 2  | 15 | 22 | 25 | 28 | 33 | 37 | 10 | 17 | 1  | 8 g  | -   | I  | 3492751 | 3492751 | 2  | 15 | 22 | 25 | 28 | 33 | 37 | 10 | 17 | 451 |
| 450 | 2021/12/17 | 2  | 7  | 12 | 15 | 21 | 23 | 30 | 9  | 31 | -  | -    | 4 g | A  | 2916074 | 2916074 | 2  | 7  | 12 | 15 | 21 | 23 | 30 | 9  | 31 | 450 |
| 449 | 2021/12/10 | 2  | 21 | 26 | 27 | 32 | 33 | 34 | 8  | 9  | 1  | 5 g  | -   | D  | 3562253 | 3562253 | 2  | 21 | 26 | 27 | 32 | 33 | 34 | 8  | 9  | 449 |
| 448 | 2021/12/3  | 7  | 21 | 24 | 29 | 32 | 36 | 37 | 22 | 27 | 1  | 10 g | 2 g | B  | 8250297 | 8250297 | 7  | 21 | 24 | 29 | 32 | 36 | 37 | 22 | 27 | 448 |
| 447 | 2021/11/26 | 3  | 5  | 8  | 13 | 26 | 30 | 37 | 25 | 28 | -  | -    | 7 g | F  | 3880097 | 3880097 | 3  | 5  | 8  | 13 | 26 | 30 | 37 | 25 | 28 | 447 |
| 446 | 2021/11/19 | 1  | 7  | 9  | 12 | 15 | 29 | 32 | 11 | 28 | 1  | 10 g | 3 g | B  | 1241514 | 1241514 | 1  | 7  | 9  | 12 | 15 | 29 | 32 | 11 | 28 | 446 |
| 445 | 2021/11/12 | 4  | 22 | 25 | 27 | 28 | 30 | 33 | 2  | 3  | 1  | 10 g | 8 g | D  | 6017308 | 6017308 | 4  | 22 | 25 | 27 | 28 | 30 | 33 | 2  | 3  | 445 |
+-----+------------+----+----+----+----+----+----+----+----+----+----+------+-----+----+---------+---------+----+----+----+----+----+----+----+----+----+-----+


CREATE TABLE alll7(
    "id" INTEGER PRIMARY KEY,
    "s1" INTEGER, 
    "s2" INTEGER, 
    "s3" INTEGER, 
    "s4" INTEGER, 
    "s5" INTEGER, 
    "s6" INTEGER, 
    "s7" INTEGER, 
    "b1" INTEGER, 
    "b2" INTEGER, 
    "t1" INTEGER
);

CREATE TABLE loto7(
    "t1" INTEGER UNIQUE,
    "d1" TEXT UNIQUE,
    "s1" INTEGER,
    "s2" INTEGER,
    "s3" INTEGER,
    "s4" INTEGER,
    "s5" INTEGER,
    "s6" INTEGER,
    "s7" INTEGER,
    "b1" INTEGER,
    "b2" INTEGER,
    "n1" INTEGER,
    "n2" INTEGER,
    "n3" INTEGER,
    "z2" INTEGER,
    "z1" INTEGER
);



"""


def createSQL():
    dbname = 'alll7.db'
    if not pathlib.Path(dbname).is_file():
        crt = "create table if not exists alll7(id INTEGER PRIMARY KEY,s1 INTEGER, s2 INTEGER, s3 INTEGER, s4 INTEGER, s5 INTEGER, s6 INTEGER, s7 INTEGER, b1 INTEGER, b2 INTEGER, t1 INTEGER)"
        con = sqlite3.connect(dbname)
        con.execute(crt)
        con.commit()
        con.close
        print('sql-end')


def createNUM():
    f = open('alll7.csv', 'a+', newline='')
    cw = csv.writer(f)
    s1, s2, s3, s4, s5, s6, s7 = 0, 0, 0, 0, 0, 0, 0
    cnt = 0
    lst = 31
    for s1 in range(1, lst+1):
        for s2 in range(s1+1, lst+2):
            for s3 in range(s2+1, lst+3):
                for s4 in range(s3+1, lst+4):
                    for s5 in range(s4+1, lst+5):
                        for s6 in range(s5+1, lst+6):
                            for s7 in range(s6+1, lst+7):
                                cnt = cnt+1
                                ast = [cnt, s1, s2, s3, s4,
                                       s5, s6, s7, '', '', '']
                                cw.writerow(ast)
    pass
    f.close()
    print(cnt)
    cnt = 0
    print('end')


createNUM()
createSQL()
