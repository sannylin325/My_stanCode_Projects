"""
File: draw_line.py
Name: Sanny Lin
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 8  # radius of circle

# global variable
window = GWindow(width=500, height=500)
circle = GOval(SIZE, SIZE)
click = 0  # to judge odd/even click


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    """
    param mouse: mouse information from onmouseclicked()
    function: odd click create a circle,
              even click create a line between now click & previous click
              (original circle will disappear)
    """
    global click
    click += 1

    if click % 2:  # odd click
        window.add(circle, x=mouse.x-0.5*SIZE, y=mouse.y-0.5*SIZE)
    else:  # even click
        window.remove(circle)
        line = GLine(circle.x+0.5*SIZE, circle.y+0.5*SIZE, mouse.x, mouse.y)
        window.add(line)


if __name__ == "__main__":
    main()
