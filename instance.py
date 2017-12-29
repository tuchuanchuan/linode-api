# coding: utf-8
import json
import logging

import paramiko

from base import Base


class Instance(Base):
    url = 'https://api.linode.com/v4/linode/instances'

    def __init__(self, id=None):
        if id:
            resp = self.fetch(self.url+'/'+str(id), method='get').json()
        else:
            data = dict(
                region='us-east-1a',
                type='g5-standard-1',
                # label='youtube',
                group='spider',
                root_pass='www8508com',
                image="linode/ubuntu16.04lts",
            )
            resp = self.fetch(self.url, method='post', data=data).json()
        print resp
        self.id = resp['id']
        self.base_url = self.url+'/'+str(self.id)
        self.label = resp['label']
        self.ipv4 = resp['ipv4']
        self.region = resp['region']

    @property
    def status(self):
        resp = self.fetch(self.base_url, 'get').json()
        return resp['status']

    @classmethod
    def list_all(cls):
        resp = cls.fetch(cls.url, 'GET')
        print(resp.json())

    def boot(self):
        url = self.base_url + '/boot'
        self.fetch(url, 'POST')

    def clone(self, region='us-east-1a', _type='g5-standard-1', label='youtube', group='spider'):
        url = self.base_url + '/clone'
        data = dict(
            region=region,
            type=_type,
            label=label,
            group=group,
        )
        resp = self.fetch(url, method='post', data=data).json()
        return Instance(resp['id'])

    def reboot(self):
        url = self.base_url + '/reboot'
        self.fetch(url, 'POST')

    def shutdown(self):
        url = self.base_url + '/shutdown'
        self.fetch(url, 'POST')

    def delete(self):
        self.fetch(self.base_url, method='delete')

    def ssh_cmd(self, cmd_list):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ipv4[0], 22, 'root', 'www8508com', timeout=100)
        for m in cmd_list:
            print m
            stdin, stdout, stderr = ssh.exec_command(m)
            out = stdout.readlines()
            for o in out:
                print o
        ssh.close()

    def init_env(self):
        self.ssh_cmd(['apt update', 'apt install -y docker.io python-pip', 'systemctl start docker', 'docker run -d --net=host --restart=always -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-firefox:3.8.1-bohrium', 'curl -O https://raw.githubusercontent.com/tuchuanchuan/linode-api/master/1.py', 'pip install selenium', 'nohup python 1.py > out 2>&1 &'])
