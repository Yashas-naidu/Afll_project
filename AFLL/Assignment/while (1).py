import ply.lex as lex
import ply.yacc as yacc
reserved={
'while':'while'
}
tokens=[
'EQUAL',
'LPAREN',
'RPAREN',
'NUMBER',
'ID',
'LCURLY',
'RCURLY',
'SEMICOLON',
'PLUS',
'LESS',
'MORE'
]+list(reserved.values())
t_EQUAL=r'\='
t_LPAREN=r'\('
t_RPAREN=r'\)'
t_LCURLY=r'\{'
t_RCURLY=r'\}'
t_SEMICOLON=r'\;'
t_PLUS=r'\+'
t_LESS=r'\<'
t_MORE=r'\>'
def t_NUMBER(t):
 r'\d+'
 t.value=int(t.value)
 return t
def t_ID(t):
 r'[a-zA-Z][a-zA-Z0-9]*'
 t.type = reserved.get(t.value,'ID')
 return t
 t_ignore=' '
def t_error(t):
 print("Illegal character '%s'" % t.value[0])
 t.lexer.skip(1)
lexer = lex.lex()
def p_s(p):
  's : w bl con br cl st cr '
def p_w(p):
  'w : while'
def p_se(p):
  'se : SEMICOLON'
def p_con1(p):
  'con : id eq eq id'
def p_con2(p):
 'con : id eq eq no'
def p_con3(p):
 'con : no eq eq id'
def p_con4(p):
 'con : no eq eq no'
def p_con5(p):
 'con : id le eq no'
def p_con6(p):
 'con : id gr eq no'
def p_con7(p):
 'con : id le eq id'
def p_con8(p):
 'con : id gr eq id'
def p_id(p):
 'id : ID'
def p_eq(p):
 'eq : EQUAL'
def p_no(p):
 'no : NUMBER'
def p_cl(p):
 'cl : LCURLY'
def p_cr(p):
 'cr : RCURLY'
def p_bl(p):
 'bl : LPAREN'
def p_br(p):
 'br : RPAREN'
def p_st1(p):
 'st : id eq no se st'
def p_st2(p):
 'st : id eq id se st'
def p_st3(p):
 'st : s'
def p_st4(p):
 'st : id pl pl se st'
def p_st5(p):
 'st : '
def p_pl(p):
 'pl : PLUS'
def p_gr(p):
 'gr : MORE'
def p_le(p):
 'le : LESS'
def p_error(t):
 if(t):
     print("Syntax error at %s" %t.value)
 else:
     print("Syntax error: missing token")
parser = yacc.yacc()
while True:
 try:
   S = input('Enter the syntax > ')
   if S=='q':
      print()
      break
   else:
      parser.parse(S)
 except EOFError:
    break