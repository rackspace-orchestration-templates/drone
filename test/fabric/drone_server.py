@task
def check():
    assert package.installed("drone")
    assert file.exists("/etc/default/drone")
    assert file.exists("/etc/drone/ssl/drone.crt")
    assert file.exists("/etc/drone/ssl/drone.key")
    assert port.is_listening(443)
    assert process.is_up("droned")
    assert service.is_enabled("droned")
