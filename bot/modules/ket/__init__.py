from telegram import InlineQueryResultArticle, InputTextMessageContent

from .http_codes import http_code_list


def inline_ket(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = [
        InlineQueryResultArticle(
            id=i + ' id',
            title=i + ' title',
            input_message_content=InputTextMessageContent(i + ' message'),
        )
        for i in http_code_list
        if i.startswith(query)
    ]
    context.bot.answer_inline_query(update.inline_query.id, results)
