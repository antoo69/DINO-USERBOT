from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.fakboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`hai cantik`")
    sleep(2)
    await typew.edit("`kamu kenapa?`")
    sleep(1)
    await typew.edit("`sini cerita sama oom`")
    sleep(1)
    await typew.edit("`jangan sedih lagi ya :)`")
    sleep(1)
    await typew.edit("`nanti oom jajanin ip 12`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi Aku mau nimbrung Kk..**")


@register(outgoing=True, pattern='^.tem(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Jordhy Fakboy☑️**")
    await typew.edit("**Jordhy Fakboy✅**")
    sleep(1)
    await typew.edit("**Jeje Stres☑️**")
    await typew.edit("**Jeje Stres✅**")
    sleep(2)
    await typew.edit("**Aci Bedegong☑️**")
    await typew.edit("**Aci Bedegong✅**")
    sleep(2)
    await typew.edit("**Dila Bucin☑️**")
    await typew.edit("**Dila Bucin✅**")
    sleep(2)
    await typew.edit("**Micin Buduh!☑️**")
    await typew.edit("**Micin Buduh!✅**")
    sleep(2)
    await typew.edit("**Boy MengGalau!☑️**")
    await typew.edit("**Boy MengGalau!✅**")
    sleep(2)
    await typew.edit("**Sirli PHP☑️**")
    await typew.edit("**Sirli PHP✅**")
    sleep(2)
    await typew.edit("**CUMA WALY YANG BENER!**")

# Create by myself @localheart

CMD_HELP.update({
    "rambot":
    "`.rambot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy` ; `.fakboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.tem`\
    \nUsage: misi."
})
