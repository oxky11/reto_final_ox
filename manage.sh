#!/bin/bash
# Requires the database to be up
FLASK_ENV=development DATABASE_URI=postgresql://postgres:postgres@127.0.0.1:5432/app-db python manage.py