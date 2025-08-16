from src.common import bot


# Handle '/start' and '/help' #Взято из файла main.py и отредактировано
@bot.message_handler(commands=['rules'])
async def send_rules(message):
    text = 'Bot rules'
    await bot.reply_to(message, text)
