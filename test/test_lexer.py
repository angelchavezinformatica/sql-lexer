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

    def test_2(self):
        sql = "INSERT INTO producto (nombre, precio, stock, description, medida)" +\
            "VALUES ('Espinaca', 7.0, 18, 'Hoja verde espinosa y rica en nutrientes', 'kg')"
        ejecutar_lexer(self, sql, [
            {'type': 'IDENTIFIER', 'value': 'INSERT'},
            {'type': 'IDENTIFIER', 'value': 'INTO'},
            {'type': 'IDENTIFIER', 'value': 'producto'},
            {'type': 'LPAREN', 'value': '('},
            {'type': 'IDENTIFIER', 'value': 'nombre'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'IDENTIFIER', 'value': 'precio'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'IDENTIFIER', 'value': 'stock'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'IDENTIFIER', 'value': 'description'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'IDENTIFIER', 'value': 'medida'},
            {'type': 'RPAREN', 'value': ')'},
            {'type': 'IDENTIFIER', 'value': 'VALUES'},
            {'type': 'LPAREN', 'value': '('},
            {'type': 'STRING', 'value': 'Espinaca'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': 7.0},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': 18},
            {'type': 'COMMA', 'value': ','},
            {'type': 'STRING', 'value': 'Hoja verde espinosa y rica en nutrientes'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'STRING', 'value': 'kg'},
            {'type': 'RPAREN', 'value': ')'},
        ])
