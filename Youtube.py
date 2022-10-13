{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "listening\n",
      "listening\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\MINH TAM PHAM\\AppData\\Local\\Temp\\ipykernel_13640\\2349910326.py:16: DeprecationWarning: executable_path has been deprecated, please pass in a Service object\n",
      "  self.driver = webdriver.Chrome(ChromeDriverManager().install())\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.chrome.service import Service\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.support.ui import WebDriverWait \n",
    "from selenium.webdriver.support import expected_conditions as EC\n",
    "from time import sleep\n",
    "import pyttsx3 as p\n",
    "import datetime\n",
    "import speech_recognition as sr\n",
    "\n",
    "\n",
    "class music():\n",
    "    def __init__(self):\n",
    "        self.driver = webdriver.Chrome(ChromeDriverManager().install())\n",
    "\n",
    "    def play(self, query):\n",
    "        self.query = query\n",
    "        self.driver.get('https://www.youtube.com/results?search_query=' + query )\n",
    "        video = self.driver.find_element(By.CLASS_NAME, \"ytd-video-renderer\")\n",
    "        video.click()\n",
    "\n",
    "engine = p.init()\n",
    "rate=engine.getProperty('rate')\n",
    "engine.setProperty('rate', 180)\n",
    "\n",
    "def speak(text):\n",
    "    engine.say(text)\n",
    "    engine.runAndWait()\n",
    "speak(\"Hello mimi, I am your assistant. How can I help you?\")\n",
    "\n",
    "r = sr.Recognizer()\n",
    "\n",
    "with sr.Microphone() as source:\n",
    "    r.energy_threshold=10000\n",
    "    r.adjust_for_ambient_noise(source, 1.2)\n",
    "    print(\"listening\")\n",
    "    audio = r.listen(source)\n",
    "    text3 = r.recognize_google(audio)\n",
    "\n",
    "if \"music\" in text3:\n",
    "    speak(\"What do you want to listen to?\")\n",
    "    with sr.Microphone() as source:\n",
    "        r.energy_threshold=10000\n",
    "        r.adjust_for_ambient_noise(source, 1.2)\n",
    "        print(\"listening\")\n",
    "        audio = r.listen(source)\n",
    "        text3 = r.recognize_google(audio)\n",
    "        music = music()\n",
    "        music.play(text3)\n",
    "        "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.4 ('Mimi')",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "ed3af5a56fa7073acdb89b31edc62ced980dabefb525042e2d2b94296569fe03"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
