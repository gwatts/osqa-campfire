osqa-campfire
=============

OSQA module to publish questions &amp; answers to Campfire

(c) Gareth Watts 2013
&lt;gareth@omnipotent.net&gt;

Licensed under the Apache 2.0 license.


## Installation

1. Install Camplight from https://github.com/mlafeldt/camplight
1. Install this project into OSQA's forum_modules directory:
    ```bash
    cd osqa/forum_modules
    git clone git@github.com:gwatts/osqa-campfire.git
    ```

1. Configure from the OSQA admin interface.


### Note for bitnami users

To install Camplight, make sure to switch to the OSQA context first:

```bash
sudo bash
cd /opt/bitnami
./use_osqa
git clone git://github.com/mlafeldt/camplight.git
cd camplight/
python setup.py install
```
