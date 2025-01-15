from typing import Callable

ColorFun = Callable[[str], str]

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

def yellow(text: str, *, escape = True):
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

def highlight(text: str, what: str, count = -1, *, colors: list[ColorFun], colors2: list[ColorFun]) -> str:
    hl2 = "".join([c(escape = False) for c in colors2])
    replacement = reset() + "".join([c(escape = False) for c in colors]) \
        + what + reset() + hl2
    return hl2 + text.replace(what, replacement, count) + reset()

def highlight_range(text: str, start: int, end: int, *, colors: list[ColorFun], colors2: list[ColorFun]) -> str:
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

# print(highlight("Hello World", "l", colors=[red], colors2=[bg_white]))
print(highlight_range("Hello World", 2, 7, colors=[b_green], colors2=[bg_blue]))