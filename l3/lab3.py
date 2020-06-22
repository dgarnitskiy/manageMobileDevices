#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docxtpl import DocxTemplate
from docx2pdf import convert

input_calls_sum = 7.52
output_calls_sum = 85.7
sms_sum = 21
net_sum = 8229.57
itog = input_calls_sum+output_calls_sum+sms_sum+net_sum
nds = itog*0.18
doc = DocxTemplate("chernovik.docx")
context = {
	'bank': 'АО "Лучший Банк" Г. Ноябрьск ',
	'INN': '7321483285',
	'KPP': '743274543',
	'Poluchatel': 'ООО "Ромашка"',
	'BIK': '142324532',
	'schet1': '45234321344325674323',
	'schet2': '85353424543545354358',
	'Number': '72',
	'Day': '05',
	'Month': 'июня',
	'Year': '15',
	'Postavshik': 'ООО "Ромашка", ИНН 7321483285, КПП 743274543, 679120, Ноябрьск г, Магистральная ул., дом №97, корпус 2',
	'Pokupatel': 'ООО ЛАГУНА, ИНН 7321483284, КПП 743274542, 679110, Ноябрьск г, Магистральная ул., дом №9, строение 1',
	'Osnovanie': '№1500004 от 13.05.2015',
	'table_number1': '1',
	'table_number2': '2',
	'table_number3': '3',
	'table_number4': '4',
	'table_name1': 'Входящие звонки',
	'table_name2': 'Исходящие звонки',
	'table_name3': 'СМС',
	'table_name4': 'Интернет',
	'table_count1': '1',
	'table_count2': '1',
	'table_count3': '1',
	'table_count4': '1',
	'table_unit1': '7.52 мин',
	'table_unit2': '85.7 мин',
	'table_unit3': '18 смс',
	'table_unit4': '8479,57 Кб',
	'table_price1': '1 руб/мин',
	'table_price2': '1 руб/мин',
	'table_price3': '1 руб/шт вторые 5 шт, 2 руб/шт после 10 шт',
	'table_price4': '0,5 руб/Кб до 500 Кб, далее 1 руб/Кб',
	'table_sum1': str(input_calls_sum)+' руб.',
	'table_sum2': str(output_calls_sum)+' руб.',
	'table_sum3': str(sms_sum)+' руб.',
	'table_sum4': str(net_sum)+' руб.',
	'Itog': str(round(itog,2))+' руб.',
	'NDS': str(round(nds,2))+' руб.',
	'oplata': str(round(itog,2))+' руб.',
	'naimenovanii': '4',
	'Sum': str(round(itog,2))+' руб.',
	'propisat': 'Восемь тысяч триста сорок три рубля семьдесят девять копеек',
	'Director': 'Иванов И.И.',
	'Accounter': 'Иванов И.И.',
}
doc.render(context)
doc.save("final.docx")
convert('final.docx','final.pdf')