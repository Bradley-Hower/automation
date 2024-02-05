from rich.console import Console
from rich.prompt import Prompt
import os
import shutil
import re

def create_folder(new_folder):
  """Creates a folder as titled dictated by 'new_folder'"""
  try:
    os.mkdir(new_folder)
    console.print(f"A new folder named {new_folder} created")
  except FileExistsError:
    console.print(f"[bold]That folder exits or can't be created[/bold]")

def move_user(user):
  """Moves user documents from a folder into a temp folder. Removes prior folder."""
  try:
    temp_name = "temp_" + user
    source_path = f"assets/user-docs/{user}"
    target_path = f"assets/user-docs/{temp_name}"
    shutil.move(source_path, target_path)
    console.print(f"[bold]User {user} files copied to temp folder[/bold]")
  except FileExistsError:
    console.print(f"[bold]That folder exits or can't be created[/bold]")

def folder_sort(folder_to_sort):
  """Sorts folders according to their extension, either '.log' or '.email'."""
  files = os.listdir(folder_to_sort)
  try:
    log_matches = [file for file in files if re.search(".log", file)]
    log_subfolder = os.path.join(folder_to_sort, "logs")
    if not os.path.exists(log_subfolder):
      os.makedirs(log_subfolder)
    for file in log_matches:
      source_path = os.path.join(folder_to_sort, file)
      target_path = os.path.join(log_subfolder, file)
      shutil.move(source_path, target_path)
  except FileExistsError:
    console.print(f"[bold]That folder exits or can't be created[/bold]")
  try:
    email_matches = [file for file in files if re.search(".mail", file)]
    email_subfolder = os.path.join(folder_to_sort, "email")
    if not os.path.exists(email_subfolder):
      os.makedirs(email_subfolder)
    for file in email_matches:
      source_path = os.path.join(folder_to_sort, file)
      target_path = os.path.join(email_subfolder, file)
      shutil.move(source_path, target_path)
  except FileExistsError:
    console.print(f"[bold]That folder exits or can't be created[/bold]")

def log_parse(folder_to_parse):
  """Parses log file contents according to either tags 'ERROR' or 'WARNING' into their respective separate log files."""
  files = os.listdir(folder_to_parse)
  for file in files:
    source_path = os.path.join(folder_to_parse, file)
    try:
      with open(source_path, 'r') as rfile:
        content = rfile.read()
        contentlist = []
        for line in re.findall(r".*ERROR.*", content):
          contentlist.append(line + "\n")
          merged = "".join(contentlist)
          target_path = os.path.join(folder_to_parse, "errors.log.txt")
          with open(target_path, "w") as writefile:
            writefile.write(merged)
    except FileNotFoundError:
      raise FileNotFoundError
    try:
      with open(source_path, 'r') as rfile:
        content = rfile.read()
        contentlist = []
        for line in re.findall(r".*WARNING.*", content):
          contentlist.append(line + "\n")
          merged = "".join(contentlist)
          target_path = os.path.join(folder_to_parse, "warnings.log.txt")
          with open(target_path, "w") as writefile:
            writefile.write(merged)
    except FileNotFoundError:
      raise FileNotFoundError
    
def backup_script(folder_to_backup, backup_target):
  """Creates backup copy of contents of a provided folder. Creates backup folder according to a name provided, with copies of files copied thereto."""
  console.print(folder_to_backup)
  console.print(backup_target)
  try:
    shutil.copytree(folder_to_backup, backup_target)
  except FileNotFoundError:
    raise FileNotFoundError


console = Console()

if __name__ == "__main__":
  while True:
    #Listed and colored blue
    console.print("[blue]\n1. Create a Folder\n2. Move User Files\n3. Document Sort\n4. Log and Warning Parse\n5. Backup\n6. Exit[/blue]")
    choice = Prompt.ask("Choose a task (Enter the number)", choices=['1', '2', '3', '4', '5', '6'], default='6')
    if choice == '1':
      new_folder = Prompt.ask("Enter the name of the folder to create")
      create_folder(new_folder)
    elif choice == '2':
      user = Prompt.ask("Enter the name of the user whose files will be moved")
      move_user(user)
    elif choice == '3':
      folder_to_sort = Prompt.ask("Enter the folder to sort")
      folder_sort(folder_to_sort)
    elif choice == '4':
      folder_to_parse = Prompt.ask("Enter the folder to parse logs")
      log_parse(folder_to_parse)
    elif choice == '5':
      folder_to_backup = Prompt.ask("Enter the folder to backup (contents)")
      backup_target = Prompt.ask("Enter the directory to backup to (folder will be created)")
      backup_script(folder_to_backup, backup_target)
    else:
      break