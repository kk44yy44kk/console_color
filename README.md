# console_color
Is a very simple python library for changing text color with ANSI escape codes

## Examples

### <code style="color: green">Hello</code> <code style="color: yellow">World</code>

```python
from console_color import green, yellow
print(green("Hello"), yellow("World"))
```

### <code style="text-decoration: underline; color: cyan">Hello <code style="background-color: red">World</code></code>

```python
from console_color import color, underline, cyan, bg_red
print(color(underline, cyan, "Hello", bg_red, "World"))
```

### <code>He<code style="background-color: green; font-style: italic">ll</code>o Wor<code style="background-color: green; font-style: italic">l</code>d</code></code>

```python
from console_color import highlight, bg_green, italic
print(highlight("Hello World", "l", colors=[bg_green, italic]))
```

### Hel<code style="color: cyan; text-decoration: underline">l Wo</code>rld

```python
from console_color import highlight_range, cyan, underline
print(highlight_range("Hello World", 3, 8, colors=[cyan, underline]))
```