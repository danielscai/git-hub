-module(pots).
-author(dcai).
-export([idle/0]).

idle()->
  receive
    {Number,incomming}->
      start_ringing(),
      ringing(Number);
    off_hook->
      start_tone(),
      dial()
   end.

ringing(Number)->
  receive
    {Number,other_on_hook}->
      stop_ringing(),
      idle();
    {Number,off_hook}->
      stop_ringing(),
      connected(Number)
  end.

start_ringing()->
  receive
  after 1->
    bell!
  end.  

start_tone()->
  .

stop_ringing()->
  .

bell()->
  receive 
    start->
      io:format("~w",[ringing]);
    stop->
      true
  end.

