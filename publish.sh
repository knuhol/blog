#!/bin/bash

BASE_PATH="${HOME}/blog"
PUBLIC_HTML=/var/www/ivadol.cz/public_html
VIRTUALENV="${HOME}/.virtualenvs/pelican"

source $VIRTUALENV/bin/activate && cd $BASE_PATH && make html && cp -R output/. $PUBLIC_HTML
