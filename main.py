import os
import yaml
import shutil

def create_structure(base_path, structure, asset_dir):
    """
    Recursively create directories and files based on the provided structure.
    
    :param base_path: The root path to create the structure.
    :param structure: A dictionary representing the folder structure.
    :param asset_dir: Path to the main asset directory containing media and markdown subdirectories.
    """
    media_dir = os.path.join(asset_dir, 'media')  # Subdirectory for images and PDFs
    markdown_dir = os.path.join(asset_dir, 'markdown')  # Subdirectory for markdown files
    error_markdown_path = os.path.join(markdown_dir, 'error.md')  # Placeholder markdown file in media

    for key, value in structure.items():
        current_path = os.path.join(base_path, key)
        
        # Case where key is a directory (value is a dict) and value is a structure (sub-dictionary)
        if isinstance(value, dict):
            if not os.path.exists(current_path):
                os.makedirs(current_path, exist_ok=True)
                print(f"Created directory: {current_path}")
            create_structure(current_path, value, asset_dir)
        
        # Case for media files like PNG, PDF, ZIP
        elif isinstance(value, list) and (key.endswith('.png') or key.endswith('.pdf') or key.endswith('.zip')):
            asset_file_path = os.path.join(media_dir, key)
            if os.path.exists(asset_file_path):
                shutil.copy(asset_file_path, current_path)
                print(f"Copied {key} from media to {current_path}")
            else:
                print(f"WARNING: {key} not found in {media_dir}, creating empty file at {current_path}")
                open(current_path, 'w').close()

        # Case for markdown files
        elif isinstance(value, list) and key.endswith('.md'):
            markdown_filename = value[0] + '.md'
            markdown_file_path = os.path.join(markdown_dir, markdown_filename)
            if os.path.exists(markdown_file_path):
                # Copy the content of the markdown file from the markdown directory
                with open(markdown_file_path, 'r') as md_file:
                    content = md_file.read()
                with open(current_path, 'w') as md_file:
                    md_file.write(content)
                print(f"Copied content from {markdown_filename} to {current_path}")
            else:
                # If markdown file is not found, use error.md from the media directory
                if os.path.exists(error_markdown_path):
                    shutil.copy(error_markdown_path, current_path)
                    print(f"WARNING: Markdown file {markdown_filename} not found, using error.md as placeholder in {current_path}")
                else:
                    print(f"ERROR: Neither markdown file {markdown_filename} nor error.md found. Creating empty file at {current_path}")
                    open(current_path, 'w').close()

        # Case for other types of files (non-asset files like .yaml, .html, etc.)
        elif isinstance(value, list):
            open(current_path, 'w').close()
            print(f"Created empty file: {current_path}")

def load_yaml_structure(yaml_file):
    """
    Load the directory structure from a YAML file.
    
    :param yaml_file: Path to the YAML file.
    :return: The directory structure.
    """
    print(f"Loading YAML file: {yaml_file}")
    with open(yaml_file, 'r') as file:
        return yaml.safe_load(file)

def main():
    # Load the YAML file containing the structure
    yaml_file = 'filesystem.yaml'  # Path to your YAML file
    try:
        structure = load_yaml_structure(yaml_file)
        print("YAML structure loaded successfully.")
    except Exception as e:
        print(f"Error loading YAML file: {e}")
        return
    
    # Define the asset directory and its subdirectories
    asset_directory = os.path.abspath('assets')  # Main asset directory
    media_directory = os.path.join(asset_directory, 'media')  # Subdirectory for images and PDFs
    markdown_directory = os.path.join(asset_directory, 'markdown')  # Subdirectory for markdown files
    
    # Check if asset subdirectories exist
    if not os.path.exists(media_directory):
        print(f"Media directory {media_directory} does not exist.")
        return
    
    if not os.path.exists(markdown_directory):
        print(f"Markdown directory {markdown_directory} does not exist.")
        return
    
    print(f"Using media directory: {media_directory}")
    print(f"Using markdown directory: {markdown_directory}")
    
    # Set the base directory for the generated file system
    base_directory = os.path.abspath('generated_filesystem')  # Root folder for the file system
    os.makedirs(base_directory, exist_ok=True)
    print(f"Base directory for filesystem creation: {base_directory}")
    
    # Create the structure from the YAML file
    create_structure(base_directory, structure, asset_directory)
    print(f"Filesystem created at: {base_directory}")

if __name__ == "__main__":
    main()
