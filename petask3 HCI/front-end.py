from tkinter import *
from PIL import Image, ImageTk
import customtkinter

# Create the main window
window = customtkinter.CTk()
customtkinter.set_appearance_mode("Dark")
window.title("Metflix")
window.geometry('800x400')

# Function to handle button clicks
def clicker(option):
    print(f"{option} clicked")

    # Clear any existing content frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Create a new frame for the selected option
    selected_frame = customtkinter.CTkFrame(content_frame, fg_color="darkgrey")
    selected_frame.pack(fill='both', expand=True, padx=20, pady=20)

    # Add a header for the selected option
    header = customtkinter.CTkLabel(selected_frame, text=f"{option} Section", text_color="white", font=("Arial", 20))
    header.pack(pady=10)

    # Add different functionalities based on the option
    if option == "Homepage":
        # Example content for Homepage
        home_label = customtkinter.CTkLabel(selected_frame, text="Welcome to the Homepage!", text_color="white")
        home_label.pack(pady=10)
        
        # Add a button for Homepage functionality
        homepage_button = customtkinter.CTkButton(selected_frame, text="Go to Dashboard", command=lambda: print("Dashboard opened"))
        homepage_button.pack(pady=5)

    elif option == "Trending":
        # Example content for Trending
        trending_label = customtkinter.CTkLabel(selected_frame, text="Trending Movies/Shows", text_color="white")
        trending_label.pack(pady=10)
        
        # Add a button for Trending functionality
        trending_button = customtkinter.CTkButton(selected_frame, text="View Trending", command=lambda: print("Trending shows viewed"))
        trending_button.pack(pady=5)

    elif option == "Favorites":
        # Example content for Favorites
        favorites_label = customtkinter.CTkLabel(selected_frame, text="Your Favorite Movies/Shows", text_color="white")
        favorites_label.pack(pady=10)

        # Add a button for Favorites functionality
        favorites_button = customtkinter.CTkButton(selected_frame, text="Manage Favorites", command=lambda: print("Favorites managed"))
        favorites_button.pack(pady=5)

# Create a frame for the buttons on the left side
button_frame = customtkinter.CTkFrame(window, fg_color="transparent")
button_frame.pack(side='left', pady=10, padx=10)  # Pack frame to the left

# Create a content frame to hold dynamic content
content_frame = customtkinter.CTkFrame(window, fg_color="transparent")
content_frame.pack(side='right', fill='both', expand=True)  # Pack frame to the right

# Define the options and their corresponding image paths
options = {
    "Homepage": "home.png",  # Replace with your image path
    "Trending": "movie.png",  # Replace with your image path
    "Favorites": "bookmark.png"  # Replace with your image path
}

# Resize dimensions for the images
resize_size = (60, 60)  # Width, Height

# Create buttons with images
for option, image_path in options.items():
    # Load and resize the image
    original_image = Image.open(image_path)
    resized_image = original_image.resize(resize_size, Image.LANCZOS)
    tk_image = ImageTk.PhotoImage(resized_image)

    # Create a button with the image
    button = customtkinter.CTkButton(
        button_frame,
        image=tk_image,
        text="",  # Set text to empty to avoid showing text beside the icon
        command=lambda opt=option: clicker(opt),  # Pass option to the clicker
        width=50,  # Set button width
        height=50,  # Set button height
        fg_color=button_frame.cget("fg_color")
    )

    # Store a reference to the image to prevent garbage collection
    button.image = tk_image  
    button.pack(side='top', anchor='w', pady=15)  # Align buttons to the top left

# Start the main loop
window.mainloop()
