import ply.lex as lex

class Lexer:
    global reserved
    reserved = {
        'true': 'TRUE',
        'false': 'FALSE',
        'return': 'RETURN',
        'print': 'PRINT',
        'void': 'VOID',
        'main': 'MAIN',
        'for': 'FOR',
        'while': 'WHILE',
        'if': 'IF',
        'else': 'ELSE',
        'elif': 'ELIF',
        'int': 'INTEGER',
        'float': 'FLOAT',
        'bool': 'BOOLEAN'
    }

    tokens = [
        'ID',
        'INTEGERNUMBER', 'FLOATNUMBER',
        'NOT', 'AND', 'OR',
        'SUM', 'SUB', 'MUL', 'DIV', 'MOD', 'ASSIGN',
        'NE', 'EQ', 'LT', 'LE', 'GT', 'GE',
        'LCB', 'RCB', 'LRB', 'RRB', 'LSB', 'RSB',
        'SEMICOLON', 'COMMA', 'ERROR'
    ] + list(reserved.values())


    # operations
    t_NOT = r'!'
    t_AND = r'&&'
    t_OR = r'\|\|'
    t_SUM = r'\+'
    t_SUB = r'-'
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_MOD = r'%'
    t_ASSIGN = r'='
    # symbols
    t_NE = r'!='
    t_EQ = r'=='
    t_LT = r'<'
    t_LE = r'<='
    t_GT = r'>'
    t_GE = r'>='
    t_LCB = r'\{'
    t_RCB = r'\}'
    t_LRB = r'\('
    t_RRB = r'\)'
    t_LSB = r'\['
    t_RSB = r'\]'
    t_SEMICOLON = r';'
    t_COMMA = r','

    def t_ERROR(self, t):
        r'([0-9]{10,}[(0-9)|.]*)|[0-9]+[a-zA-Z_][0-9|a-zA-Z_]*|[\+\-\*\/\%]+(\s)*[\+\-\*\/\%]+([\+\-\*\/\%]|(\s))*|(\+\-\*\/\%)]*|[0-9](\.)[0-9](\.)[(0-9)|\.]*'
        return t
        #raise Exception('ERROR at', t.value)

    # identifier
    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reserved.get(t.value, 'ID')  # Check for reserved words
        return t

    # numbers
    def t_FLOATNUMBER(self, t):
        r'([0-9]{1,9})(\.)([0-9]+)'
        t.value = float(t.value)
        return t

    def t_INTEGERNUMBER(self, t):
        r'([0-9]{1,9})'
        t.value = int(t.value)
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = '\n \t'

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer

