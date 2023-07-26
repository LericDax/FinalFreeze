import os
import subprocess
from tkinter import filedialog
from tkinter import Tk
from datetime import datetime

def select_file():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = filedialog.askopenfilename() # show an "Open" dialog box and return the path to the selected file
    return filename

def extract_last_frame(input_file, output_folder):
    # Generate a unique filename using the current date and time
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    output_file = os.path.join(output_folder, f'output_{timestamp}.jpg')
    
    # Quote the file paths
    input_file_quoted = f'"{input_file}"'
    output_file_quoted = f'"{output_file}"'
    
    cmd = f'ffmpeg -sseof -3 -i {input_file_quoted} -update 1 -q:v 1 {output_file_quoted}' # ffmpeg command
    subprocess.run(cmd, shell=True) # run the command


def main():
    # Determine the path of the script's directory
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Create the output folder as a subfolder of the script's directory
    output_folder = os.path.join(script_dir, 'output')
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    # Select the input file and extract the last frame
    input_file = select_file()
    extract_last_frame(input_file, output_folder)

if __name__ == '__main__':
    main()
