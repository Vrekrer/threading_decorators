# coding=utf-8

# Author: Diego Gonzalez Chavez
# email : diegogch@cbpf.br / diego.gonzalez.chavez@gmail.com

import matplotlib

_bk = matplotlib.get_backend()
if _bk == 'Qt5Agg':
    from PyQt5 import QtCore
elif _bk == 'Qt4Agg':
    from PyQt4 import QtCore
else:
    raise(ImportError('Matplotlib backend must Qt4Agg or Qt5Agg'))


class Main_Loop_Caller(QtCore.QObject):
    signal = QtCore.pyqtSignal()

    def __init__(self, func):
        super().__init__()
        self.func = func
        self.args = list()
        self.kwargs = dict()
        self.signal.connect(self._target)

    def _target(self):
        self.func(*self.args, **self.kwargs)

    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.signal.emit()
