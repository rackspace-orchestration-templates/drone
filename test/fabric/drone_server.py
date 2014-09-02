# coding=utf8

import re

from fabric.api import env, hide, run, task
from envassert import detect, file, package, port, process, service


def drone_is_responding():
    with hide('running', 'stdout'):
        site = "https://localhost/"
        homepage = run("wget --quiet --output-document - --no-check-certificate %s" % site)
        if re.search('Login · drone.io', homepage):
            return True
        else:
            return False


@task
def check():
    env.platform_family = detect.detect()

    assert package.installed("drone")
    assert file.exists("/etc/default/drone")
    assert file.exists("/etc/drone/ssl/drone.crt")
    assert file.exists("/etc/drone/ssl/drone.key")
    assert port.is_listening(443)
    assert process.is_up("droned")
    assert service.is_enabled("drone")
    assert drone_is_responding()
