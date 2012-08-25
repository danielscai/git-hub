%{
#include <stdio.h>

void yyerror(const char *str)
{
  fprintf(stderr,"error:%s\n",str);
}


int main()
{
  yyparse();
  return 0;
}

%}

%%
statements:
  | statements statement
  ;

statement:
  SET VARIABLE ASSIGN expression END
  {
    printf("properly formed\n");
  }
  ;

expression:
  NUMBER
  |
  VARIABLE
  |
  VARIABLE operator NUMBER
  |
  VARIABLE operator VARIABLE
  ;

operator:
  OP_MINUS
  |
  OP_PLUS
  ;


