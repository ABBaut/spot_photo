# Deep Learning project - Bootcamp Le Wagon #1035 
- Spot-photo
- Description: Creation of a photo search engine application using several models of Deep Learning, image recognition and “natural language processing”. Building of an API, a Streamlit interface and deployment on the cloud (Docker, GCP).

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for spot-photo in github.com/{group}. If your project is not set please add it:

Create a new project on github.com/{group}/spot-photo
Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "spot-photo"
git remote add origin git@github.com:{group}/spot-photo.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
spot-photo-run
```

# Install

Go to `https://github.com/{group}/spot-photo` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/spot-photo.git
cd spot-photo
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
spot-photo-run
```
