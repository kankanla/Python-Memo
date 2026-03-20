# pip install selenium
# pip install pywin32
# https://www.rakuten-sec.co.jp/web/fx/rate-member.html
# https://fx.minkabu.jp/pair/chart



import subprocess
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import win32com.client

# ===== 言語選択 =====
# "ja" = 日本語
# "zh" = 中国語
LANG = "ja"

# ===== 音声エンジン =====
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def set_voice(lang):
    voices = speaker.GetVoices()
    for v in voices:
        if lang == "ja" and "Japanese" in v.GetDescription():
            speaker.Voice = v
            return
        if lang == "zh" and ("Chinese" in v.GetDescription() or "Huihui" in v.GetDescription()):
            speaker.Voice = v
            return

set_voice(LANG)

def speak(text):
    speaker.Speak(text)

# ===== Chrome起動 =====
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

subprocess.Popen([
    chrome_path,
    "--remote-debugging-port=9222",
    '--user-data-dir=C:\\temp\\chrome_debug',
    "https://fx.minkabu.jp/pair/USDJPY"
])

time.sleep(5)

# ===== Selenium接続 =====
options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:9222"
driver = webdriver.Chrome(options=options)

# ===== メインループ =====
while True:
    try:
        rate = driver.find_element(By.CLASS_NAME, "pairbox__rate__item").text
        
        if LANG == "ja":
            # msg = f"{rate}"
            msg = rate
        elif LANG == "zh":
            msg = f"美元兑日元是 {rate}"
        
        print(msg)
        speak(msg)

    except Exception as e:
        print("エラー:", e)

    time.sleep(5)
    
