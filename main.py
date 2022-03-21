import subprocess
import sys
import psutil
import threading
from semaphore import Semaphore as S

def detect_darkmode_in_windows():
    try:
        import winreg
    except ImportError:
        return False
    registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    reg_keypath = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize'
    try:
        reg_key = winreg.OpenKey(registry, reg_keypath)
    except FileNotFoundError:
        return False

    for i in range(1024):
        try:
            value_name, value, _ = winreg.EnumValue(reg_key, i)
            if value_name == 'AppsUseLightTheme':
                return value == 0
        except OSError:
            break
    raise Exception("Incompatible OS")


def toggleOSThemeColor():
    command = []
    try:
        if detect_darkmode_in_windows():
            command = ['reg.exe', 'add', 'HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize',
                '/v', 'AppsUseLightTheme', '/t', 'REG_DWORD', '/d', '1', '/f']
        else:
            command = ['reg.exe', 'add', 'HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize',
                '/v', 'AppsUseLightTheme', '/t', 'REG_DWORD', '/d', '0', '/f']
        subprocess.run(command)
    except Exception as e:
        print("Incompatible OS - Only Works with Windows")


toggleOSThemeColor()