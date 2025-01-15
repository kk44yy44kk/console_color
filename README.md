# console_color
Is a very simple python library for changing text color with ANSI escape codes

## Examples

### <span style="color: green">Hello</span> <span style="color: yellow">World</span>

```python
from console_color import green, yellow
print(green("Hello"), yellow("World"))
```

### <span style="text-decoration: underline; color: cyan">Hello <span style="background-color: red">World</span></span>

```python
from console_color import color, underline, cyan, bg_red
print(color(underline, cyan, "Hello", bg_red, "World"))
```

### <span>He<span style="background-color: green; font-style: italic">ll</span>o Wor<span style="background-color: green; font-style: italic">l</span>d</span><span>

```python
from console_color import highlight, bg_green, italic
print(highlight("Hello World", "l", colors=[bg_green, italic]))
```

### Hel<span style="color: cyan; text-decoration: underline">l Wo</span>rld

```python
from console_color import highlight_range, cyan, underline
print(highlight_range("Hello World", 3, 8, colors=[cyan, underline]))
```