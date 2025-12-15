import os

# 1. Create file
def create_file():
    filename = input("Enter file name to create: ")
    if os.path.exists(filename):
        print("File already exists")
    else:
        f = open(filename, 'w')
        f.close()
        print("File created successfully")

# 2. Write file (overwrite)
def write_file():
    filename = input("Enter file name to write: ")
    f = open(filename, 'w')
    content = input("Enter content: ")
    f.write(content)
    f.close()
    print("Content written successfully")

# 3. Replace file content
def replace_file():
    filename = input("Enter file name: ")
    if os.path.exists(filename):
        f = open(filename, 'w')
        content = input("Enter new content: ")
        f.write(content)
        f.close()
        print("File content replaced")
    else:
        print("File not found")

# 4. Append file
def append_file():
    filename = input("Enter file name: ")
    f = open(filename, 'a')
    content = input("Enter content to append: ")
    f.write(content)
    f.close()
    print("Content appended successfully")

# 5. Read file
def read_file():
    filename = input("Enter file name to read: ")
    if os.path.exists(filename):
        f = open(filename, 'r')
        print("\nFile Content:\n")
        print(f.read())
        f.close()
    else:
        print("File not found")

# 6. Rename file
def rename_file():
    old_name = input("Enter current file name: ")
    new_name = input("Enter new file name: ")
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print("File renamed successfully")
    else:
        print("File not found")

# 7. Delete file
def delete_file():
    filename = input("Enter file name to delete: ")
    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted successfully")
    else:
        print("File not found")

# Menu-driven program
while True:
    print("\n📂 FILE HANDLING MENU")
    print("1. Create File")
    print("2. Write File")
    print("3. Replace File Content")
    print("4. Append File")
    print("5. Read File")
    print("6. Rename File")
    print("7. Delete File")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        create_file()
    elif choice == '2':
        write_file()
    elif choice == '3':
        replace_file()
    elif choice == '4':
        append_file()
    elif choice == '5':
        read_file()
    elif choice == '6':
        rename_file()
    elif choice == '7':
        delete_file()
    elif choice == '8':
        print("Exiting program...")
        break
    else:
        print(" Invalid entry! Please choose a valid option.")
