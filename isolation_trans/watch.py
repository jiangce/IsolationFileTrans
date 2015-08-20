# -*- coding: utf-8 -*-

from watchdog.events import RegexMatchingEventHandler
from watchdog.observers import Observer


class _NewFileHandler(RegexMatchingEventHandler):
    def __init__(self):
        super(_NewFileHandler, self).__init__(ignore_directories=True)
        self.created_processors = []
        self.modified_processors = []

    def add_created_processors(self, processor):
        if processor:
            if isinstance(processor, (list, set, tuple)):
                self.created_processors.extend(list(processor))
            else:
                self.created_processors.append(processor)

    def add_modified_processors(self, processor):
        if processor:
            if isinstance(processor, (list, set, tuple)):
                self.modified_processors.extend(list(processor))
            else:
                self.modified_processors.append(processor)

    def on_moved(self, event):
        # print('on_moved')
        super(_NewFileHandler, self).on_moved(event)
        fullname = event.dest_path.lower()
        self.process_created_file(fullname)

    def on_created(self, event):
        # print('on_created')
        super(_NewFileHandler, self).on_created(event)
        fullname = event.src_path.lower()
        self.process_created_file(fullname)

    def on_modified(self, event):
        # print('on_modified')
        super(_NewFileHandler, self).on_modified(event)
        fullname = event.src_path.lower()
        self.process_modified_file(fullname)

    def process_created_file(self, fullname):
        if fullname.endswith('.tmp'):
            return
        if self.created_processors:
            for processor in self.created_processors:
                processor(fullname)

    def process_modified_file(self, fullname):
        if fullname.endswith('.tmp'):
            return
        if self.modified_processors:
            for processor in self.modified_processors:
                processor(fullname)


class FileWatchDog:
    def __init__(self, path):
        self._observer = None
        self.path = path

    def start_watch(self, created_processors=None, modified_processors=None):
        self.stop_watch()
        self._observer = Observer()
        handler = _NewFileHandler()
        handler.add_created_processors(created_processors)
        handler.add_modified_processors(modified_processors)
        self._observer.schedule(handler, self.path)
        self._observer.start()

    def join_watch(self):
        if self._observer:
            self._observer.join()

    def stop_watch(self):
        if self._observer:
            self._observer.stop()
            self._observer = None


if __name__ == '__main__':
    def p1(fullname):
        print('create: %s' % fullname)


    def p2(fullname):
        print('modify: %s' % fullname)


    dog = FileWatchDog('d:\\')
    print('监听目录：%s' % dog.path)
    dog.start_watch(p1, p2)
    dog.join_watch()
