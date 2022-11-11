# 2)Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор( можно добавить работу с рациональными и комплексными числами), организовать меню, добавив в неё систему логирования

# Имя бота: python_test_homework_bot


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hello\n/sum\n/dif')

async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')

async def dif(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} - {y} = {x - y}')

app = ApplicationBuilder().token("5788610930:AAHHW-FsfifxsGD7w6l6ah5e4FvLo3s7BGY").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sum",sum))
app.add_handler(CommandHandler("dif",dif))
app.add_handler(CommandHandler("help",help))

print("сервер запущен")

app.run_polling()