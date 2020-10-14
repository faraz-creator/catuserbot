# created by @eve_enryu
# edited & fix by @Jisan7509


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import bot

from ..utils import admin_cmd, edit_or_reply, sudo_cmd


@borg.on(admin_cmd(pattern="firmware(?: |$)(.*)"))
@borg.on(sudo_cmd(outgoing=True, pattern="firmware(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    firmware = f"firmware"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{firmware} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)

            
@borg.on(admin_cmd(pattern="specs(?: |$)(.*)"))
@borg.on(sudo_cmd(outgoing=True, pattern="specs(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    specs = f"specs"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{specs} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@borg.on(admin_cmd(pattern="fastboot(?: |$)(.*)"))
@borg.on(sudo_cmd(outgoing=True, pattern="fastboot(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    fboot = f"fastboot"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{fboot} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@borg.on(admin_cmd(pattern="recovery(?: |$)(.*)"))
@borg.on(sudo_cmd(outgoing=True, pattern="recovery(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    recovery = f"recovery"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{recovery} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@borg.on(admin_cmd(pattern="pb(?: |$)(.*)"))
@borg.on(sudo_cmd(outgoing=True, pattern="pb(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    pitch = f"pb"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{pitch} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@borg.on(admin_cmd(pattern="of(?: |$)(.*)"))
@borg.on(sudo_cmd(outgoing=True, pattern="of(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    ofox = f"of"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{ofox} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


CMD_HELP.update(
    {
        "xiaomi": "__**PLUGIN NAME :** Xiaomi__\
        \n\n__**For Xiaomeme devices only!**__\
\n\n📌** CMD ➥** `.firmware` (codename)\
\n**USAGE   ➥  **Get lastest Firmware\
\n\n📌** CMD ➥** `.pb` (codename)\
\n**USAGE   ➥  **Get latest PBRP\
\n\n📌** CMD ➥** `.specs` (codename)\
\n**USAGE   ➥  **Get quick spec information about device\
\n\n📌** CMD ➥** `.fastboot` (codename)\
\n**USAGE   ➥  **Get latest fastboot MIUI\
\n\n📌** CMD ➥** `.recovery` (codename)\
\n**USAGE   ➥  **Get latest recovery MIUI\
\n\n📌** CMD ➥** `.of` (codename)\
\n**USAGE   ➥  **Get latest ORangeFox Recovery"
    }
)
