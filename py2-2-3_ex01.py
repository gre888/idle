import json


student_info={
    "id":"A123"
    "course":["Python","爬蟲","AI"]
    "is_graduated": False
    }

out_json = json.dumps(student_info, indent=4, ensure_ascii=False)
print(out_json)



