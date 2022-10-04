class Query:

    def __init__(self, conn):
        self.conn = conn

    # CREATION DES TABLES

    def create_tables(self):
        self.conn.execute('''CREATE TABLE PERSON
                (NAME TEXT PRIMARY KEY   NOT NULL);''')

        self.conn.execute('''CREATE TABLE ITEM 
                (NAME TEXT PRIMARY KEY   NOT NULL);''')

        self.conn.execute('''CREATE TABLE QUANTITY
                (QTY       INTEGER NOT NULL,
                ITEMNAME INTEGER NOT NULL,
                PERSONNAME INTEGER NOT NULL, 
                FOREIGN KEY (ITEMNAME) REFERENCES ITEM(NAME),
                FOREIGN KEY (PERSONNAME) REFERENCES PERSON(NAME),
                PRIMARY KEY (PERSONNAME, ITEMNAME));''')

    # PREDICAT EXISTENCE        

    def person_exists(self, name):
        cursor= self.conn.cursor()
        cursor.execute("SELECT count(*) FROM PERSON WHERE name=?", (name,))
        return cursor.fetchone()[0] == 1

    def item_exists(self, name):
        cursor= self.conn.cursor()
        cursor.execute("SELECT count(*) FROM ITEM WHERE name=?", (name,))
        return cursor.fetchone()[0] == 1

    def quantity_exists(self, person_name, item_name):
        cursor= self.conn.cursor()
        cursor.execute("SELECT count(*) FROM QUANTITY WHERE PERSONNAME=? AND ITEMNAME =?", (person_name, item_name))
        return cursor.fetchone()[0] == 1

    # INSERT VALUE

    def insert_person(self, name):
        self.conn.execute("INSERT INTO PERSON (NAME) VALUES (?)", (name,))
        self.conn.commit()

    def insert_item(self, name):
        self.conn.execute("INSERT INTO ITEM (NAME) VALUES (?)", (name,))
        self.conn.commit()

    def insert_quantity(self, person_name, item_name, qty):
        self.conn.execute("INSERT INTO QUANTITY (PERSONNAME, ITEMNAME, QTY) VALUES (?,?,?)", (person_name, item_name, qty))
        self.conn.commit()

    # UPDATE 

    def add_quantity(self, person_name, item_name, added_qty):
        # on vérifie que l'item existe (methode exists de la classe item)
        # si non on le crée et on l'ajoute à la liste
        # si oui, on regarde si déjà dans la liste de self (method exists de classe quantity)
            # si non, on crée un objet quantity
            # si oui, on modifie cet objet
        cur = self.conn.cursor()
        cur.execute("UPDATE QUANTITY SET QTY = QTY + ? WHERE PERSONNAME = ? AND ITEMNAME = ?", (added_qty, person_name, item_name))
        self.conn.commit()
    
    def get_list(self, person_name):
        cursor= self.conn.cursor()
        cursor.execute("SELECT qty, itemname FROM QUANTITY WHERE PERSONNAME=?", (person_name,))
        rows = cursor.fetchall()
        if not rows:
            return "Votre liste est vide."
        else:
            list = ""
            for row in rows:
                list += "- " + str(row[0]) + " " + row[1] +"\n"
            return list[:-1]
