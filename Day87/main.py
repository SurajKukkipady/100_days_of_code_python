import tkinter as tk
import random

# Game Constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 10
BALL_RADIUS = 10
BRICK_ROWS = 5
BRICK_COLS = 8
BRICK_WIDTH = 50
BRICK_HEIGHT = 20

class BreakoutGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Breakout Game")

        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
        self.canvas.pack()

        self.paddle = self.canvas.create_rectangle(200, 380, 280, 390, fill="white")
        self.ball = self.canvas.create_oval(245, 245, 255, 255, fill="red")

        self.ball_dx = 3
        self.ball_dy = -3

        self.bricks = []
        self.create_bricks()

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        self.running = True
        self.update_game()

    def create_bricks(self):
        colors = ["red", "orange", "yellow", "green", "blue"]
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                x1 = col * BRICK_WIDTH + 5
                y1 = row * BRICK_HEIGHT + 5
                x2 = x1 + BRICK_WIDTH - 10
                y2 = y1 + BRICK_HEIGHT - 5
                brick = self.canvas.create_rectangle(x1, y1, x2, y2, fill=colors[row])
                self.bricks.append(brick)

    def move_left(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.paddle)
        if x1 > 0:
            self.canvas.move(self.paddle, -20, 0)

    def move_right(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.paddle)
        if x2 < WINDOW_WIDTH:
            self.canvas.move(self.paddle, 20, 0)

    def update_game(self):
        if not self.running:
            return

        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        self.check_collisions()
        self.root.after(20, self.update_game)

    def check_collisions(self):
        ball_coords = self.canvas.coords(self.ball)
        x1, y1, x2, y2 = ball_coords

        # Bounce off walls
        if x1 <= 0 or x2 >= WINDOW_WIDTH:
            self.ball_dx *= -1
        if y1 <= 0:
            self.ball_dy *= -1

        # Ball hits paddle
        paddle_coords = self.canvas.coords(self.paddle)
        if self.is_collision(ball_coords, paddle_coords):
            self.ball_dy *= -1

        # Ball hits bricks
        for brick in self.bricks[:]:
            brick_coords = self.canvas.coords(brick)
            if self.is_collision(ball_coords, brick_coords):
                self.canvas.delete(brick)
                self.bricks.remove(brick)
                self.ball_dy *= -1
                break

        # Ball falls below paddle
        if y2 >= WINDOW_HEIGHT:
            self.running = False
            self.canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, text="Game Over", fill="white", font=("Arial", 24))

        # Win condition
        if not self.bricks:
            self.running = False
            self.canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, text="You Win!", fill="white", font=("Arial", 24))

    def is_collision(self, coords1, coords2):
        x1, y1, x2, y2 = coords1
        a1, b1, a2, b2 = coords2
        return not (x2 < a1 or x1 > a2 or y2 < b1 or y1 > b2)

if __name__ == "__main__":
    root = tk.Tk()
    game = BreakoutGame(root)
    root.mainloop()
