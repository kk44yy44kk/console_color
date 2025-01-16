from src.color_console import \
    color, highlight, highlight_range, uncolor, progress_bar, \
    green, yellow, cyan, red, b_white, \
    underline, italic, bold, \
    bg_red, bg_green, bg_yellow, bg_b_white, bg_b_green

def c(txt: str) -> str:
    return color(b_white, italic, f"\"{txt}\"")

print(c('print(green("Hello"), yellow("World"))'))
print(green("Hello"), yellow("World"))
print()

print(c('print(x := color(cyan, underline, "Hello", bg_red, "World"))'))
print(x := color(cyan, underline, "Hello", bg_red, "World"))
print()

print(c('print(uncolor(x))'))
print(uncolor(x))
print()

print(c('print(highlight("Hello World", "l", colors=[bg_green, italic, bold]))'))
print(highlight("Hello World", "l", colors=[bg_green, italic, bold]))
print()

print(c('print(highlight_range("Hello World", 3, 8, colors=[cyan, underline]))'))
print(highlight_range("Hello World", 3, 8, colors=[cyan, underline]))
print()

print(c('print(highlight("Hello World", "l", colors=[red, underline, bold], colors2=[bg_yellow, italic]))'))
print(highlight("Hello World", "l", colors=[red, underline, bold], colors2=[bg_yellow, italic]))
print()

print(c('print("\\n", progress_bar(0.35, 20, colors=[bg_b_green], colors2=[bg_b_white], char=" ", char2=" "), sep="")'))
print("\n", progress_bar(0.35, 20, colors=[bg_b_green], colors2=[bg_b_white], char=" ", char2=" "), sep="")
print()
