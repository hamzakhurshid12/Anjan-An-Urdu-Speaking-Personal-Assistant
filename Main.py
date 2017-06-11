# Anjan-An-Urdu-Speaking-Personal-Assistant
#This is a python based personal Assistant which can listen to your commands in Urdu language, it can perform some various functions such as minimizing, browsing through files, playing songs for you,answering your questions, telling you time, introducing itself to you, and Checking weather for your location. Everything is processed in Urdu. Love Urdu,  Love Pakistan!

import speech_recognition as sr
from mtranslate import translate as tr
import time, pyautogui,os, pygame, datetime, gtts, random
import urllib.request , urllib, json, codecs #For Weather

def song():
    directory_path='D:\Downloads Backup\Music-OLD'
    directory_list=os.listdir(directory_path)
    song_no=random.randint(0,(len(directory_list)-1))
    os.startfile(directory_path+'\\'+directory_list[song_no])
def temp_f2c(f):
    return (f-32)*(5/9)
def weather():
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    woeid=2210800
    yql_query = "select item from weather.forecast where woeid="+woeid
    yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
    result = urllib.request.urlopen(yql_url).read().decode('utf8')
    data = json.loads(result)
    return (data['query']['results']['channel']['item']['forecast'][0]['low'])
def speak(data):
    try:
        tts_key='AIzaSyAIwcKb9GpuoAN3Nvj6OGkKJOqnxrLCLbI'
        tts = gtts.gTTS(text=tr(data,l), lang=l)
        pygame.mixer.music.load('can_speak.mp3')
        while pygame.mixer.music.get_busy():
            pass
        tts.save("temp.mp3")
        just_speak("temp.mp3")
        while pygame.mixer.music.get_busy():
            pass
    except:
        print("کنکشن میں پرابلم ہے.براہ مہربانی اسے درست کریں")
def speak_h(data):
    try:
        tts = gtts.gTTS(text=data, lang=l)
        while pygame.mixer.music.get_busy():
            pass
        tts_key='AIzaSyAIwcKb9GpuoAN3Nvj6OGkKJOqnxrLCLbI'
        tts.save("temp.mp3")
        just_speak("temp.mp3")
        while pygame.mixer.music.get_busy():
            pass
    except:
        print("کنکشن میں پرابلم ہے.براہ مہربانی اسے درست کریں")
def just_speak(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
def recordAudio():
    time.sleep(1)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    data = ""
    try:
        API_key='AIzaSyAIwcKb9GpuoAN3Nvj6OGkKJOqnxrLCLbI'
        data = r.recognize_google(audio, language=la)
    except sr.UnknownValueError:
##        speak("مجھے کچھ سمجھ نہیں آ رہا آپ کیا بول رہے ہیں")
        pass
    except sr.RequestError:
        print("'API-KEY' بند ہو گی ہے")
    except:
        print('نامعلوم پرابلم پیش آ گی ہے .ہم معذرت چاھتے ہیں ')
    return data

def anjan(data):
    if "منيماج" in data:
        pyautogui.hotkey('win','down')
    elif "مےكسماج" in data:
        pyautogui.hotkey('win','up')
    elif "سٹارٹ" in data or 'مینیو' in data:
        pyautogui.press('win')
    elif 'گانا' in data:
        song()
    elif "ایںٹر" in data or 'چلاؤ' in data or 'کھولو' in data:
        pyautogui.press('enter')
    elif "نیچے" in data:
        pyautogui.press('down')
    elif 'صبر' in data:
        time.sleep(90)
    elif "اوپر" in data:
        pyautogui.press('up')
    elif 'بند' in data:
        pyautogui.hotkey('alt','f4')
    elif 'واپس' in data:
        pyautogui.press('esc')
        pyautogui.press('backspace')
    elif 'دائیں' in data:
        pyautogui.press('right')
    elif 'بائے' in data or 'بائی' in data or 'بائیں'in data or 'باے' in data:
        pyautogui.press('left')
    elif "وقت" in data or 'ٹائم' in data:
        speak('waqt ہوا ہے ')
        speak(datetime.datetime.now().strftime('%H:%M'))
    elif "اوپر" in data and '10' in data or 'ڈیسک ٹاپ' in data:
        pyautogui.hotkey('win','d')
    elif "اللہ" in data and 'حافظ' in data:
        print("Exiting...")
        return 'exit'
    elif "کس طرح" in data or 'کیسے' in data or 'کیسی' in data:
        speak("میں ٹھیک ہوں آپ کیسے ہو")
    elif "نام" in data and "میرا" in data or 'میں کون' in data:
        speak("آپ کا نام ہمزہ خورشید ہے")
    elif "نام" in data or 'تم کون' in data:
        speak("میرا نام اردو روبوٹ ہے. مجھے یکم فروری٢٠١٧ کو شام کو ٤ بجی بنایا گیا. مجھے ہمزہ خورشید نے program کیا. میں ابھی تک سیکھ راہی ہوں.")
    elif 'رکو' in data or 'رک جاؤ' in data:
        print('5-Minute sleep')
        time.sleep(3000)
    else:
        speak("مجھے کچھ سمجھ نہیں آ رہا آپ کیا بول رہے ہیں")
pygame.mixer.init()
l='hi'
la='hi-IN'
speak_h('aaj ka darja hararat hai 38 degree celsius')
speak("asalam elaykum‎‎")
speak('ہمزہ میں امید کرتی ہوں aap ٹھیک ہوں گے')
speak('آج tareekh ہے')
speak(datetime.datetime.now().strftime('%m/%d/%Y'))
speak('waqt ہوا ہے ')
speak(datetime.datetime.now().strftime('%H:%M'))
speak("سافٹ ویئر شروع ہو چکا ہے")
while 1:
    time.sleep(2.5)
    just_speak('can_speak.mp3')
    data = recordAudio()
    if data=="":
        speak('مجھے کچھ سنائی نہیں دیا')
        continue
    data=tr(data,'ur')
    print('You said: ',data)
    exit_check=anjan(data)
    if exit_check:
        speak('Shukriya')
        break
print("اللہ حافظ")
