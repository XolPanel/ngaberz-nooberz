####### VARIABLE #######
ADMIN=010101010101 # One whitelisted telegram ID
TOKEN="" # Bot token from BotFather
PATH = "/etc/noobzvpns/" # DO NOT CHANGE THIS VALUE IF YOU DONT KNOW WHAT YOURE DOING
HOST = "HostName.com" # Domain for your server
####### VARIABLE #######

try:
	open("/etc/noobzvpns/config.json")
except:
	exit("Install Noobz-VPN first dumbass !!!")
else:
	pass

from pystemd.systemd1 import Unit
from telethon import *
import subprocess, asyncio
import requests, json
bot = TelegramClient("xv-noobz-manager-xv","6","eb06d4abfb49dc3eeb1aeb98ae0f581e").start(bot_token=TOKEN)
g = "🟢"
r = "🔴"
b = "🔵"
p = "🟣"
check = "✅️"
nocheck = "❌️"

@bot.on(events.CallbackQuery(data=b"create"))
async def CreateZ(event):
	s = await event.get_sender()
	sender = await event.get_sender()
	if s.id == ADMIN:
		try:
			js = json.loads(open(PATH + "users.json").read())
			ll = []
			for x in js:
				ll.append(x)
		except:
			ll = []
		else:
			pass
		await event.edit("**Username: **")
		async with bot.conversation(event.chat_id) as user:
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = await user
			user = user.message.message
		if len(user) > 10:
			await event.respond("**Max username length is 10 characters !!!**")
		else:
			if user not in ll:
				await event.respond("**Password: **")
				async with bot.conversation(event.chat_id) as password:
					password = password.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
					password = await password
					password = password.message.message
				await event.respond("**Expiry (Days) on number: **")
				async with bot.conversation(event.chat_id) as exp:
					exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
					exp = await exp
					exp = exp.message.message
				out = subprocess.check_output(["noobzvpns","--add-user", user, password])
				print(out)
				if "success" in str(out):
					out = subprocess.check_output(["noobzvpns", "--expired-user", user, exp])
					print(out)
					if "success" in str(out):
						await event.respond(f"""===[ NOOBZ-VPN ACCOUNT ]===

**• Hostname:** `{HOST}`
**• User:** `{user}`
**• Password:** `{password}`
**• Expired On:** `{exp}` Days

ENJOY !

===[ NOOBZ-MANAGER ]===
""")

@bot.on(events.CallbackQuery(data=b"renew"))
async def renewZ(event):
	s = await event.get_sender()
	sender = await event.get_sender()
	if s.id == ADMIN:
		try:
			js = json.loads(open(PATH + "users.json").read())
			ll = []
			for x in js:
				ll.append(x)
		except:
			ll = []
		else:
			pass
		await event.edit("**Username: **")
		async with bot.conversation(event.chat_id) as user:
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = await user
			user = user.message.message
		if len(user) > 10:
			await event.respond("**Max username length is 10 characters !!!**")
		else:
			if user not in ll:
				await event.respond("**Username not found**")
			else:
				out = subprocess.check_output(["noobzvpns", "--renew-user", user])
				if "success" in str(out):
					await event.respond(f"**User** `{user}` successfully renewed")
				else:
					await event.respond("**Something went wrong**")




@bot.on(events.CallbackQuery(data=b"delete"))
async def deleteZ(event):
	s = await event.get_sender()
	sender = await event.get_sender()
	if s.id == ADMIN:
		try:
			js = json.loads(open(PATH + "users.json").read())
			ll = []
			for x in js:
				ll.append(x)
		except:
			ll = []
		else:
			pass
		await event.edit("**Username: **")
		async with bot.conversation(event.chat_id) as user:
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = await user
			user = user.message.message
		if len(user) > 10:
			await event.respond("**Max username length is 10 characters !!!**")
		else:
			if user not in ll:
				await event.respond("**Username not found**")
			else:
				out = subprocess.check_output(["noobzvpns", "--remove-user", user])
				if "success" in str(out):
					await event.respond(f"**User** `{user}` successfully removed")
				else:
					await event.respond("**Something went wrong**")


@bot.on(events.CallbackQuery(data=b"unblock"))
async def UnblockZ(event):
	s = await event.get_sender()
	sender = await event.get_sender()
	if s.id == ADMIN:
		try:
			js = json.loads(open(PATH + "users.json").read())
			ll = []
			for x in js:
				ll.append(x)
		except:
			ll = []
		else:
			pass
		await event.edit("**Username: **")
		async with bot.conversation(event.chat_id) as user:
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = await user
			user = user.message.message
		if len(user) > 10:
			await event.respond("**Max username length is 10 characters !!!**")
		else:
			if user not in ll:
				await event.respond("**Username not found**")
			else:
				out = subprocess.check_output(["noobzvpns", "--unblock-user", user])
				if "success" in str(out):
					await event.respond(f"**User** `{user}` successfully unblocked")
				else:
					await event.respond("**Something went wrong**")



@bot.on(events.CallbackQuery(data=b"block"))
async def BlockZ(event):
	s = await event.get_sender()
	sender = await event.get_sender()
	if s.id == ADMIN:
		try:
			js = json.loads(open(PATH + "users.json").read())
			ll = []
			for x in js:
				ll.append(x)
		except:
			ll = []
		else:
			pass
		await event.edit("**Username: **")
		async with bot.conversation(event.chat_id) as user:
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = await user
			user = user.message.message
		if len(user) > 10:
			await event.respond("**Max username length is 10 characters !!!**")
		else:
			if user not in ll:
				await event.respond("**Username not found**")
			else:
				out = subprocess.check_output(["noobzvpns", "--block-user", user])
				if "success" in str(out):
					await event.respond(f"**User** `{user}` successfully blocked")
				else:
					await event.respond("**Something went wrong**")


@bot.on(events.CallbackQuery)
async def actioneer(event):
	s = await event.get_sender()
	if s.id == ADMIN:
		c = event.data.decode("utf-8")
		if "-" in c:
			act = c.split("-")[0]
			x = user = c.split("-")[1]
			if act == "delete":
				out = subprocess.check_output(["noobzvpns", "--remove-user", user])
				if "success" in str(out):
					await event.edit(f"**User `{x}` successfully removed**")
			if act == "block":
				out = subprocess.check_output(["noobzvpns", "--block-user", user])
				if "success" in str(out):
					await event.edit(f"**User `{x}` successfully blocked**")
			if act == "unblock":
				out = subprocess.check_output(["noobzvpns", "--unblock-user", user])
				if "success" in str(out):
					await event.edit(f"**User `{x}` successfully unblocked**")
			if act == "renew":
				out = subprocess.check_output(["noobzvpns", "--renew-user", user])
				if "success" in str(out):
					await event.edit(f"**User `{x}` successfully renewed**")


@bot.on(events.CallbackQuery(data=b"show"))
async def shows(event):
	s = await event.get_sender()
	if s.id == ADMIN:
		js = json.loads(open(PATH + "users.json").read())
		for x in js:
			wir = await event.respond(f"""**• User:** `{x}`
**• Hash Key:** `{js[x]["hash_key"]}`
**• Created On:** `{js[x]["issued"]}`
**• Expired (Days):** `{js[x]["expired"]}`

**• Blocked:** `{"Yes " + g if js[x]["blocked"] != False else "No " + r}`

===[ Action ]===
""",buttons=[
[Button.inline(f"{r} Delete",f"delete-{x}"),
Button.inline(f"{r} Block",f"block-{x}")],
[Button.inline(f"{g} Unblock",f"unblock-{x}"),
Button.inline(f"{b} Renew",f"renew-{x}")]] )

			await asyncio.sleep(1.2)


@bot.on(events.CallbackQuery(data=b"service"))
async def seervicez(event):
	s = await event.get_sender()
	sender = await event.get_sender()
	if s.id == ADMIN:
		unit = Unit(b"noobzvpns.service")
		unit.load()
		unit.Unit.Stop("fail") if unit.Unit.SubState == b"running" else unit.Unit.Start("fail")
		unit = Unit(b"noobzvpns.service")
		unit.load()
		v = subprocess.check_output(["vnstat","--oneline"])
		today_total = str(v).split(";")[5]
		month_total = str(v).split(";")[14].replace("\\n","")
		isp = requests.get("http://ip-api.com/json/").json()["isp"]
		msg = f"""**Welcome {s.first_name} To Noobz-Manager**

**===[ INFO ]===**
**• Noobz-VPN Status: **`{"[ON]" + g if unit.Unit.SubState == b"running" else "[OFF]"+r}`
**• Server Domain: **`{HOST}`
**• Server ISP:** `{isp}`
**===[ PORTS ]===**
**• TCP STD:** {str(json.loads(open(PATH + "config.json").read())["tcp_std"])}
**• TCP SSL:** {str(json.loads(open(PATH + "config.json").read())["tcp_ssl"])}
**===[ USAGE ]===**
**• Today RX/TX Total:** `[{today_total}]`
**• This Month RX/TX Total:** `[{month_total}]`
**===[ NOOBZ-MANAGER ]===**"""
		if unit.Unit.SubState != b"running":
			butt = [
[Button.inline(f"{check} Start Noobz-VPN Service","service")],
[Button.inline(f"{g} Create User","create"),
Button.inline(f"{r} Delete User ","delete")],
[Button.inline(f"{r} Block User ","block"),
Button.inline(f"{g} Unblock User ","unblock")],
[Button.inline(f"{b} Renew User ","renew"),
Button.inline(f"{p} Show All User ","show")]]
		else:
			butt = [
[Button.inline(f"{nocheck} Stop Noobz-VPN Service","service")],
[Button.inline(f"{g} Create User","create"),
Button.inline(f"{r} Delete User ","delete")],
[Button.inline(f"{r} Block User ","block"),
Button.inline(f"{g} Unblock User ","unblock")],
[Button.inline(f"{b} Renew User ","renew"),
Button.inline(f"{p} Show All User ","show")]]

		await event.edit(msg,buttons=butt)



@bot.on(events.NewMessage(pattern="(?:.start|/start)"))
async def start(event):
#	u = event.pattern_match.group(1)
#	s = requests.get(f"http://sg-de.cobeksawit.xyz/api/user/{u}", headers=head)
#	await event.reply("```json"+s.text+"```")
	s = await event.get_sender()
	if s.id == ADMIN:
		unit = Unit(b"noobzvpns.service")
		unit.load()
		v = subprocess.check_output(["vnstat","--oneline"])
		today_total = str(v).split(";")[5]
		month_total = str(v).split(";")[14].replace("\\n","")
		isp = requests.get("http://ip-api.com/json/").json()["isp"]
		msg = f"""**Welcome {s.first_name} To Noobz-Manager**

**===[ INFO ]===**
**• Noobz-VPN Status: **`{"[ON]" + g if unit.Unit.SubState == b"running" else "[OFF]"+r}`
**• Server Domain: **`{HOST}`
**• Server ISP: **`{isp}`
**===[ PORTS ]===**
**• TCP STD:** {str(json.loads(open(PATH + "config.json").read())["tcp_std"])}
**• TCP SSL:** {str(json.loads(open(PATH + "config.json").read())["tcp_ssl"])}
**===[ USAGE ]===**
**• Today RX/TX Total:** `[{today_total}]`
**• This Month RX/TX Total:** `[{month_total}]`
**===[ NOOBZ-MANAGER ]===**
"""
		if unit.Unit.SubState != b"running":
			butt = [
[Button.inline(f"{check} Start Noobz-VPN Service","service")],
[Button.inline(f"{g} Create User","create"),
Button.inline(f"{r} Delete User ","delete")],
[Button.inline(f"{r} Block User ","block"),
Button.inline(f"{g} Unblock User ","unblock")],
[Button.inline(f"{b} Renew User ","renew"),
Button.inline(f"{p} Show All User ","show")]]
		else:
			butt = [
[Button.inline(f"{nocheck} Stop Noobz-VPN Service","service")],
[Button.inline(f"{g} Create User","create"),
Button.inline(f"{r} Delete User ","delete")],
[Button.inline(f"{r} Block User ","block"),
Button.inline(f"{g} Unblock User ","unblock")],
[Button.inline(f"{b} Renew User ","renew"),
Button.inline(f"{p} Show All User ","show")]]

		await event.respond(msg,buttons=butt)



#print(bot.get_me())
if __name__ == "__main__":
	bot.run_until_disconnected()
