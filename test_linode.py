# coding: utf-8
import time
from multiprocessing import Process

from instance import Instance


def create_new_linode(linde_id=None):
    j = Instance(linde_id)

    while j.status != 'running':
        time.sleep(5)

    time.sleep(5)
    j.init_env()
    # j.ssh_cmd(['nohup python 1.py > out 2>&1 &'])


id_list = [4828542, 4828628, 4828629, 4828630, 4828632, 4828633, 4828634, 4828635, 4828636, 4828638, 4828639]


for i in id_list:
    p = Process(target=create_new_linode, args=(i, ))
    p.start()
    break
