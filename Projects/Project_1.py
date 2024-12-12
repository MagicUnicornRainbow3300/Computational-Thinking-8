###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background ("winter")
q1 = codesters.Square(100, 100, 200, 'gold') 
q2 = codesters.Square(-100, 100, 200, 'black')
q3 = codesters.Square(-100, -100,200, 'gold')
q4 = codesters.Square(100, -100, 200, 'black')
s1 = codesters.Sprite("Van", 100, 100)
s1.set_size(0.3)
s2 = codesters.Sprite("", -100, 100)
s2.set_size(0.3)
s3 = codesters.Sprite("Brady", -100, -90)
s3.set_size(0.3)
s4 = codesters.Sprite("Me", 100, -90)
s4.set_size(0.3)