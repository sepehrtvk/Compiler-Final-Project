# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'program': 'PROGRAM',
    'int': 'INT',
    'real': 'REAL',
    'begin': 'BEGIN',
    'end': 'END',
    'while': 'WHILE',
    'do': 'DO',
    'switch': 'SWITCH',
    'of': 'OF',
    'done': 'DONE',
    'default': 'DEFAULT'
}

tokens = [
             'TRUE', 'FALSE',
             'AND', 'OR', 'NOT',
             'LPAREN', 'RPAREN',
             'LT', 'GT', 'EQ', 'NEQ', 'GTE', 'LTE', 'PLUS', 'MINUS', 'CROSS', 'MUL', 'MOD', 'ASSIGNMENT',
             'SCOLON', 'COLON', 'COMMA', 'PERIOD'
         ] + list(reserved.values())

# Tokens
t_OR = r'or'
t_AND = r'and'
t_NOT = r'not'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_TRUE = r'true'
t_FALSE = r'false'
t_LT = r'\<'
t_GT = r'\>'
t_EQ = r'\='
t_NEQ = r'<>'
t_GTE = r'>='
t_LTE = r'<='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_CROSS = r'\*'
t_MUL = r'\/'
t_ASSIGNMENT = r':='
t_MOD = r'mod'

# ignored characters
t_ignore = " \t"


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_NAME(t):
    r'[_a-zA-Z][_a-zA-Z0-9]*'
    t.type = 'NAME'
    return t


#
# def t_IF(t):
#     r'if'
#     return t
#
#
# def t_FOR(t):
#     r'for'
#     return t
#
#
# def t_WHILE(t):
#     r'while'
#     return t
#
#
# def t_MAIN(t):
#     r'main'
#     return t
#
#
# def t_VOID(t):
#     r'void'
#     return t
#
#
# def t_PRINT(t):
#     r'print'
#     return t
#

# def t_FLOAT(t):
#     r'float'
#     return t
#
#
# def t_INT(t):
#     r'int'
#     return t

#
# def t_BOOLEAN(t):
#     r'bool'
#     return t
#

# def t_TRUE(t):
#     r'true'
#     return t
#
#
# def t_FALSE(t):
#     r'false'
#     return t
#
#
# def t_RETURN(t):
#     r'return'
#     return t
#
#
# def t_ELIF(t):
#     r'elif'
#     return t
#
#
# def t_ELSE(t):
#     r'else'
#     return t
#
#
# def t_FLOATNUMBER(t):
#     r'[+-]?([0-9]{0,9}[.])[0-9]+'
#     return t
#
#
# def t_INTEGERNUMBER(t):
#     r'[-|+]?(\d+)'
#     return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


# def t_ERROR(t):
#     r'(\d+[a-zA-Z][a-zA-Z0-9]*) | (([0-9]*[.])[0-9]+[.][0-9]+) | ([-][/+][-]) | ([/+][/+]) | ([+-]?([0-9]{10,}[.])[0-9]+) | ([- | /* | // | /+][\s][- | /* | // | /+][\s][- | /* | // | /+]) | ([-|+]?(\d{10,}))'
#     return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer

lexer = lex.lex()

lexer.input('abc=123')

while True:
    tok = lexer.token()
    if not tok:
        break

    print(tok)
