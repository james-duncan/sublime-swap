================
Swap
================

Designed for convenience, this package provides a command which will swap a recognised word for a related word.  For example:

- true *becomes* false
- top *becomes* bottom

Swap can use more than two values as well:

- left --> right --> center
 
The Problem
===========

For those times when you're editing text by changing "left" to "right", or "top" to "bottom", and you think:

*"It'd be nice if something just did this for me..."*

Getting Started
===============

- Install `%(package_name)s`_

.. _%(package_name)s: https://

If you're running a full installation of Sublime Text, simply doublelick on the
``.sublime-package`` file. If you're running a portable installation, you need
to perform an `installation by hand`_.

.. _installation by hand: http://sublimetext.info/docs/extensibility/packages.html#installation-of-packages-with-sublime-package-archives

Once installed, run the following command from the Python console (``Ctrl+```)::

      view.run_command("COMMAND")

Alternatively, you can define a new key binding for this command.

How to Use
==========

