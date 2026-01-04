import os
import shutil

def copy_static(src, dest):
    if os.path.isfile(src):
        shutil.copyfile(src, dest)
        return
    
    if os.path.exists(dest):
        shutil.rmtree(dest)
        os.mkdir(dest)
    else:
        os.mkdir(dest)
    
    dir_list = os.listdir(src)

    for item in dir_list:
        src_item_path = os.path.join(src, item)
        dest_item_path = os.path.join(dest, item)
        copy_static(src_item_path, dest_item_path)
    return