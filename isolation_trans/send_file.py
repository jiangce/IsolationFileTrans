# -*- coding: utf-8 -*-

from .watch import FileWatchDog
import os
import time


class SendFileProcessor:
    def __init__(self, target_path):
        self.target_path = target_path

    def __call__(self, fullname):
        while True:
            try:
                if os.path.exists(fullname):
                    size = os.path.getsize(fullname)
                    target_name = '%s.%s' % (os.path.basename(fullname), size)
                    target_fullname = os.path.join(self.target_path, target_name)
                    if os.path.exists(target_fullname):
                        os.remove(target_fullname)
                    os.rename(fullname, target_fullname)
                return
            except:
                time.sleep(1)


def start_watch_send(watch_path, target_path):
    dog = FileWatchDog(watch_path)
    print('监听目录：%s' % watch_path)
    print('隔离发送目录：%s' % target_path)
    dog.start_watch(created_processors=SendFileProcessor(target_path))
    dog.join_watch()
