-module(echo).
-export([go/0,loop/0]).

go()->
  Loop=spawn(echo,loop,[]),
  Loop!{self(),hello}.

loop()->
  receive
    {_From,Msg}->
      {self(),Msg},
      loop();
    stop->
      true
  end.
