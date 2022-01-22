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


def createSQL():
    dbname = 'alll7.db'
    if not pathlib.Path(dbname).is_file():
        crt = "create table if not exists alll7(id INTEGER PRIMARY KEY,s1 text, s2 text, s3 text, s4 text, s5 text, s6 text, s7 text, b1 text, b2 text, n1 text)"
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
