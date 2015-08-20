# -*- coding: utf-8 -*-

from isolation_trans import start_watch_receive

ISOLATION_PATH = r'C:\togeek\isolation'
FILE_PATH = r'C:\togeek\com\receive'


def start():
    start_watch_receive(ISOLATION_PATH, FILE_PATH)


if __name__ == '__main__':
    start()
