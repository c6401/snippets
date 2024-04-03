async def sms_messages(starting=None):
    chunks = []
    for offset in range(1000000):
        logging.info('fetching sms chunk')
        raw_data = await asyncronously(
          sh, f'ssh ... termux-sms-list -o {offset * 100} -l 100'
        )
        msgs = json.loads(raw_data)
        if not msgs:
            break
        chunks.append(msgs)

        if starting and msgs[0]['received'] < starting:
            break

    for chunk in chunks[::-1]:
        for msg in chunk:
            if starting and msg['received'] <= starting:
                continue
            yield msg
