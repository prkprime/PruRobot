from telegram import InlineQueryResultPhoto
from uuid import uuid4

from .http_codes import http_code_list


def inline_ket(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = [
        InlineQueryResultPhoto(
            id=uuid4(),
            type='photo',
            title=i,
            photo_url=f'https://http.cat/{i}',
            thumb_url=f'https://http.cat/{i}',
            caption=i,
        )
        for i in http_code_list
        if i.startswith(query)
    ]
    context.bot.answer_inline_query(update.inline_query.id, results)
