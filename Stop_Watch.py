# define global variables

import simplegui

time = 0
message = ""
attempts = 0
success = 0

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D

def format(t):
    global message
    D = t % 10
    C = t / 10
    B = int ( C / 60 )
    A = int ( C % 60 )
    if A < 10:
        A = "0" + str(A)
        message = str(B) + ":" + A + "." + str(D)
    else :
        message = str(B) + ":" + str(A) + "." + str(D)

     
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    timer.stop()
    global attempts
    global success
    global label
    if time % 50 == 0: # success increases at every 5 seconds
        success = success + 1
    if time == 0:
        attempt = 0 
    else:
        attempts = attempts + 1
    label.set_text ("Successful/Total Attempts=" + str(success)+"/"+str(attempts))

def reset():
    global time
    global started
    global attempts
    global success
    attempts = 0
    success = 0
    timer.stop()
    time = 0
    format(time)
    label.set_text ("Successful/Total Attempts=" + str(success)+"/"+str(attempts))

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time = time + 1
    format(time)   

#draw canvas
def draw(canvas):
    canvas.draw_text(message, [100,110], 24, "White")

# create frame
frame = simplegui.create_frame("StopWatch-Game", 300, 200)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 150)
frame.add_button("Reset", reset, 100)
label = frame.add_label("Successful/Total Attempts="+str(success)+"/"+str(attempts),300)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)

# start timer and frame
frame.start()
