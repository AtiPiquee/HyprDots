if status is-interactive
    # Commands to run in interactive sessions can go here

    function lk
        set loc (walk $argv); and cd $loc;
    end
end


set fish_greeting

