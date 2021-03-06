PyScaffold
==========

PyScaffold helps you to easily setup a new Python project, it is as easy as::

    putup my_project

Type ``putup -h`` to learn about more configuration options.
The scaffold of ``my_project`` provides you with following features:

Packaging
---------

Run ``python setup.py sdist``, ``python setup.py bdist`` or
``python setup.py bdist_wheel`` to build a source, binary or wheel
distribution.


Complete Git integration
------------------------

Your project is already an initialised Git repository and ``setup.py`` uses
the information of tags to infer the version of your project with the help of
versioneer.
To use this feature you need to tag with the format ``vMAJOR.MINOR.REVISION``,
e.g. ``v0.0.1`` or ``v0.1``. The prefix ``v`` is needed!
Run ``python setup.py version`` to retrieve the current version. The version
will be ``unknown`` until you have added a first tag.


Sphinx documentation integration
--------------------------------

Build the documentation with ``python setup.py docs`` and run doctests with
``python setup.py doctest``. Start editing the file ``docs/index.rst`` to
extend the documentation.


Unittest integration
--------------------

Run ``python setup.py test`` to run all unittests defined in the subfolder
``tests`` with the help of `py.test <http://pytest.org/>`_.


Requirements management
-----------------------

Add the requirements of your project to the ``requirements.txt`` file which
will be automatically used by ``setup.py``.


.. note::
    PyScaffold assumes that you have `git  <http://git-scm.com/>`_ installed
    and set up on your PC.
