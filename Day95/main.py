import turtle
import math
import random
import time

# Set up the screen
win = turtle.Screen()
win.bgcolor("black")
win.title("Space Invaders with Turtle")
win.setup(width=600, height=600)

# Register shapes (optional: use custom images)
player_img = "triangle"
enemy_img = "circle"
bullet_img = "square"

# Draw border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.goto(-280, -280)
border.pendown()
for _ in range(4):
    border.forward(560)
    border.left(90)
border.hideturtle()

# Set up score
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.goto(-270, 260)
score_display.hideturtle()
score_display.write(f"Score: {score}", font=("Arial", 14, "normal"))

# Player setup
player = turtle.Turtle()
player.color("blue")
player.shape(player_img)
player.penup()
player.goto(0, -250)
player.setheading(90)  # Point upwards
player_speed = 15

# Bullet setup
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape(bullet_img)
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(stretch_wid=0.2, stretch_len=0.8)
bullet.hideturtle()
bullet_speed = 20
bullet_state = "ready"

# Enemy setup
num_enemies = 5
enemies = []

for _ in range(num_enemies):
    enemy = turtle.Turtle()
    enemy.color("red")
    enemy.shape(enemy_img)
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.goto(x, y)
    enemies.append(enemy)

enemy_speed = 5

# Move player functions
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -270:
        x = -270
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 270:
        x = 270
    player.setx(x)

def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

def is_collision(t1, t2):
    distance = math.hypot(t1.xcor() - t2.xcor(), t1.ycor() - t2.ycor())
    return distance < 20

# Key bindings
win.listen()
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")
win.onkeypress(fire_bullet, "space")

# Main game loop
while True:
    for enemy in enemies:
        # Move enemy
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # Change direction at border
        if x > 270 or x < -270:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemy_speed *= -1
            break

        # Check for collision with bullet
        if is_collision(bullet, enemy):
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.goto(0, -400)
            enemy.goto(random.randint(-200, 200), random.randint(100, 250))
            score += 10
            score_display.clear()
            score_display.write(f"Score: {score}", font=("Arial", 14, "normal"))

        # Check for collision with player
        if is_collision(enemy, player):
            player.hideturtle()
            enemy.hideturtle()
            score_display.goto(0, 0)
            score_display.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
            time.sleep(3)
            win.bye()

    # Move bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

        # Bullet reset if it goes off screen
        if y > 275:
            bullet.hideturtle()
            bullet_state = "ready"

    win.update()
