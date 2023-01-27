from ply import yacc
from lexer import Lexer


class Parser:
    tokens = Lexer().tokens

    def __init__(self):
        pass

    def p_program(self, p):
        "program : PROGRAM identifier declarations compstatement"
        print("start : program identifier declarations compstatement")

    def p_declarations_list(self, p):
        "declarations : VAR declarationlist"
        print("declarations : var declarationlist")

    def p_declarations_epsilon(self, p):
        "declarations : "
        print("declarations : ")

    def p_declarationlist_type(self, p):
        "declarationlist : identifierlist COLON type"
        print("declarationlist : identifierlist COLON type")

    def p_declarationlist_identifier(self, p):
        "declarationlist : declarationlist SCOLON identifierlist COLON type"
        print("declarationlist : identifierlist COLON type")

    def p_identifierlist_id(self, p):
        "identifierlist : identifier"
        print("identifierlist : identifier")

    def p_identifierlist_list(self, p):
        "identifierlist : identifierlist COMMA identifier"
        print("identifierlist : identifierlist COMMA identifier")

    def p_type_int(self, p):
        "type : INT"
        print("type : INT")

    def p_type_real(self, p):
        "type : REAL"
        print("type : REAL")

    def p_compstatement(self, p):
        "compstatement : BEGIN statementlist END"
        print("compstatement : BEGIN statementlist END")

    def p_statementlist(self, p):
        "statementlist : statement"
        print("statementlist : statement")

    def p_statementlist_list(self, p):
        "statementlist : statementlist SCOLON statement"
        print("statementlist : statementlist SCOLON statement")

    def p_statement_expr(self, p):
        "statement : identifier ASSIGNMENT expression"

    def p_statement_if_else(self, p):
        "statement : IF expression THEN statement ELSE statement"

    def p_statement_if(self, p):
        "statement : IF expression THEN statement"

    def p_statement_while(self, p):
        "statement : WHILE expression DO statement"

    def p_statement_compstatement(self, p):
        "statement : compstatement"

    def p_statement_print(self, p):
        "statement : print LPAREN expression RPAREN"

    def p_statement_switch(self, p):
        "statement : SWITCH expression OF cases defaultcase DONE"

    def p_defaultcase_statement(self, p):
        "defaultcase : DEFAULT statement SCOLON"

    def p_defaultcase_epsilon(self, p):
        "defaultcase : "

    def p_cases_list(self, p):
        "cases : constantlist COLON statement SCOLON cases"

    def p_cases_epsilon(self, p):
        "cases : "

    def p_constantlist_const(self, p):
        "constantlist : constant"

    def p_constantlist_list(self, p):
        "constantlist : constantlist COMMA constant"

    def p_constant_real(self, p):
        "constant : real"

    def p_constant_integer(self, p):
        "constant : integer"

    def p_expression_integer(self, p):
        "expression : integer"

    def p_expression_real(self, p):
        "expression : real"

    def p_expression_identifier(self, p):
        "expression : identifier"

    def p_expression_sum(self, p):
        "expression : expression SUM expression"
        p[0] = (p[2], p[1], p[3])

    def p_expression_minus(self, p):
        "expression : expression MINUS expression"

    def p_expression_cross(self, p):
        "expression : expression CROSS expression"

    def p_expression_div(self, p):
        "expression : expression DIV expression"

    def p_expression_uminus(self, p):
        "expression : MINUS expression"

    def p_expression_mod(self, p):
        "expression : expression MOD expression"

    def p_expression_lt(self, p):
        "expression : expression LT expression"

    def p_expression_eq(self, p):
        "expression : expression EQ expression"

    def p_expression_gt(self, p):
        "expression : expression GT expression"

    def p_expression_neq(self, p):
        "expression : expression NEQ expression"

    def p_expression_lte(self, p):
        "expression : expression LTE expression"

    def p_expression_gte(self, p):
        "expression : expression GTE expression"

    def p_expression_and(self, p):
        "expression : expression AND expression"

    def p_expression_or(self, p):
        "expression : expression OR expression"

    def p_expression_not(self, p):
        "expression : NOT expression"

    def p_expression_block(self, p):
        "expression : LPAREN expression RPAREN"


    # def p_type_bool(self, p):
    #     "type : BOOLEAN"
    #     print("type : BOOLEAN", p[1])
    #
    # def p_iddec_id1(self, p):
    #     "iddec : ID"
    #     print("iddec : ID", p[1])
    #
    # def p_iddec_id2(self, p):
    #     "iddec : ID LSB exp RSB"
    #     print("iddec : ID LSB exp RSB")
    #
    # def p_iddec_id3(self, p):
    #     "iddec : ID ASSIGN exp"
    #     print("iddec : ID ASSIGN exp")
    #
    # def p_idlist_iddec1(self, p):
    #     "idlist : iddec"
    #     print("idlist : iddec", p[1])
    #
    # def p_idlist_iddec2(self, p):
    #     "idlist : iddec COMMA idlist"
    #     print("idlist : iddec COMMA idlist")
    #
    # def p_vardec(self, p):
    #     "vardec : type idlist SEMICOLON"
    #     print("vardec : type idlist SEMICOLON")
    #
    # def p_funcdec_type(self, p):
    #     "funcdec : type ID LRB paramdecs RRB block"
    #     print("funcdec : type ID LRB paramdecs RRB block")
    #
    # def p_funcdec_void(self, p):
    #     "funcdec : VOID ID LRB paramdecs RRB block"
    #     print("funcdec : VOID ID LRB paramdecs RRB block")
    #
    # def p_paramdecs_paramdecslist(self, p):
    #     "paramdecs : paramdecslist"
    #     print("paramdecs : paramdecslist", p[1])
    #
    # def p_paramdecs_epsilon(self, p):
    #     "paramdecs : "
    #     print("paramdecs : ")
    #
    # def p_paramdecslist_paramdec1(self, p):
    #     "paramdecslist : paramdec"
    #     print("paramdecslist : paramdec", p[1])
    #
    # def p_paramdecslist_paramdec2(self, p):
    #     "paramdecslist : paramdec COMMA paramdecslist"
    #     print("paramdecslist : paramdec COMMA paramdecslist")
    #
    # def p_paramdec_type1(self, p):
    #     "paramdec : type ID"
    #     print("paramdec : type ID")
    #
    # def p_paramdec_type2(self, p):
    #     "paramdec : type ID LSB RSB"
    #     print("paramdec : type ID LSB RSB")
    #
    # def p_varlist_vardec(self, p):
    #     "varlist : vardec varlist"
    #     print("varlist : vardec varlist")
    #
    # def p_varlist_epsilon(self, p):
    #     "varlist : "
    #     print("varlist : ")
    #
    # def p_block(self, p):
    #     "block : LCB varlist stmtlist RCB"
    #     print("block : LCB varlist stmtlist RCB")
    #
    # def p_stmtlist_stmt(self, p):
    #     "stmtlist : stmt stmtlist"
    #     print("stmtlist : stmt stmtlist")
    #
    # def p_stmtlist_epsilon(self, p):
    #     "stmtlist : "
    #     print("stmtlist : ")
    #
    # def p_lvalue_id1(self, p):
    #     "lvalue : ID"
    #     print("lvalue : ID", p[1])
    #
    # def p_lvalue_id2(self, p):
    #     "lvalue : ID LSB exp RSB"
    #     print("lvalue : ID LSB exp RSB")
    #
    # def p_stmt_return(self, p):
    #     "stmt : RETURN exp SEMICOLON"
    #     print("stmt : RETURN exp SEMICOLON")
    #
    # def p_stmt_exp(self, p):
    #     "stmt : exp SEMICOLON"
    #     print("stmt : exp SEMICOLON")
    #
    # def p_stmt_block(self, p):
    #     "stmt : block"
    #     print("stmt : block", p[1])
    #
    # def p_stmt_while(self, p):
    #     "stmt : WHILE LRB exp RRB stmt"
    #     print("stmt : WHILE LRB exp RRB stmt")
    #
    # def p_stmt_for(self, p):
    #     "stmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt"
    #     print("stmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt")
    #
    # def p_stmt_if1(self, p):
    #     "stmt : IF LRB exp RRB stmt elseiflist %prec if1"
    #     print("stmt : IF LRB exp RRB stmt elseiflist")
    #
    # def p_stmt_if2(self, p):
    #     "stmt : IF LRB exp RRB stmt elseiflist ELSE stmt"
    #     print("stmt : IF LRB exp RRB stmt elseiflist ELSE stmt")
    #
    # def p_stmt_print(self, p):
    #     "stmt : PRINT LRB ID RRB SEMICOLON"
    #     print("stmt : PRINT LRB ID RRB SEMICOLON")
    #
    # def p_elseiflist_elif(self, p):
    #     "elseiflist : ELIF LRB exp RRB stmt"
    #     print("elseiflist : ELIF LRB exp RRB stmt")
    #
    # def p_elseiflist_elseiflist(self, p):
    #     "elseiflist : elseiflist ELIF LRB exp RRB stmt"
    #     print("elseiflist : elseiflist ELIF LRB exp RRB stmt")
    #
    # def p_elseiflist_epsilon(self, p):
    #     "elseiflist : %prec eliflist3"
    #     print("elseiflist : ")
    #
    # def p_exp_lvalue1(self, p):
    #     "exp : lvalue ASSIGN exp"
    #     print("exp : lvalue ASSIGN exp")
    #
    # def p_exp_lvalue2(self, p):
    #     "exp : lvalue"
    #     print("exp : lvalue", p[1])
    #
    # def p_exp_or(self, p):
    #     "exp : exp OR exp"
    #     print("exp : exp OR exp")
    #
    # def p_exp_and(self, p):
    #     "exp : exp AND exp"
    #     print("exp : exp AND exp")
    #
    # def p_exp_sum(self, p):
    #     "exp : exp SUM exp"
    #     print("exp : exp SUM exp")
    #
    # def p_exp_sub(self, p):
    #     "exp : exp SUB exp"
    #     print("exp : exp SUB exp")
    #
    # def p_exp_mul(self, p):
    #     "exp : exp MUL exp"
    #     print("exp : exp MUL exp")
    #
    # def p_exp_div(self, p):
    #     "exp : exp DIV exp"
    #     print("exp : exp DIV exp")
    #
    # def p_exp_mod(self, p):
    #     "exp : exp MOD exp"
    #     print("exp : exp MOD exp")
    #
    # def p_exp_gt(self, p):
    #     "exp : exp GT exp"
    #     print("exp : exp GT exp")
    #
    # def p_exp_lt(self, p):
    #     "exp : exp LT exp"
    #     print("exp : exp LT exp")
    #
    # def p_exp_ne(self, p):
    #     "exp : exp NE exp"
    #     print("exp : exp NE exp")
    #
    # def p_exp_eq(self, p):
    #     "exp : exp EQ exp"
    #     print("exp : exp EQ exp")
    #
    # def p_exp_le(self, p):
    #     "exp : exp LE exp"
    #     print("exp : exp LE exp")
    #
    # def p_exp_ge(self, p):
    #     "exp : exp GE exp"
    #     print("exp : exp GE exp")
    #
    # def p_exp_exp3(self, p):
    #     "exp : LRB exp RRB"
    #     print("exp : LRB exp RRB")
    #
    # def p_exp_exp4(self, p):
    #     "exp : SUB exp"
    #     print("exp : SUB exp")
    #
    # def p_exp_exp5(self, p):
    #     "exp : NOT exp"
    #     print("exp : NOT exp")
    #
    # def p_exp_const(self, p):
    #     "exp : const"
    #     print("exp : const", p[1])
    #
    # def p_exp_id1(self, p):
    #     "exp : ID LRB explist RRB"
    #     print("exp : ID LRB explist RRB")
    #
    # def p_exp_id2(self, p):
    #     "exp : ID LRB RRB"
    #     print("exp : ID LRB RRB")
    #
    # def p_const_intnumber(self, p):
    #     "const : INTEGERNUMBER"
    #     print("const : INTEGERNUMBER", p[1])
    #
    # def p_const_floatnumber(self, p):
    #     "const : FLOATNUMBER"
    #     print("const : FLOATNUMBER", p[1])
    #
    # def p_const_true(self, p):
    #     "const : TRUE"
    #     print("const : TRUE", p[1])
    #
    # def p_const_false(self, p):
    #     "const : FALSE"
    #     print("const : FALSE", p[1])
    #
    # def p_explist_exp1(self, p):
    #     "explist : exp"
    #     print("explist : exp", p[1])
    #
    # def p_explist_exp2(self, p):
    #     "explist : exp COMMA explist"
    #     print("explist : exp COMMA explist")

    def p_error(self, p):
        print(p.value)
        raise Exception('Parsing Error: Invalid grammar at', p)

    precedence = (
        ('left', 'IF'),
        ('left', 'NOT'),
        ('left', 'COMMA'),
        ('right', 'ASSIGN'),
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'EQ', 'NE'),
        ('left', 'GT', 'GE'),
        ('left', 'LT', 'LE'),
        ('left', 'SUM', 'SUB'),
        ('left', 'MUL', 'DIV', 'MOD'),
        ('right', 'if1', 'eliflist3', 'ELSE', 'ELIF')
    )

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
