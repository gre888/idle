import os
import shutil
from datetime import datetime


def backup_file(source_file, target_folder):
    if not os.path.exists(source_file):
        print(f"找不到 {source_file}")
        return
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        print(f"建立新資料夾 {target_folder}")

    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = os.path.basename(source_file)
        new_file_name = f"{timestamp}_{file_name}"
        destination = os.path.join(target_folder, new_file_name)
        shutil.copy2(source_file, destination)
        print(f"備份成功，檔案存至 {destination}")
        
    except Exception as e:
        print(f"備份過程發生錯誤：{e}")
        
backup_file("data.txt",".")
