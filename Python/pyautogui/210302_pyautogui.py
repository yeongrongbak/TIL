import pyautogui
 
# 1. 저장된 이미지가 있는 경우에 아래의 이미지를 가져와서 자동으로 클릭함
# num7 = pyautogui.locateCenterOnScreen('7.png')
# pyautogui.click(num7)

# 2. 저장된 이미지가 없는 경우에는 좌표를 알아낸 뒤 이미지를 가져와야 함
# 좌표 알아내기
# print(pyautogui.position())

# 특정 포인트의 좌표를 알아낸 뒤 스크린샷으로 해당 좌표의 이미지를 저장
pyautogui.screenshot('1.png', region=(1465, 676, 30, 30))

# 저장된 이미지를 기반으로 화면을 클릭함
num1 = pyautogui.locateCenterOnScreen('1.png')
pyautogui.click(num1)