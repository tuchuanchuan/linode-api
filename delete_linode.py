# coding: utf-8

from instance import Instance

with open('linodes') as f:
    for line in f:
        id = line.strip()
        if id:
            ins = Instance(id)
            ins.delete()
