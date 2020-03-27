from datetime import datetime
import webbrowser
import speech_recognition as sr
import time
from gtts import gTTS
from playsound import playsound
import random
import os

r = sr.Recognizer() #sesleri tanımak için

def record(ask = False): #Mikrofondan ses alması için gerekli fonksiyon
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)  # sesi döndürür
        voice = ''
        try: #sesi algılayamadığında veya sistem çalışmadığında
            voice = r.recognize_google(audio, language='tr-TR')  # anlamlı bir metin oluşturur
        except sr.UnknownValueError:
            speak('Üzgünüm ne demek istediğini anlayamadım')
        except sr.RequestError:
            speak('Sistem yanıt vermiyor')
        return voice

def response(voice): #sistemin kullanıcıya cevap verebilmesi için gerekli fonksiyon
    if 'nasılsın' in voice:
        speak('İyiyim ya sen?')
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        search = record('Ne aramak istiyorsun?')
        url = 'https://google.com/search?g='+search #google'yi açar
        webbrowser.get().open(url) #url'i browserda açar
        speak(search + ' için bulduklarım')
    if 'bugün neler yaptın' in voice:
        print('Bütün gün insanlar ile uğraştım')
    if 'hayat nasıl gidiyor' in voice:
        print('Çok şükür bugün de ölmedik')
    if 'bay' in voice:
        speak('Görüşürüz')
        exit()

def speak(string): #asistanı konuşturmak için gerekli fonksiyon
    tts = gTTS(string, lang='tr') #google speech to text ile string'i alır
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3' #dosya ismini belirler
    tts.save(file) #dosyayı kaydeder
    playsound(file) #dosyayı seslendirir
    os.remove(file) #dosyayı kaldırır

speak('Nasıl yardımcı olabilirim?')
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)

