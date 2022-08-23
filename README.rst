pl-array_interpolation
================================

.. image:: https://img.shields.io/docker/v/fnndsc/pl-array_interpolation?sort=semver
    :target: https://hub.docker.com/r/fnndsc/pl-array_interpolation

.. image:: https://img.shields.io/github/license/fnndsc/pl-array_interpolation
    :target: https://github.com/FNNDSC/pl-array_interpolation/blob/master/LICENSE

.. image:: https://github.com/FNNDSC/pl-array_interpolation/workflows/ci/badge.svg
    :target: https://github.com/FNNDSC/pl-array_interpolation/actions


.. contents:: Table of Contents


Abstract
--------

An app to ...


Description
-----------


``array_interpolation`` is a *ChRIS ds-type* application that takes in ... as ... files
and produces ...


Usage
-----

.. code::

    docker run --rm fnndsc/pl-array_interpolation array_interpolation
        [-h|--help]
        [--json] [--man] [--meta]
        [--savejson <DIR>]
        [-v|--verbosity <level>]
        [--version]
        <inputDir> <outputDir>


Arguments
~~~~~~~~~

.. code::

    [-h] [--help]
    If specified, show help message and exit.
    
    [--json]
    If specified, show json representation of app and exit.
    
    [--man]
    If specified, print (this) man page and exit.

    [--meta]
    If specified, print plugin meta data and exit.
    
    [--savejson <DIR>] 
    If specified, save json representation file to DIR and exit. 
    
    [-v <level>] [--verbosity <level>]
    Verbosity level for app. Not used currently.
    
    [--version]
    If specified, print version number and exit. 


Getting inline help is:

.. code:: bash

    docker run --rm fnndsc/pl-array_interpolation array_interpolation --man

Run
~~~

You need to specify input and output directories using the `-v` flag to `docker run`.


.. code:: bash

    docker run --rm -u $(id -u)                             \
        -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
        fnndsc/pl-array_interpolation array_interpolation                        \
        /incoming /outgoing


Development
-----------

Build the Docker container:

.. code:: bash

    docker build -t local/pl-array_interpolation .

Run unit tests:

.. code:: bash

    docker run --rm local/pl-array_interpolation nosetests

Examples
--------

Put some examples here!


.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstore.co
