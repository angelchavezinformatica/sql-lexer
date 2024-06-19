from typing import Dict, List
import unittest

from lexer import SQLLexer


def ejecutar_lexer(self, sql: str, token_list: List[Dict[str, str]]):
    lexer = SQLLexer()
    lexer.build()
    tokens = lexer.test(sql)

    for token1, token2 in zip(tokens, token_list):
        self.assertEqual(token1, token2)


class SQLLexerTest(unittest.TestCase):
    def test_1(self):
        sql = "SELECT * FROM my_table;"
        ejecutar_lexer(self, sql, [
            {'type': 'IDENTIFIER', 'value': 'SELECT'},
            {'type': 'STAR', 'value': '*'},
            {'type': 'IDENTIFIER', 'value': 'FROM'},
            {'type': 'IDENTIFIER', 'value': 'my_table'},
            {'type': 'SEMICOLON', 'value': ';'},
        ])

    def test_2(self):
        sql = "SELECT name, age FROM users WHERE age > 30;"
        ejecutar_lexer(self, sql, [
            {'type': 'IDENTIFIER', 'value': 'SELECT'},
            {'type': 'IDENTIFIER', 'value': 'name'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'IDENTIFIER', 'value': 'age'},
            {'type': 'IDENTIFIER', 'value': 'FROM'},
            {'type': 'IDENTIFIER', 'value': 'users'},
            {'type': 'IDENTIFIER', 'value': 'WHERE'},
            {'type': 'IDENTIFIER', 'value': 'age'},
            {'type': 'GREATER', 'value': '>'},
            {'type': 'NUMBER', 'value': 30},
            {'type': 'SEMICOLON', 'value': ';'}
        ])
