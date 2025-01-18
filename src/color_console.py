from typing import Callable
from math import floor, ceil

ColorFun = Callable[[str], str]
RGB = tuple[int, int, int]

def make_color(code: int):
    def ret(text = "", *, escape = True) -> str:
        return f"\033[{code}m{text}\033[0m" if escape else f"\033[{code}m{text}"
    return ret

reset = make_color(0)
bold = make_color(1)
italic = make_color(3)
underline = make_color(4)
hide = make_color(8)
black = make_color(30)
red = make_color(31)
green = make_color(32)
yellow = make_color(33)
blue = make_color(34)
magenta = make_color(35)
cyan = make_color(36)
white = make_color(37)
gray = make_color(90)
default = make_color(39)
bg_black = make_color(30+10)
bg_red = make_color(31+10)
bg_green = make_color(32+10)
bg_yellow = make_color(33+10)
bg_blue = make_color(34+10)
bg_magenta = make_color(35+10)
bg_cyan = make_color(36+10)
bg_white = make_color(37+10)
bg_gray = make_color(90+10)
b_red = make_color(91)
b_green = make_color(92)
b_yellow = make_color(93)
b_blue = make_color(94)
b_magenta = make_color(95)
b_cyan = make_color(96)
b_white = make_color(97)
bg_b_red = make_color(91+10)
bg_b_green = make_color(92+10)
bg_b_yellow = make_color(93+10)
bg_b_blue = make_color(94+10)
bg_b_magenta = make_color(95+10)
bg_b_cyan = make_color(96+10)
bg_b_white = make_color(97+10)
bg_default = make_color(39+10)

def color(*args: any | ColorFun, escape = True, sep = " ") -> str:
    ret = ""
    for arg in args:
        if isinstance(arg, Callable):
            ret += arg(escape = False)
        else:
            ret += str(arg) + sep
    if ret.endswith(sep):
        ret = ret.removesuffix(sep)
    if escape:
        ret += reset()
    return ret

def highlight(text: str, what: str, count = -1, *, colors: list[ColorFun], colors2: list[ColorFun] = []) -> str:
    hl2 = "".join([c(escape = False) for c in colors2])
    replacement = reset() + "".join([c(escape = False) for c in colors]) \
        + what + reset() + hl2
    return hl2 + text.replace(what, replacement, count) + reset()

def highlight_range(text: str, start: int, stop: int, *, colors: list[ColorFun], colors2: list[ColorFun] = []) -> str:
    """
    Returns `text` if `start >= stop`. Throws an `AssertionError` if indexes are out of bounds
    """
    if start >= stop:
        return text
    assert start >= 0 and start < len(text), f"Out of bounds start={start}"
    assert stop >= 0 and stop < len(text), f"Out of bounds stop={stop}"
    hl2 = "".join([c(escape = False) for c in colors2])
    return hl2 + text[:start] + reset() \
        + "".join([c(escape = False) for c in colors]) \
        + text[start:stop] \
        + reset() + hl2 + text[stop:] + reset()

def highlight_between(text: str, start: str, stop: str, *, colors: list[ColorFun], colors2: list[ColorFun] = []) -> str:
    i = 0
    hl = default() + "".join([c(escape = False) for c in colors])
    hl2 = default() + "".join([c(escape = False) for c in colors2])
    ret = hl2
    while True:
        old_i = i
        i = text.find(start, i)
        j = text.find(stop, i + 1)
        if -1 in [i, j]:
            i = old_i
            break
        ret += text[old_i:i] + hl + text[i:j+1] + hl2
        i = j + 1
    return ret + text[i:] + default()

def uncolor(text: str) -> str:
    ret = ""
    last = 0
    while last < len(text):
        start = text.find("\033", last)
        ret += text[last:start]
        last = text.find("m", start) + 1
    return ret

def progress_bar(value: float, width: int, *, colors: list[ColorFun] = [green], colors2: list[ColorFun] = [white], char = "#", char2 = ".", percentage = True, on_complete: str | None = None) -> str:
    assert char != "" and char2 != "", "Chars can't be empty strings"
    clr = "".join([c(escape = False) for c in colors])
    clr2 = "".join([c(escape = False) for c in colors2])
    tail: str
    if on_complete is not None and value >= 1:
        tail = " " + on_complete
    elif percentage:
        tail = f"({int(value * 100)}%)"
        tail = f" {tail:<6}"
    progress_width = floor(value * width)
    progress = (char * width)[:progress_width]
    background = (char2 * width)[progress_width:width]
    return f"\033[A{clr}{progress}\033[0m{clr2}{background}\033[0m{tail}"

colors = [
    ((0, 0, 0), black, bg_black),
    ((128, 0, 0), red, bg_red),
    ((170, 85, 0), yellow, bg_yellow),
    ((0, 0, 170), blue, bg_blue),
    ((170, 0, 170), magenta, bg_magenta),
    ((0, 170, 170), cyan, bg_cyan),
    ((170, 170, 170), white, bg_white),
    ((255, 85, 85), b_red, bg_b_red),
    ((85, 255, 85), b_green, bg_b_green),
    ((255, 255, 85), b_yellow, bg_b_yellow),
    ((85, 85, 255), b_blue, bg_b_blue),
    ((255, 85, 255), b_magenta, bg_b_magenta),
    ((85, 255, 255), b_cyan, bg_b_cyan),
    ((255, 255, 255), b_white, bg_b_white),
    ((100, 100, 100), gray, bg_gray),
]

def closest_rgb_i(r: int, g: int, b: int) -> int:
    minimum = 256*3
    minimum_i = -1
    for i, clr in enumerate(colors):
        r2, g2, b2 = clr[0]
        diff = abs(r2 - r) + abs(g2 - g) + abs(b2 - b)
        if diff < minimum:
            minimum = diff
            minimum_i = i
    return minimum_i

force_4_bit = False

def set_force_4_bit(value: bool) -> None:
    """
    If `force_4_bit` is `True`, then functions `rgb` and `bg_rgb` will return the closest predefined color functions

    Ex. `rgb(0, 0, 0)` will return the `black` function
    """
    global force_4_bit
    force_4_bit = value

def rgb(r: int, g: int, b: int):
    """
    Returns a custom 24-bit color function
    """
    assert r in range(256), f"r = {r}, it needs to be in range 0..255"
    assert g in range(256), f"g = {g}, it needs to be in range 0..255"
    assert b in range(256), f"b = {b}, it needs to be in range 0..255"
    global force_4_bit
    if force_4_bit:
        i = closest_rgb_i(r, g, b)
        return colors[i][1]
    def ret(txt: str, escape = True) -> str:
        return f"\033[38;2;{r};{g};{b}m{txt}\033[0m" if escape else f"\033[38;2;{r};{g};{b}m{txt}"
    return ret

def bg_rgb(r: int, g: int, b: int):
    """
    Returns a custom 24-bit color function for backgrounds
    """
    assert r in range(256), f"r = {r}, it needs to be in range 0..255"
    assert g in range(256), f"g = {g}, it needs to be in range 0..255"
    assert b in range(256), f"b = {b}, it needs to be in range 0..255"
    global force_4_bit
    if force_4_bit:
        i = closest_rgb_i(r, g, b)
        return colors[i][2]
    def ret(txt: str, escape = True) -> str:
        return f"\033[48;2;{r};{g};{b}m{txt}\033[0m" if escape else f"\033[48;2;{r};{g};{b}m{txt}"
    return ret

def gradient_rgb(start: RGB, stop: RGB):
    def ret(text: str) -> str:
        ret = ""
        clr = start
        for i, char in enumerate(text):
            clr = (
                clr[0] + (1 / len(text)) * (stop[0] - start[0]),
                clr[1] + (1 / len(text)) * (stop[1] - start[1]),
                clr[2] + (1 / len(text)) * (stop[2] - start[2]),
            )
            print(clr)
            ret += rgb(int(clr[0]), int(clr[1]), int(clr[2]))(char, escape=False)
        return ret + reset()
    return ret
