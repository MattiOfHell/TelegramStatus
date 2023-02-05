from telethon import TelegramClient, types
import asyncio, os, subprocess

api_id = 0000000
api_hash = 'YOUR_API_HASH'
target = 'YOUR_TARGET' # Example: @MattiOfHell // @Telegram 
#targetmsg = 'YOUR_TARGET_MSG' # Example: @MattiOfHell // @Telegram

client = TelegramClient('session_name', api_id, api_hash)

print("Userbot avviato!")

async def main():
    await client.start()
    user = await client.get_entity(f'{target}')
    me = await client.get_me()

    async def check_user_status():
        while True:
            user_status = await client.get_entity(user)
            if isinstance(user_status.status, types.UserStatusOnline):

                
                print(f"{user_status.first_name} is now online!") # Use this to send to the console "Name is now online!"

                #os.system("start cmd") # Use this to open a Windows cmd

                #with open("temp.txt", "w") as f:              # Use these 3 lines to open a notepad and write inside:
                #    f.write("AlexDiego è online!")            # to open a notepad and write inside:
                #subprocess.Popen(["notepad.exe", "temp.txt"]) # "Name is now online!"

                #await client.send_message(f'{targetmsg}', f'{user_status.first_name} è ora online!') # Use this line to send "Name is now online!" on telegram to one person (change the "targetmsg" on line 7 to work)

                break
            await asyncio.sleep(1)
    
    await check_user_status()

with client:
    client.loop.run_until_complete(main())
