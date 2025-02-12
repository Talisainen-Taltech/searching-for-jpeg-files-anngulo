import os

folder = "random_files"

for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    with open(file_path, "rb") as f:
        file = f.read(3)
    if file == (b'\xff\xd8\xff'):
        print("Rename file: " + filename + ".jpg")
        os.rename(file_path, file_path + ".jpg")
    else:
        os.remove(file_path)