import os
import yaml
import shutil

def create_structure(base_path, structure, asset_dir):
    """
    Recursively create directories and files based on the provided structure.
    
    :param base_path: The root path to create the structure.
    :param structure: A dictionary representing the folder structure.
    :param asset_dir: Path to the directory containing asset files (.png, .pdf, .zip).
    """
    for key, value in structure.items():
        current_path = os.path.join(base_path, key)
        
        # Case where key is a directory (value is a dict) and value is a structure (sub-dictionary)
        if isinstance(value, dict):
            if not os.path.exists(current_path):
                os.makedirs(current_path, exist_ok=True)
                print(f"Created directory: {current_path}")
            create_structure(current_path, value, asset_dir)
        
        # Case where key is a file directly (e.g., PNG, PDF, ZIP, etc.)
        elif isinstance(value, list) and (key.endswith('.png') or key.endswith('.pdf') or key.endswith('.zip')):
            asset_file_path = os.path.join(asset_dir, key)
            if os.path.exists(asset_file_path):
                shutil.copy(asset_file_path, current_path)
                print(f"Copied {key} from assets to {current_path}")
            else:
                print(f"WARNING: {key} not found in {asset_dir}, creating empty file at {current_path}")
                open(current_path, 'w').close()

        # Case for markdown files with content defined in the list
        elif isinstance(value, list) and key.endswith('.md'):
            content = "\n".join(value)  # Join all elements of the list as the file content
            with open(current_path, 'w') as md_file:
                md_file.write(content)
            print(f"Created markdown file with content: {current_path}")

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
    
    # Define the asset directory where PNG, PDF, and ZIP files are stored
    asset_directory = os.path.abspath('assets')  # Path to the asset directory (containing PNG, PDF, ZIP files)
    
    if not os.path.exists(asset_directory):
        print(f"Asset directory {asset_directory} does not exist.")
        return
    
    print(f"Using asset directory: {asset_directory}")
    
    # Set the base directory for the generated file system
    base_directory = os.path.abspath('generated_filesystem')  # Root folder for the file system
    os.makedirs(base_directory, exist_ok=True)
    print(f"Base directory for filesystem creation: {base_directory}")
    
    # Create the structure from the YAML file
    create_structure(base_directory, structure, asset_directory)
    print(f"Filesystem created at: {base_directory}")

if __name__ == "__main__":
    main()
