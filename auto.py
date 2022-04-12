import pyautogui
import time

def get_status():
    # マウスの位置を取得する
    return pyautogui.position()
    # 画面のサイズを取得する
    # print(pyautogui.size())

def crick(x,y):
    # 左クリック
    pyautogui.click(x,y, clicks=1, interval=1, button="left")
    # 右クリック
    # pyautogui.rightClick(x=700, y=700)
    # ダブルクリック
    # pyautogui.doubleClick()
print('カーソルをクリックしたいところに合わせてください。')
for i in range(5):
    print(f'{4-i}秒前')
    time.sleep(1)
print('クリック開始')
x,y = get_status()
while 1:
    crick(x,y)
    a,b = get_status()
    if a != x or b != y:
        print("終了")
        break
    time.sleep(0.5)