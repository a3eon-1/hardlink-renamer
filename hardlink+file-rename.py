import shutil, os, re, glob
from os.path import join

def hardlink():
    def ignore_files(dir, files):
        return [f for f in files if os.path.isfile(os.path.join(dir, f))]
    
    global og_folder_structure
    global new_folder_structure_location
    
    og_folder_structure = input("input original file location:")
    new_folder_structure_location = input("input new file location:")

    shutil.copytree(og_folder_structure,
                new_folder_structure_location,
                copy_function=os.link)


def rename():
    path = new_folder_structure_location + "\*"
    for dirs in glob.glob(path):
        newname = re.sub("[\(\[].*?[\)\]]", "", dirs)
        os.rename(dirs, newname)
        print("x")
    for files in glob.glob(path + "\*"):
        newname = re.sub("[\(\[].*?[\)\]]", "", files)
        os.rename(files, newname)
        print("x")

hardlink()
rename()