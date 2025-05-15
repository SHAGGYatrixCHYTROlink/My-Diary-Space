import sqlite3
#Funkce pro vlozeni do tabulky NOTES v mds.db
def insert_to_diarybase(note_name, note):
    conn = sqlite3.connect("msd_sql_base/msd_sql_base.db")# Připojení k databázi
    cursor = conn.cursor()# Vytvoreni cursoru

    cursor.execute("INSERT INTO notes (note_name, note) VALUES (?, ?)", (note_name, note))# Volezeni hodnot do tabulky NOTES s hodnotami pass: static ID + datetime, ativ: note name + note text

    conn.commit()#potvrzeni zmen
    conn.close()#uzavreni pripojeni do db


#Funkce pro vypis dat z tabulky NOTES
def get_data_from_diarybase():
    pass