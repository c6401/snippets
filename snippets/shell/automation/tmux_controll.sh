tmux new-session -d -s my_session 'app'
tmux send-keys -t my_session Enter
tmux capture-pane -pt my_session:0.0 -S -1000 \; show-buffer
tmux delete-buffer
tmux kill-session -t my_session
