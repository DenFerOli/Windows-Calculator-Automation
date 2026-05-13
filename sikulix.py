# coding=utf-8

"""

SikuliX Mock Interface for VS Code

This file serves as a mock interface for SikuliX in Python, allowing for code completion and error checking in VS Code without actually running SikuliX.

"""

# --- Interaction Functions (Mouse and Keyboard) ---

def click(target, modifiers=0): pass
def doubleClick(target, modifiers=0): pass
def rightClick(target, modifiers=0): pass
def hover(target): pass
def dragDrop(t1, t2): pass
def type(text, modifiers=None): pass
def paste(text): pass
def wheel(target, direction, steps): pass

# --- Flow and Wait Functions ---

def wait(target, timeout=None): pass
def waitVanish(target, timeout=None): pass
def exists(target, timeout=None): pass
def sleep(seconds): pass

# --- Dialog and Message Functions ---

def popup(message, title="SikuliX"): pass
def input(message, default="", title="SikuliX", hidden=False): pass
def inputText(message, title="SikuliX", lines=5, width=300): pass
def select(message, options, title="SikuliX"): pass
def popError(message, title="SikuliX"): pass
def popAsk(message, title="SikuliX"): pass

# --- Main Classes ---

class Screen:

    def click(self, target): pass
    def find(self, target): pass
    def capture(self, *args): pass

class Region:

    def click(self, target): pass
    def find(self, target): pass
    def highlight(self, seconds=None): pass
    def setAutoWaitTimeout(self, seconds): pass

class Pattern:

    def __init__(self, target): pass
    def similar(self, similarity): pass
    def targetOffset(self, x, y): pass

class App:

    def __init__(self, name): pass
    def open(self): pass
    def focus(self): pass
    def close(self): pass

# --- Key Constants ---

class Key:

    ENTER = "\n"
    ESC = "\x1b"
    BACKSPACE = "\b"
    TAB = "\t"
    CTRL = "CTRL"
    SHIFT = "SHIFT"
    ALT = "ALT"
    WIN = "WIN"
    CMD = "CMD"
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

# Common Global Variables

SCREEN = Screen()