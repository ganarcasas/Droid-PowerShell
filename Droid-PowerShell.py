import os
import shutil

RED_TEXT = "\033[91m"
RESET = "\033[0m"

def get_android_version():
    try:
        version = os.popen("getprop ro.build.version.release").read().strip()
        return version if version else "Unknown"
    except:
        return "Unknown"

def get_disk_info():
    try:
        total, used, free = shutil.disk_usage("/storage/emulated/0/")
        total_gb = total / (1024**3)
        used_gb = used / (1024**3)
        free_gb = free / (1024**3)
        return total_gb, used_gb, free_gb
    except:
        return None

def list_directory(filter_type=None):
    try:
        files = os.listdir("/storage/emulated/0/")
        if filter_type == 'folders':
            return [f for f in files if os.path.isdir(os.path.join("/storage/emulated/0/", f))]
        elif filter_type == 'all_files':
            return [f for f in files if os.path.isfile(os.path.join("/storage/emulated/0/", f))]
        else:
            return files
    except:
        return []

def clear_screen():
    print("\n" * 10000)

def terminal():
    print("\n" + "=" * 40)
    print("      D R O I D   P O W E R S H E L L")
    print("=" * 40)
    print("\n           Created by LaLolaApps\n")
    
    android_version = get_android_version()

    while True:
        command = input("\n/storage/emulated/0/ ")
        
        if command.lower() == "info":
            print("\nDroid PowerShell 0.1")
            print(f"Android {android_version}")

        elif command.lower() == "info -disk":
            disk_info = get_disk_info()
            if disk_info:
                total_gb, used_gb, free_gb = disk_info
                print(f"\nTotal Storage: {total_gb:.2f} GB")
                print(f"Used Storage: {used_gb:.2f} GB")
                print(f"Free Storage: {free_gb:.2f} GB")
            else:
                print("\nUnable to retrieve disk information.")
        
        elif command.startswith("text "):
            print(command[5:])
        
        elif command.lower() == "list":
            files = list_directory()
            if files:
                print("\n".join(files))
            else:
                print("\nUnable to list files or directory is empty.")
        
        elif command.lower() == "list -folders":
            folders = list_directory(filter_type='folders')
            if folders:
                print("\n".join(folders))
            else:
                print("\nNo folders found.")
        
        elif command.lower() == "list -archives":
            all_files = list_directory(filter_type='all_files')
            if all_files:
                print("\n".join(all_files))
            else:
                print("\nNo files found.")
        
        elif command.lower() == "clear":
            clear_screen()
        
        else:
            print(f"{RED_TEXT}The term '{command}' is not recognized as a function.{RESET}")

if __name__ == "__main__":
    terminal()
