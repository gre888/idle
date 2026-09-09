

import os
folder="scraped_images"
files=os.listdir(folder)
for index, filename in enumerate(files):
    new_name=f"pet_{index}.jpg"
    old_path=os.path.join(folder,filename)
    new_path=os.path.join(folder,new_name)
    os.rename(old_path,new_path)
    print(f"更名成功{filename}->{new_name}")




