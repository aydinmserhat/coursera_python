# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
RIGHT_GUTTER = WIDTH-PAD_WIDTH	
LEFT_GUTTER = PAD_WIDTH	
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table

ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0,0]
paddle1_pos = 150
paddle2_pos = 150
paddle1_vel = 0
paddle2_vel = 0
score1=0
score2=0
direction = 'LEFT'

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos[0] = WIDTH/2
    ball_pos[1] = HEIGHT/2
    if direction == 'RIGHT':
        ball_vel[0] = random.randrange(120, 240)//60
        ball_vel[1] = -1*random.randrange(60, 180)//60
    elif direction == 'LEFT':
        ball_vel[0] = -1*random.randrange(60, 180)//60
        ball_vel[1] = -1*random.randrange(120, 240)//60


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(direction)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, direction
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -1*ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -1*ball_vel[1]
     
    # reflection of ball from paddles
    if ((ball_pos[1] >= paddle2_pos and	
    ball_pos[1] < paddle2_pos+PAD_HEIGHT and
    ball_pos[0] + BALL_RADIUS >= RIGHT_GUTTER)	
    or
    (ball_pos[1] >= paddle1_pos and
    ball_pos[1] < paddle1_pos+PAD_HEIGHT and
    ball_pos[0] - BALL_RADIUS <= LEFT_GUTTER)):
        ball_vel[0] = -1*(ball_vel[0] + ball_vel[0] / 10)
        
    elif ball_pos[0] + BALL_RADIUS >= RIGHT_GUTTER:	
        score1 += 1
        direction = 'LEFT'
        new_game()
    elif ball_pos[0] - BALL_RADIUS <= LEFT_GUTTER:
        score2 += 1
        direction = 'RIGHT'
        new_game() 
      
    # optinal add-ons   
    if score1 == 10 or score2==10:
        new_game()		
        canvas.draw_text('GAME OVER', (225,40), 25,'white') 
    if score1 == 10:
        new_game()
        canvas.draw_text('WINNER', (140,240), 20,'green')
    if score2 == 10:
        canvas.draw_text('WINNER', (360,240), 20,'red')
        
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 5 ,"red", "yellow")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    if paddle1_pos < 0:
        paddle1_pos = 0
    if paddle1_pos > HEIGHT - PAD_HEIGHT:
        paddle1_pos = HEIGHT - PAD_HEIGHT
    if paddle2_pos < 0:
        paddle2_pos = 0
    if paddle2_pos > HEIGHT - PAD_HEIGHT:
        paddle2_pos = HEIGHT - PAD_HEIGHT
        
        
    
    # draw paddles
      ## left paddle
    canvas.draw_polygon([(0,paddle1_pos),(LEFT_GUTTER,paddle1_pos),(LEFT_GUTTER,paddle1_pos+PAD_HEIGHT),
    (0, paddle1_pos+PAD_HEIGHT)],1,'white','white')
    
      ## right poddle
    canvas.draw_polygon([(WIDTH, paddle2_pos),(RIGHT_GUTTER, paddle2_pos),(RIGHT_GUTTER, paddle2_pos+PAD_HEIGHT),(WIDTH, paddle2_pos+PAD_HEIGHT)], 1, "white", "white")
    
    
    # draw scores
    canvas.draw_text('%d' % (score1),(250,390),30,'green')
    canvas.draw_text('%d' % (score2),(330,390),30,'red')
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 5
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = acc
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -acc
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = acc
    if key== simplegui.KEY_MAP['w']:
        paddle1_vel = -acc
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0

def restart():
    global score1, score2, ball_pos
    score1 = score2 = 0
    new_game()
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('RESTART' , restart, 150)


# start frame
new_game()
frame.start()
