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

    def query_all_from_table(self, table: str, *columns: str) -> list:
        cursor = self.connection.cursor()
        cols = ", ".join(columns) or "*"
        cursor.execute(f"SELECT {cols.lower()} FROM {table.lower()}")
        return cursor.fetchall()

    def insert_into(self, table: str, **values):
        pass

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

    def query_definitions_by_word_id(self, word_id: int) -> list:
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
            SELECT 
                *                
            FROM definitions
            WHERE definitions.word_id = '{word_id}'
            """
        )
        return cursor.fetchall()

    def query_examples_by_definition_id(self, definition_id: int) -> list:
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
            SELECT 
                *
            FROM examples
            WHERE examples.definition_id = '{definition_id}'
            """
        )
        return cursor.fetchall()

    def query_examples_by_word_id(self, word_id: int) -> list:
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
            SELECT 
                words.id AS word_id,
                definitions.id AS def_id,
                examples.id AS ex_id,

                words.word,
                words.cefr,
                words.speaking,
                words.writing,
                words.word_type,
                words.ipa_nam,
                words.ipa_br,
                
                definitions.definition,
                definitions.cefr AS def_cefr,
                definitions.grammar,
                definitions.def_type,
                definitions.context AS def_context,
                definitions.labels AS def_labels,
                definitions.variants,
                definitions.use,
                definitions.synonyms,
                
                examples.example,
                examples.context AS ex_context,
                examples.labels AS ex_labels
                
            FROM examples
            INNER JOIN words ON examples.word_id = words.id
            INNER JOIN definitions ON examples.definition_id = definitions.id
            WHERE examples.word_id = '{word_id}'
            """
        )
        return cursor.fetchall()


if __name__ == "__main__":
    sqlite = SqliteORM("longman_levels.db")
    sqlite.connect()

    # print(sqlite.query_all_from_table("words", "id", "speaking", "word"))
    print(sqlite.query_examples_by_word_id(3190))

    sqlite.close()
