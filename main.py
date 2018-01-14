#!/usr/bin/python
# -*- coding:utf8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import pytesseract
import win32gui
from PIL import ImageGrab
import re

cur_dir = os.path.dirname(os.path.realpath(__file__))

driver = webdriver.Chrome('tools/chromedriver.exe')

driver.get('http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E4%B8%AD%E5%9B%BD%E4%BA%BA%E5%8F%A3%E6%98%AF%E5%A4%9A%E5%B0%91%E4%BA%BF&rsv_pq=efa2e9cb0001913a&rsv_t=74b56E0sE2sNX4qR%2FATUtIGSPipBCLAwSusK%2FcpVBqJdqOONvmmpIjtJoWI&rqlang=cn&rsv_enter=0&rsv_sug3=8&inputT=357&rsv_sug4=357')

time.sleep(1)

tessdata_dir_config = '--tessdata-dir "'+cur_dir+'\\tessdata"'
pytesseract.pytesseract.tesseract_cmd = 'D:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# 获取句柄
hwhd = win32gui.FindWindow(0,u'夜神模拟器')

while True:
	# raw_input_A = input("raw_input: ")
	# 获取模拟器位置
	l,t,r,b = win32gui.GetWindowRect(hwhd)

	img = ImageGrab.grab((l,t+30,r,2*b/3))
	w = img.size[0]
	h = img.size[1]
	text=pytesseract.image_to_string(img,lang='chi_sim',config=tessdata_dir_config)
	ls = text.split('\n')
	question = ''
	for s in ls:
		question +=s
	question = question.replace(' ', '')
	if re.match('\d+\.+.*\?+', question):
		driver.find_element(by=By.ID, value='kw').clear()
		driver.find_element(by=By.ID, value='kw').send_keys(question.split('.')[-1])
		driver.find_element_by_id("su").click()
		time.sleep(10)
		continue

	


