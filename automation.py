from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import os
import shutil
import re

def create_folder(new_folder):
  try:
    os.mkdir(new_folder)
    console.print(f"A new folder named {new_folder} created")
  except FileExistsError:
    console.print(f"[bold]That folder exits or can't be created[/bold]")

def move_user(user):
  try:
    temp_name = "temp_" + user
    source_path = f"assets/user-docs/{user}"
    target_path = f"assets/user-docs/{temp_name}"
    shutil.move(source_path, target_path)
    console.print(f"[bold]User {user} files copied to temp folder[/bold]")
  except FileExistsError:
    console.print(f"[bold]That folder exits or can't be created[/bold]")

def folder_sort(folder_to_sort):
  try:
    files = os.listdir(folder_to_sort)
    log_matches = [file for file in files if re.search("log", file)]
    subfolder = os.path.join(folder_to_sort, "logs")
    for file in log_matches:
      source_path = os.path.join(folder_to_sort, file)
      target_path = os.path.join(subfolder, file)
      console.print(source_path)
      console.print(target_path)
      shutil.copy2(source_path, target_path)
  except FileExistsError:
    console.print(f"[bold]That folder exits or can't be created[/bold]")

console = Console()

if __name__ == "__main__":
  while True:
    #Listed and colored blue
    console.print("[blue]\n1. Create a Folder\n2. Move User Files\n3. Document Sort\n4. Something else\n5. Exit[/blue]")
    choice = Prompt.ask("Choose a task (Enter the number)", choices=['1', '2', '3', '4'], default='5')
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
      pass
    else:
      break