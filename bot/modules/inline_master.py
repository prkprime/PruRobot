from bot.modules import inline_ket
from bot.modules import inline_dogge

def inline_master(update, context):
    query = update.inline_query.query
    if query.startswith('ket'):
        inline_ket(update, context)
    elif query.startswith('dogge'):
        inline_dogge(update, context)
    else:
        return