# Copyright (C) 2025 Ваше Имя или Название Проекта
#
# Этот файл является частью проекта Hellomynameis.
#
# Этот проект распространяется под лицензией GNU General Public License v3.0.
# Подробности можно найти в файле LICENSE или по ссылке: https://www.gnu.org/licenses/gpl-3.0.html

from dash import dcc, html, callback, Input, Output, Dash
from PIL import Image
import io
import base64
import qrcode
import vobject


app = Dash()

app.layout = html.Div([
    html.Div([
        html.H1('Hello, my name is...'),
        dcc.Input(id='lname', placeholder='Фамилия'), html.Br(),
        dcc.Input(id='fname', placeholder='Имя*'), html.Br(),
        dcc.Input(id='phone', placeholder='Телефон'), html.Br(),
        dcc.Input(id='email', placeholder='e-mail*'), html.Br(),
        dcc.Input(id='org', placeholder='Название организации'), html.Br(),
        dcc.Input(id='pos', placeholder='Должность'), html.Br(),
        dcc.Input(id='address', placeholder='Адрес компании'), html.Br(),
        dcc.Input(id='site', placeholder='Адрес сайта'), html.Br(),
        dcc.Input(id='note', placeholder='Заметка'), html.Br(),

        html.Br(),
        html.Img(id='image', src='', style={'width': '300px', 'height': '300px', 'border': '1px solid black'}),
    ], className="content"),
])


@callback(
    Output('image', 'src'),
    Input('fname', 'value'),
    Input('lname', 'value'),
    Input('phone', 'value'),
    Input('email', 'value'),
    Input('org', 'value'),
    Input('pos', 'value'),
    Input('address', 'value'),
    Input('site', 'value'),
    Input('note', 'value'),
    )
def make_magic(fname, lname, phone, email, org, pos, address, site, note):
    """
Фукнкия, которая принимает на входе данные из полей и генерирует QR с карточкой, если обязательные поля заполненны.
Если не заполненны - возвращает белый прямоугольник.
    :param fname: Имя
    :param lname: Фамилия
    :param phone: Телефон
    :param email: email
    :param org: Организация
    :param pos: Должность
    :param address: Адрес
    :param site: Сайт
    :param note: Заметка
    :return: Изображение
    """
    if not fname or not email:
        img = Image.new('RGB', (300, 300), color='white')
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return f"data:image/png;base64,{img_str}"

    if fname is None:
        fname = ''
    if lname is None:
        lname = ''

    vcard = vobject.vCard()
    vcard.add('n')
    vcard.n.value = vobject.vcard.Name(family=lname, given=fname)
    vcard.add('fn')
    vcard.fn.value = f"{fname} {lname}"
    if phone:
        vcard.add('tel')
        vcard.tel.value = phone
    if email:
        vcard.add('email')
        vcard.email.value = email
    if org:
        vcard.add('org')
        vcard.org.value = [org]
    if pos:
        vcard.add('title')
        vcard.title.value = pos
    if address:
        vcard.add('adr')
        vcard.adr.value = vobject.vcard.Address(
            street=address,
        )
    if site:
        vcard.add('url')
        vcard.url.value = site
    if note:
        vcard.add('note')
        vcard.note.value = note
    vcard_data = vcard.serialize()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffered = io.BytesIO()
    img.save(buffered)
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"

    
if __name__ == '__main__':
    app.run_server(debug=True, port="8050", host="127.0.0.1", use_reloader=True)
