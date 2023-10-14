import filecmp
import os
import shutil

from services.service_logger import Logger


def file_write(file: str, message: str):
    """
    Write a message in a file
    :param file: File path
    :param message: Message to write
    :return: None
    """

    file = open(file, "a", encoding="utf-8")
    file.write("\n" + message)
    file.close()


def create_folder(folder_name):
    """
    Create a folder if it does not exist
    :param folder_name: Folder name
    :return: None
    """

    if not os.path.exists(folder_name):
        try:
            os.mkdir(folder_name)
            Logger.info("[FILEMANAGER]" + folder_name + " folder was created", False)
        except:
            Logger.error("[FILEMANAGER]" + "Unable to create " + folder_name + " folder", )
    else:
        Logger.info("[FILEMANAGER]" + folder_name + " folder already exists")


# Delete a folder if it exists
def delete_folder(folder_name):
    if os.path.exists(folder_name):
        try:
            shutil.rmtree(folder_name)
            Logger.info("[FILEMANAGER]" + folder_name + " folder was deleted")
        except:
            Logger.error("[FILEMANAGER]" + "Unable to delete " + folder_name + " folder")
    else:
        Logger.info("[FILEMANAGER]" + folder_name + " folder does not exist")


# Copy a folder if it exists
def copy_folder(folder_name, destination):
    if os.path.exists(folder_name):
        try:
            shutil.copytree(folder_name, destination)
            Logger.info("[FILEMANAGER]" + folder_name + " folder was copied")
        except:
            Logger.error("[FILEMANAGER]" + "Unable to copy " + folder_name + " folder")
    else:
        Logger.info("[FILEMANAGER]" + folder_name + " folder does not exist")


def extract_zip(zip_file, destination):
    if os.path.exists(zip_file):
        try:
            shutil.unpack_archive(zip_file, destination)
            Logger.info("[FILEMANAGER]" + zip_file + " was extracted")
        except:
            Logger.error("[FILEMANAGER]" + "Unable to extract " + zip_file)
    else:
        Logger.info("[FILEMANAGER]" + zip_file + " does not exist")


def delete_file(file):
    if os.path.exists(file):
        try:
            os.remove(file)
            Logger.info("[FILEMANAGER]" + file + " was deleted")
        except Exception as error:
            Logger.error("[FILEMANAGER]" + "Unable to delete " + str(error))
    else:
        Logger.info("[FILEMANAGER]" + file + " does not exist")


def replace_folder(source, destination):
    if os.path.exists(source):
        try:

            for root, dirs, files in os.walk(source):
                for file in files:

                    source_path = os.path.join(root, file)
                    destination_path = os.path.join(destination, os.path.relpath(source_path, source))

                    if os.path.exists(destination_path):

                        if not filecmp.cmp(source_path, destination_path):

                            shutil.copy2(source_path, destination_path)
                            Logger.debug("[FILEMANAGER] " + destination_path + " was replaced")
                        else:
                            Logger.debug("[FILEMANAGER] " + destination_path + " is the same")
                    else:

                        if not os.path.exists(os.path.dirname(destination_path)):
                            os.makedirs(os.path.dirname(destination_path))

                            Logger.debug("[FILEMANAGER] " + os.path.dirname(destination_path) + " folder was created")

                        shutil.copy2(source_path, destination_path)

                        Logger.debug("[FILEMANAGER] " + destination_path + " does not exist, copied from source")
        except Exception as error:
            Logger.error("[FILEMANAGER] Unable to replace " + source)
            Logger.critical("[FILEMANAGER] " + str(error))

    else:
        Logger.error("[FILEMANAGER] " + source + " does not exist")
