from math import floor
from random import randint
from time import sleep
import settings
from entities.paddle import Paddle
from entities.ball import Ball
from entities.brick import Brick
import pygame
import turtle

class BreakOutGame:
    def __init__(self):
        pygame.mixer.init()
        self.screen = self.init_screen()
        self.sounds = self.init_sounds()


        self.brick_collection = []
        self.draw_layout()

        self.is_running = True
        self.state_of_press = {"Right": False, "Left": False}
        self.ball = Ball()
        self.ball.setup()
        self.paddle = Paddle()
        self.paddle.draw_paddle()


        self.setup_inputs()


    def init_sounds(self):
        self.sounds = {
            "hit_sound": pygame.mixer.Sound("universfield-cinematic-impact-hit-352702.mp3"),
            "game_over": pygame.mixer.Sound("freesound_community-negative_beeps-6008.mp3"),
            "paddle_hit": pygame.mixer.Sound("aberrantrealities-funny-lighthearted-springy-boing-effect-01-416262.mp3")
        }
        return self.sounds

    def on_key_press_left(self):
        self.state_of_press["Left"] = True

    def on_key_press_right(self):
        self.state_of_press["Right"] = True

    def on_key_release_left(self):
        self.state_of_press["Left"] = False

    def on_key_release_right(self):
        self.state_of_press["Right"] = False

    def init_screen(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor(settings.BG_COLOR)
        self.screen.tracer(0)
        return self.screen

    def draw_layout(self):
        top_wall = Brick(settings.TOP_WALL, settings.WALL_COLOR)
        top_wall.draw_brick(800, 50)

        left_wall = Brick(settings.LEFT_WALL, settings.WALL_COLOR)
        left_wall.draw_brick(30, 800)

        right_wall = Brick(settings.RIGHT_WALL, settings.WALL_COLOR)
        right_wall.draw_brick(10, 800)

        bottom_wall = Brick(settings.BOTTOM_WALL, settings.WALL_COLOR)
        bottom_wall.draw_brick(800, 50)

        for i in range(5 * 12):

           x = -370 + ((i % 12) * 60)
           y = 250 - floor(i / 12) * 30
           if i <= 12:
               color = settings.ROW1_COLOR
           elif 12 <= i <= 12 * 2:
               color = settings.ROW2_COLOR
           elif 12 * 2 < i <= 12 * 3:
               color = settings.ROW3_COLOR
           elif 12 * 3 < i <= 12 * 4:
               color = settings.ROW4_COLOR
           else:
               color = settings.ROW5_COLOR
           brick = Brick((x, y), color)
           brick.draw_brick(50, 25)
           self.brick_collection.append(brick)

    def setup_inputs(self):
        self.screen.listen()
        self.screen.onkeypress(fun=self.on_key_press_left, key="Left")
        self.screen.onkeypress(fun=self.on_key_press_right, key="Right")
        self.screen.onkeyrelease(fun=self.on_key_release_left, key="Left")
        self.screen.onkeyrelease(fun=self.on_key_release_right, key="Right")

    def collision_detection(self):

        x, y = self.ball.curr_position()

        if x <= settings.LEFT_WALL[0] + 50:
            self.ball.dx = -self.ball.dx
        elif x >= settings.RIGHT_WALL[0] - 5:
            self.ball.dx = -self.ball.dx
        elif y >= settings.TOP_WALL[1] - 10:
            self.ball.dy = - self.ball.dy
        elif y <= settings.BOTTOM_WALL[1] + 50:
            print("GAME 0VER....")
            self.sounds["game_over"].play()
            self.is_running = False
            return

        paddle_x, paddle_y = self.paddle.curr_position()

        if (paddle_x - 5) < x < (paddle_x + 55) and (paddle_y - 1) < y < (paddle_y + 10):
            self.ball.dy = - self.ball.dy
            self.sounds["paddle_hit"].play(maxtime=950)
            if paddle_x - 5 < x < paddle_x + 20:
                if randint(0, 1):
                    sign = -1
                else:
                    sign = 1
                self.ball.dx = sign * abs(self.ball.dx)
            elif paddle_x + 20 <= x <= paddle_x + 30:
                self.ball.dx = 1
                self.ball.dy = -4
            else:
                if randint(0, 1):
                    sign = -1
                else:
                    sign = 1
                self.ball.dx = sign * abs(self.ball.dx)

        i = 0
        while i < len(self.brick_collection):

            brick_x, brick_y = self.brick_collection[i].curr_position()

            if brick_x - 2 < x < (brick_x + 52) and brick_y - 2 < y < (brick_y + 25):
                self.ball.dy = - self.ball.dy
                self.brick_collection[i].delete_brick()
                self.brick_collection.remove(self.brick_collection[i])
                self.sounds["hit_sound"].play(maxtime=950)
            else:
                i += 1

    def run(self):
        self.screen.update()

        while self.is_running:
            self.ball.move()
            self.collision_detection()

            if self.state_of_press["Right"]:
                self.paddle.move_right()

            if self.state_of_press["Left"]:
                self.paddle.move_left()

            sleep(0.01)
            self.screen.update()

        self.screen.exitonclick()
