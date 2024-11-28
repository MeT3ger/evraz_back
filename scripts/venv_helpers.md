# ======================= #
#      venv SECTION       #
# ======================= #

# init .venv (Mac|Linux) / Windows
Linux: python3 -m venv .venv

Windows: python -m venv .venv

# activate .venv (Mac|Linux) / Windows
All: source .venv/bin/activate

# install venv requirements (Mac|Linux) / Windows
All: pip install -r pip_freeze/requirements.txt

# freeze venv requirements (Mac|Linux) / Windows
All: pip freeze > pip_freeze/requirements.txt

