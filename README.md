# CS Hackathon 2022

## Academics Round

### Concept
In this round, you'll be working in your groups to create some form of art using python turtle.
You'll only have 30 minutes to create your deliverable.  Aim for a concept, or showcase.
The 5 teams with the most promising showcases will be given a week to finalise their result.

### Deliverables
- A readme file named groupname.md, containing
	- Your group name
	- a list of your usernames (ab123)
	- a few words describing your concept
- A python script named groupname.py
	- Using python.turtle to produce some result
- A png file name groupname.png
	- you can use https://convertio.co/ps-png/ to convert your groupname.ps file to png

### Delivery
- Submit a pull request with all your files in a subfolder called YourGroupName
To do this:
- Put all three files in a folder called YourGroupName
- Fork this repo
- Click "add files" in the web interface
- Drag the folder onto the interface
- Provide a commit message
- Make a pull request to this repository

### You can go about this in different ways:
- Using loops and maths to produce interesting paths
- Using discrete instrcutions to create shapes
- Using fonts to include text or glyphs
- Other creative uses of the turtle library
- Any combination of the above

### Here's a few hints and suggestions:
- You can be creative with more than paths. Fill color, stroke color, stroke width are all parameters you can play with during the turtle's travel
- Using variables for different components of your code will help you make tweaks faster.
- You can experiement with different things in smaller groups, and bring them together
- Your output could be repeatable or randomised, your choice.
- By default, the turtle moves slowly. Make it fast for testing, slow for debugging.
- If your design is intricate, you can specify when you want the canvas to update for MUCH faster generation.
- You can have a look at turtle art online, but you're very short on time, start tinkering quickly.

### A few bits of code and syntax to help you get started
- `turtle.left(X)` and `turtle.right(X)`. Change the heading of the turtle by X degrees
- `turtle.color(stroke_color, fill_color)` Set the colors of your drawings
- Colors can be names `"white"`,` "blue"`... or rgb values `(255, 255, 255)`,` (0, 0, 255)`...
- `turtle.up()` and `turtle.down()` to stop drawing as you move, or resume drawing as you move
- `turtle.forward(length)` to move straight.
- `turtle.position()` to get the turtle's coordinates. is an array : `[x,y]`
- https://holypython.com/python-turtle-tutorial/turtle-positioning-goto-setpos-setx-sety-setheading/ has some more means of moving your turtle.
- `turtle.speed(X)`, 0-10, 0 fastest, 10 slowest. Save precious time only running slow if you need to.
- You can set `turtle.tracer(0, 0)`, and use `turtle.update()` in key places to dramatically reduce render time
