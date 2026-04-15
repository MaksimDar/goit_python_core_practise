####### 1-st option

# from pathlib import Path

# file_name = Path("././Temp/jokes.txt")

# try:
#     file_name.unlink()
# except FileNotFoundError:
#     print("File is not found")


###### 2-nd option to create a directory 

# from pathlib import Path

# new_dir = Path('ABg')

# if not new_dir.exists():
#     new_dir.mkdir()

##or

# new_dir.mkdir(exist_ok=True)

######## rename function 
# from pathlib import Path

# old_dir = Path('example2.txt')
# new_dir = Path('ABC/text_data.txt')
# old_dir.rename(new_dir)



