from telethon import TelegramClient

# Define your API ID, API hash, and phone number
api_id = '1234567'
api_hash = 'abcdefghijk123456789lmnopqrst1112'
phone = '+1234567890'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone)

    # Join a group and send a message
    await client.send_message('CryptoTradingGroup', 'Check out Pump.fun trading bot!')

with client:
    client.loop.run_until_complete(main())
