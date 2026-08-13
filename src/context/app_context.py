from ..utils.app_info import *

class AppContext:
    def __init__(self):
        self.work_dir: str = get_app_work_dir()
        self.name: str = get_app_name()
        self.version: str = get_app_version()
        self.author: str = get_app_author()

    