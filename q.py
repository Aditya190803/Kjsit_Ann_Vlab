import os

# Function to create directories and files
def create_exp_folders(parent_dir, num_folders):
    # Create 'exp' directory
    exp_dir = os.path.join(parent_dir, 'exp')
    os.makedirs(exp_dir, exist_ok=True)
    
    # Create exp1 to exp{num_folders} directories
    for i in range(1, num_folders+1):
        exp_folder = os.path.join(exp_dir, f'exp{i}')
        os.makedirs(exp_folder, exist_ok=True)
        
        # Create HTML and CSS files
        with open(os.path.join(exp_folder, f'exp{i}_theory.html'), 'w') as f:
            f.write('<!-- Add theory content here -->')
        
        with open(os.path.join(exp_folder, f'exp{i}_simulation.html'), 'w') as f:
            f.write('<!-- Add simulation content here -->')
        
        # Create tf.js and style.css files
        with open(os.path.join(exp_folder, f'tf{i}.js'), 'w') as f:
            pass  # empty file
        
        with open(os.path.join(exp_folder, f'style{i}.css'), 'w') as f:
            pass  # empty file

# Example usage
parent_directory = '.'  # You can change this to the desired parent directory
num_exp_folders = 8     # Number of 'exp' folders to create

create_exp_folders(parent_directory, num_exp_folders)
