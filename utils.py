import os

def adjust_path_for_os(image_path):
    # Check the current operating system
    current_os = os.name
    
    if current_os == 'nt':  # Windows
        # Convert the path to use backslashes for Windows
        adjusted_path = image_path.replace('/', '\\')
    else:  # Unix-based (Linux, macOS)
        # Ensure the path uses forward slashes for Unix-based OS
        adjusted_path = image_path.replace('\\', '/')
    
    return adjusted_path
