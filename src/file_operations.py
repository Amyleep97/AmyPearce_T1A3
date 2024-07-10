import json

def load_trivia(file_path):
    """
    Load trivia from a JSON File.

    parameters: file_path: Path to the JSON file
    return: List of questions or an empty list if an error occurs
    """
    try:
        with open(file_path, 'r') as file:
            trivia = json.load(file)
        return trivia
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        return []

def save_trivia(file_path, trivia):
    try:
        with open(file_path, 'w') as file:
            json.dump(trivia, file, indent=4)
        print(f"Trivia successfully saved to {file_path}.")
    except PermissionError:
        print(f"Error: Permission denied to write.")
    except Exception as e:
        print("An unexpected error occured", e)