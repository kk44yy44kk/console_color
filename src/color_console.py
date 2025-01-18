from typing import Callable
from math import floor, ceil

ColorFun = Callable[[str], str]
RGB = tuple[int, int, int]

def reset(text = "", *, escape = True) -> str:
    return f"\033[0m{text}"

def bold(text = "", *, escape = True) -> str:
    return f"\033[1m{text}\033[0m" if escape else f"\033[1m{text}"

def italic(text = "", *, escape = True) -> str:
    return f"\033[3m{text}\033[0m" if escape else f"\033[3m{text}"

def underline(text = "", *, escape = True) -> str:
    return f"\033[4m{text}\033[0m" if escape else f"\033[4m{text}"

def hide(text = "", *, escape = True) -> str:
    return f"\033[8m{text}\033[0m" if escape else f"\033[8m{text}"

def black(text = "", *, escape = True) -> str:
    return f"\033[30m{text}\033[0m" if escape else f"\033[30m{text}"

def red(text = "", *, escape = True) -> str:
    return f"\033[31m{text}\033[0m" if escape else f"\033[31m{text}"

def green(text = "", *, escape = True) -> str:
    return f"\033[32m{text}\033[0m" if escape else f"\033[32m{text}"

def yellow(text = "", *, escape = True):
    return f"\033[33m{text}\033[0m" if escape else f"\033[33m{text}"

def blue(text = "", *, escape = True) -> str:
    return f"\033[34m{text}\033[0m" if escape else f"\033[34m{text}"

def magenta(text = "", *, escape = True) -> str:
    return f"\033[35m{text}\033[0m" if escape else f"\033[35m{text}"

def cyan(text = "", *, escape = True) -> str:
    return f"\033[36m{text}\033[0m" if escape else f"\033[36m{text}"

def white(text = "", *, escape = True) -> str:
    return f"\033[37m{text}\033[0m" if escape else f"\033[37m{text}"

def gray(text = "", *, escape = True) -> str:
    return f"\033[90m{text}\033[0m" if escape else f"\033[90m{text}"

def default(text = "", *, escape = True) -> str:
    return f"\033[39m{text}\033[0m" if escape else f"\033[39m{text}"

def bg_black(text = "", *, escape = True) -> str:
    return f"\033[40m{text}\033[0m" if escape else f"\033[40m{text}"

def bg_red(text = "", *, escape = True) -> str:
    return f"\033[41m{text}\033[0m" if escape else f"\033[41m{text}"

def bg_green(text = "", *, escape = True) -> str:
    return f"\033[42m{text}\033[0m" if escape else f"\033[42m{text}"

def bg_yellow(text = "", *, escape = True) -> str:
    return f"\033[43m{text}\033[0m" if escape else f"\033[43m{text}"

def bg_blue(text = "", *, escape = True) -> str:
    return f"\033[44m{text}\033[0m" if escape else f"\033[44m{text}"

def bg_magenta(text = "", *, escape = True) -> str:
    return f"\033[45m{text}\033[0m" if escape else f"\033[45m{text}"

def bg_cyan(text = "", *, escape = True) -> str:
    return f"\033[46m{text}\033[0m" if escape else f"\033[46m{text}"

def bg_white(text = "", *, escape = True) -> str:
    return f"\033[47m{text}\033[0m" if escape else f"\033[47m{text}"

def bg_gray(text = "", *, escape = True) -> str:
    return f"\033[100m{text}\033[0m" if escape else f"\033[100m{text}"

def bg_default(text = "", *, escape = True) -> str:
    return f"\033[49m{text}\033[0m" if escape else f"\033[49m{text}"

def b_red(text = "", *, escape = True) -> str:
    return f"\033[91m{text}\033[0m" if escape else f"\033[91m{text}"

def b_green(text = "", *, escape = True) -> str:
    return f"\033[92m{text}\033[0m" if escape else f"\033[92m{text}"

def b_yellow(text = "", *, escape = True) -> str:
    return f"\033[93m{text}\033[0m" if escape else f"\033[93m{text}"

def b_blue(text = "", *, escape = True) -> str:
    return f"\033[94m{text}\033[0m" if escape else f"\033[94m{text}"

def b_magenta(text = "", *, escape = True) -> str:
    return f"\033[95m{text}\033[0m" if escape else f"\033[95m{text}"

def b_cyan(text = "", *, escape = True) -> str:
    return f"\033[96m{text}\033[0m" if escape else f"\033[96m{text}"

def b_white(text = "", *, escape = True) -> str:
    return f"\033[97m{text}\033[0m" if escape else f"\033[97m{text}"

def bg_b_red(text = "", *, escape = True) -> str:
    return f"\033[101m{text}\033[0m" if escape else f"\033[101m{text}"

def bg_b_green(text = "", *, escape = True) -> str:
    return f"\033[102m{text}\033[0m" if escape else f"\033[102m{text}"

def bg_b_yellow(text = "", *, escape = True) -> str:
    return f"\033[103m{text}\033[0m" if escape else f"\033[103m{text}"

def bg_b_blue(text = "", *, escape = True) -> str:
    return f"\033[104m{text}\033[0m" if escape else f"\033[104m{text}"

def bg_b_magenta(text = "", *, escape = True) -> str:
    return f"\033[105m{text}\033[0m" if escape else f"\033[105m{text}"

def bg_b_cyan(text = "", *, escape = True) -> str:
    return f"\033[106m{text}\033[0m" if escape else f"\033[106m{text}"

def bg_b_white(text = "", *, escape = True) -> str:
    return f"\033[107m{text}\033[0m" if escape else f"\033[107m{text}"


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

def highlight_range(text: str, start: int, end: int, *, colors: list[ColorFun], colors2: list[ColorFun] = []) -> str:
    """
    Returns `text` if `start >= end`. Throws an `AssertionError` if indexes are out of bounds
    """
    if start >= end:
        return text
    assert start >= 0 and start < len(text), f"Out of bounds start={start}"
    assert end >= 0 and end < len(text), f"Out of bounds end={end}"
    hl2 = "".join([c(escape = False) for c in colors2])
    return hl2 + text[:start] + reset() \
        + "".join([c(escape = False) for c in colors]) \
        + text[start:end] \
        + reset() + hl2 + text[end:] + reset()

def highlight_between(text: str, start: str, end: str, *, colors: list[ColorFun], colors2: list[ColorFun] = []) -> str:
    i = 0
    hl = default() + "".join([c(escape = False) for c in colors])
    hl2 = default() + "".join([c(escape = False) for c in colors2])
    ret = hl2
    while True:
        old_i = i
        i = text.find(start, i)
        j = text.find(end, i + 1)
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

def gradient_rgb(start: RGB, end: RGB):
    def ret(text: str) -> str:
        ret = ""
        clr = start
        for i, char in enumerate(text):
            clr = (
                clr[0] + (1 / len(text)) * (end[0] - start[0]),
                clr[1] + (1 / len(text)) * (end[1] - start[1]),
                clr[2] + (1 / len(text)) * (end[2] - start[2]),
            )
            print(clr)
            ret += rgb(int(clr[0]), int(clr[1]), int(clr[2]))(char, escape=False)
        return ret + reset()
    return ret
