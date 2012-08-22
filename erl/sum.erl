-module(sum).
-export([sum/1]).

sum([])->0;
sum([Head|Tail])->Head+sum(Tail).


