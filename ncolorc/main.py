from typing import Callable
from math import floor

ColorFun = Callable[[str], str]
"""It also has a `escape = True` keyword only argument"""
RGB = tuple[int, int, int]

def _make_color(code: int):
    def ret(text = "", *, escape = True) -> str:
        return f"\033[{code}m{text}\033[0m" if escape else f"\033[{code}m{text}"
    return ret

def compose(funcs: list[ColorFun]):
    """
    Composes many color function into one function
    """
    def ret(text: str, escape = True) -> str:
        for func in funcs:
            text = func(text, escape=escape)
        return text
    return ret

reset = _make_color(0)
bold = _make_color(1)
italic = _make_color(3)
underline = _make_color(4)
hide = _make_color(8)
default = _make_color(39)
black = _make_color(30)
red = _make_color(31)
green = _make_color(32)
yellow = _make_color(33)
blue = _make_color(34)
magenta = _make_color(35)
cyan = _make_color(36)
white = _make_color(37)
gray = _make_color(90)
b_red = _make_color(91)
b_green = _make_color(92)
b_yellow = _make_color(93)
b_blue = _make_color(94)
b_magenta = _make_color(95)
b_cyan = _make_color(96)
b_white = _make_color(97)
bg_default = _make_color(39+10)
bg_black = _make_color(30+10)
bg_red = _make_color(31+10)
bg_green = _make_color(32+10)
bg_yellow = _make_color(33+10)
bg_blue = _make_color(34+10)
bg_magenta = _make_color(35+10)
bg_cyan = _make_color(36+10)
bg_white = _make_color(37+10)
bg_gray = _make_color(90+10)
bg_b_red = _make_color(91+10)
bg_b_green = _make_color(92+10)
bg_b_yellow = _make_color(93+10)
bg_b_blue = _make_color(94+10)
bg_b_magenta = _make_color(95+10)
bg_b_cyan = _make_color(96+10)
bg_b_white = _make_color(97+10)

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

def highlight(text: str, sub: str, *, colors: list[ColorFun], colors2: list[ColorFun] = []) -> str:
    ret = ""
    hl = compose(colors)
    hl2 = compose(colors2)
    i = 0
    i_prev = -99
    # Gaps are characters between islands of neighbouring subs
    gap_start = 0
    gap_end = 0
    while True:
        i = text.find(sub, i)
        if i == -1:
            break
        if i_prev != i - len(sub):
            ret += hl(text[gap_end:gap_start]) + hl2(text[gap_start:i])
            gap_end = i
        gap_start = i + len(sub)
        i_prev = i
        i += 1
    return ret + hl(text[gap_end:gap_start]) + hl2(text[gap_start:])

def highlight_range(text: str, start: int, stop: int, *, colors: list[ColorFun], colors2: list[ColorFun] = []) -> str:
    """
    Returns `text` if `start >= stop`. Throws an `AssertionError` if indexes are out of bounds
    """
    hl = compose(colors)
    hl2 = compose(colors2)
    if start >= stop:
        return text
    assert start >= 0 and start < len(text), f"Out of bounds start={start}"
    assert stop >= 0 and stop < len(text), f"Out of bounds stop={stop}"
    return hl2(text[:start]) + hl(text[start:stop]) + hl2(text[stop:])

def highlight_between(text: str, start: str, stop: str, *, colors: list[ColorFun], colors2: list[ColorFun] = []) -> str:
    i = 0
    hl = compose(colors)
    hl2 = compose(colors2)
    ret = ""
    while True:
        old_i = i
        i = text.find(start, i)
        j = text.find(stop, i + 1)
        if -1 in [i, j]:
            i = old_i
            break
        ret += hl2(text[old_i:i]) + hl(text[i:j+1])
        i = j + 1
    return ret + hl2(text[i:])

def uncolor(text: str) -> str:
    """Removes all ANSI graphical renditions"""
    ret = ""
    last = 0
    while last < len(text):
        start = text.find("\033", last)
        ret += text[last:start]
        last = text.find("m", start) + 1
    return ret

def progress_bar(value: float, width: int, *, colors: list[ColorFun] = [green], colors2: list[ColorFun] = [white], char = "#", char2 = ".", percentage = True, on_complete: str | None = None) -> str:
    # TODO?: make gradients scale properly
    assert char != "" and char2 != "", "Chars can't be empty strings"
    hl = compose(colors)
    hl2 = compose(colors2)
    tail = ""
    if on_complete is not None and value >= 1:
        tail = " " + on_complete
    elif percentage:
        tail = f"({int(value * 100)}%)"
        tail = f" {tail:<6}"
    progress_width = floor(value * width)
    progress = (char * width)[:progress_width]
    background = (char2 * width)[progress_width:width]
    return f"\033[A{hl(progress)}{hl2(background)}{tail}"

_dim, _nrm, _bri = 90, 180, 255
approx_colors: tuple[RGB, ColorFun, ColorFun] = [
    ((0, 0, 0), black, bg_black),
    ((_nrm, 0, 0), red, bg_red),
    ((0, _nrm, 0), green, bg_green),
    ((_nrm, _dim, 0), yellow, bg_yellow),
    ((0, 0, _nrm), blue, bg_blue),
    ((_nrm, 0, _nrm), magenta, bg_magenta),
    ((0, _nrm, _nrm), cyan, bg_cyan),
    ((_nrm, _nrm, _nrm), white, bg_white),
    ((_bri, _dim, _dim), b_red, bg_b_red),
    ((_dim, _bri, _dim), b_green, bg_b_green),
    ((_bri, _bri, _dim), b_yellow, bg_b_yellow),
    ((_dim, _dim, _bri), b_blue, bg_b_blue),
    ((_bri, _dim, _bri), b_magenta, bg_b_magenta),
    ((_dim, _bri, _bri), b_cyan, bg_b_cyan),
    ((_bri, _bri, _bri), b_white, bg_b_white),
    ((_dim, _dim, _dim), gray, bg_gray),
]

_color2approx: dict[ColorFun, RGB]

def approx_colors_set(new: tuple[RGB, ColorFun, ColorFun]) -> None:
    global approx_colors
    global _color2approx
    approx_colors = new
    _color2approx = {fn: rgb for rgb, fn, bg_fn in approx_colors}
    _color2approx.update({bg_fn: rgb for rgb, fn, bg_fn in approx_colors})

approx_colors_set(approx_colors)

def _approx_color_i_get(r: int, g: int, b: int) -> int:
    minimum = 256*3
    minimum_i = -1
    for i, clr in enumerate(approx_colors):
        r2, g2, b2 = clr[0]
        diff = abs(r2 - r) + abs(g2 - g) + abs(b2 - b)
        if diff < minimum:
            minimum = diff
            minimum_i = i
    return minimum_i

approx_colors_force = False

def approx_colors_force_set(value: bool) -> None:
    """
    If `approx_colors_force` is `True`, then functions `rgb` and `bg_rgb` will return the closest predefined color functions

    Ex. `rgb(0, 0, 0)` will return the `black` function
    """
    global approx_colors_force
    approx_colors_force = value

def rgb(rgb: RGB):
    """
    Returns a custom 24-bit color function
    """
    r, g, b = rgb
    assert r in range(256), f"r = {r}, it needs to be in range 0..255"
    assert g in range(256), f"g = {g}, it needs to be in range 0..255"
    assert b in range(256), f"b = {b}, it needs to be in range 0..255"
    global approx_colors_force
    if approx_colors_force:
        i = _approx_color_i_get(r, g, b)
        return approx_colors[i][1]
    def ret(txt: str, escape = True) -> str:
        return f"\033[38;2;{r};{g};{b}m{txt}\033[0m" if escape else f"\033[38;2;{r};{g};{b}m{txt}"
    return ret

def bg_rgb(rgb: RGB):
    """
    Returns a custom 24-bit color function for backgrounds
    """
    r, g, b = rgb
    assert r in range(256), f"r = {r}, it needs to be in range 0..255"
    assert g in range(256), f"g = {g}, it needs to be in range 0..255"
    assert b in range(256), f"b = {b}, it needs to be in range 0..255"
    global approx_colors_force
    if approx_colors_force:
        i = _approx_color_i_get(r, g, b)
        return approx_colors[i][2]
    def ret(txt: str, escape = True) -> str:
        return f"\033[48;2;{r};{g};{b}m{txt}\033[0m" if escape else f"\033[48;2;{r};{g};{b}m{txt}"
    return ret


def _make_gradient_rgb(rgb_fn: Callable):
    assert rgb_fn in [rgb, bg_rgb], "It needs to be one of these two functions"
    def gradient_rgb(start: RGB, stop: RGB):
        def ret(text = "", escape = True) -> str:
            ret = ""
            rgb = start
            if text != "":
                fraction = 1 / len(text)
            for char in text:
                rgb = (
                    rgb[0] + (fraction) * (stop[0] - start[0]),
                    rgb[1] + (fraction) * (stop[1] - start[1]),
                    rgb[2] + (fraction) * (stop[2] - start[2]),
                )
                ret += rgb_fn((int(rgb[0]), int(rgb[1]), int(rgb[2])))(char, escape=False)
            if escape:
                ret += reset()
            return ret
        return ret
    return gradient_rgb

gradient_rgb = _make_gradient_rgb(rgb)
bg_gradient_rgb = _make_gradient_rgb(bg_rgb)

def gradient(start: ColorFun, stop: ColorFun):
    assert start in _color2approx.keys(), "This function only accepts premade color functions like red or bg_cyan"
    assert stop in _color2approx.keys(), "This function only accepts premade color functions like red or bg_cyan"
    return gradient_rgb(_color2approx[start], _color2approx[stop])

def bg_gradient(start: ColorFun, stop: ColorFun):
    assert start in _color2approx.keys(), "This function only accepts premade color functions like red or bg_cyan"
    assert stop in _color2approx.keys(), "This function only accepts premade color functions like red or bg_cyan"
    return bg_gradient_rgb(_color2approx[start], _color2approx[stop])

def hex2rgb(code: str) -> RGB:
    code = code.removeprefix("#")
    assert len(code) == 6, "TODO"
    return (int(code[0:2], 16), int(code[2:4], 16), int(code[4:6], 16))