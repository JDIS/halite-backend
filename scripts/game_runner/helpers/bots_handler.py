import os
import shutil
import helpers.directories as directories
from zipfile import ZipFile
from helpers.language import Language


def unzip_bots(bots):
    tmp_directory = directories.get_base_directory() + 'tmp/'
    bots_directory = directories.get_base_directory() + 'bots/'
    bots_extracted = {}

    # Delete tmp before copying bots
    if os.path.exists(tmp_directory):
        shutil.rmtree(tmp_directory)
    os.makedirs(tmp_directory)

    for bot in bots:
        zip_bot = ZipFile(bots_directory + str(bot) + '.zip', 'r')

        bot_path = tmp_directory + str(bot)
        zip_bot.extractall(bot_path)
        bots_extracted[bot] = {'path': bot_path, 'language': _detect_language(bot_path)}

        if bots_extracted[bot]['language'].value.get('compiler'):
            # Compile
            pass

        zip_bot.close()

    return bots_extracted


def _detect_language(bot_path):
    for lang in Language:
        path = bot_path + '/MyBot' + lang.value.get('extension')
        if os.path.isfile(path):
            return lang
    # throw


