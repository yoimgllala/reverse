RuKeys = """ёйцукенгшщзхъфывапролджэячсмитьбю.Ё"№;%:?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"""
EnKeys = """`qwertyuiop[]asdfghjkl;'zxcvbnm,./~@#$%^&QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?"""
if not message.is_reply: return ""
text = reply.raw_text
change = str.maketrans(RuKeys + EnKeys, EnKeys + RuKeys)
text = str.translate(text, change)
if message.from_id != reply.from_id:
    await message.edit(text)
else:
    await message.delete()
    await reply.edit(text)