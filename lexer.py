# -----------------------------------------------------------------------------
# lexer.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

import ply.lex as lex
import ply.yacc as yacc


class Lexer:

    def __init__(self):
        pass

    global reserved
    reserved = {
        'program': 'PROGRAM',
        'if': 'IF',
        'then': 'THEN',
        'else': 'ELSE',
        'begin': 'BEGIN',
        'end': 'END',
        'while': 'WHILE',
        'do': 'DO',
        'switch': 'SWITCH',
        'of': 'OF',
        'done': 'DONE',
        'default': 'DEFAULT',
        'mod': 'MOD',
        'print': 'PRINT',
        'var': 'VAR',
        'True': 'TRUE',
        'False': 'FALSE',
        'and': 'AND',
        'or': 'OR',
        'not': 'NOT',
    }

    tokens = ['LPAREN', 'RPAREN', 'LT', 'GT', 'EQ', 'NEQ', 'GTE', 'LTE', 'PLUS', 'MINUS', 'MULTIPLY', 'DIV',
              'ASSIGNMENT', 'SCOLON', 'COLON', 'COMMA', 'PERIOD', 'IDENTIFIER', 'TYPE', 'INT', 'REAL'] + list(
        reserved.values())

    # Tokens
    t_OR = r'or'
    t_AND = r'and'
    t_NOT = r'not'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    # t_TRUE = r'true'
    # t_FALSE = r'false'
    t_LT = r'\<'
    t_GT = r'\>'
    t_EQ = r'\='
    t_NEQ = r'<>'
    t_GTE = r'>='
    t_LTE = r'<='
    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_MULTIPLY = r'\*'
    t_DIV = r'\/'
    t_ASSIGNMENT = r':='
    t_PRINT = r'print'
    t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'

    # ignored characters
    t_ignore = " \t"

    def t_FLOAT(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_INT(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        return t

    def t_TRUE(self, t):
        r'true'
        return t

    def t_FALSE(self, t):
        r'false'
        return t

    # def t_FLOATNUMBER(self, t):
    #     r'[+-]?([0-9]{0,9}[.])[0-9]+'
    #     return t
    #
    # def t_INTEGERNUMBER(self, t):
    #     r'[-|+]?(\d+)'
    #     return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    #
    # # def t_ERROR(self, t):
    # #     r'(\d+[a-zA-Z][a-zA-Z0-9]*) | (([0-9]*[.])[0-9]+[.][0-9]+) | ([-][/+][-]) | ([/+][/+]) | ([+-]?([0-9]{10,}[.])[0-9]+) | ([- | /* | // | /+][\s][- | /* | // | /+][\s][- | /* | // | /+]) | ([-|+]?(\d{10,}))'
    # #     return t

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer


# precedence = (
#     ('left', 'OR'),
#     ('left', 'AND'),
#     ('right', 'UNOT'),
# )

# dictionary of names
names = {}
#
# quadruples = []
#
#
# def backpatch(l: list, i: int):
#     for line_number in l:
#         quadruples[line_number - 1] = ("goto", i)
#
#
# def nextinstr():
#     return len(quadruples) + 1
#
#
# def p_marker(self, t):
#     'marker : '
#     t[0] = nextinstr()
#
#
# class E:
#     def __init__(self, t, f):
#         self.truelist = t
#         self.falselist = f
#
#
# def p_expression_or(self, t):
#     '''expression : expression OR marker expression'''
#     backpatch(t[1].falselist, t[3])
#     truelist = t[1].truelist + t[4].truelist
#     falselist = t[4].falselist
#     t[0] = E(truelist, falselist)
#
#
# def p_expression_and(self, t):
#     'expression : expression AND marker expression'
#     backpatch(t[1].truelist, t[3])
#     truelist = t[4].truelist
#     falselist = t[4].falselist + t[1].falselist
#     t[0] = E(truelist, falselist)
#
#
# def p_expression_unot(self, t):
#     'expression : NOT expression %prec UNOT'
#     t[0] = E(t[2].falselist, t[2].truelist)
#
#
# def p_expression_group(self, t):
#     'expression : LPAREN expression RPAREN'
#     t[0] = t[2]
#
#
# def p_expression_true(self, t):
#     'expression : TRUE'
#     t[0] = E([nextinstr()], [])
#     quadruples.append(("goto",))
#
#
# def p_expression_false(self, t):
#     'expression : FALSE'
#     t[0] = E([], [nextinstr()])
#     quadruples.append(("goto",))
#
