-module(bump).
-export([bump/1]).

%bump test
bump([])->[];
bump([Head|Tail])->[Head+1|bump(Tail)].
