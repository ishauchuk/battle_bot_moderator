from telethon import events
from telethon.tl.custom import Message
from telethon.tl.types import InputMediaDice
from app import bot


@bot.on(events.ChatAction(
    func=lambda e: e.is_group and e.user_added and e.user_id == bot.me.id))
async def on_join(event: events.ChatAction.Event):
    await event.respond("Categorically welcome, gentlemen!")


@bot.on(events.NewMessage(
    func=lambda e: e.text.lower() == "say something"))
async def who_are_you(event: Message):
    await event.respond(
        "I am a smart, handsome, moderately well-fed man in full of strength")


@bot.on(events.NewMessage(func=lambda e: e.text.lower() == '/dice'))
async def send_dice(event: Message):
    await bot.send_message(event.chat.id, file=InputMediaDice(""))


@bot.on(events.ChatAction(
    func=lambda e: (e.user_added or e.user_joined) and e.user_id != bot.me.id))
async def greet(event: events.ChatAction.Event):
    await event.respond('Shalom!')


@bot.on(events.NewMessage(func=lambda e: e.text.lower() == '/cat'))
async def cat(event: Message):
    photo = open("app/cat.png", 'rb')
    await bot.send_message(event.chat.id, file=photo)
