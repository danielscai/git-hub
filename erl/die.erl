-module(die).
-export([die/1]).

die(N)->
  (1+die(N))/2.
