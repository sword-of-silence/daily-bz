# This workflow will upload a Python Package using Twine when a release is created
# For more information see: https://help.github.com/en/actions/language-and-framework-guides/using-python-with-github-actions#publishing-to-package-registries

name: Daily Sign On WoZaiXiaoYuan

on:
  push:
    branches:    
      - nhentai
  schedule:
    - cron: '30 12 * * *'

jobs:
  deploy:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        sudo apt install aria2 -y
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: daily sign
      run: |
        python3 doSign.py
    
