from collections import defaultdict

class Input:
    def __init__(self):
        self.heldKeys = defaultdict(bool)
        self.pressedKeys = defaultdict(bool)
        self.releasedKeys = defaultdict(bool)

        self.heldButtons = defaultdict(bool)
        self.pressedButtons = defaultdict(bool)
        self.releasedButtons = defaultdict(bool)

        self.mouseX = 0
        self.mouseY = 0

    def beginNewFrame(self):
        self.pressedKeys.clear()
        self.releasedKeys.clear()

        self.pressedButtons.clear()
        self.releasedButtons.clear()

        self.mouseMoved = False

    def keyDownEvent(self, event):
        self.pressedKeys[event.key.keysym.sym] = True
        self.heldKeys[event.key.keysym.sym] = True

    def keyUpEvent(self, event):
        self.releasedKeys[event.key.keysym.sym] = True
        self.heldKeys[event.key.keysym.sym] = False

    def buttonDownEvent(self, event):
        self.pressedButtons[event.button.button] = True
        self.heldButtons[event.button.button] = True

    def buttonUpEvent(self, event):
        self.releasedButtons[event.button.button] = True
        self.heldButtons[event.button.button] = False

    def mouseMoveEvent(self, event):
        self.mouseX = event.motion.x
        self.mouseY = event.motion.y
        self.mouseMoved = True

    def wasKeyPressed(self, key):
        return self.pressedKeys[key]

    def wasKeyReleased(self, key):
        return self.releasedKeys[key]

    def isKeyHeld(self, key):
        return self.heldKeys[key]

    def wasButtonPressed(self, button):
        return self.pressedButtons[button]

    def wasButtonReleased(self, button):
        return self.releasedButtons[button]

    def isButtonHeld(self, button):
        return self.heldButtons[button]
