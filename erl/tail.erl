-module(tail).
-export([sum/1]).

sum_acc([],Sum)->Sum;
sum_acc([Head|Tail],Sum)->sum_acc(Tail,Head+Sum).

sum(List)->sum_acc(List,0).
