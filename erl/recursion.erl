-module(recursion).
-export([r/0]).

r()->
  r().

