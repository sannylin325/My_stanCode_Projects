"""
File: breakoutgraphics.py
Name: Sanny Lin
-------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This program is about the background setting of game "breakout",
such as the default of window, paddle, ball, bricks, and the random velocity of the ball.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
NUM_LIVES = 3		   # Number of attempts


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # other variable
        self.paddle_offset = paddle_offset
        self.mouseclick = False
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_offset = brick_offset
        self.brick_spacing = brick_spacing
        self.num_of_bricks = brick_rows * brick_cols
        self.clear_bricks = int(0)  # count the bricks cleared, if all cleared, game win
        self.num_lives = NUM_LIVES

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = "black"
        self.window.add(self.paddle, x=(self.window_width-paddle_width)//2, y=self.window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(width=ball_radius*2, height=ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = "black"
        self.window.add(self.ball, x=(self.window_width-ball_radius)//2, y=(self.window_height-ball_radius)//2)

        # score board
        self.score_label = GLabel("Score: " + str(self.clear_bricks))
        self.score_label.font = "-25"
        self.window.add(self.score_label, x=0, y=self.score_label.height+10)

        # remain lives
        self.num_lives_label = GLabel("∮" * self.num_lives)
        self.num_lives_label.font = "-25"
        self.window.add(self.num_lives_label, x=self.window.width-self.num_lives_label.width, y=self.window_height)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_move)

        # Draw bricks(colorful)
        self.set_bricks()

        # pop rect
        self.p_rect_width = self.window.width - brick_width * 2
        self.p_rect_height = brick_height * 3
        self.p_rect = GRect(width=self.p_rect_width, height=self.p_rect_height)
        self.p_rect.filled = True
        self.p_rect.fill_color = "gray"

    def set_bricks(self):
        for i in range(self.brick_rows):
            for j in range(self.brick_cols):
                bricks = GRect(width=self.brick_width, height=self.brick_height)
                bricks.filled = True
                if self.brick_rows >= 10:
                    if i == 0 or i == 1:
                        bricks.fill_color = "red"
                    elif i == 2 or i == 3:
                        bricks.fill_color = "orange"
                    elif i == 4 or i == 5:
                        bricks.fill_color = "yellow"
                    elif i == 6 or i == 7:
                        bricks.fill_color = "green"
                    elif i == 8 or i == 9:
                        bricks.fill_color = "blue"
                    else:
                        bricks.fill_color = "purple"
                elif 5 <= self.brick_rows < 10:
                    if i == 0:
                        bricks.fill_color = "red"
                    elif i == 1:
                        bricks.fill_color = "orange"
                    elif i == 2:
                        bricks.fill_color = "yellow"
                    elif i == 3:
                        bricks.fill_color = "green"
                    elif i == 4:
                        bricks.fill_color = "blue"
                    else:
                        bricks.fill_color = "purple"
                else:
                    bricks.fill_color = "purple"
                self.window.add(bricks, x=(self.brick_width+self.brick_spacing)*j,
                                y=self.brick_offset+(self.brick_height+self.brick_spacing)*i)

    def paddle_move(self, event):
        if self.paddle.width // 2 <= event.x < self.window.width - self.paddle.width // 2:  # head & end both //2
            self.paddle.x = event.x - self.paddle.width // 2
        elif event.x < 0:
            self.paddle.x = 0
        elif event.x > self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width

    def ball_move(self, event):
        if not self.mouseclick:
            self.mouseclick = True  # the velocity will not change in mode "True"
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    # getter & setter of the velocity of the ball (property)
    @property
    def vy(self):
        return self.__dy

    @vy.setter
    def vy(self, new_dy):
        self.__dy = new_dy

    @property
    def vx(self):
        return self.__dx

    @vx.setter
    def vx(self, new_dx):
        self.__dx = new_dx

    # # getter the velocity of the ball
    # def get_vy(self):
    #     return self.__dy
    #
    # def get_vx(self):
    #     return self.__dx
    #
    # # when user-py change velocity, coder-py will also change
    # def set_dy(self, new_dy):
    #     self.__dy = new_dy
    #
    # def set_dx(self, new_dx):
    #     self.__dx = new_dx

    def pop(self):
        self.window.add(self.p_rect, x=(self.window_width-self.p_rect_width)//2,
                        y=(self.window_height-self.p_rect_height)//2)
