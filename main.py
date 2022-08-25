import requests
import bs4
import re
import json
import urllib
from bs4 import BeautifulSoup
import pytz
import os
import telebot
from datetime import timedelta
from datetime import datetime, tzinfo
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
dtObject_local = datetime.now()
dtObject_usc = dtObject_local.astimezone(pytz.timezone('Asia/Tashkent'))
api_token = os.getenv("api_token")
bot = telebot.TeleBot(api_token)
def solve(arr):
	date_format = "%H:%M:%S"
	now = datetime.now()
	m = []
	M = 100000
	for i in arr:
	    t = datetime(year=2022,month=datetime.now().month,day=datetime.now().day,hour=int(i[0].split(":")[0]),minute=int(i[0].split(":")[1]))
	    z = abs((t-now).total_seconds()/60)
	    if z<M:
	        m = i
	        M = z
	time_end = str(f'{m[0]}:00')
	return m[1]
full_name = lambda u: f'{u.first_name} {u.last_name}' if u.last_name else u.first_name
def api(location):
	try:
		arr = []
		time = []
		o = location.lower()
		url = f"https://namozvaqti.uz/uz/shahar/{o}"
		r = requests.get(url)
		soup = BeautifulSoup(r.content, 'html5lib')

		active = soup.find_all('div',class_='ad__item bor')
		for i in active:
			arr.append([i.find('p',class_="time").text,i.find('h2',class_="nam").text])
		l = solve(arr)

		y = soup.find('h5',class_='vil')
		p = y.find_all('strong')
		year = p[0].text + " " + p[1].text

		full = soup.find_all('div',class_='ad__item bor')

		for i in full:
			time.append(str(i.find('p',class_='time').text.strip()))
		
		vaqt = soup.find_all('span',id='current_time')[0].text.strip()
		text = f"""<b>{l} vaqti</b>\n==============================\n{year}\n==============================\n🕌 <b>{o.upper()}</b> shahridagi namoz vaqtlari:\n--------------------------------------------\n🕰 Bomdod: {time[0]}\n🕰 Quyosh: {time[1]}\n🕰 Peshin: {time[2]}\n🕰 Asr so'ng (Iftor): {time[3]}\n🕰 Shom: {time[4]}\n🕰 Xufton: {time[5]}\n--------------------------------------------\n📅 Hozirgi vaqt: {vaqt}"""
		return (text)
	except Exception as e:
		print(e)
def settings():
	markup = InlineKeyboardMarkup()
	markup.row_width = 2
	markup.add(InlineKeyboardButton("⬅️ Ortga qaytish",callback_data='ortga'),InlineKeyboardButton("🗑 O'chirish",callback_data='delete'))
	return markup
def tumanlar(a):
	nom,link = [],[]
	markup = InlineKeyboardMarkup()
	markup.row_width = 2
	viloyatlar = [
		'🕌 Toshkent viloyati',
		'🕌 Buxoro viloyati',
		'🕌 Farg\'ona viloyati',
		'🕌 Sirdaryo viloyati',
		'🕌 Jizzax viloyati',
		'🕌 Navoiy viloyati',
		'🕌 Namangan viloyati',
		'🕌 Qoraqalpog\'iston',
		'🕌 Samarqand viloyati',
		'🕌 Surxondaryo viloyati',
		'🕌 Qashqadaryo viloyati',
		'🕌 Andijon viloyati',
		'🕌 Xorazm viloyati'
	]
	toshkent={
		'Toshkent':'toshkent',
		'Angren':'angren',
		'Piskent':'piskent',
		'Bekobod':'bekobot',
		'Parkent':'parkent',
		'Ga\'zalkent':'gazalkent',
		'Olmaliq':'olmaliq',
		'Bo\'ka':'boka',
		'Yangiyo\'l':'yangiyol',
		'Nurafshon':'nurafshon'
	}

	buxoro = {
		'Buxoro':'buxoro',
		'Gazli':'gazli',
		'G\'ijduvon':'gijduvon',
		'Qorako\'l':'qorakol',
		'Jondor':'jondor'
	}

	fargona = {
		'Farg\'ona':'fargona',
		'Marg\'ilon':'margilon',
		'Qo\'qon':'qoqon',
		'Quva':'quva',
		'Rishton':'rishton',
		'Bog\'dod':'bogdod',
		'Oltiariq':'oltiariq'
	}
	sirdaryo = {
		'Guliston':'Guliston',
		'Boyovut':'Boyovut',
		'Sardoba':'Sardoba',
		'Paxtaobod':'Paxtaobod',
		'Sirdaryo':'Sirdaryo'
	}

	jizzax = {
		'Jizzax':'Jizzax',
		'G\'allaorol':'gallaorol',
		'Zomin':'Zomin',
		'Do\'stlik':'dostlik',
		'Forish':'Forish'
	}
	navoiy = {
		'Navoiy':'Navoiy',
		'Nurota':'Nurota',
		'Zarafshon':'Zarafshon',
		'Uchquduq':'Uchquduq',
		'Konimex':'Konimex'
	}
	namangan = {
		'Namangan':'Namangan',
		'Pop':'Pop',
		'Chortoq':'Chortoq',
		'Uchqo\'rg\'on':'Uchqorgon',
		'Chust':'Chust'
	}
	qoraqalpogistonrespublikasi = {
		'Nukus':'nukus',
		'Mo\'ynoq':'moynoq',
		'Taxtako\'pir':'taxtakopir',
		'To\'rtko\'l':'tortkol',
		'Qo\'ng\'irot':'qongirot'
	}
	samarqand = {
		'Samarqand':'Samarqand',
		'Kattaqo\'rg\'on':'Kattaqorgon',
		'Ishtixon':'Ishtixon',
		'Urgut':'Urgut',
		'Mirbozor':'Mirbozor'
	}
	surxondaryo = {
		'Termiz':'Termiz',
		'Sherobod':'Sherobod',
		'Boysun':'Boysun',
		'Sho\'rchi':'Shorchi',
		'Denov':'Denov'
	}
	qashqadaryo = {
		'Qarshi':'Qarshi',
		'Shahrisabz':'Shahrisabz',
		'Dehqonobod':'Dehqonobod',
		'G\'uzor':'Guzor',
		'Muborak':'Muborak'
	}
	andijon = {
		'Andijon':'Andijon',
		'Xo\'jaobod':'Xojaobod',
		'Poytug\'':'Poytug',
		'Xonobod':'Xonobod',
		'Asaka':'Asaka',
		'Shahrixon':'Shahrixon',
		'Marhamat':'Marhamat'
	}
	xorazm = {
		'Urganch':'urganch',
		'Yangibozor':'Yangibozor',
		'Hazorasp':'hazorasp',
		'Shovot':'shovot',
		'Xonqa':'xonqa',
		'Xiva':'xiva'
	}
	if(a == "toshkent"):
		tuman = toshkent
	if a == "buxoro":
		tuman = buxoro
	if a == "fargona":
		tuman = fargona
	if a == "sirdaryo":
		tuman = sirdaryo
	if a == "jizzax":
		tuman = jizzax
	if a == "navoiy":
		tuman = navoiy
	if a == "namangan":
		tuman = namangan
	if a == "qoraqalpogistonrespublikasi":
		tuman = qoraqalpogistonrespublikasi
	if a == "samarqand":
		tuman = samarqand
	if a == "surxondaryo":
		tuman = surxondaryo
	if a == "qashqadaryo":
		tuman = qashqadaryo
	if a == "andijon":
		tuman = andijon
	if a == "xorazm":
		tuman = xorazm
	for i in tuman:
		nom.append(i)
		link.append(tuman[i])
	for i in range(1,len(nom),2):
		markup.add(InlineKeyboardButton(f"🕌 {nom[i-1]}", callback_data=link[i-1]+"1"),InlineKeyboardButton(f"🕌 {nom[i]}", callback_data=link[i]+"1"))
	markup.add(InlineKeyboardButton("⬅️ Ortga qaytish",callback_data='ortga'))
	return markup
def viloyatlar():
	markup = InlineKeyboardMarkup()
	markup.row_width = 2
	link = [
		'toshkent2',
		'buxoro2',
		'fargona2',
		'sirdaryo2',
		'jizzax2',
		'navoiy2',
		'namangan2',
		'qoraqalpogistonrespublikasi2',
		'samarqand2',
		'surxondaryo2',
		'qashqadaryo2',
		'andijon2',
		'xorazm2'
	]
	viloyatlar = [
		'🕌 Toshkent viloyati',
		'🕌 Buxoro viloyati',
		'🕌 Farg\'ona viloyati',
		'🕌 Sirdaryo viloyati',
		'🕌 Jizzax viloyati',
		'🕌 Navoiy viloyati',
		'🕌 Namangan viloyati',
		'🕌 Qoraqalpog\'iston',
		'🕌 Samarqand viloyati',
		'🕌 Surxondaryo viloyati',
		'🕌 Qashqadaryo viloyati',
		'🕌 Andijon viloyati',
		'🕌 Xorazm viloyati'
	]
	for i in range(1,len(viloyatlar),2):
		markup.add(InlineKeyboardButton(f"{viloyatlar[i-1]}", callback_data=link[i-1]),InlineKeyboardButton(f"{viloyatlar[i]}", callback_data=link[i]))
	return markup

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	start = f"""Assalomu Alaykum <a href='tg://user?id={message.from_user.id}'>{full_name(message.from_user)}</a> !.\nUshbu bot orqali o'z shahringizdagi namoz vaqtlarini bilib olishingiz mumkin!\n\nO'zingizga kerakli viloyatni tanlang:"""
	bot.send_message(message.chat.id,start,reply_markup=viloyatlar(),parse_mode='html',disable_web_page_preview=True)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
	link = [
		'toshkent2',
		'buxoro2',
		'fargona2',
		'sirdaryo2',
		'jizzax2',
		'navoiy2',
		'namangan2',
		'qoraqalpogistonrespublikasi2',
		'samarqand2',
		'surxondaryo2',
		'qashqadaryo2',
		'andijon2',
		'xorazm2'
	]
	if call.data == "ortga":
		text = f"""Assalomu Alaykum <a href='tg://user?id={call.message.from_user.id}'>{full_name(call.message.from_user)}</a>ga xush kelibsiz !.\nUshbu bot orqali o'z shahringizdagi namoz vaqtlarini bilib olishingiz mumkin!\n\nO'zingizga kerakli viloyatni tanlang:"""
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=text,reply_markup=viloyatlar(),parse_mode='html')
	elif call.data in link:
		text = """Kerakli shaharni tanlang:"""
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=text,reply_markup=tumanlar(call.data.replace('2','')))
	elif call.data == "delete":
		bot.delete_message(call.message.chat.id,call.message.message_id)
	else:
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=api(call.data.replace('1','')),reply_markup=settings(),parse_mode='html')	
bot.infinity_polling()
