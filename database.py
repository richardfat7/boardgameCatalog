import sqlite3


class CatalogDB:
    def __init__(self, db_path):
        self.db_path = db_path
        
    def get_con(self):
        self.con = sqlite3.connect(self.db_path)
        self.con.row_factory = sqlite3.Row
        return self.con
    
    def init_table(self, force = False):
        with self.get_con() as c:
            if force:
                c.execute("""DROP TABLE home""")
                c.execute("""DROP TABLE game""")
                c.execute("""DROP TABLE game_has_tag""")
            c.execute("""CREATE TABLE IF NOT EXISTS home (
                id TEXT PRIMARY KEY
            )""")
            c.execute("""CREATE TABLE IF NOT EXISTS game (
                id INTEGER PRIMARY KEY,
                home_id TEXT,
                name TEXT,
                alt_name TEXT,
                description TEXT,
                cover_photo_path TEXT,
                other_photo_paths TEXT,
                min_player INTEGER,
                max_player INTEGER,
                lang TEXT,
                duration_min INTEGER,
                explore_url TEXT
            )""")
            c.execute("""CREATE TABLE IF NOT EXISTS game_has_tag (
                id INTEGER PRIMARY KEY,
                tag TEXT
            )""")