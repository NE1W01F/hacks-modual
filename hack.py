import logging
from .. import loader, utils
from random import randint
import time, secrets, hashlib
from datetime import datetime
from telethon import types

logger = logging.getLogger(__name__)

def register(cb):
    cb(hacksMod())

@loader.tds
class hacksMod(loader.Module):
    """Fack FBI Hacking Script and Other Cool Scripts"""
    strings = {"name": "Hacks"}

    love_jokes = [
        "Baby are you a motherboard?, Cause I'd RAM you all night long.",
        "You make me want to calibrate my joystick without the latest drivers",
        "You want to learn about computers huh, you've already passed the first lesson. Turning Me On",
        "You defragment my life",
        "Girl, are you Wi-Fi? Cuz im feeling the connection!",
        "Would you like to enjoy my laptop, I promise I don't have any viruses...",
        "Girl, you got software? I've got hardware. Together, we can liveware ever we want.",
        "Baby, there is no part of my body that is Micro or Soft",
        "I'm definitely in the range of your hotspot. How about you let me connect and get full access.",
        "You PnP? I wanna RAM this RAW Hard Disk up your Megahertz'd Computer. Nothing PC bout it.",
        "There is no cache, lets go straight to the hard drive.",
        "If I were an assembly language, I'd jump to your address, shift right a bit, push it in, pop it out, load a byte into your accumulator, then jump if you're negative.",
        "You can put a Trojan on my Hard Drive anytime",
        "If I were an operating system, your process would be real-time priority.",
        "Nobody turns me on from a cold boot like you.",
        "Baby, you overclock my processor.",
        "Baby, you make my floppy disk turn into a hard drive",
        "You still use Internet Explorer, you must like it nice and slow",
        "Are you a computer whiz? it seems you know how to turn my software to hardware.",
        "Baby you're so cute you made my page 404.",
        "Hey baby, I'm a power source, and you're the kind of resistor i'd like to deliver my load to.",
        "Baby, let's configure our hard drives in master and slave position."
    ]
    
    def __init__(self):
        pass


    async def timecmd(self, message):
        """Gets the Current Time"""
        data = datetime.now()
        dt_string = data.strftime("%d/%m/%Y %H:%M:%S")
        await utils.answer(message, dt_string)


    async def hashcmd(self, message):
        """Makes a SHA256 hash when you type .hash"""
        text = utils.get_args_raw(message.message)
        if len(text) == 0:
            return
        logger.debug("Running Hash!")
        hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
        ret = "<b>Text:</b> <code>{}</code>\n".format(text)
        ret += "<b>SHA256:</b> <code>{}</code>".format(hash)
        await utils.answer(message, ret)


    async def lovecmd(self, message):
        rad = randint(0, len(self.love_jokes))
        await utils.answer(message, self.love_jokes[rad])

    async def hackscmd(self, message):
        """Hacks the FBI when you type .hacks"""
        logger.debug("Running Hacks!")
        a = 0
        while a < 100:
            await utils.answer(message, "<b>Hacking FBI</b> <code>{}%</code>".format(a))
            time.sleep(2)
            a = a + randint(0, 20)
        
        ret = "<b>FBI Hacked!!</b>\n"
        ret += "<b>IP: </b><code>{}.{}.{}.{}</code>\n".format(randint(0, 255), randint(0, 255), randint(0, 255), randint(10, 255))
        ret += "<b>Username: </b><code>root</code>\n"
        ret += "<b>Password: </b><code>{}</code>".format(secrets.token_hex(5))
        await utils.answer(message, ret)