def write_file(file_name, file_content):
    """
    Write content to a file

    Args:
    file_name (str): The name of the file.
    file_content (str): The content that will be written in the file.   

    """
    try:
        with open(file_name, 'w') as f:
            f.write(file_content)
        print(f"Content successfully written to {file_name}")
    except Exception as e:
        print(f"Error writing to {file_name}: {e}")

def append_file(file_name, append_content):
    """
    Append content to an existing file or create it if not exists

    Args:
    file_name (str): The name of the file.
    append_content (str): The content that will be appended to the file.

    """
    try:
        with open(file_name, 'a') as file:
            file.write(file_content)
            print(f"{append_content} was added to {file_name}")
    except FileNotFoundError:
        with open(file_name, 'a') as file:
            file.write(file_content + '\n' + append_content)
            print(f"{append_content} was added to {file_name}")
    except Exception as e:
            print(f"Error appending to {file_name}: {e}")
            


def read_file(file_name):
    """
    Read content from a .txt file.

    Args:
        file_name (str): The name or path of the .txt file.

    Returns:
        str: The content of the .txt file.
    """
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return None
    except Exception as e:
        print(f"Error reading from {file_name}: {e}")
        return None
