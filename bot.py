from googletrans import Translator
from config import API_TOKEN
from buttons import til
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery
from class1 import Sql

logging.basicConfig(level=logging.INFO)

skl = Sql()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
tr = Translator()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	global idi
	idi = message.from_user.id
	username = message.from_user.username
	firstname = message.from_user.first_name
	skl.yaratish()
	data3 = skl.id_user(idi)
	if data3 is None:
		skl.qoshish(idi,username,firstname)
		await message.reply(f"salom!, привет!, hello! \nRo'yxatan o'tingiz!:  \nIsm: {firstname} User: @{username}\nidi: {idi} \nSoz kiriting:\nОтправьте текст:\nSend text:")

	else:
		await message.reply("Ro'yxatan o'tgansiz so'z yuboring!:\nОтправьте текст:\nSend text:")
		

	


@dp.message_handler(commands=['alluser'])
async def send_welcome(message: types.Message):
	idi = message.from_user.id
	data2 = skl.aluser(idi)
	for i in data2:
		x = i[0]
	await message.reply(f'Foydalanuvchilar soni {x} ta')

	





@dp.message_handler()
async def echo(message: types.Message): 
	global t
	t = message.text
	await message.reply("Tilni tanlang", reply_markup= til)

@dp.callback_query_handler(text = 'ru')
async def fo(call: CallbackQuery):
	tar = tr.translate(t, dest = 'ru')
	await call.message.reply(tar.text)

@dp.callback_query_handler(text = 'uz')
async def fo(call: CallbackQuery):
	tar = tr.translate(t, dest = 'uz')
	await call.message.reply(tar.text)

@dp.callback_query_handler(text = 'us')
async def fo(call: CallbackQuery):
	tar = tr.translate(t, dest = 'en')
	await call.message.reply(tar.text)

@dp.callback_query_handler(text = 'ar')
async def fo(call: CallbackQuery):
	tar = tr.translate(t, dest = 'ar')
	await call.message.reply(tar.text)

@dp.callback_query_handler(text = 'tr')
async def fo(call: CallbackQuery):
	tar = tr.translate(t, dest = 'tr')
	await call.message.reply(tar.text)

@dp.callback_query_handler(text = 'in')
async def fo(call: CallbackQuery):
	tar = tr.translate(t, dest = 'hindi')
	await call.message.reply(tar.text)

@dp.callback_query_handler(text = 'kr')
async def fo(call: CallbackQuery):
	tar = tr.translate(t, dest = 'korean')
	await call.message.reply(tar.text)

@dp.callback_query_handler(text = 'kz')
async def fo(call: CallbackQuery):
	tar = tr.translate(t, dest = 'kazakh')
	await call.message.reply(tar.text)

@dp.callback_query_handler(text = 'fr')
async def fo(call: CallbackQuery):
	tar = tr.translate(t, dest = 'french')
	await call.message.reply(tar.text)

@dp.callback_query_handler(text = 'ge')
async def fo(call: CallbackQuery):
	tar = tr.translate(t, dest = 'german')
	await call.message.reply(tar.text)

@dp.callback_query_handler(text = 'ky')
async def fo(call: CallbackQuery):
	tar = tr.translate(t, dest = 'kyrgyz')
	await call.message.reply(tar.text)

@dp.callback_query_handler(text = 'pl')
async def fo(call: CallbackQuery):
	tar = tr.translate(t, dest = 'polish')
	await call.message.reply(tar.text)

@dp.callback_query_handler(text = 'tj')
async def fo(call: CallbackQuery):
	tar = tr.translate(t, dest = 'tajik')
	await call.message.reply(tar.text)

@dp.callback_query_handler(text = 'ukr')
async def fo(call: CallbackQuery):
	tar = tr.translate(t, dest = 'ukrainian')
	await call.message.reply(tar.text)

@dp.callback_query_handler(text = 'bul')
async def fo(call: CallbackQuery):
	tar = tr.translate(t, dest = 'bulgarian')
	await call.message.reply(tar.text)

@dp.callback_query_handler(text = 'fi')
async def fo(call: CallbackQuery):
	tar = tr.translate(t, dest = 'filipino')
	await call.message.reply(tar.text)

@dp.callback_query_handler(text = 'lat')
async def fo(call: CallbackQuery):
	tar = tr.translate(t, dest = 'latin')
	await call.message.reply(tar.text)

@dp.callback_query_handler(text = 'ir')
async def fo(call: CallbackQuery):
	tar = tr.translate(t, dest = 'irish')
	await call.message.reply(tar.text)






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)