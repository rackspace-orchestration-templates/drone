Description
===========

A template that deploys open source Drone.io onto a single Linux server.
Requires you provide a Github Application Client ID and Secret.


Requirements
============
* A Heat provider that supports the following:
  * OS::Nova::KeyPair
  * Rackspace::Cloud::Server
* An OpenStack username, password, and tenant id.
* [python-heatclient](https://github.com/openstack/python-heatclient)
`>= v0.2.8`:

```bash
pip install python-heatclient
```

We recommend installing the client within a [Python virtual
environment](http://www.virtualenv.org/).

Parameters
==========
Parameters can be replaced with your own values when standing up a stack. Use
the `-P` flag to specify a custom parameter.

* `github_client_secret`: The Github Application Client Secret. (Default: '')
* `drone_deb_location`: Location of the Drone Deb File. (Default: http://downloads.drone.io/master/drone.deb
)
* `server_name`: The instance name (Default: drone)
* `image`: Server image used for all servers that are created as a part of this
deployment
 (Default: Ubuntu 14.04 LTS (Trusty Tahr))
* `flavor`: Rackspace Cloud Server flavor to use. The size is based on the amount of
RAM for the provisioned server.
 (Default: 1 GB Performance)
* `github_client_id`: The Github Application Client ID. (Default: '')

Outputs
=======
Once a stack comes online, use `heat output-list` to see all available outputs.
Use `heat output-show <OUTPUT NAME>` to get the value of a specific output.

* `drone_url`: Drone URL 
* `private_key`: SSH Private Key 
* `server_ip`: Server IP 

For multi-line values, the response will come in an escaped form. To get rid of
the escapes, use `echo -e '<STRING>' > file.txt`. For vim users, a substitution
can be done within a file using `%s/\\n/\r/g`.
