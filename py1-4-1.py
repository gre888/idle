import os
import shutil


target_dir = "history_logs"


def move_files(sourcefile):
        
        if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            
        if os.path.exists(sourcefile):
                shutil.move(sourcefile, os.path.join(target_dir,"old_"+sourcefile))
                print(f"{sourcefile} 已經歸檔")

print(os.listdir("."))
for f in os.listdir("."):
        if os.path.isfile(f):
                if "txt" in f:
                        move_files(f)
                        print(f)
