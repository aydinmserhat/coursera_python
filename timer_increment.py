## timer-increment simple program

# SimpleGUI program template

# Import the module
import simplegui

# Define global variables (program state)
counter = 0 

# Define "helper" functions

def increment():
    global counter
    counter = counter + 1
    
def decrease() :
    global counter
    counter = counter - 1    

# Define event handler functions

def tick():
    increment()
    print counter

def restarting() : 
    global counter
    counter = 0
    
def back() :
    decrease()
    print counter
    
# Create a frame

frame=simplegui.create_frame('SIMPLEGUI TEST!!', 200, 200)


# Register event handlers

timer = simplegui.create_timer(1000, tick)

frame.add_button('0. START!!', timer.start)
frame.add_button('1. Click me', tick)
frame.add_button('2. Restart', restarting)
frame.add_button('3. Back', decrease)


# Start frame and timers
frame.start()

