{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\MINH TAM PHAM\\AppData\\Local\\Temp\\ipykernel_12056\\3452265746.py:10: DeprecationWarning: executable_path has been deprecated, please pass in a Service object\n",
      "  driver = webdriver.Chrome(ChromeDriverManager().install())\n"
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
    "\n",
    "driver = webdriver.Chrome(ChromeDriverManager().install())\n",
    "driver.get('http://127.0.0.1:8000/')\n",
    "search = driver.find_element(By.XPATH, '//input[@name=\"username\"]')\n",
    "search.send_keys('mimipretty')\n",
    "password = driver.find_element(By.XPATH, '//input[@name=\"password\"]')\n",
    "password.send_keys('poiu1234')\n",
    "sleep(2)\n",
    "login = driver.find_element(By.XPATH, '//input[@value=\"Login\"]')\n",
    "login.click()\n",
    "\n",
    "createpost = driver.find_element(By.ID, 'create-post')\n",
    "createpost.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
