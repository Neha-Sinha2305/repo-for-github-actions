import os

filepath= os.path.join(str(os.environ.get("GITHUB_WORKSPACE")),str(os.environ.get("FILE_NAME")))

with open(filepath) as f:
    newText=f.read().replace(os.environ.get("find"),os.environ.get("replace"))

with open(filepath, "w") as f:
    f.write(newText)

with open(filepath, "r") as f:
    print(f.read())
