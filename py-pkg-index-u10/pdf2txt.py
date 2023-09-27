""" This module provides functions to convert a PDF to text.""" 

class Converter():
    """This class is used to define the PDF file to convert."""

    def text_upload(text):
        """
        This method upload the text to a repo
        
        Parameters:
        text (str): Text to be uploaded it
        
        Returns:
        done (boolean): Indicates if the text was uploaded
        """

        print("The text was uploaded")

        return True

def convert(path:str):
    """
    Convert the given PDF to text.

    Parameters:
    path (str): The Path to a PDF file.

    Returns:
    str: The content of the PDF file as text.
    """
    print("pdf2text")