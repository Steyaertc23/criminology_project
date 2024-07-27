<!-- title: How to setup Criminology Site -->
# How to setup Criminology Site <!-- omit from toc -->


- [Clone this repository](#clone-this-repository)
- [Installing Python 3.10.10](#installing-python-31010)
- [Installing the Packages](#installing-the-packages)
- [Unzip 'Nginx.zip'](#unzip-nginxzip)
- [Installing nginx](#installing-nginx)
- [Running the Site](#running-the-site)


# Clone this repository

To clone this repository, run the following command:
```
git clone https://github.com/Steyaertc23/criminology_site.git
```

# Installing Python 3.10.10

On the vm's terminal, you will need to move into the `criminology_project` directory to install Python and run the program. To do such, run the following commands: 

```
tar -xvzf /path/to/Python-3.10.10.tgz # if you are in the criminology_project directory just run tar -xvzf Python-3.10.10.tgz
cd /path/to/Python-3.10.10/ # or just: cd Python-3.10.10/
./configure
make
sudo make install
```
Make sure to add python to your PATH variable.
If it worked correctly, you should be able to run the `python` or `python3` command, and to exit it, run:
```python
exit() # or quit()
```


# Installing the Packages

To be able to run the site on the vm, you will need to run the following commands in the vm's terminal:
```
# to make sure requirements.zip is in here
ls -ap 
unzip -q requirements.zip
```

You have to install the packages in the following order by using these commands:

```
pip3 install --no-index --find-links /path/to/requirements pycparser # it may be pip instead of pip3
pip3 install --no-index --find-links /path/to/requirements cffi # it may be pip instead of pip3
pip3 install --no-index --find-links /path/to/requirements cryptography # it may be pip instead of pip3
pip3 install --no-index --find-links /path/to/requirements oracledb # it may be pip instead of pip3
pip3 install --no-index --find-links /path/to/requirements typing-extensions # it may be pip instead of pip3
pip3 install --no-index --find-links /path/to/requirements asgiref # it may be pip instead of pip3
pip3 install --no-index --find-links /path/to/requirements sqlparse # it may be pip instead of pip3
pip3 install --no-index --find-links /path/to/requirements django # it may be pip instead of pip3
pip3 install --no-index --find-links /path/to/requirements django-crispy-forms # it may be pip instead of pip3
pip3 install --no-index --find-links /path/to/requirements crispy-forms-foundation # it may be pip instead of pip3
pip3 install --no-index --find-links /path/to/requirements packaging # it may be pip instead of pip3
pip3 install --no-index --find-links /path/to/requirements gunicorn # it may be pip instead of pip3
pip3 install --no-index --find-links /path/to/requirements whitenoise # it may be pip instead of pip3
```

### <strong>IF PIP DOESN'T WORK</strong> <!-- omit in toc -->

If pip doesn't work, in the `requirements` directory, there is a `pip` folder. Move into that folder and run the following commands:

```
tar -xvzf setuptools.71.0.3.tar.gz
python setup.py install
tar -xvzf pip-24.1.2.tar.gz
python setup.py install
```
Then try running the installations again.

# Unzip 'Nginx.zip'

Next, you need to unzip the 'Nginx.zip' folder using the following command:
```
unzip -q Nginx.zip
```

# Installing nginx

Once unzipped, there will be 2 folders called "ubuntu20.04" and "ubuntu22.04". 
Try installing one of the 2 by doing the following:
```
cd /location/of/criminology/ubuntu(version)
```
and going here: <a href="https://docs.nginx.com/nginx-management-suite/installation/vm-bare-metal/offline-install-guide/">Nginx Guide to offline installation</a>, and going to step 3 for the following:
```
tar -kzxvf ./nms-dependencies-ubuntu(version).tar.gz
sudo dpkg -i ./*.deb
```

# Running the Site


In order to run the site, you will need to run Nginx and Gunicorn, then the site itself from there. Use this YouTube Video to help:
<a href="https://youtu.be/YnrgBeIRtvo?si=bEv8kw21n6nYsuRR&t=277">Running the Site</a>

You can choose however many workers you want, the video just had 3. Make sure to copy and paste these lines into the `conf/gunicorn_config.py` file by either using nano or vim (The file is already made for you): 

```py
command = '/path/to/env/bin/gunicorn'
pythonpath = '/path/to/criminology_project/criminology'
bind = 'ip:8000' # change ip to actual ip
workers = 3 # number of workers change if you wish
```

