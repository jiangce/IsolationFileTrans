# -*- coding: utf-8 -*-

from isolation_trans import start_watch_send

FILE_PATH = r'C:\togeek\com\send'
ISOLATION_PATH = r'C:\togeek\isolation'


def start():
    start_watch_send(FILE_PATH, ISOLATION_PATH)


if __name__ == '__main__':
    start()
