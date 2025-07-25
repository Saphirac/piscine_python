set script_path (realpath (dirname (status --current-filename)))

# Create a virtual environment
python3 -m venv $script_path/myenv

# Activate it using the fish-specific activate script
source $script_path/myenv/bin/activate.fish

pip install --upgrade pip

pip install -r $script_path/dep.txt

echo "venv launched!"
