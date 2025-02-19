### section 1
import codesters, random
from codesters import StageClass
stage = StageClass()
stage.disable_floor()
stage.set_background("moon")
s1 = codesters.Sprite("Seba", 0, -200)
s1.set_size(0.5)


## section 2 objects
object_speed = 5  
lives = 7  

def falling_object():
    global object_speed, lives

    if lives > 0:
       
        x_position = random.randint(-250, 250)
        object = codesters.Sprite("Van", x_position, 275)
        object.set_size(0.2)
        object.set_y_speed(object_speed)
        object_speed += 0.1

        
        stage.event_interval(falling_object, 0.5)

# section 3 collision
def collision(s1, object):
    global lives
    if object.get_image_name() == "Van": 
        stage.remove_sprite(object)
        lives -= 1
        if lives == 0:
            s1.say("Out of lives - you lose!",0.8, color="white")
        else:
            s1.say(f"{lives} lives", 0.8, color="white")


s1.event_collision(collision)


falling_object()

# Section 4 - Controls

# Move right when the right arrow key is pressed
def go_right():
    s1.move_right(10)

s1.event_key("right", go_right)

# Move left when the left arrow key is pressed
def go_left():
    s1.move_left(10)

s1.event_key("left", go_left)
