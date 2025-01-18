# from src.color_console import \
#     color, highlight, highlight_range, uncolor, progress_bar, highlight_between, \
#     green, yellow, cyan, red, b_white, \
#     underline, italic, bold, \
#     bg_red, bg_green, bg_yellow, bg_b_white, bg_b_green

from src.color_console import *

def c(txt: str) -> str:
    return color(b_white, italic, f"\"{txt}\"")

print(c('print(green("Hello"), yellow("World"))'))
print(green("Hello"), yellow("World"))
print()

print(c('print(x := color(cyan, underline, "Hello", bg_red, "World"))'))
print(x := color(cyan, underline, "Hello", red, "World"))
print()

print(c('print(uncolor(x))'))
print(uncolor(x))
print()

print(c('print(rgb(255, 0, 100)("Hello"), bg_rgb(100, 0, 255)("World"))'))
print(rgb(255, 0, 100)("Hello"), bg_rgb(100, 0, 255)("World"))
print()

print(c('set_force_4_bit(True)'))
print(c('print(rgb(255, 0, 100)("Hello"), bg_rgb(100, 0, 255)("World"))'))
set_force_4_bit(True)
print(rgb(255, 0, 100)("Hello"), bg_rgb(100, 0, 255)("World"))
print()
set_force_4_bit(False)

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
print("\n", progress_bar(0.999, 20, colors=[bg_b_green], colors2=[bg_b_white], char=" ", char2=" "), sep="")
print()

print(c('print("\\n", progress_bar(0.55, 10, colors=[bold, green], char="Loading...", char2="Loading..."), sep="")'))
print("\n", progress_bar(0.3333, 10, colors=[bold, green], char="Loading...", char2="Loading..."), sep="")
print()

print(c('print("\\n", progress_bar(1, 10, colors=[bold, green], char="Loading...", char2="Loading...", on_complete="Done!"), sep="")'))
print("\n", progress_bar(1, 10, colors=[bold, green], char="Loading...", char2="Loading...", on_complete="Done!"), sep="")
print()

print(c('print(highlight_between("H\'ell\'o W\'orl\'d", "\'", "\'", colors=[green], colors2=[italic, yellow]))'))
print(highlight_between("H'ell'o W'orl'd", "'", "'", colors=[green], colors2=[italic, yellow]))


gr = gradient_rgb((255, 0, 0), (0, 0, 255))
print(gr("Hello Worldqqqqqqqqqqqqqq"))


# i = 0
# for r in range(256):
#     for g in range(256):
#         for b in range(256):
#             closest = closest_rgb_i(r, g, b)
#             t = f"{str((r, g, b)):>15} -> {str(colors[closest][0]):<13}" \
#                 + rgb(r, g, b)("x") + bg_rgb(r, g, b)("x") \
#                 + " " \
#                 + rgb(r, g, b, safe=True)("x") + bg_rgb(r, g, b, safe=True)("x")
#             print(t, end="")
#             i += 1
#             if i == 2:
#                 i = 0
#                 print()


# def test_rgb(r, g, b):
#     print(
#         rgb(r,g,b)("x"),
#         bg_rgb(r,g,b)("x"),
#         rgb(r,g,b,safe=True)("x"),
#         bg_rgb(r,g,b, safe=True)("x"),
#     )

# test_rgb(200, 200, 200)

# for (r, g, b), clr, bg_clr in colors:
#     print((r, g, b), closest_rgb_i(r, g, b))