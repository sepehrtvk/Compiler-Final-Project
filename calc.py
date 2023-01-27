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
             'LT', 'GT', 'EQ', 'NEQ', 'GTE', 'LTE', 'PLUS', 'MINUS', 'CROSS', 'DIV', 'MOD', 'ASSIGNMENT',
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
t_DIV = r'\/'
t_ASSIGNMENT = r':='
t_MOD = r'mod'

# ignored characters
t_ignore = " \t"


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_ID(t):
    r'[_a-zA-Z][_a-zA-Z0-9]*'
    return t


def t_IF(t):
    r'if'
    return t


def t_FOR(t):
    r'for'
    return t


def t_WHILE(t):
    r'while'
    return t


def t_MAIN(t):
    r'main'
    return t


def t_VOID(t):
    r'void'
    return t


def t_PRINT(t):
    r'print'
    return t


def t_FLOAT(t):
    r'float'
    return t


def t_INT(t):
    r'int'
    return t


def t_BOOLEAN(t):
    r'bool'
    return t


def t_TRUE(t):
    r'true'
    return t


def t_FALSE(t):
    r'false'
    return t


def t_RETURN(t):
    r'return'
    return t


def t_ELIF(t):
    r'elif'
    return t


def t_ELSE(t):
    r'else'
    return t


def t_FLOATNUMBER(t):
    r'[+-]?([0-9]{0,9}[.])[0-9]+'
    return t


def t_INTEGERNUMBER(t):
    r'[-|+]?(\d+)'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_ERROR(t):
    r'(\d+[a-zA-Z][a-zA-Z0-9]*) | (([0-9]*[.])[0-9]+[.][0-9]+) | ([-][/+][-]) | ([/+][/+]) | ([+-]?([0-9]{10,}[.])[0-9]+) | ([- | /* | // | /+][\s][- | /* | // | /+][\s][- | /* | // | /+]) | ([-|+]?(\d{10,}))'
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer

lexer = lex.lex()

# Parsing rules

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'UNOT'),
)

# dictionary of names
names = {}

quadruples = []


def backpatch(l: list, i: int):
    for line_number in l:
        quadruples[line_number - 1] = ("goto", i)


def nextinstr():
    return len(quadruples) + 1


def p_marker(t):
    'marker : '
    t[0] = nextinstr()


class E:
    def __init__(self, t, f):
        self.truelist = t
        self.falselist = f


def p_expression_or(t):
    '''expression : expression OR marker expression'''
    backpatch(t[1].falselist, t[3])
    truelist = t[1].truelist + t[4].truelist
    falselist = t[4].falselist
    t[0] = E(truelist, falselist)


def p_expression_and(t):
    'expression : expression AND marker expression'
    backpatch(t[1].truelist, t[3])
    truelist = t[4].truelist
    falselist = t[4].falselist + t[1].falselist
    t[0] = E(truelist, falselist)


def p_expression_unot(t):
    'expression : NOT expression %prec UNOT'
    t[0] = E(t[2].falselist, t[2].truelist)


def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]


def p_expression_true(t):
    'expression : TRUE'
    t[0] = E([nextinstr()], [])
    quadruples.append(("goto",))


def p_expression_false(t):
    'expression : FALSE'
    t[0] = E([], [nextinstr()])
    quadruples.append(("goto",))


def p_error(t):
    print("Syntax error at '%s'" % t.value)


parser = yacc.yacc(start="expression")

while True:
    try:
        s = input('calc > ')  # Use raw_input on Python 2
    except EOFError:
        break
    r = parser.parse(s)
    print(quadruples)
    print(r.truelist, r.falselist)
    quadruples.clear()
