
def read_file(filename):
    """
    Read and return the contents of a file.

    Para:
        filename (str): The name of the file to be read.

    Returns:
        str: The contents of the file.
    """
    with open(filename, "r") as f:
        return f.read()
