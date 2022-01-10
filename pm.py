import sqlite3

dbname = "xxx.db"
c = sqlite3.connect(dbname)
c.execute("PRAGMA foreign_keys=1")

ddl ="""
create table item
(
    item_code INTEGER PRIMARY KEY,
    item_name TEXT NOT NULL UNIQUE
);
"""
c.execute(ddl)

ddl ="""
CREATE TABLE acc_data
( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    acc_date DATE NOT NULL,
    item_code INTEGER NOT NULL,
    amount INTEGER,
    FOREIGN KEY(item_code) REFERENCES item(item_code)
);
"""
c.execute(ddl)
