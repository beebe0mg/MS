from gtts import gTTS
from playsound import playsound

text = "안녕하세요 호호호"
speech = "tts.mp3"
tts = gTTS(text, lang="ko")
tts.save(speech)
playsound(speech)