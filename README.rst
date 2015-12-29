========
sutasshu
========

.. code-block:: bash

    $ virtualenv -p /usr/bin/python3 env
    $ source env/bin/activate
    $ sudo dnf install libtiff-devel libjpeg-devel libzip-devel \
          freetype-devel lcms2-devel libwebp-devel tcl-devel tk-devel \
          python3-devel
    $ pip install -r requirements.txt
