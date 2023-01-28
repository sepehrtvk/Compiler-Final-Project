from ply import yacc
from lexer import Lexer
from validation import Validation
from colorama import Fore

validate = Validation()


class Parser:
    tokens = Lexer().tokens

    variables = {}

    def __init__(self):
        pass

    def p_program(self, p):
        "program : PROGRAM IDENTIFIER declarations compstatement"
        print("program : PROGRAM IDENTIFIER declarations compstatement")

    def p_declarations_list(self, p):
        "declarations : VAR IDENTIFIER COLON type"
        print("declarations : var", p[2], ":", p[4])
        self.variables[p[2]] = 0
        print(self.variables)

    def p_declarations_epsilon(self, p):
        "declarations : "
        print("declarations : ")

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

    def p_type_int(self, p):
        "type : INTEGER"
        print("type : INTEGER")
        p[0] = p[1]

    def p_type_real(self, p):
        "type : REAL"
        print("type : REAL")
        p[0] = p[1]

    def p_compstatement(self, p):
        "compstatement : BEGIN statementlist END"
        print("compstatement : BEGIN statement END")

    def p_statementlist(self, p):
        "statementlist : statement"
        print("statementlist : statement")

    def p_statementlist_list(self, p):
        "statementlist : statementlist SCOLON statement"
        print("statementlist : statementlist SCOLON statement")

    def p_statement_assignment(self, p):
        'statement : IDENTIFIER ASSIGNMENT expression'
        print("statement : IDENTIFIER ASSIGNMENT expression")

        self.variables[p[1]] = p[3]
        print(self.variables)

    def p_statement_expression(self, p):
        "statement : expression"
        print("statement : expression", p[1])
        p[0] = p[1]

    def p_statement_if_else(self, p):
        "statement : IF expression THEN statement ELSE statement"
        print("statement : IF expression THEN statement ELSE statement")
        print(p[0], p[1], p[2], p[3], p[4], p[5], p[6])

        if bool(p[2]):
            p[0] = p[4]
        else:
            p[0] = p[6]

        print(p[0])

    def p_statement_if(self, p):
        "statement : IF expression THEN statement %prec IF"
        print("statement : IF expression THEN statement")
        print(p[0], p[1], p[2], p[3], p[4])

        if bool(p[2]):
            p[0] = p[4]

        print(p[0])

    def p_statement_while(self, p):
        "statement : WHILE expression DO statement"
        print("statement : WHILE expression DO statement")

        if bool(p[2]):
            pass

    # def p_statement_compstatement(self, p):
    #     "statement : compstatement"

    def p_print(self, p):
        "statement : PRINT LPAREN expression RPAREN"
        print("statement : PRINT LPAREN expression RPAREN")
        print(p[3])

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
    #     "constant : FLOAT"
    #
    # def p_constant_integer(self, p):
    #     "constant : INT"
    #
    def p_expression_integer(self, p):
        "expression : INT"
        print("expression : INT")
        p[0] = p[1]

    def p_expression_real(self, p):
        "expression : FLOAT"
        print("expression : FLOAT")
        p[0] = p[1]

    def p_expression_identifier(self, p):
        "expression : IDENTIFIER"
        print("expression : IDENTIFIER")
        try:
            p[0] = self.variables[p[1]]
        except LookupError:
            print(Fore.RED, p[1], 'is not declared.')

    def p_expression_sum(self, p):
        'expression : expression PLUS expression'
        print("expression : expression PLUS expression")

        if not validate.check_operands_type(p):
            return print(Fore.RED + "ERROR: SUM: operands types are not int or float")

        p[0] = p[1] + p[3]
        print(p[0], "=", p[1], p[2], p[3])

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

        if not validate.check_operands_type(p):
            return print(Fore.RED + "ERROR: MINUS: operands types are not int or float")

        p[0] = p[1] - p[3]
        print(p[0], "=", p[1], p[2], p[3])

    def p_expression_cross(self, p):
        "expression : expression MULTIPLY expression"
        print("expression : expression MULTIPLY expression")

        if (type(p[1]) == int or type(p[1]) == float) and (type(p[3]) == int or type(p[3]) == float):
            p[0] = p[1] * p[3]
            print(p[0], "=", p[1], p[2], p[3])
            return

        return print(Fore.RED + "ERROR: CROSS: operands types are not int or float")

    def p_expression_div(self, p):
        "expression : expression DIV expression"
        print("expression : expression DIV expression")

        if (type(p[1]) == int or type(p[1]) == float) and (type(p[3]) == int or type(p[3]) == float):
            p[0] = p[1] / p[3]
            print(p[0], "=", p[1], p[2], p[3])
            return

        return print(Fore.RED + "ERROR: DIVIDE: operands types are not int or float")

    def p_expression_uminus(self, p):
        "expression : MINUS expression %prec UMINUS"
        print("expression : MINUS expression")

        p[0] = -p[2]

    def p_expression_mod(self, p):
        "expression : expression MOD expression"
        print("expression : expression MOD expression")

        if type(p[1]) == int and type(p[3]) == int:
            p[0] = p[1] % p[3]
            print(p[0], "=", p[1], p[2], p[3])
            return

        return print(Fore.RED + "ERROR: MOD: operands types are not int")

    def p_expression_lt(self, p):
        "expression : expression LT expression"
        print("expression : expression LT expression")

        if not ((type(p[1]) == int or type(p[1]) == float) and (type(p[3]) == int or type(p[3]) == float)):
            return print(Fore.RED + "ERROR: LESS_THAN: operands types are not int or float")

        p[0] = p[1] < p[3]
        print(p[0], "=", p[1], p[2], p[3])

    def p_expression_eq(self, p):
        "expression : expression EQ expression"
        print("expression : expression EQ expression")

        if not ((type(p[1]) == int or type(p[1]) == float) and (type(p[3]) == int or type(p[3]) == float)):
            return print(Fore.RED + "ERROR: EQUAL: operands types are not int or float")

        p[0] = p[1] == p[3]

    def p_expression_gt(self, p):
        "expression : expression GT expression"
        print("expression : expression GT expression")

        if not ((type(p[1]) == int or type(p[1]) == float) and (type(p[3]) == int or type(p[3]) == float)):
            return print(Fore.RED + "ERROR: GREATER_THAN: operands types are not int or float")

        p[0] = p[1] > p[3]
        print(p[0], ":", p[1], p[2], p[3])

    def p_expression_neq(self, p):
        "expression : expression NEQ expression"
        print("expression : expression NEQ expression")

        if not ((type(p[1]) == int or type(p[1]) == float) and (type(p[3]) == int or type(p[3]) == float)):
            return print(Fore.RED + "ERROR: NOT_EQUAL: operands types are not int or float")

        p[0] = p[1] != p[3]

    def p_expression_lte(self, p):
        "expression : expression LTE expression"
        print("expression : expression LTE expression")

        if not ((type(p[1]) == int or type(p[1]) == float) and (type(p[3]) == int or type(p[3]) == float)):
            return print(Fore.RED + "ERROR: LESS_THAN_EQ: operands types are not int or float")

        p[0] = p[1] <= p[3]

    def p_expression_gte(self, p):
        "expression : expression GTE expression"
        print("expression : expression GTE expression")

        if not ((type(p[1]) == int or type(p[1]) == float) and (type(p[3]) == int or type(p[3]) == float)):
            return print(Fore.RED + "ERROR: GREATER_THAN_EQ: operands types are not int or float")

        p[0] = p[1] >= p[3]

    def p_expression_and(self, p):
        "expression : expression AND expression"
        print("expression : expression AND expression")
        if not validate.check_operands_boolean(p):
            return print(Fore.RED + "ERROR: AND: operands types are not bool")

        p[0] = p[1] and p[3]

    def p_expression_or(self, p):
        "expression : expression OR expression"
        print("expression : expression OR expression")
        if not validate.check_operands_boolean(p):
            return print(Fore.RED + "ERROR: OR: operands types are not bool")

        p[0] = p[1] or p[3]

    def p_expression_not(self, p):
        "expression : NOT expression"
        if not validate.check_is_bool(p):
            return print(Fore.RED + "ERROR: NOT: operands types are not bool")

        p[0] = not p[2]

    def p_expression_block(self, p):
        "expression : LPAREN expression RPAREN"
        print("expression : LPAREN expression RPAREN")

        p[0] = p[2]

    def p_error(self, p):
        print('p.value', p.value)
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
        ('right', 'UMINUS'),
        ('right', 'IF'),
        ('left', 'ELSE')
    )

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
