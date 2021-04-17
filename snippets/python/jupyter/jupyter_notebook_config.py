# jupyter_notebook_config.py in $JUPYTER_CONFIG_DIR
c = get_config()

# c.NotebookApp.allow_root = True
c.NotebookApp.ip = '*'
c.NotebookApp.port = 8888  # NOTE don't forget to open
c.NotebookApp.open_browser = False
c.NotebookApp.allow_remote_access = True
c.NotebookApp.password_required = False
c.NotebookApp.password = ''
c.NotebookApp.token = ''
