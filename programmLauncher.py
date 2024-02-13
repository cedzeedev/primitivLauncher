import subprocess
#change this variable
langage = "python"
fileName = "main.exe"

def execute_programm():
  try:
    subprocess.run([langage, fileName], check=True)
  except subprocess.CalledProcessError as e:
    print(f"Launch System Error: {e}")
  except FileNotFoundError:
    print("Programm not found")
if __name__ == "__name__":
  execute_programm()
