import codesters
from codesters import StageClass
stage = StageClass()


stage.set_background("moon")
s1 = codesters.Sprite ("person1", 0 ,-200)
s1.set_size(0.5)


def move_up(sprite):
    sprite.move_up(10)

def move_down(sprite):
    sprite.move_down(10)

def move_left(sprite):
    sprite.move_left(10)

def move_right(sprite):
    sprite.move_right(10)

def show(sprite):
    sprite.show()

def turn_left(sprite):
    heading = sprite.heading
    sprite.set_heading(heading + 1)

def turn_right(sprite):
    heading = sprite.heading
    sprite.set_heading(heading - 1)

def forwrd(sprite):
    sprite.forward(1)

def hide(sprite):
    sprite.hide()



s1.event_key("up", move_up)
s1.event_key("down",move_down)
s1.event_key("left",move_left)
s1.event_key("right",move_right)

s1.event_key("h", hide)
s1.event_key("g",show)


print("game has started. Open the screen using PORTS to play")