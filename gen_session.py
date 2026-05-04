"""
سكربت توليد SESSION_STRING لحساب مستخدم (userbot) باستخدام Kurigram.
شغّله مرة واحدة فقط ثم احفظ الناتج في .env كمتغير SESSION_STRING.
"""
from pyrogram import Client

API_ID = int(input("API_ID: ").strip())
API_HASH = input("API_HASH: ").strip()

with Client("session_gen", api_id=API_ID, api_hash=API_HASH, in_memory=True) as app:
    s = app.export_session_string()
    print("\n=== SESSION_STRING ===")
    print(s)
    print("======================\n")
    print("احفظه في ملف .env كقيمة لـ SESSION_STRING")
