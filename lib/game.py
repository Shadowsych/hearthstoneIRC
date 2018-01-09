import win32api
import win32con
import time

class Game:

    keymap = {
        'up': 0x49,
        'down': 0x4B,
        'left': 0x4A,
        'right': 0x4C,
        'click': 0x4F,
	'endturn': 0x45,
        'play': 0x4D,
	'cancel': 0x4E,
	'switchl': 0x50,
	'switchr': 0x55,
        'options': 0x42
    }

    def get_valid_buttons(self):
        return [button for button in self.keymap.keys()]

    def is_valid_button(self, button):
        return button in self.keymap.keys()

    def button_to_key(self, button):
        return self.keymap[button]

    def push_button(self, button):
        win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
        time.sleep(.15)
        win32api.keybd_event(self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)
