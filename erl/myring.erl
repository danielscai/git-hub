-module(myring).
-export([start/1,start_proc/2]).
-export([sleep/2]).
%%-export([sleep/1]).

start(Num)->
  FristLoop=spawn(myring,start_proc,[Num,self()]),
  receive last -> io:format("~w~w~n",[last,FristLoop]) end,
  FristLoop!ok.

start_proc(0,Start)->
  Start!last;
start_proc(Num,Start)->
%%  io:format("~w -- ",[Num rem 1000]), 
%%    0->io:format("~w -- ",[Num])
%%    0->ok
%%    0->sleep(1000)
%%  end,
%%  sleep(Num,1000),
  sleep(Num,1000),
  io:format("~w~n",[Num-1]),
  NPid=spawn(myring,start_proc,[Num-1,Start]),
  receive 
    ok-> io:format("number:~w - pid:~w ~n",[Num,NPid])
%%      ok->ok
  end,
  NPid!ok.

sleep(Num,T)->
  case Num rem 100 of
    0-> 
      receive
      after T -> ok
      end
  end.
