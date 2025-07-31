## Introduction
This is a Flask app to perform operations on images.

## Functionality
1. rotate images
2. download images
3. (just this for now, more coming soon probably)

## Prerequisites
- python 3.6+
- `pip`

## How to install

`git clone https://github.com/actuallyarnav/img-tools.git`

`make run`

Then, open `localhost:8000` on a web browser.

## Uploads

Uploaded images are saved to:

`{PROJECT_ROOT}/static/uploads/`

## Notes

Files without extensions will not be properly detected, as the app looks for the file extension to determine if it's a valid image file or not.
Definitely not an ideal way to do that, will get fixed later

Flask’s app.secret_key is loaded via .env file (see .env.example).

## TODO

Crop tool

Resize images

Drag-and-drop uploads

History of uploaded images
