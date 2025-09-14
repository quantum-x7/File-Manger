import os
import shutil
#create_files______________________________________________
def create_file(*filenames):
    for filename in filenames: 
        try:
            with open(filename , "x") as f:
                print(f"File Name {filename}: Created sucessfully")  
        except FileExistsError:
            print(f"File name {filename} Already exists!")
        except PermissionError:
            print(f"❌ Permission denied! Cannot create '{filename}' in this location.")
        except IsADirectoryError:
            print(f"❌ '{filename}' is a directory, not a file!")
        except OSError as e:
            print("Os Error",e)
        except Exception as e:
            print("An Error occurred!",e)
#view_files________________________________________________
def view_all_files():
    with os.scandir() as entries:
        all_entries = list(entries)
        files = [entry.name for entry in all_entries if entry.is_file()]
        dirs = [entry.name for entry in all_entries if entry.is_dir()]

    if not  files and not dirs:
        print("No file found")
    else:
        if files:
            print("Files in directory")
            print("📄 Files:", files)
        if dirs:
            print("All Directrories")
            print("📂 Directories:", dirs)
#del_files_________________________________________________
def delete_file(*filenames):
    for filename in filenames:
        try:
            os.remove(filename)
            print(f"{filename} has been removed Successfully!")

        except IsADirectoryError:
            print("❌ That's a directory, not a file!")
        except FileNotFoundError:
            print(f"❌ The file '{filename}' not found!")
        except PermissionError:
            print("❌ Permission denied! File might be in use or protected.")
        except  OSError as e:
            print("An OsError has been occurred",e)
        except Exception as e:
            print("An unexpected Error",e)  

def make_directory(*dirnames):
    for dirname in dirnames:
        try:
            os.makedirs(dirname)
            print(f"📂 Directory '{dirname}' created successfully!")
        except FileExistsError:
            print(f"❌ Directory '{dirname}' already exists.")
            user = input("You want to re-create this directory(Yes/NO): ").strip()
            if user.lower() == "yes": #if user choose yes it creates an back that tempory store the old dir then if exist it removed by shutill.rmtree then new_name copy data from old dir then re-make the directry 
                backup = dirname + "_backup"
                if os.path.exists(backup):
                    shutil.rmtree(backup)
                shutil.copytree(dirname, backup)
                #remove the old dir
                shutil.rmtree(dirname)
                os.makedirs(dirname, exist_ok=True)
                print(f"🔄 Directory '{dirname}' recreated successfully!")
            else:
                print(f"✅ Keeping the existing directory '{dirname}'.")

        except PermissionError:
            print(f"❌ Permission denied! Cannot create '{dirname}' here.")
        except OSError as e:
            print(f"❌ OS error while creating directory: {e}")
        except Exception as e:
            print("An unexpected Error",e)

def del_dir(*dirnames):
    for dirname  in dirnames:  
        try:
            shutil.rmtree(dirname)
            print(f"The Directory {dirname} is Successfuly deleted")
        except NotADirectoryError:
            print("❌ That's a file not a directory")
        except FileNotFoundError:
            print(f"❌ Directory '{dirname}' Not found!.")
        except PermissionError:
            print("❌ Permission denied! Directory might be in use or protected.")
        except  OSError as e:
            print("An OsError has been occurred",e)
        except Exception as e:
            print("An unexpected Error",e)  

def read_file(*filenames):
    for filename in filenames:
        try:
            with open(filename,"r") as f:
                content = f.read()
                print(f"Content of '{filename}':\n{content}")
        except FileNotFoundError:
            print(f"❌ The file '{filename}' not found!")
        except PermissionError:
            print(f"❌ Permission denied! Cannot read '{filename}'.")
        except IsADirectoryError:
            print(f"❌ '{filename}' is a directory, not a file.")
        except OSError as e:
            print(f"❌ OS error while reading file: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
def edit_file(filename):
    try:
        with open(filename,'a') as f:
            content = input("Enter data to ADD: ")
            f.write(content + "\n")
            print(f"Content Added to {filename} Successfully")
    except FileNotFoundError:
        print(f"The File {filename} not found!")
    except PermissionError:
        print(f"❌ Permission denied! Cannot write to '{filename}'.")
    except IsADirectoryError:
        print(f"❌ '{filename}' is a directory, not a file!")
    except OSError as e:
        print(f"❌ OS error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")    

#------------APP------------
print("FILE MANAGEMENT APP")
def main():
    while True:
        print("1: Create File")
        print("2: View All Files/Directories")
        print("3: Delete File")
        print("4: Create Directory")
        print("5: Delete Directory")
        print("6: Read File")
        print("7: Edit File(Append/Data)")
        print("8: Exit")
        choice = input("Enter your choice(1-8): ").strip()
        print("Please All entries space separeted")
        if choice == '1':
            filenames = input("Enter the file-name to create = ").strip().split()
            create_file(*filenames)
       
        elif choice == '2':
            view_all_files()
       
        elif choice == '3':
            filenames_to_del =  input("Enter the file-name to Delete = ").strip().split()
            delete_file(*filenames_to_del)
       
        elif choice == '4':
            make_dir = input("Enter directory name you want to create = ").strip().split()
            make_directory(*make_dir)
       
        elif choice == '5':
            del_directory = input("Enter directory name you want to Delete = ").strip().split()
            del_dir(*del_directory)
       
        elif choice == '6':
            read_a_file = input("Enter file-name to read = ").strip().split()
            read_file(*read_a_file)
       
        elif choice == '7':
            file_to_edit = input("Enter the file-name to edit: ").strip()
            edit_file(file_to_edit)
        elif choice == '8':
            print("Exiting the App. GoodBye!")
            break
        else:
            print("Invalid Entry")

if __name__ == "__main__":
    main()