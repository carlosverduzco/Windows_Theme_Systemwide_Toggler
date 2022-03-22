import subprocess
from semaphore import Semaphore as S
import sys

def detect_darkmode_in_windows():
    import winreg
    registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    reg_keypath = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize'
    reg_key = winreg.OpenKey(registry, reg_keypath)

    for i in range(1024):
        value_name, value, _ = winreg.EnumValue(reg_key, i)
        if value_name == 'AppsUseLightTheme':
            return value == 0

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
        sys.exit(0)