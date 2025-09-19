"""
File: breakout.py
Name: Sanny Lin
-------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program import the background setting of game "breakout" from breakoutgraphics.py,
and set the conditions of ball's moving and bouncing.
"""

from campy.gui.events.timer import pause
from SC101_a2_breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second


def main():
    """
    This function set the conditions of ball's moving and bouncing.
    If the ball drop out the bottom of the window 3 times, game lose;
    if all the bricks were cleared, game win.
    Different color of the bricks get different score.
    A little challenge: when 1/2 bricks are cleared, a rect will appear to bind.
    """
    # get "Breakout" background
    graphics = BreakoutGraphics()

    # variable
    drop_times = 0  # the times the ball drop out the window
    score = 0  # count score
    base_y = graphics.brick_height+graphics.brick_spacing  # variable in order to get maybe_obj color

    # ball start moving
    while True:
        # get velocity at the start of every while loop
        vx = graphics.vx
        vy = graphics.vy

        if graphics.num_lives > 0:
            while graphics.mouseclick:
                # update
                graphics.ball.move(vx, vy)

                # check bouncing condition
                # side wall
                # about velocity: change self.__dy/self__.dx, and get new velocity
                if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width-graphics.ball.width:
                    graphics.vx = -vx
                    vx = graphics.vx
                if graphics.ball.y <= 0:
                    graphics.vy = -vy
                    vy = graphics.vy

                # paddle or bricks
                for x in range(graphics.ball.x, graphics.ball.x+graphics.ball.width+1, graphics.ball.width):
                    for y in range(graphics.ball.y, graphics.ball.y+graphics.ball.height+1, graphics.ball.height):
                        maybe_obj = graphics.window.get_object_at(x, y)
                        if maybe_obj is not None \
                                and maybe_obj is not graphics.score_label \
                                and maybe_obj is not graphics.num_lives_label \
                                and maybe_obj is not graphics.p_rect:
                            if maybe_obj is graphics.paddle:
                                if vy > 0:
                                    graphics.vy = -vy
                                    vy = graphics.vy
                            else:
                                graphics.vy = -vy
                                vy = graphics.vy
                                # # bricks with different color get different points
                                if graphics.brick_rows >= 10:
                                    if maybe_obj.y-graphics.brick_offset <= base_y:
                                        score += 6
                                    elif base_y * 2 <= maybe_obj.y-graphics.brick_offset <= base_y * 3:
                                        score += 5
                                    elif base_y * 4 <= maybe_obj.y-graphics.brick_offset <= base_y * 5:
                                        score += 4
                                    elif base_y * 6 <= maybe_obj.y-graphics.brick_offset <= base_y * 7:
                                        score += 3
                                    elif base_y * 8 <= maybe_obj.y-graphics.brick_offset <= base_y * 9:
                                        score += 2
                                    else:
                                        score += 1
                                elif 5 <= graphics.brick_rows < 10:
                                    if maybe_obj.y-graphics.brick_offset == base_y:
                                        score += 6
                                    elif maybe_obj.y-graphics.brick_offset == base_y * 2:
                                        score += 5
                                    elif maybe_obj.y-graphics.brick_offset == base_y * 3:
                                        score += 4
                                    elif maybe_obj.y-graphics.brick_offset == base_y * 4:
                                        score += 3
                                    elif maybe_obj.y-graphics.brick_offset == base_y * 5:
                                        score += 2
                                    else:
                                        score += 1
                                else:
                                    score += 1
                                # remove bricks and count clear_bricks & score
                                graphics.window.remove(maybe_obj)
                                graphics.clear_bricks += 1
                                graphics.score_label.text = "Score: " + str(score)

                # pop rect: to bind
                if graphics.clear_bricks >= graphics.num_of_bricks // 2:
                    graphics.pop()

                # drop below the window
                if graphics.ball.y > graphics.window.height:
                    graphics.num_lives -= 1
                    drop_times += 1
                    graphics.num_lives_label.text = " " * 3 * drop_times + "∮" * graphics.num_lives
                    # reset ball's location and close the mouseclick
                    graphics.ball.x = (graphics.window.width-graphics.ball.width)//2
                    graphics.ball.y = (graphics.window.height-graphics.ball.height)//2
                    graphics.mouseclick = False

                # end the game (win or lose)
                if graphics.clear_bricks >= graphics.num_of_bricks:
                    graphics.num_lives_label.text = "YOU WIN!! :)) "
                    graphics.num_lives_label.x = graphics.window.width - graphics.num_lives_label.width
                    break

                if graphics.num_lives == 0:
                    graphics.num_lives_label.text = "GAME OVER :( "
                    graphics.num_lives_label.x = graphics.window.width - graphics.num_lives_label.width
                    break

                # pause
                pause(FRAME_RATE)

        # when game win: let ball stay still
        if graphics.clear_bricks >= graphics.num_of_bricks:
            break

        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
