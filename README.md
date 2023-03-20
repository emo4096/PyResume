# PyResume

This project is a rudimentary attempt at creating an automated Resume generator in python.<br>

It's in a very early stage. I am considering restarting this project in another language so it may end up abandoned.

### Dependencies

PyResume (in its current state) depends on two libraries. The first is `tomllib`, which
is included as a builtin library for parsing TOML only in **Python 3.11**, therefore that is the required version of Python.<br>

The second dependency is `fpdf` which is used to generate the PDF file. This can be installed with `pip install fpdf`.

### TODO:

- Implement class to read resume data as input from user.
  Currently, the resume data is hardcoded in `main.py`.

- Potentially turn this into a web application to allow
  anyone to upload text and download a formatted resume.

- Implement Python version and dependency checking/installation


