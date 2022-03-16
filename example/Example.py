from _pycovid import covid

import os


@_pycovid
async def startpycovid(covid):
   if covid.text == "start":
      await _pycovid.Send_Message(covid.chat.id, "ok")




#ok lol

#fix code

