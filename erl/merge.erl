-module(merge).
-export([merge/2]).

merge(Xs,Ys)->
  lists:reverse(mergeL(Xs,Ys,[])).

mergeL([X|Xs],Ys,Zs)->
  mergeR(Xs,Ys,[X|Zs]);
mergeL([],[],Zs) -> 
  Zs.

mergeR(Xs,[Y|Ys],Zs)->
  mergeL(Xs,Ys,[Y|Zs]);
mergeR([],[],Zs)->
  Zs.


