from _pycovid.py import covid
from _pycovid import database


@_pycovid
async def dedpepol(ded):
   covid = await logging.info(ded, ded.message)
   await _pycovid.Send_Message(ded.chat.id, f"{covid}")


#Go on
