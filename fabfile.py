# -*- coding: utf-8 -*-
from fabric.api import task, env, run, local, prompt
from fabric.context_managers import cd, prefix

env.hosts = ['fast.pe.kr']
env.user = 'chat_deploy'


@task
def update():
    with cd('/home/chat_deploy/service/chatchat'):
        run('git pull origin master')
