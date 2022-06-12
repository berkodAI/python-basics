def main():
    extensions = input("File name: ")
    find(extensions)


def find(file):
    file = file.lower().strip()
    point_position = file.rfind('.')
    extension = file[point_position + 1 :]  # start from "." till the end -> extension

    if extension == 'jpg' or extension == 'jpeg':
        print("image/jpeg")
    elif extension == 'png' or extension == 'gif':
        print(f"image/{extension}")
    elif extension == 'pdf' or extension == 'zip':
        print(f"application/{extension}")
    elif extension == 'txt':
        print(f"text/plain")
    else:
        print("application/octet-stream")


main()
