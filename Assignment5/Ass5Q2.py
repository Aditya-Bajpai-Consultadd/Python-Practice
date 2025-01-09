#Develop a program to merge multiple text files into one while
#handling exceptions for missing or unreadable files. Include
#options to remove duplicate lines.


def main(*files):
    try:
        with open('merged.txt', 'w') as outfile:
            for file in files:
                with open(file, 'r') as infile:
                    for line in infile:
                        outfile.write(line)
        print("Files merged successfully")
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
    except:
        print("Unexpected error:")
    return
main('file1.txt','file2.txt','file3.txt')
