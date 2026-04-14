if status is-interactive
    # Commands to run in interactive sessions can go here
end

function lk
  set loc (walk $argv); and cd $loc;
end

set fish_greeting

