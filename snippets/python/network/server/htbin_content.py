content_length = int(os.environ["CONTENT_LENGTH"])
stdin = sys.stdin.read(content_length)
