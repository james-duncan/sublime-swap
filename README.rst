================
Swap
================

Designed for convenience, this package provides a command which will swap recognised words for corresponding words.  For example:

- *true* becomes *false*
- *top* becomes *bottom*

Swap can use more than two values as well:

- left --> right --> center

The plug-in comes with some default swaps, which are arranged by category.  Categories can be enabled and disabled by changing the config (Preferences -> Package Settings -> Swap).  It is recommended that you take a copy of the default settings and place these into the user settings file.  Do NOT make changes in the default settings files, as these changes will be overwritten and lost when the plug-in gets updated.

This plug-in is available under a BSD license.  See "LICENSE.txt" for further details.

The Problem
===========

That a text editor should be clever enough to do this sort of thing for you.

Getting Started
===============

Installation is currently a manual affair.

1.  First, download the source files from https://bitbucket.org/james_duncan/swap/ (the download link can be found on the right hand side of page).
2.  Navigate to the Sublime Text 2 Packages folder (Preferences -> Browse Packages...) and create a new folder called "Swap".
3.  Extract the source files from the downloaded zip into the new "Swap" folder.
4.  Restart Sublime Text 2.

How to Use
==========

Run the following command from the Python console (``Ctrl+```)::

      view.run_command("swap")

Alternatively, you can define a new key binding (Preferences -> Key Bindings -> User) for the command.  For example:

    { "keys": ["super+alt+s"], "command": "swap" }


Defining new swaps
===================

You can add new swaps really easily - just take a look at the existing settings files (Preferences -> Package Settings -> Swap).  As noted above, it is recommended that you take a copy of the default settings file and place this into the user settings file.  Do NOT make changes in the default settings file as these will be overwritten when the plug-in gets updated.  If you make changes if the user settings file, these changes will persist through updates.

Swaps are grouped in categories, and are loaded in the order they appear in the "enabled_categories" option.  If two swaps use the same word, the last one to get loaded will override any previous definitions.  User settings take priority over default settings, and observe the same rules.

Options
==========

1.  "enabled_categories":  Defines which groups of swaps should be used.  See above for how swaps using words already defined in other swaps are handled.
2.  "deselect":  If set to true, the selected text will be un-highlighted after swapping.

Future development
=====================

1.  The ability to scope categories to file types - for example, you could choose to have the categories "dev-generic" and "dev-web" enabled for JavaScript files.  An additional benefit of this will be the provision of a much better way of dealing with duplicate swaps.