import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
from turtle import TurtleScreen, RawTurtle
import turtle
import random


def draw_flower():
    # Create a new window for the turtle
    flower_window = tk.Toplevel(root)
    flower_window.title("Dhruv and Ishika")

    # Embed Turtle inside the Tkinter window
    canvas = tk.Canvas(flower_window, width=1200, height=500)
    canvas.pack()

    # Create a turtle screen inside the canvas
    turtle_screen = TurtleScreen(canvas)
    turtle_screen.bgcolor("skyblue")  # Change background to sky blue

    # Create a RawTurtle instance
    my_turtle = RawTurtle(turtle_screen)
    my_turtle.shape("turtle")
    my_turtle.speed(0)  # Fastest speed

    # Function to draw a petal
    def draw_petal(size):
        my_turtle.circle(size, 60)  # Draw part of a circle for one side of the petal
        my_turtle.left(120)         # Turn left to form the petal shape
        my_turtle.circle(size, 60)  # Draw the other side
        my_turtle.left(120)         # Reset direction

    # Function to draw a stem
    def draw_stem():
        my_turtle.color("green")
        my_turtle.setheading(-90)   # Face downwards for the stem
        my_turtle.forward(150)      # Draw the stem
        my_turtle.backward(150)     # Reset turtle position
        my_turtle.setheading(0)     # Reset direction

    # Function to draw the center of the flower
    def draw_center():
        my_turtle.color("yellow")
        my_turtle.begin_fill()
        my_turtle.circle(10)  # Draw a small yellow circle in the center
        my_turtle.end_fill()

    # Function to draw a full flower
    def draw_flower_at(x, y):
        my_turtle.penup()
        my_turtle.goto(x, y)
        my_turtle.pendown()

        # Draw the stem first
        draw_stem()

        # Draw 30 petals of varying sizes
        my_turtle.color("white")
        for _ in range(30):
            draw_petal(random.randint(40, 70))  # Petal size will vary between 40 and 70 units
            my_turtle.left(360 / 30)  # Space petals evenly

        # Draw the yellow center
        draw_center()

    # Draw multiple flowers in different positions
    positions = [(-100, 0), (100, 100), (-150, -150), (50, -100), (0, 150)]

    for pos in positions:
        draw_flower_at(pos[0], pos[1])

    my_turtle.penup()
    my_turtle.goto(0, -200)  # Position the text below the flowers
    my_turtle.pendown()
    my_turtle.color("black")
    my_turtle.write("It's us. Dhruv and Ishika. Can't let go of you this easily. I like you and I'll always do.", align="center", font=("Arial", 18, "bold"))

    # Hide the turtle once the drawing is complete
    my_turtle.hideturtle()
def open_last_window():
    last_window = tk.Toplevel(root)
    last_window.geometry("600x150")
    last_window.title("Last Window")

    # Add a label in the second window
    label = tk.Label(last_window, text="Thanks for having  me till the end. Kindly Don't forget the options you clicked today. Consider them.", font=("Arial", 10))
    label.pack(pady=20)

    # Function for the second button in the new window
    def last_button_click():
        draw_flower()  # Open the third window

    # Add a button in the second window
    button_in_new_window = tk.Button(last_window, text="Click Me", command=last_button_click)
    button_in_new_window.pack(pady=10)

def open_fifth_window():
    fifth_window = tk.Toplevel(root)
    fifth_window.geometry("800x700")
    fifth_window.title("Fifth Window")

    # Add a label in the fifth window
    label = tk.Label(fifth_window, text=" Since you agreed with me, (which you should)", font=("Arial", 12))
    label.pack(pady=20)
    label = tk.Label(fifth_window, text="I can generate a picture of you depending on how you are feeling right now. So, how are you feeling right now Dhruv? ", font=("Arial", 12))
    label.pack(pady=20)

    img_label=None
    text_label=None
    

    def button_click(name):
        if name == "Happy":
            display_image("https://media.istockphoto.com/id/511375254/photo/dog-having-a-big-smile.jpg?s=612x612&w=0&k=20&c=dXmUrYXGEoZmaBqJ2md7WAVCJGWO5UiD5plNs1bDfcM=", "Well, try to be happy more. Around everyone else and I will try to make you happy around me. You can trust me on this ")
        elif name =="Sexy":
            display_image("https://i.pinimg.com/originals/06/1d/a0/061da038843ba200427d2a52c2cd021a.jpg", "I really want one picture of you like this")
        elif name=="Sad":
            display_image("https://cdn.quotesgram.com/img/82/66/1301852227-Boo-The-Dog-sad.jpg", "I didn't knew I was such a good artist. The eyes. It's so you")
        elif name=="Cute":
            display_image("https://c4.wallpaperflare.com/wallpaper/737/192/969/animal-cute-dog-puppy-wallpaper-preview.jpg", "The small one is me, I know I am cute")
        elif name=="Angry":
            display_image("https://www.usatoday.com/gcdn/-mm-/d22797dd5b2058d5bf8c19a1eae7510d58536ed0/c=0-0-1024-768/local/-/media/2018/05/14/USATODAY/usatsports/wp-USAT-allthemoms-front1-18809-angrydogx.jpg", "This is definetely you!!")
        elif name=="Cozy":
            display_image("https://t3.ftcdn.net/jpg/04/92/56/36/360_F_492563617_Kh31s1XYeHGb6Ff65DXfEpol23Su60ad.jpg", "The other one is me BTW ;)")


 # Function to display the image in the window
    def display_image(url,text):
        nonlocal img_label, text_label  # To update the existing image label
        response = requests.get(url)
        
        if response.status_code == 200:  # Ensure the request was successful
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            img = img.resize((300, 300))  # Resize image to fit the window
            img_tk = ImageTk.PhotoImage(img)

            # If there's already an image, remove it first
            if img_label:
                img_label.destroy()
            if text_label:
                text_label.destroy()

            # Display the new image
            img_label = tk.Label(fifth_window, image=img_tk)
            img_label.image = img_tk  # Keep a reference to avoid garbage collection
            img_label.pack(pady=20)

            text_label = tk.Label(fifth_window, text=text, font=("Arial", 20))
            text_label.pack(pady=10)
        else:
            print("Failed to retrieve the image. Status code:", response.status_code)


    # Button names list
    button_names = ["Happy", "Sad", "Cute", "Angry", "Sexy", "Cozy"]

    # Frame to hold the buttons (optional for better layout control)
    button_frame = tk.Frame(fifth_window)
    button_frame.pack(pady=20)

    # Generate buttons with different names
    for name in button_names:
        button = tk.Button(button_frame, text=name, command=lambda name=name: button_click(name))
        button.pack(side=tk.LEFT, padx=10)

    def next_button_click():
        open_last_window()
    button_frame = tk.Frame(fifth_window)
    button_frame.pack(pady=10)

    # Add a button in the second window
    button_in_reply_window = tk.Button(button_frame, text="Next ", command=next_button_click)
    button_in_reply_window.grid(row=0, column=0, padx=10)

def open_reply_window():
    reply_window = tk.Toplevel(root)
    reply_window.geometry("400x250")
    reply_window.title("Third Window")

    # Add a label in the third window
    label = tk.Label(reply_window, text="You are not lying. are you?", font=("Arial", 12))
    label.pack(pady=20)
    label = tk.Label(reply_window, text="Can i believe you this time?", font=("Arial", 12))
    label.pack(pady=20)

    def reply_button_click():
        open_fifth_window()  # Open the third window
    def show_error_message():
        messagebox.showerror("Error", "This option is not available!")

    button_frame = tk.Frame(reply_window)
    button_frame.pack(pady=10)

    # Add a button in the second window
    button_in_reply_window = tk.Button(button_frame, text="ofc Not ", command=show_error_message)
    button_in_reply_window.grid(row=0, column=0, padx=10)

    button_in_reply_window_2 = tk.Button(button_frame, text="Ofc Ishika. I will", command=reply_button_click)
    button_in_reply_window_2.grid(row=0, column=1, padx=10)
def open_fourth_window():
    fourth_window = tk.Toplevel(root)
    fourth_window.geometry("400x250")
    fourth_window.title("Fourth Window")

    # Add a label in the third window
    label = tk.Label(fourth_window, text="Will you reply to me texts, Bhargav?", font=("Arial", 12))
    label.pack(pady=20)

    def fourth_button_click():
        open_reply_window()  # Open the third window

    def show_error_message():
        messagebox.showerror("Error", "This option is not available!")

   
    button_frame = tk.Frame(fourth_window)
    button_frame.pack(pady=10)

    # Add a button in the second window
    button_in_third_window = tk.Button(button_frame, text="Sochunga", command=show_error_message)
    button_in_third_window.grid(row=0, column=0, padx=10, pady=10)

    button_in_fourth_window_2 = tk.Button(button_frame, text="Dekhte h", command=show_error_message)
    button_in_fourth_window_2.grid(row=0, column=1, padx=10, pady=10)

    button_in_fourth_window_3 = tk.Button(button_frame, text="Saaf saaf na", command=show_error_message)
    button_in_fourth_window_3.grid(row=1, column=0, padx=10, pady=20)
    button_in_fourth_window_4 = tk.Button(button_frame, text="Okay Ishika.Jesa tu bole", command=fourth_button_click)
    button_in_fourth_window_4.grid(row=1, column=1, padx=10, pady=20)

# Function to create the third window


def open_third_window():
    third_window = tk.Toplevel(root)
    third_window.geometry("400x250")
    third_window.title("Third Window")

    # Add a label in the third window
    label = tk.Label(third_window, text="You have to wait a little ig. !", font=("Arial", 12))
    label.pack(pady=20)
    label = tk.Label(third_window, text="Lemme ask you some questions till then!", font=("Arial", 12))
    label.pack(pady=20)

    def third_button_click():
        open_fourth_window()  # Open the third window

    button_frame = tk.Frame(third_window)
    button_frame.pack(pady=10)

    # Add a button in the second window
    button_in_third_window = tk.Button(button_frame, text="Okay", command=third_button_click)
    button_in_third_window.grid(row=0, column=0, padx=10)

    button_in_third_window_2 = tk.Button(button_frame, text="Sure", command=third_button_click)
    button_in_third_window_2.grid(row=0, column=1, padx=10)

# Function to create the second window
def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.geometry("400x150")
    new_window.title("Second Window")

    # Add a label in the second window
    label = tk.Label(new_window, text="There is a little surprise for you.", font=("Arial", 14))
    label.pack(pady=20)

    # Function for the second button in the new window
    def second_button_click():
        open_third_window()  # Open the third window

    # Add a button in the second window
    button_in_new_window = tk.Button(new_window, text="Click Me", command=second_button_click)
    button_in_new_window.pack(pady=10)

# Create the main window
root = tk.Tk()
root.geometry("300x200")
root.title("Main Window")

# Add a label in the main window
label = tk.Label(root, text="Hi, Dhruv.", font=("Arial", 20))
label.pack(pady=20)

# Add a button in the main window to open a new window
button = tk.Button(root, text="Click Me", command=open_new_window)
button.pack(pady=20)

# Start the main event loop
root.mainloop()
