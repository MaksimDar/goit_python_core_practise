from pathlib import Path
import shutil

def remove_empty_folders(path):
    for folder in sorted(path.rglob('*'), reverse=True):
        ######## Check if folder is empty
        if folder.is_dir() and not any(folder.iterdir()):
            try:
                folder.rmdir()
                print(f"Removed empty folder: {folder}")
            except OSError as error:
                print(f"Error removing folder {folder} : {error}")

def organise_file_recursevily(base_path):
    archieve = base_path / 'Archieves'
    archieve.mkdir(parents=True, exist_ok=True)

    for item in base_path.rglob('*'):
        #### Skip directories, process only files
        if item.is_dir():
            continue

        ### determine file extension
        file_extension = item.suffix.lstrip('.').lower()

        if not file_extension:
            continue

        if file_extension in ('zip', 'tar', 'qztar'):
            extract_dir = archieve / item
            extract_dir.mkdir(parents=True,exist_ok=True)

            try:
                shutil.unpack_archive(str(item), extract_dir)
            except (shutil.ReadError, FileNotFoundError) as e:
                print(f"Identified error in {item}: {e}")
            item.unlink() ### Remove the original archieve
            continue
            ### Move files to directories based on their extensions

        target_dir = base_path / file_extension.upper()
        target_dir.mkdir(parents=True,exist_ok=True)
        try:
            shutil.move(str(item), target_dir / item.name)
        except Exception as e:
            print(f"Error moving {item}: {e}")
    remove_empty_folders(base_path)
    print(f"Files in {base_path} organized recursively")


if __name__ == "__main__":
    parent_folder_path = Path('Temp')
    organise_file_recursevily(parent_folder_path)

