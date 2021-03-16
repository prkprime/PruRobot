from bot.modules import inline_ket
from bot.modules import inline_dogge
from bot.modules.assets import inline_welp


def inline_master(update, context):
    query = update.inline_query.query
    if query.startswith('ket'):
        inline_ket(update, context)
    elif query.startswith('dogge'):
        inline_dogge(update, context)
    else:
        context.bot.answer_inline_query(update.inline_query.id, [inline_welp])
