import filecmp
import os
import shutil

from services.service_logger import Logger


def create_folder(path: str):
    """
    Create a folder if it does not exist
    :param path: Folder path
    :return: True if the folder was created or already exists, False otherwise
    """

    if os.path.exists(path):
        Logger.debug(f"[SERVICE][FILEMANAGER][CREATE FOLDER] The directory '{path}' already exists", False)
        return True

    try:
        os.mkdir(path)
        Logger.debug(f"[SERVICE][FILEMANAGER][CREATE FOLDER] The directory '{path}' has been created", False)
        return True
    except Exception as error:
        Logger.warning(f"[SERVICE][FILEMANAGER][CREATE FOLDER] Unable to create the directory '{path}': {error}", False)
        return False


def delete_folder(path):
    """
    Delete a folder if it exists
    :param path: Folder path
    :return: None
    """
    if os.path.exists(path):
        try:
            shutil.rmtree(path)
            Logger.debug(f"[SERVICE][FILEMANAGER][DELETE FOLDER] Folder '{path}' was successfully deleted", False)
        except OSError as error:
            Logger.warning(f"[SERVICE][FILEMANAGER][DELETE FOLDER] Unable to delete folder '{path}': {error}", False)
    else:
        Logger.debug(f"[SERVICE][FILEMANAGER][DELETE FOLDER] Folder '{path}' does not exist", False)


def copy_folder(source, destination):
    """
    Copy a folder if it exists
    :param source: Source folder
    :param destination: Destination folder
    :return: None
    """
    if os.path.exists(source):
        try:
            shutil.copytree(source, destination)
            Logger.debug(f"[SERVICE][FILEMANAGER][COPY FOLDER] Folder '{source}' was successfully copied to '{destination}'", False)
        except shutil.Error as error:
            Logger.warning(f"[SERVICE][FILEMANAGER][COPY FOLDER] Error while copying folder '{source}' to '{destination}': {error}", False)
        except Exception as error:
            Logger.warning(f"[SERVICE][FILEMANAGER][COPY FOLDER] Unable to copy folder '{source}' to '{destination}': {error}", False)
    else:
        Logger.debug(f"[SERVICE][FILEMANAGER][COPY FOLDER] Source folder '{source}' does not exist", False)


def replace_folder(source, destination):
    """
    Replace a folder if it exists
    :param source: Source folder
    :param destination: Destination folder
    """
    if os.path.exists(source):
        try:
            for root, dirs, files in os.walk(source):
                for file in files:
                    source_path = os.path.join(root, file)
                    destination_path = os.path.join(destination, os.path.relpath(source_path, source))

                    if os.path.exists(destination_path):
                        if not filecmp.cmp(source_path, destination_path, shallow=False):
                            shutil.copy2(source_path, destination_path)
                            Logger.debug(f"[SERVICE][FILEMANAGER][REPLACE FOLDER] File '{destination_path}' was replaced", False)
                        else:
                            Logger.debug(f"[SERVICE][FILEMANAGER][REPLACE FOLDER] File '{destination_path}' is the same", False)
                    else:
                        if not os.path.exists(os.path.dirname(destination_path)):
                            os.makedirs(os.path.dirname(destination_path))
                            Logger.debug(f"[SERVICE][FILEMANAGER][REPLACE FOLDER] Folder '{os.path.dirname(destination_path)}' was created", False)

                        shutil.copy2(source_path, destination_path)
                        Logger.debug(f"[SERVICE][FILEMANAGER][REPLACE FOLDER] File '{destination_path}' does not exist, copied from source", False)
        except Exception as error:
            Logger.debug(f"[SERVICE][FILEMANAGER][REPLACE FOLDER] Unable to replace {source}: {error}", False)
    else:
        Logger.debug(f"[SERVICE][FILEMANAGER][REPLACE FOLDER] Source folder '{source}' does not exist", False)


def extract_zip(zip_file, destination):
    """
    Extract a zip file if it exists
    :param zip_file: Zip file
    :param destination: Destination folder
    :return: None
    """
    if os.path.exists(zip_file):
        try:
            shutil.unpack_archive(zip_file, destination)
            Logger.debug(f"[SERVICE][FILEMANAGER][EXTRACT ZIP] Zip file '{zip_file}' was successfully extracted to '{destination}'", False)
        except shutil.ReadError as error:
            Logger.warning(f"[SERVICE][FILEMANAGER][EXTRACT ZIP] Error while extracting zip file '{zip_file}': {error}", False)
        except Exception as error:
            Logger.warning(f"[SERVICE][FILEMANAGER][EXTRACT ZIP] Unable to extract zip file '{zip_file}': {error}", False)
    else:
        Logger.debug(f"[SERVICE][FILEMANAGER][EXTRACT ZIP] Zip file '{zip_file}' does not exist", False)


def create_zip(archive_name, source, destination=None):
    """
    Create a zip file if it does not exist and folder exists
    :param archive_name: Zip file name
    :param source: Folder to zip
    :param destination: Destination folder
    :return: None
    """
    if os.path.exists(source):
        try:
            shutil.make_archive(archive_name, 'zip', source)
            shutil.move(archive_name + ".zip", destination)
            Logger.debug(f"[SERVICE][FILEMANAGER][CREATE ZIP] Zip file '{archive_name}' was successfully created from '{source}'", False)
        except shutil.ReadError as error:
            Logger.warning(f"[SERVICE][FILEMANAGER][CREATE ZIP] Error while creating zip file '{archive_name}': {error}", False)
        except Exception as error:
            Logger.warning(f"[SERVICE][FILEMANAGER][CREATE ZIP] Unable to create zip file '{archive_name}': {error}", False)
    else:
        Logger.debug(f"[SERVICE][FILEMANAGER][CREATE ZIP] Folder '{source}' does not exist", False)


def file_write(path: str, data: str):
    """
    Write a message in a file
    :param path: File path
    :param data: Content to write
    :return: None
    """
    try:
        with open(path, "a", encoding="utf-8") as file:
            file.write(data + "\n")
        Logger.debug(f"[SERVICE][FILEMANAGER][FILE WRITE] Data written to '{path}'", False)
    except Exception as error:
        Logger.debug(f"[SERVICE][FILEMANAGER][FILE WRITE] Unable to write data to '{path}': {error}", False)


def delete_file(file):
    """
    Delete a file if it exists
    :param file: File path
    :return: None
    """
    if os.path.exists(file):
        try:
            os.remove(file)
            Logger.debug(f"[SERVICE][FILEMANAGER][DELETE FILE] File '{file}' was successfully deleted", False)
        except OSError as error:
            Logger.warning(f"[SERVICE][FILEMANAGER][DELETE FILE] Error while deleting file '{file}': {error}", False)
        except Exception as error:
            Logger.warning(f"[SERVICE][FILEMANAGER][DELETE FILE] Unable to delete file '{file}': {error}", False)
    else:
        Logger.debug(f"[SERVICE][FILEMANAGER][DELETE FILE] File '{file}' does not exist", False)
