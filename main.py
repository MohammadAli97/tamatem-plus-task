#!/usr/bin/env python3

import os
import shutil


def main():
    x = '1'
    while x == '1':
        # Asking the user to Enter his directory
        directory = input('Please Enter Your Directory\n')
        if not os.path.exists(directory):
            print("This directory is not exist")
        else:
            from os import listdir
            from os.path import isfile, join
            # Getting all files inside the directory
            only_files = [f for f in listdir(directory) if isfile(join(directory, f))]

            flag = True
            for file in only_files:
                # Pick the files with 'txt' extension
                if file.split(".")[-1] == "txt":
                    flag = False
                    # Getting the language from the file name
                    language = file.split('-')[0].lower()
                    # Create a new path for the language
                    path = os.path.join(directory, language)
                    # check if there's a directory for the language and create it if npt
                    if not os.path.exists(path):
                        os.mkdir(path)
                        print("Directory '% s' created" % language)
                    # The source path for the desire file
                    source_path = os.path.join(directory, file)
                    # The destination path for the desire file
                    destination_path = os.path.join(path, file)
                    # Check if the file is exist in the source path and not exist in the destination path
                    if os.path.exists(source_path) and not os.path.exists(destination_path):
                        # Moving the file
                        shutil.move(source_path, destination_path)
            if flag:
                print("There's no txt file in this directory")
        # Allowing user to enter another directory
        x = input('If you want to enter another directory enter 1\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

