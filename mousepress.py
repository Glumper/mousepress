import arcade
from random import randint
WIDTH = 800
HEIGHT = 600
radius = 25
window = arcade.Window(WIDTH, HEIGHT, "My Arcade Game")
arcade.set_background_color(arcade.color.AMAZON)

# Initialize your variables here
circle_x = WIDTH/3
circle_y = HEIGHT/3
circle_r = radius
circleclicks = 0
color = (randint(0, 255), randint(0, 255), randint(0, 255))
@window.event("on_draw")
def game_loop():
    # import global variables here.
    global circle_x, circle_y, circle_r, circleclicks, color

    # update your variables here.

    # Draw things here.
    arcade.start_render()
    arcade.draw_circle_filled(circle_x, circle_y, circle_r, color)
@window.event
def on_mouse_press(mouse_x, mouse_y, button, modifiers):
    global circle_r, circle_x, circle_y, circleclicks, color
    print('click!')
    print('x = {}, y = {}'.format(mouse_x, mouse_y))
    if (mouse_x-circle_x)**2 + (mouse_y-circle_y)**2 <= (circle_r)**2:
        circle_r = circle_r + 10
        circle_x = randint(0, 800)
        circle_y = randint(0, 600)   
        circleclicks = circleclicks + 1
        print("amount of circleclicks:{} ".format(circleclicks))
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
arcade.run()
