import os
import re

file_suffix = ['java', 'xml', "gradle"]
# TODO:完善去除//注释的正则
comment_pattern = [r"(?<!:)//[\s\S]*\n", r"<!-[\s\S]*?-->",r"/\*{1,2}[\s\S]*?\*/"]


dir = "/Users/zhaowenhai/Desktop/test"

def resolve_dir(dir):
    print("处理目录： %s" % dir)
    if os.path.isfile(dir):
        resolve_file(dir)    
    else:
        for file in os.listdir(dir):
            resolve_dir(dir+os.path.sep+file)



def resolve_file(file):
    print("处理文件:%s" % file)
    filename = os.path.split(file)[1]
    print("文件名：%s" % filename)
    names = filename.split(".")
    if len(names) < 2:
        return
    # 不是待处理的文件类型
    if names[-1] not in file_suffix:
        return
    
    with open(file, "r",encoding="utf-8") as f:
        lines = f.read()
        for p in comment_pattern:
            lines = re.sub(p, "", lines)
        with open(file, "w", encoding="utf-8") as fi:
            fi.write(lines)               



resolve_dir(dir)