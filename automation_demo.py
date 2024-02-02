from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import os
import shutil
import re

def list_files(directory):
  """List directory files"""
  try:
    files = os.listdir(directory)
    table = Table(title=f"Files in {directory}")
    # Add some style
    table.add_column("File Name", style="green")
    for file in files:
      table.add_row(file)
    console.print(table)
  except FileNotFoundError:
    console.print("[bold][red]Directory not found.[/red][/bold]")

def move_file(directory, file, target_directory):
  """Move the given file from the current directory to the target directory."""
  try:
    source_path = os.path.join(directory, file) # Platform specific file path
    target_path = os.path.join(target_directory, file)
    shutil.move(source_path, target_path)
    console.print(f"[bold green]{file}[/bold green] has been moved from [bold blue]{directory}[/bold blue] to [bold yellow]{target_directory}[/bold yellow]")
  except FileNotFoundError:
    console.print("[bold][red]Directory or file not found.[/red][/bold]")

def search_files(directory, pattern):
  try:
    files = os.listdir(directory)
    matches = [file for file in files if re.search(pattern, file)]
    table = Table(title=f"Files in [bold green]{directory}[/bold green] matching [bold blue]{pattern}[/bold blue]")
    table.add_column("Matching File Name", style="blue")
    for match in matches:
      table.add_row(match)
    console.print(table)
  except FileExistsError:
    console.print("[bold][red]Directory not found.[/red][/bold]")


console = Console()

if __name__ == "__main__":
  while True:
    #Listed and colored blue
    console.print("[blue]\n1. List files\n2. Move file\n3. Search files\n4. Exit[/blue]")
    choice = Prompt.ask("Choose a task (Enter the number)", choices=['1', '2', '3', '4'], default='4')
    if choice == '1':
      directory = Prompt.ask("Enter the directory to list files")
      list_files(directory)
    elif choice == '2':
      directory = Prompt.ask("Enter the current directory of the file.")
      file = Prompt.ask("Enter the file to move")
      target_directory = Prompt.ask("Enter the target directory to move to")
      move_file(directory, file, target_directory)
    elif choice == '3':
      directory = Prompt.ask("Enter the directory to search files")
      pattern = Prompt.ask("Enter the regex pattern to search for")
      search_files(directory, pattern)
    else:
      break