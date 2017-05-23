# coding=utf-8

# Author: Diego Gonzalez Chavez
# email : diegogch@cbpf.br / diego.gonzalez.chavez@gmail.com

import threading


class _Exception_StopThread(Exception):
    pass


class Treaded_Function(object):

    def __init__(self, traget):
        self._traget = traget
        self.thread = None

    def Stop(self):
        if self.thread is not None:
            self.thread._TD_stop = True

    def __call__(self, *args, **kwargs):

        def stoppable_traget():
            try:
                self._traget(*args, **kwargs)
            except _Exception_StopThread:
                pass

        self.thread = threading.Thread(target=stoppable_traget)
        self.thread._TD_stop = False
        self.thread.start()


def AsQThread(traget):
    '''Executes traget as a thread'''
    return Treaded_Function(traget)


def check_stop():
    if threading.current_thread()._TD_stop:
        raise _Exception_StopThread()
