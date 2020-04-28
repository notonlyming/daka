import os
import time
from personalInfo import *

counter = 0

def printNumberPrompt(msg):
    global counter
    print(str(counter) + '.', msg)
    counter += 1

def click(x, y):
    os.system('adb shell input tap {} {}'.format(x, y))


os.system('adb devices')
#检查是否连接成功
if input('检查是否连接成功，输入y继续：') != 'y':
    exit(1)

print('=======================完美校园打卡开始============================')

printNumberPrompt('启用定位')
os.system('adb shell settings put secure location_mode 3')

printNumberPrompt('返回home')
os.system('adb shell input keyevent HOME')

printNumberPrompt('滑动到最后一页')
for i in range(2):
    os.system('adb shell input swipe 740 1550 400 1550 25')
    time.sleep(0.3)

printNumberPrompt('打开完美校园')
click(185, 265)

printNumberPrompt('等待8秒')
time.sleep(8) 

printNumberPrompt('点击学生上报图标')
click(165, 780)

printNumberPrompt('等待学生上报页面加载')
time.sleep(5)

printNumberPrompt('滑动到底部')
for i in range(2):
    os.system('adb shell input swipe 1010 2060 1010 1400 25')
    time.sleep(0.3)

printNumberPrompt('点击单选项')
click(150, 460)
click(150, 1840)

#检查是否有错
if input('检查是否有错，输入y继续：') != 'y':
    exit(1)

printNumberPrompt('点击提交信息')
click(560, 2018)

printNumberPrompt('等待弹出动画结束')
time.sleep(1)

printNumberPrompt('点击确认提交')
click(790, 1820)

printNumberPrompt('等待成功页面加载完成')
time.sleep(1)

printNumberPrompt('截屏,保存为666.png')
os.system('adb shell screencap -p /sdcard/DCIM/camera/666.png')

print('=======================省教育系统打卡开始============================')

counter = 0
printNumberPrompt('返回home')
os.system('adb shell input keyevent HOME')

printNumberPrompt('打开填报页面')
click(400, 265)

printNumberPrompt('等待3秒')
time.sleep(3)

printNumberPrompt('点击学生健康填报按钮')
click(544, 1032)

printNumberPrompt('等待2s页面加载')
time.sleep(2)

printNumberPrompt('点击我已填过个人信息')
click(548, 586)

printNumberPrompt('等待2s页面加载')
time.sleep(2)

printNumberPrompt('点击手机号输入框')
click(380, 670)

printNumberPrompt('输入手机号')
os.system('adb shell input text "{}"'.format(phoneNumber))

printNumberPrompt('点击空白处折叠弹出框')
click(877, 505)

printNumberPrompt('点击身份证号框')
click(380, 900)

printNumberPrompt('输入身份证尾号')
os.system('adb shell input text "{}"'.format(idCard))

printNumberPrompt('点击提交')
click(580, 1120)

printNumberPrompt('等待4s加载')
time.sleep(4)

printNumberPrompt('点击每日健康填报按钮')
click(544, 1032)

printNumberPrompt('等待3s加载')
time.sleep(3)

printNumberPrompt('滑到底部')
os.system('adb shell input swipe 1010 1900 1010 400 200')

printNumberPrompt('等待2s滑动动画')
time.sleep(2)

printNumberPrompt('点击提交')
click(550,1700)

printNumberPrompt('等待成功页面加载')
time.sleep(5)

printNumberPrompt('截屏, 保存为777.png')
os.system('adb shell screencap -p /sdcard/DCIM/camera/777.png')

print('=======================打开 QQ 提交作业============================')

counter = 0
printNumberPrompt('启动手机QQ')
os.system('adb shell am force-stop com.tencent.mobileqq')
os.system('adb shell am start -n com.tencent.mobileqq/.activity.SplashActivity')

printNumberPrompt('等待QQ加载')
time.sleep(3)

printNumberPrompt('关闭定位')
os.system('adb shell settings put secure location_mode 3')

printNumberPrompt('点击搜索框')
click(550, 330)

printNumberPrompt('等待搜索界面加载')
time.sleep(1)

printNumberPrompt('输入群号')
os.system('adb shell input text "{}"'.format(groupNumber))

printNumberPrompt('等待搜索界面加载')
time.sleep(0.5)

printNumberPrompt('进入群')
click(455, 480)

printNumberPrompt('等待群页面加载完毕0.5s')
time.sleep(0.5)

printNumberPrompt('进入群功能')
click(995, 162)

printNumberPrompt('等待群功能页面加载完毕1s')
time.sleep(1)

printNumberPrompt('点击群作业')
click(760, 1150)

printNumberPrompt('等待作业页面加载完毕3s')
time.sleep(5)

printNumberPrompt('点击第一个作业')
click(760, 579)