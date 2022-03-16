from _pycovid import covid

import os


@_pycovid
async def startpycovid(covid):
   await _pycovid.Send_Message(covid.cha.id, "ok")
