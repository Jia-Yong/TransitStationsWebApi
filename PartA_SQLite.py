import sqlite3

db = sqlite3.connect('db.sqlite')

db.execute('DROP TABLE IF EXISTS stations')

db.execute('''CREATE TABLE stations(
        id integer PRIMARY KEY,
        code text NOT NULL,
        name text NOT NULL,
        type text NOT NULL
        )''')

cursor = db.cursor()

cursor.execute('''INSERT INTO stations(id, code, name, type) VALUES
               (17, 'SBK07', 'Surian', 'Elevated'),
               (18, 'SBK08', 'Mutiara Damansara', 'Elevated'),
               (19, 'SBK09', 'Bandar Utama', 'Elevated'),
               (20, 'SBK10', 'TTDI', 'Elevated'),
               (25, 'SBK12', 'Phileo Damansara', 'Elevated'),
               (26, 'SBK13', 'Pusat Bandar Damansara', 'Elevated'),
               (27, 'SBK14', 'Semantan', 'Elevated'),
               (29, 'SBK15', 'Muzium Negara', 'Underground'),
               (30, 'SBK16', 'Pasar Seni', 'Underground'),
               (31, 'SBK17', 'Merdeka', 'Underground'),
               (33, 'SBK18A', 'Bukit Bintang', 'Underground')''')

db.commit()
db.close()