import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Christmas Tree Canvas")

# Create a canvas with specified dimensions and background color
canvas = tk.Canvas(root, width=400, height=400, bg='white', borderwidth=2)
canvas.pack()

# Draw the tree (triangle) list goes x0,y0,x1,y1,x2,y2 drawing the vertexes
canvas.create_polygon(200,
                      150,
                      300,
                      300,
                      100,
                      300,
                      outline='black', fill='green', width=2)

canvas.create_polygon(200,  # x0
                      100,  # y0
                      290,  # x1
                      225,  # y1
                      110,  # x2
                      225,  # y2
                      outline='black', fill='green', width=2)


canvas.create_polygon(200,
                      100,
                      275,
                      175,
                      125,
                      175,
                      outline='black', fill='green', width=2)

canvas.create_polygon(200,  # x0
                      50,  # y0
                      250,  # x1
                      150,  # y1
                      150,  # x2
                      150,  # y2
                      outline='black', fill='green', width=2)

# star piece 1
canvas.create_polygon(200,  # x0
                      50,  # y0
                      205,  # x1
                      40,  # y1
                      195,  # x2
                      40,  # y2
                      outline='yellow', fill='yellow', width=2)
# star piece 2
canvas.create_polygon(200,  # x0
                      35,  # y0
                      205,  # x1
                      45,  # y1
                      195,  # x2
                      45,  # y2
                      outline='yellow', fill='yellow', width=2)


# Draw the trunk (rectangle) x1,y1,x2,y2
canvas.create_rectangle(
    160, 300, 240, 350, outline='black', fill='brown', width=2)

# Draw ornaments (circles)
canvas.create_oval(200, 120, 190, 130, outline='red', fill='red', width=2)
canvas.create_oval(240, 160, 230, 170, outline='blue', fill='blue', width=2)
canvas.create_oval(150, 220, 160, 230, outline='yellow',
                   fill='yellow', width=2)

# Add text
canvas.create_text(200, 380, text="Merry Christmas!",
                   font=('Comic Sans MS', 20), fill='black')

# Start the Tkinter event loop
root.mainloop()
