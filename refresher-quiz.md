### Quiz on Pygame Basics

#### Question 1: Drawing a Rectangle
**Code Snippet:**
```python
pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 50))
```
**Question:** What does this code do? \
a) Draws a blue ellipse on the screen.  
b) Draws a red rectangle on the screen.  
c) Draws a green polygon on the screen.  
d) Draws a white circle on the screen.

#### Question 2: Moving an Object
**Code Snippet:**
```python
rect_x, rect_y = 100, 100

if keys[pygame.K_LEFT]:
    rect_x -= 5
```
**Question:** What happens when the left arrow key is pressed? \
a) The rectangle moves up.  
b) The rectangle moves down.  
c) The rectangle moves to the left.  
d) The rectangle moves to the right.

#### Question 3: Changing Game State
**Code Snippet:**
```python
if event.key == pygame.K_r:
    game_state = "red"
    shape_color = (255, 0, 0)
```
**Question:** What does this code do when the 'r' key is pressed? \
a) Changes the game state to "blue" and makes shapes blue.  
b) Changes the game state to "red" and makes shapes red.  
c) Quits the game.  
d) Moves the rectangle to the right.

#### Question 4: Drawing an Ellipse
**Code Snippet:**
```python
pygame.draw.ellipse(screen, (0, 0, 255), (200, 200, 150, 75))
```
**Question:** What does this code do? \
a) Draws a blue ellipse on the screen.  
b) Draws a green rectangle on the screen.  
c) Draws a red polygon on the screen.  
d) Draws a yellow circle on the screen.

#### Question 5: Displaying Text
**Code Snippet:**
```python
draw_text('Game State: ' + game_state, font, (0, 0, 0), screen, screen_width // 2, 30)
```
**Question:** What does this code do? \
a) Displays the game state as text on the screen.  
b) Changes the game state to "Game State: ".  
c) Draws a black rectangle on the screen.  
d) Moves the rectangle to a new position.
