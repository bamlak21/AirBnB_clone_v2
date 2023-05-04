#!/usr/bin/python3
"""destribute an archive to a web server"""

from fabric.api import *
import os
import os.path
import datetime
env.hosts = ['100.25.12.18', '54.196.181.206']


def do_pack():
    """compress + bundle local sweb files"""
    try:
        if os.path.isdir("versions") is False:
                os.mkdir("versions")
        time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        packed = 'versions/web_static_' + time + '.tgz'
        fabric.api.local("tar -cvzf {} web_static".format(packed))
        return packed
    except:
        return None


def do_deploy(archive_path):
    """deploy an archive from the archive_path"""
    if os.path.exists(archive_path) is False:
        return False

    file_name = os.path.splitext(os.path.split(archive_path)[1])[0]
    target = '/data/web_static/releases/' + file_name
    path = archive_path.split('/')[1]
    try:
        put(archive_path, "/tmp/")
        run('sudo mkdir -p ' + target)
        run('sudo tar -xzf /tmp/' + path + ' -C ' + target + '/')
        run('sudo rm /tmp/' + path)
        run('sudo mv ' + target + '/web_static/* ' + target + '/')
        run('sudo rm -rf ' + target + '/web_static')
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s ' + target + '/ /data/web_static/current')
        print('deploy success')
        return True
    except:
        return False
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["100.25.12.18", "54.196.181.206"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True
