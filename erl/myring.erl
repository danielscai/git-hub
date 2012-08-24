-module(myring).
-export([start/1,start_proc/2]).

start(Num)->
  FristLoop=spawn(myring,start_proc,[Num,self()]),
  receive last -> io:format("~w~w~n",[last,FristLoop]) end,
  FristLoop!ok.

start_proc(0,Start)->
  Start!last;
start_proc(Num,Start)->
  NPid=spawn(myring,start_proc,[Num-1,Start]),
  receive 
    ok-> io:format("number:~w - pid:~w ~n",[Num,NPid])
  end,
  NPid!ok.
