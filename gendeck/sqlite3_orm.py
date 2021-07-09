import sqlite3
from sqlite3 import Connection, Cursor
from typing import Type


class SqliteORM:
    def __init__(self, db_name):
        self.db_name: str = db_name
        self.connection: Type[Connection] = None

    def connect(self) -> Type[Connection]:
        self.connection = sqlite3.connect(self.db_name)

    def close(self) -> None:
        self.connection.close()

    def rollback(self) -> None:
        self.connection.rollback()

    def try_to_commit_and_close(self):
        try:
            self.connection.commit()
        except:
            self.connection.rollback()
            self.connection.close()
            raise
        finally:
            self.connection.close()

    def create_table(self, table: str) -> None:
        cursor = self.connection.cursor()
        cursor.execute(table)

    def insert_word(self, values: dict) -> int:
        cursor = self.connection.cursor()
        word = values.get("word")
        cefr = values.get("cefr")
        speaking = values.get("speaking")
        writing = values.get("writing")
        word_type = values.get("word_type")
        ipa_nam = values.get("ipa_nam")
        ipa_br = values.get("ipa_br")
        cursor.execute(
            "INSERT INTO words VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",
            (
                word,
                cefr,
                speaking,
                writing,
                word_type,
                ipa_nam,
                ipa_br,
            ),
        )
        return cursor.lastrowid

    def insert_definition(self, values: dict) -> int:
        cursor = self.connection.cursor()

        definition = values.get("definition")
        cefr = values.get("cefr")
        grammar = values.get("grammar")
        def_type = values.get("def_type")
        context = values.get("context")
        labels = values.get("labels")
        variants = values.get("variants")
        use = values.get("use")
        synonyms = values.get("synonyms")
        word_id = values.get("word_id")
        cursor.execute(
            "INSERT INTO definitions VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                definition,
                cefr,
                grammar,
                def_type,
                context,
                labels,
                variants,
                use,
                synonyms,
                word_id,
            ),
        )
        return cursor.lastrowid

    def insert_example(self, values: dict) -> int:
        cursor = self.connection.cursor()

        example = values.get("example")
        context = values.get("context")
        labels = values.get("labels")
        definition_id = values.get("definition_id")
        word_id = values.get("word_id")
        cursor.execute(
            "INSERT INTO examples VALUES (NULL, ?, ?, ?, ?, ?)",
            (
                example,
                context,
                labels,
                definition_id,
                word_id,
            ),
        )
        return cursor.lastrowid

    def insert_many_definitions(self, values: list) -> None:
        cursor = self.connection.cursor()
        cursor.executemany(
            "INSERT INTO definitions VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            values,
        )

    def last_word_id_inserted(self, cursor):
        return cursor.lastrowid

    def query_word(self, word: str, word_type: str) -> tuple:
        cursor = self.connection.cursor()
        cursor.execute(
            f"SELECT rowid, * FROM words WHERE word = '{word}' AND word_type = '{word_type}'"
        )
        return cursor.fetchone()

    def query_definition(self, definition: str) -> tuple:
        cursor = self.connection.cursor()
        cursor.execute(
            f'SELECT rowid, * FROM definitions WHERE definition = "{definition}"'
        )
        return cursor.fetchone()
