import os

filepath= str(os.environ.get("GITHUB_WORKSPACE")) + "/" + str(os.environ.get("FILE_NAME"))
with open(filepath, "rt") as fin:
    with open(filepath, "wt") as fout:
        for line in fin:
            fout.write(line.replace(find, replace))

with open(filepath, "r") as text_file:
    print(text_file.read())
