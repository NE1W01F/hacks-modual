import logging

from .. import loader, utils
from random import randint
import time, secrets

logger = logging.getLogger(__name__)


def register(cb):
    cb(HacksMod())


class HacksMod(loader.Module):

    """Fack FBI Hacking Script"""
    def __init__(self):
        pass

    async def hackscmd(self, message):
        """Hacks the FBI when you type .hacks"""
        logger.debug("Running Hacks!")
        a = 0
        while a < 100:
            await utils.answer(message, "<b>Hacking FBI</b> <code>{}%</code>".format(a))
            time.sleep(2)
            a = a + randint(0, 20)
        
        ret = "<b>FBI Hacked!!</b>\n"
        ret += "<b>IP:</b> <code>{}.{}.{}.{}</code>\n".format(randint(0, 255), randint(0, 255), randint(0, 255), randint(10, 255))
        ret += "<b>Username:</b> <code>root</code>\n"
        ret += "<b>Password:</b> <code>{}</code>".format(secrets.token_hex(15))
        await utils.answer(message, ret)
