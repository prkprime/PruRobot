from telegram import InlineQueryResultArticle, InputTextMessageContent
from uuid import uuid4

inline_welp_message = '''Hello There.\n
@PruRobot ket <http status code>\n
@PruRobot dogge <http status code>\n

Kode l1nk : https://github.com/prkprime/PruRobot
'''

inline_welp = InlineQueryResultArticle(
    id=uuid4(),
    title='Click here for Welp',
    input_message_content=InputTextMessageContent(message_text=inline_welp_message),
)
