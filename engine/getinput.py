import pygame

_currentState = {}
_previousState = {}

_keyMap = {
    "left": pygame.K_a,
    "right": pygame.K_d,
    "up": pygame.K_w,
    "down": pygame.K_s,
    "jump": pygame.K_SPACE,
    "interact": pygame.K_e
}

def init():
    global _currentState, _previousState
    for action in _keyMap:
        _currentState[action] = False
        _previousState[action] = False

def update():
    global _currentState, _previousState

    _previousState = _currentState.copy()

    keysPressed = pygame.key.get_pressed()

    for action, keymap in _keyMap.items():
        _currentState[action] = keysPressed[keymap]

def keyDown(action):
    """return true if the key is currently held down"""
    return _currentState.get(action, False)

def justPressed(action):
    """return true on the frame the key was pressed"""
    return _currentState.get(action, False) and not _previousState.get(action, False)

def justReleased(action):
    """return true only on the frame the key was released"""
    return not _currentState.get(action, False) and _previousState.get(action, False)



