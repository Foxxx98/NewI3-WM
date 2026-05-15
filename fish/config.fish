if status is-interactive
    # Commands to run in interactive sessions can go he
    fastfetch
end
#neofetch
function fish_greeting
    # do nothing
end
function fish_prompt
    set_color purple
    echo -n (prompt_pwd)
    set_color cyan
    echo -n " "
    echo -n "$USER@$hostname"
    set_color purple
    echo -n "~>"
end
