from lexer import Lexer
from parser import Parser

lexer = Lexer().build()
filename = 'test.txt'
file = open(filename)
text_input = file.read()
file.close()
lexer.input(text_input)
for tok in lexer:
    print(tok)
parser = Parser()
parser.build().parse(text_input, lexer, False)
