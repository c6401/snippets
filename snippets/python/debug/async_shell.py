from ptpython.repl import embed
await embed(globals=globals(), locals=locals(), return_asyncio_coroutine=True, patch_stdout=True)
