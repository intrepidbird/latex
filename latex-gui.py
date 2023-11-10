import tkinter as tk
from PIL import ImageTk, Image

def generate_latex_image(latex_input):
    """
    Function to generate a LaTeX image based on user input.

    Parameters:
    - latex_input: str
        The LaTeX code provided by the user.

    Returns:
    - None

    Raises:
    - ValueError:
        Raises an error if the LaTeX code is empty or invalid.
    """

    # Checking if the LaTeX input is empty or invalid
    if not latex_input:
        raise ValueError("LaTeX input cannot be empty.")

    # Creating a tkinter window
    window = tk.Tk()
    window.title("LaTeX Image Generator")

    # Creating a label to display the LaTeX image
    label = tk.Label(window)

    try:
        # Generating the LaTeX image using matplotlib
        import matplotlib.pyplot as plt
        from io import BytesIO

        # Setting up the LaTeX rendering backend
        plt.rcParams["text.usetex"] = True

        # Creating a figure and axis
        fig, ax = plt.subplots()

        # Plotting an empty graph to generate the LaTeX image
        ax.plot([])

        # Rendering the LaTeX code on the graph
        ax.text(0.5, 0.5, f"${latex_input}$", fontsize=16, ha="center", va="center")

        # Saving the figure as a PNG image
        image_buffer = BytesIO()
        plt.savefig(image_buffer, format="png")
        plt.close(fig)

        # Creating a PIL Image object from the buffer
        image_buffer.seek(0)
        image = Image.open(image_buffer)

        # Creating a PhotoImage object from the PIL Image
        photo = ImageTk.PhotoImage(image)

        # Updating the label with the LaTeX image
        label.config(image=photo)
        label.image = photo

    except ImportError:
        # Displaying an error message if matplotlib is not installed
        label.config(text="Error: Matplotlib is not installed.")
    
    except Exception as e:
        # Displaying an error message if there is an exception during LaTeX rendering
        label.config(text=f"Error: {str(e)}")

    # Packing the label into the window
    label.pack()

    # Running the tkinter event loop
    window.mainloop()

# Example usage of the generate_latex_image function:

# Prompting the user for LaTeX input
latex_input = input("Enter LaTeX code: ")

try:
    # Generating the LaTeX image
    generate_latex_image(latex_input)
except ValueError as e:
    print(f"Error: {str(e)}")
