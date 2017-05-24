# coding=utf-8

# Author: Diego Gonzalez Chavez
# email : diegogch@cbpf.br / diego.gonzalez.chavez@gmail.com

from .threading_decorators import Threaded_Function, as_thread, check_stop

del(threading_decorators)

try:
    import IPython
    if IPython.get_ipython() is not None:  # We are in an IPython session
        try:
            from .matplotlib_qt_signals import Main_Loop_Caller
            gui_safe = Main_Loop_Caller
        except:
            pass
        else:
            del(matplotlib_qt_signals)
except:
    pass
else:
    del(IPython)
