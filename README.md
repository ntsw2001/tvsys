# tvsys
A system designed for management of devices in NjtechTV
Version 0.7.202104


Editor: @ntsw2001   github.com/ntsw2001
        @NortheBei  github.com/NortheBei

The project has two parts. First, the backend is based on Django with Django REST Framework. While the frontend is mainly based on Vue.js, along with Webpack.

DIR Structure:
├─ api
├─ app_basic
├─ app_database
├─ app_manage
├─ app_utils
├─ frontend
│  ├─ .babelrc
│  ├─ dist
│  ├─ Makefile
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ postcss.config.js
│  ├─ src
│  ├─ webpack.config.js
│  └─ yarn.lock
├─ manage.py
├─ package-lock.json
├─ requirements.txt
└─ tvsys

Introduction: 1. 'api' is includes some functions for management.
              2. 'app_basic' includes basic functions.
              3. 'app_database' is designed for setting models.
              4. 'app_utils' includes some functions for authentication.
              5. 'frontend' is the main dir for the frontend.
              6. 'tvsys' is the main Diango booting dir.
