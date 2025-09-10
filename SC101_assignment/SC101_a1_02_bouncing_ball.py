"""
File: bouncing_ball.py
Name: Sanny Lin
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3          # vx of ball
DELAY = 10      # pause
GRAVITY = 1     # vy += GRAVITY in each while loop
SIZE = 20       # radius of ball
REDUCE = 0.9    # vx *= REDUCE in each bouncing
START_X = 30    # ball.x at start
START_Y = 40    # ball.y at start
COUNT = 3       # the times limit of ball dropping

# global variable
window = GWindow(800, 500, title='bouncing_ball.py')
check = False  # control if onmouseclicked work


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global check
    onmouseclicked(drop)

    # set background & count
    ball = GOval(SIZE, SIZE)
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    count = COUNT

    while True:
        if check and count > 0:  # only if check == True, ball start dropping
            vy = 0
            while ball.x <= window.width:
                # update
                ball.move(VX, vy)
                # check
                if vy > 0 and ball.y+SIZE > window.height:
                    vy = - vy * REDUCE
                vy += GRAVITY
                # pause
                pause(DELAY)
            # count program times
            count -= 1
            # reset ball & check
            ball.x, ball.y = START_X, START_Y
            check = False
        pause(DELAY)


def drop(mouse):
    """
    check of onmouseclicked: if check change 'False' in while loop, mouseclick won't work
    """
    global check
    check = True


if __name__ == "__main__":
    main()
