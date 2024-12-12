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
s1 = codesters.Sprite("alex", 100, 100)
s1.set_size(0.24)
s2 = codesters.Sprite("Seba", -100, 100)
s2.set_size(0.26)
s3 = codesters.Sprite("Sebmom", -100, -90)
s3.set_size(0.3)
s4 = codesters.Sprite("andy", 100, -90)
s4.set_size(0.5)
message1 = codesters.Text("ILL REMEMBER THIS DAY",-100,150,"red")
message2 = codesters.Text("THE BALL IS COMING TO YOU!",60,-30,"red")