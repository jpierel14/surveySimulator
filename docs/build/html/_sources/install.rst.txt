************
Installation
************

SNSEDextend works on Python 2.7 and Python 3.4+ and requires the
following Python packages:

- `numpy <http://www.numpy.org/>`_
- `scipy <http://www.scipy.org/>`_
- `astropy <http://www.astropy.org>`_
- `SNCosmo <http://sncosmo.readthedocs.io>`_

Install using pip
=================

Using pip::

    pip install surveySim

.. note::

    You will need a C compiler (e.g. ``gcc`` or ``clang``) to be
    installed for the installation to succeed due to SNCosmo.


Install latest development version
==================================

SNSEDextend is being developed `on github
<https://github.com/surveySim>`_. To get the latest development
version using ``git``::

    git clone git://github.com/surveySim.git
    cd surveySim

then::

    python setup.py install
