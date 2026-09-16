

import os
import shutil
target_dir="old_notes"
sourcefile="notes.txt"
if not os.path.exists(target_dir):
        os.makedirs(target_dir)
if os.path.exists(sourcefile):
        destination=os.path.join(target_dir,"backup_"+sourcefile)
        if os.path.exists(destination):
                print("檔案存在")
        else:
                shutil.move(sourcefile, destination)
                print(f"{sourcefile} 已經歸檔")



