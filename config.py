TOKEN = "2106640014:AAFPE196Nb4JI4afWXw7VKuKm6D_s5UbqRY"

from gtts import gTTS
import os

def text_to_speech(mytext, lang):
    myobj = gTTS(text=mytext, lang=lang, slow=False)
    myobj.save("audio.mp3")