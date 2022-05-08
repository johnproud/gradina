from typing import Optional

from fastapi import FastAPI
from telegram.ext import Updater
from pydantic import BaseModel

app = FastAPI()
updater = Updater("5335002137:AAE4xLCtIeean8hVOSsR32l3DGlZjaRKaOo", arbitrary_callback_data=True)


class Data(BaseModel):
    full_name: str
    email: Optional[str] = 'nu a trimis numarul'
    phone_number: str
    message: str


def make_text(data: Data):
    return f"""
        \n*_Numele si prenumele_*:  {data.full_name}\n*_Email\-ul_*:  {data.email}\n*_Numarul de telefon_*:  {data.phone_number}\n*_Mesajul_*:  {data.message}\n
    """


@app.post("/send_email")
async def send_email(data: Data):
    updater.bot.sendMessage(chat_id='730014397', text=make_text(data), parse_mode='MarkdownV2')
    return {"message": "success"}
