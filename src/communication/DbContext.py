import sqlite3
import string


class SQLiteDB:
    def __init__(self, db_path):
        """Initialisiert die Verbindung zur SQLite-Datenbank."""
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def select(self, query: string, params=()):
        """
            Führt einen SELECT-Befehl aus und gibt das Ergebnis zurück.
            ergebnis = db.select('SELECT * FROM meine_tabelle')
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def insert(self, table: string, data):
        """
            Fügt Daten in eine bestimmte Tabelle ein.
            'data' sollte ein Dictionary sein, das die Spaltennamen und Werte enthält.
            db.insert('meine_tabelle', {'spalte1': 'Wert1', 'spalte2': 'Wert2'})
        """
        columns = ', '.join(data.keys())
        placeholders = ', '.join('?' * len(data))
        query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
        self.cursor.execute(query, tuple(data.values()))
        self.connection.commit()

    def reset_table(self, table: string):
        """
            Löscht alle Einträge in einer spezifischen Tabelle.
            db.reset_table('meine_tabelle')
        """
        self.cursor.execute(f'DELETE FROM {table}')
        self.connection.commit()

    def close(self):
        """Schließt die Verbindung zur Datenbank."""
        self.connection.close()