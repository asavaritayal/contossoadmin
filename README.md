## Prerequisites

To use this sample:

- Install [Python 3.6](https://www.python.org/downloads/)

### Download the sample

```bash
git clone https://github.com/asavaritayal/contossoadmin.git
cd contossoadmin
```

### Create and activate a virtual environment

Run the following commands to create and activate a virtual environment named .env.

```bash
# In Bash
python3.6 -m venv .env
source .env/bin/activate

# In PowerShell
py -3.6 -m venv .env
.env\scripts\activate
```

### Install dependencies

The names and versions of the required packages are already listed in the `requirements.txt` file. Use the following command to install these dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### Test

Use the following command to run the app locally.

```bash
python app.py
```