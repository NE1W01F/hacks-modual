import logging

from .. import loader, utils
from random import randint
import time, secrets, hashlib
from datetime import datetime
logger = logging.getLogger(__name__)


def register(cb):
    cb(hacksMod())


class hacksMod(loader.Module):
    """Fack FBI Hacking Script"""
    
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