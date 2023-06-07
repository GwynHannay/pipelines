"""
NOTE: Scratchpad blocks are used only for experimentation and testing out code.
The code written here will not be executed as part of the pipeline.
"""

import os

dropbox_location = '/home/dropbox'
ynab_folder = 'YNAB'
budget_folder = 'Household Budget~C4A2E070.ynab4'

filetypes_wanted = ['ymeta', 'ydiff', 'yfull', 'ybsettings', 'ydevice']

budget_filepath = os.path.join(dropbox_location, ynab_folder, budget_folder)

def walk_with_attributes(dir_to_walk: str):
    if not os.path.isdir(dir_to_walk):
        print("Fail")

    with os.scandir(dir_to_walk) as dir_contents:
        for item in dir_contents:
            if item.is_dir():
                yield from walk_with_attributes(item.path)
            elif item.path.endswith('.'.join):
                yield item

i = 0
for file in walk_with_attributes(budget_filepath):
    print(file.path, file.stat())
    i = i + 1
    
    if i > 10:
        break