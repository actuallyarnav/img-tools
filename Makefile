PY:=python3
PIP:=pip
build:
	cd img-tools && cp -n .env.example .env && $(PIP) install --no-cache-dir -r requirements.txt


run: build
	cd img-tools && $(PY) app.py
