import pyautogui

class Hands:
    """
    Athena's digital hands: control mouse, keyboard, and screen automation.
    """
    def move_cursor(self, x: int, y: int, duration: float = 0.2):
        pyautogui.moveTo(x, y, duration=duration)

    def click(self, x: int = None, y: int = None, button: str = 'left'):
        pyautogui.click(x=x, y=y, button=button)

    def type_text(self, text: str, interval: float = 0.05):
        pyautogui.write(text, interval=interval)

    def press_key(self, key: str):
        pyautogui.press(key)

    def screenshot(self, path: str = 'screenshot.png'):
        pyautogui.screenshot(path)
        return path

    def scroll(self, clicks: int):
        pyautogui.scroll(clicks)
