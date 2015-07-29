[![Circle CI](https://circleci.com/gh/rackspace-orchestration-templates/drone/tree/master.png?style=shield)](https://circleci.com/gh/rackspace-orchestration-templates/drone)
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

* `github_client_secret`: Required: The Github Application Client Secret. See
[Creating a new Github application](#creating-a-new-github-application)
(Default: '')
* `drone_deb_location`: Location of the Drone Deb File.
(Default: http://downloads.drone.io/master/drone.deb)
* `server_name`: The instance name (Default: drone)
* `image`: Server image used for all servers that are created as a part of this
deployment (Default: Ubuntu 14.04 LTS (Trusty Tahr))
* `flavor`: Rackspace Cloud Server flavor to use. The size is based on the
amount of RAM for the provisioned server.
 (Default: 1 GB Performance)
* `github_client_id`: Rerquired: The Github Application Client ID. See
[Creating a new Github application](#creating-a-new-github-application)
(Default: '')

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

Configuring Github Oauth for Drone
==================================

## Creating a new Github application

Drone is configured to authenticate using Github. To allow this, you will need
to register a new application at github.com for this deployment. Follow these
steps:

1. Go to Github's [New OAuth Application form](https://github.com/settings/applications/new).
2. Enter a name into the *Application name* field. This is an arbitrary string.
You may wish to use `drone`.
3. Enter a valid URL into the *Homepage URL* field, such as `http://example.com`.
4. Enter another valid URL into the *Application callback URL* field, such as `http://example.com`
5. Click the *Register application* button. You will come to the
*OAuth Application Settings* page for your new application.
6. Note the values at the top of the page: *Client ID* and *Client Secret*
7. Use these two values to populate the `github_client_id` &
`github_client_secret` parameters.

## Updating Github after deployment

Once the deployment is created, edit the Github Application you created before
your deployment to reference the *Homepage URL* and *Authorization callback*
URL for your newly deployed Drone server.

Collect the `server_ip` output from the deployment and follow these steps:

1. Go to https://github.com/settings/applications
2. Select the registered application you created before the deployment
3. Change the *Homepage URL* field to `https://{your_server_ip}/`
3. Change the *Authorization callback URL* field to: `https://{your_server_ip}/api/auth/github.com`
4. Click the *Update application* button.

License
=======
```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
