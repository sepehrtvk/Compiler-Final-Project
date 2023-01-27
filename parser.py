from ply import yacc
from lexer import Lexer
from validation import Validation

validate = Validation()


class Parser:
    tokens = Lexer().tokens

    def __init__(self):
        pass

    # def p_program(self, p):
    #     "program : PROGRAM IDENTIFIER declarations compstatement"
    #     print("start : program IDENTIFIER declarations compstatement")

    # def p_declarations_list(self, p):
    #     "declarations : VAR declarationlist"
    #     print("declarations : var declarationlist")
    #
    # def p_declarations_epsilon(self, p):
    #     "declarations : "
    #     print("declarations : ")

    # def p_declarationlist_type(self, p):
    #     "declarationlist : identifierlist COLON type"
    #     print("declarationlist : identifierlist COLON type")

    # def p_declarationlist_identifier(self, p):
    #     "declarationlist : declarationlist SCOLON identifierlist COLON type"
    #     print("declarationlist : identifierlist COLON type")

    # def p_identifierlist_id(self, p):
    #     "identifierlist : IDENTIFIER"
    #     print("identifierlist : identifier")

    # def p_identifierlist_list(self, p):
    #     "identifierlist : identifierlist COMMA IDENTIFIER"
    #     print("identifierlist : identifierlist COMMA identifier")

    # def p_type_int(self, p):
    #     "type : INT"
    #     print("type : INT")
    #
    # def p_type_real(self, p):
    #     "type : REAL"
    #     print("type : REAL")

    # def p_compstatement(self, p):
    #     "compstatement : BEGIN statementlist END"
    #     print("compstatement : BEGIN statementlist END")

    # def p_statementlist(self, p):
    #     "statementlist : statement"
    #     print("statementlist : statement")
    #
    # def p_statementlist_list(self, p):
    #     "statementlist : statementlist SCOLON statement"
    #     print("statementlist : statementlist SCOLON statement")
    #

    def p_statement_assignment(self, p):
        'statement : IDENTIFIER ASSIGNMENT expression'
        print("statement : IDENTIFIER ASSIGNMENT expression")

    def p_statement_expression(self, p):
        "statement : expression"
        print("statement : expression")

    def p_statement_if_else(self, p):
        "statement : IF expression THEN statement ELSE statement"
        print("statement : IF expression THEN statement ELSE statement")

    def p_statement_if(self, p):
        "statement : IF expression THEN statement"
        print("statement : IF expression THEN statement")

    def p_statement_while(self, p):
        "statement : WHILE expression DO statement"
        print("statement : WHILE expression DO statement")

    # def p_statement_compstatement(self, p):
    #     "statement : compstatement"

    # "statement : PRINT LPAREN expression RPAREN"
    # print("statement : PRINT LPAREN expression RPAREN")

    # def p_statement_switch(self, p):
    #     "statement : SWITCH expression OF cases defaultcase DONE"

    # def p_defaultcase_statement(self, p):
    #     "defaultcase : DEFAULT statement SCOLON"
    #
    # def p_defaultcase_epsilon(self, p):
    #     "defaultcase : "

    # def p_cases_list(self, p):
    #     "cases : constantlist COLON statement SCOLON cases"
    #
    # def p_cases_epsilon(self, p):
    #     "cases : "
    #
    # def p_constantlist_const(self, p):
    #     "constantlist : constant"
    #
    # def p_constantlist_list(self, p):
    #     "constantlist : constantlist COMMA constant"

    # def p_constant_real(self, p):
    #     "constant : REAL"
    #
    # def p_constant_integer(self, p):
    #     "constant : INT"
    #
    def p_expression_integer(self, p):
        "expression : INT"
        print("expression : INT")
        p[0] = p[1]

    def p_expression_real(self, p):
        "expression : REAL"
        print("expression : REAL")
        p[0] = p[1]

    def p_expression_identifier(self, p):
        "expression : IDENTIFIER"
        print("expression : IDENTIFIER")
        p[0] = p[1]

    def p_expression_sum(self, p):
        'expression : expression PLUS expression'
        print("expression : expression PLUS expression")

        if not validate.check_operands_type(p):
            return

        p[0] = (p[2], p[1], p[3])
        print(p[0], ":", p[1], p[2], p[3])

    # def run(self, p):
    #     global env
    #     if type(p) == tuple:
    #         if p[0] == '+':
    #             return self.run(p[1]) + self.run(p[2])
    #         elif p[0] == '-':
    #             return self.run(p[1]) - self.run(p[2])
    #         elif p[0] == '*':
    #             return self.run(p[1]) * self.run(p[2])
    #         elif p[0] == '/':
    #             return self.run(p[1]) / self.run(p[2])
    #         elif p[0] == '=':
    #             env[p[1]] = self.run(p[2])
    #             return ''
    #         elif p[0] == 'var':
    #             if p[1] not in env:
    #                 return 'Undeclared variable found!'
    #             else:
    #                 return env[p[1]]
    #     else:
    #         return p

    def p_expression_minus(self, p):
        "expression : expression MINUS expression"
        print("expression : expression MINUS expression")

    def p_expression_cross(self, p):
        "expression : expression MULTIPLY expression"
        print("expression : expression MULTIPLY expression")

    def p_expression_div(self, p):
        "expression : expression DIV expression"
        print("expression : expression DIV expression")

    def p_expression_uminus(self, p):
        "expression : MINUS expression"
        print("expression : MINUS expression")

    def p_expression_mod(self, p):
        "expression : expression MOD expression"
        print("expression : expression MOD expression")

    def p_expression_lt(self, p):
        "expression : expression LT expression"
        print("expression : expression LT expression")

        if not ((type(p[1]) == int or type(p[1]) == float) and (type(p[3]) == int or type(p[3]) == float)):
            return print("Can only operate comparison on integers and floats")

        p[0] = p[1] < p[3]


    def p_expression_eq(self, p):
        "expression : expression EQ expression"
        print("expression : expression EQ expression")

        if not ((type(p[1]) == int or type(p[1]) == float) and (type(p[3]) == int or type(p[3]) == float)):
            return print("Can only operate comparison on integers and floats")

        p[0] = p[1] == p[3]

    def p_expression_gt(self, p):
        "expression : expression GT expression"
        print("expression : expression GT expression")

        if not ((type(p[1]) == int or type(p[1]) == float) and (type(p[3]) == int or type(p[3]) == float)):
            return print("Can only operate comparison on integers and floats")

        p[0] = p[1] > p[3]

    def p_expression_neq(self, p):
        "expression : expression NEQ expression"
        print("expression : expression NEQ expression")

        if not ((type(p[1]) == int or type(p[1]) == float) and (type(p[3]) == int or type(p[3]) == float)):
            return print("Can only operate comparison on integers and floats")

        p[0] = p[1] != p[3]

    def p_expression_lte(self, p):
        "expression : expression LTE expression"
        print("expression : expression LTE expression")

        if not ((type(p[1]) == int or type(p[1]) == float) and (type(p[3]) == int or type(p[3]) == float)):
            return print("Can only operate comparison on integers and floats")

        p[0] = p[1] <= p[3]

    def p_expression_gte(self, p):
        "expression : expression GTE expression"
        print("expression : expression GTE expression")

        if not ((type(p[1]) == int or type(p[1]) == float) and (type(p[3]) == int or type(p[3]) == float)):
            return print("Can only operate comparison on integers and floats")

        p[0] = p[1] >= p[3]

    def p_expression_and(self, p):
        "expression : expression AND expression"
        print("expression : expression AND expression")
        if not validate.check_operands_boolean(p):
            return print("Can only operate comparison on booleans")


    def p_expression_or(self, p):
        "expression : expression OR expression"
        print("expression : expression OR expression")
        if not validate.check_operands_boolean(p):
            return print("Can only operate comparison on booleans")

    def p_expression_not(self, p):
        "expression : NOT expression"
        if type(p[2]) != bool:
            return print("Can only operate logical not on booleans")

        p[0] = not p[2]

    def p_expression_block(self, p):
        "expression : LPAREN expression RPAREN"
        print("expression : LPAREN expression RPAREN")

        p[0] = p[2]


    # def p_stmt_if1(self, p):
    #     "stmt : IF LRB exp RRB stmt elseiflist %prec if1"
    #     print("stmt : IF LRB exp RRB stmt elseiflist %prec if1")
    #
    # def p_stmt_if2(self, p):
    #     "stmt : IF LRB exp RRB stmt elseiflist ELSE stmt"
    #     print("stmt : IF LRB exp RRB stmt elseiflist ELSE stmt")
    #
    # def p_elseiflist_epsilon(self, p):
    #     "elseiflist : %prec eliflist3"
    #     print("elseiflist : ")
    #

    def p_error(self, p):
        print(p.value)
        raise Exception('Parsing Error: Invalid grammar at', p)

    precedence = (
        ('left', 'NOT'),
        ('left', 'COMMA'),
        ('right', 'ASSIGNMENT'),
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'EQ', 'NEQ'),
        ('left', 'GT', 'GTE'),
        ('left', 'LT', 'LTE'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'MULTIPLY', 'DIV', 'MOD'),
        ('right', 'IF', 'THEN', 'ELSE')
    )

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
