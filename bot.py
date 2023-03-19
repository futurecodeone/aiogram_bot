from aiogram import Bot, Dispatcher, types, executor
import logging

TOKEN = '6200931564:AAHkMfW_Q_dHQ9YdRitmcVLxsx8UvgMGr34'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
	await message.answer(message.text)


if __name__ == '__main__':
	executor.start_polling(dp)
