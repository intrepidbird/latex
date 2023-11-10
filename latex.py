import subprocess

def generate_latex_image(latex_code: str, output_file: str):
    """
    Generates a LaTeX image based on the user inputted LaTeX code.

    Parameters:
    - latex_code: str
        The LaTeX code provided by the user.
    - output_file: str
        The name of the output file where the generated image will be saved.

    Raises:
    - ValueError:
        Raises an error if the LaTeX code is empty or if the output file name is not provided.

    Returns:
    - str:
        Returns the path of the generated image file.
    """

    # Checking if the LaTeX code is empty
    if not latex_code:
        raise ValueError("LaTeX code cannot be empty.")

    # Checking if the output file name is provided
    if not output_file:
        raise ValueError("Output file name is required.")

    # Creating a temporary LaTeX file
    temp_file = "temp.tex"

    # Writing the LaTeX code to the temporary file
    with open(temp_file, "w") as file:
        file.write(latex_code)

    # Generating the image using pdflatex command
    subprocess.run(["pdflatex", "-halt-on-error", "-output-directory", ".", temp_file])

    # Converting the generated PDF to an image using pdftoppm command
    subprocess.run(["pdftoppm", "-png", "-r", "300", f"{temp_file[:-4]}.pdf", output_file])

    # Removing the temporary LaTeX and PDF files
    subprocess.run(["rm", temp_file])
    subprocess.run(["rm", f"{temp_file[:-4]}.pdf"])

    return output_file

# Example usage of the generate_latex_image function:

# Example 1: Generating an image from LaTeX code
latex_code = r"""
\documentclass{article}
\begin{document}
Hello, \LaTeX!
\end{document}
"""
output_file = "latex_image.png"
image_path = generate_latex_image(latex_code, output_file)
print(f"Image generated and saved at: {image_path}")

# Example 2: Empty LaTeX code (should raise an error)
try:
    empty_latex_code = ""
    output_file = "empty_latex_image.png"
    image_path = generate_latex_image(empty_latex_code, output_file)
    print(f"Image generated and saved at: {image_path}")
except ValueError as e:
    print(f"Error generating LaTeX image: {e}")

# Example 3: Missing output file name (should raise an error)
try:
    latex_code = r"""
    \documentclass{article}
    \begin{document}
    Hello, \LaTeX!
    \end{document}
    """
    missing_output_file = ""
    image_path = generate_latex_image(latex_code, missing_output_file)
    print(f"Image generated and saved at: {image_path}")
except ValueError as e:
    print(f"Error generating LaTeX image: {e}")
