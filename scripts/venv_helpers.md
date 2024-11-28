# ======================= #
#      venv SECTION       #
# ======================= #

# init .venv (Mac/Linux) / Windows (?)
python3 -m venv .venv

# activate .venv (Mac/Linux) / Windows (?)
source venv/bin/activate

# install venv requirements (Mac/Linux) / Windows (?)
pip install -r pip_freeze/requirements.txt

# freeze venv requirements  (Mac/Linux) / Windows (?)
pip freeze > pip_freeze/requirements.txt

