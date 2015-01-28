# coding=utf8

import re
import os

from fabric.api import env, hide, run, task, get
from envassert import detect, file, package, port, process, service


def drone_is_responding():
    with hide('running', 'stdout'):
        site = "https://localhost/"
        homepage = run("wget --quiet --output-document - --no-check-certificate %s" % site)
        if re.search('Brad Rydzewski', homepage):
            return True
        else:
            return False


@task
def check():
    env.platform_family = detect.detect()

    assert package.installed("drone"), "Package drone is missing."
    assert file.exists("/etc/drone/drone.toml"), "/etc/drone/drone.toml is missing."
    assert file.exists("/etc/drone/ssl/drone.crt"), "SSL certificate missing."
    assert file.exists("/etc/drone/ssl/drone.key"), "SSL key missing."
    assert port.is_listening(443), "Port 443 is not listening."
    assert process.is_up("droned"), "The droned process is not running."
    assert service.is_enabled("drone"), "The drone service is not enabled."
    assert drone_is_responding(), "Drone is not responding."


@task
def artifacts():
    env.platform_family = detect.detect()

    # Logs to pull
    logs = ['/root/cfn-userdata.log',
            '/root/heat-script.log']

    # Artifacts target location
    try:
        os.environ['CIRCLE_ARTIFACTS']
    except:
        artifacts = 'tmp'
    else:
        artifacts = os.environ['CIRCLE_ARTIFACTS']

    # For each log, get it down
    for log in logs:
        target = artifacts + "/%(host)s/%(path)s"
        get(log, target)
