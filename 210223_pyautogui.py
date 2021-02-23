import pyautogui
import time

# pyautogui.click(clicks= 2, interval=2)

# 파일 열람 후 텍스트 입력하기
pyautogui.moveTo(338, 416, 1) # 파일 위치로 이동
pyautogui.doubleClick()
time.sleep(1) # 파일이 열린 뒤 타이핑이 이뤄져야 하므로 1초의 time sleep을 줘야함
pyautogui.typewrite('Hello')
pyautogui.typewrite(['enter'])
pyautogui.typewrite('World!')