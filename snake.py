import tkinter as tk
import random

WIDTH = 500
HEIGHT = 500
CELL = 20

window = tk.Tk()
window.title("Snake Game")

score = 0
game_running = True

label = tk.Label(window, text="Score: 0", font=("Arial", 14))
label.pack()

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

snake = [(100, 100), (80, 100), (60, 100)]
direction = "Right"


def new_food():
    while True:
        x = random.randint(0, (WIDTH // CELL) - 1) * CELL
        y = random.randint(0, (HEIGHT // CELL) - 1) * CELL
        if (x, y) not in snake:
            return (x, y)


food = new_food()


def draw():
    canvas.delete("all")

    # อาหาร
    canvas.create_oval(
        food[0],
        food[1],
        food[0] + CELL,
        food[1] + CELL,
        fill="red",
        outline="red",
    )

    # งู
    for i, (x, y) in enumerate(snake):
        color = "green" if i == 0 else "lime"
        canvas.create_rectangle(
            x,
            y,
            x + CELL,
            y + CELL,
            fill=color,
            outline="black",
        )


def move():
    global food, score, game_running

    if not game_running:
        return

    head_x, head_y = snake[0]

    if direction == "Up":
        head_y -= CELL
    elif direction == "Down":
        head_y += CELL
    elif direction == "Left":
        head_x -= CELL
    elif direction == "Right":
        head_x += CELL

    new_head = (head_x, head_y)

    # ชนกำแพงหรือชนตัวเอง
    if (
        head_x < 0
        or head_x >= WIDTH
        or head_y < 0
        or head_y >= HEIGHT
        or new_head in snake
    ):
        game_over()
        return

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        label.config(text=f"Score: {score}")
        food = new_food()
    else:
        snake.pop()

    draw()
    window.after(120, move)


def game_over():
    global game_running

    game_running = False

    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2 - 30,
        text="GAME OVER",
        fill="white",
        font=("Arial", 28, "bold"),
    )

    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2 + 20,
        text=f"Score : {score}\n\nPress SPACE to Restart",
        fill="yellow",
        font=("Arial", 16),
        justify="center",
    )


def restart():
    global snake, direction, food, score, game_running

    snake = [(100, 100), (80, 100), (60, 100)]
    direction = "Right"

    score = 0
    label.config(text="Score: 0")

    food = new_food()

    game_running = True

    draw()
    move()


def change_direction(event):
    global direction

    # กด Space เพื่อเริ่มใหม่
    if not game_running:
        if event.keysym == "space":
            restart()
        return

    key = event.keysym

    if key == "Up" and direction != "Down":
        direction = "Up"
    elif key == "Down" and direction != "Up":
        direction = "Down"
    elif key == "Left" and direction != "Right":
        direction = "Left"
    elif key == "Right" and direction != "Left":
        direction = "Right"


window.bind("<Key>", change_direction)

draw()
move()

window.mainloop()