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
        sql = "SELECT * FROM producto;"
        ejecutar_lexer(self, sql, [
            {'type': 'IDENTIFIER', 'value': 'SELECT'},
            {'type': 'STAR', 'value': '*'},
            {'type': 'IDENTIFIER', 'value': 'FROM'},
            {'type': 'IDENTIFIER', 'value': 'producto'},
            {'type': 'SEMICOLON', 'value': ';'},
        ])
