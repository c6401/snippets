import logging, sys, traceback

logging.Formatter.formatException = lambda _, ei: "".join(traceback.TracebackException(*ei, capture_locals=True).format())  # ty: ignore
sys.excepthook = lambda t, v, tb: sys.stderr.write("".join(traceback.TracebackException(t, v, tb, capture_locals=True).format()))  # ty: ignore
