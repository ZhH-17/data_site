from django.db import models
from django.db.models.signals import post_init
import os
import glob
from .settings import DATA_BASEPATH


# Create your models here.
class Record(models.Model):
    index = models.CharField(max_length=30)
    record_date = models.DateTimeField('date recorded')
    wl_step = models.IntegerField(default=0)
    wl_start = models.IntegerField(default=0)
    wl_end = models.IntegerField(default=0)
    operator = models.CharField(max_length=30)
    datapath = models.CharField(max_length=20, default="None")
    exist = models.IntegerField(default=0)
    data_time = models.CharField(max_length=20, default="None")

    def __str__(self):
        return self.index


def extraInitForRecord(**kwargs):
    instance = kwargs.get('instance')
    datapath = os.path.join(DATA_BASEPATH, instance.index)
    if len(instance.index) > 0 and os.path.isdir(datapath):
        dirs = [os.path.join(datapath, d) for d in os.listdir(datapath)
                if os.path.isdir(os.path.join(datapath, d))
                and d[:4].isnumeric()]
        dirs.sort()
        instance.datapath = dirs[-1]
        instance.exist = 1
        instance.data_time = os.path.basename(dirs[-1])
        fns = [fn for fn in
               glob.glob(os.path.join(dirs[-1], "[0-9][0-9][0-9][0-9]_*.bmp"))]
        wls = list(set([int(os.path.basename(fn)[:4]) for fn in fns]))
        instance.wl_start = min(wls)
        instance.wl_end = max(wls)
        instance.wl_step = (instance.wl_end - instance.wl_start) // (len(wls) - 1)

    print(datapath)


post_init.connect(extraInitForRecord, Record)
