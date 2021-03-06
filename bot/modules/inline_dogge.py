from telegram import InlineQueryResultPhoto
from uuid import uuid4

from bot.modules.assets import http_code_list_dogge, inline_welp


def inline_dogge(update, context):
    results = []
    query = update.inline_query.query
    if not query:
        context.bot.answer_inline_query(update.inline_query.id, [inline_welp])
    query = query.split(' ', 1)
    if len(query) < 2:
        context.bot.answer_inline_query(update.inline_query.id, [inline_welp])
    else:
        results = [
            InlineQueryResultPhoto(
                id=uuid4(),
                type='photo',
                title=i,
                photo_url=f'https://httpstatusdogs.com/img/{i}.jpg',
                thumb_url=f'https://httpstatusdogs.com/img/{i}.jpg',
                caption=i,
            )
            for i in http_code_list_dogge
            if i.startswith(query[1])
        ]
    if not results:
        context.bot.answer_inline_query(update.inline_query.id, [inline_welp])
    context.bot.answer_inline_query(update.inline_query.id, results)
