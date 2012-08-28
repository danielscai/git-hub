-module(sleep).
-export([say/0,sleep/1]).

say()->
  sleep(1000),
  io:format("~w~n",[hello]),
  sleep(1000),
  io:format("~w~n",[world]).


sleep(T)->
  receive
  after T ->true 
  end.

