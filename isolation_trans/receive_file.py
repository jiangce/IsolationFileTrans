# -*- coding: utf-8 -*-

from .watch import FileWatchDog
import os
import time


class ReceiveFileProcessor:
    def __init__(self, target_path):
        self.target_path = target_path

    @staticmethod
    def check_size(fullname):
        try:
            return int(os.path.splitext(fullname)[1][1:])
        except ValueError:
            return None

    def __call__(self, fullname):
        while True:
            try:
                if os.path.exists(fullname) and os.path.getsize(fullname) == self.check_size(fullname):
                    target_name = os.path.basename(os.path.splitext(fullname)[0])
                    target_fullname = os.path.join(self.target_path, target_name)
                    if os.path.exists(target_fullname):
                        os.remove(target_fullname)
                    os.rename(fullname, target_fullname)
                return
            except:
                time.sleep(1)


def start_watch_receive(watch_path, target_path):
    dog = FileWatchDog(watch_path)
    print('隔离监听目录：%s' % watch_path)
    print('接收目录：%s' % target_path)
    processor = ReceiveFileProcessor(target_path)
    dog.start_watch(created_processors=processor, modified_processors=processor)
    dog.join_watch()
