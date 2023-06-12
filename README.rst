Introduction
============

This product provides administrative login functionality for Plone sites using
a central authentication server (CAS).

It's goal is to make locally stored passwords for administrative accounts
obsolete and instead authenticate users with their personal, centrally managed
account when logging in with an administrative account to a Plone site.

This is helpful when running a lot of Plone sites and having multiple people
that need administrative access as there's no need to share and manage
administrative passwords.


Compatibility
=============

This package is officially tested with plone 5.1.x and plone 6.
Plone 4.3 should work as well, but is not tested and will not be maintained.


Session authentication plugin
-----------------------------

A session authentication PAS plugin is automatically installed in the Zope root
user folder (acl_users) if needed as the root user folder does not provide any
session-based authentication on default installations. The plugin is based on
``plone.session``.

After installation of the session plugin the password of the user defined in ADMIN_AUTH_USERID
is reset to a random value to disable password-based login.


Installation
============

Add ``wcs.adminauth`` to the list of eggs in your buildout, run buildout and
restart your instance.


Usage
=====

Open the ``@@adminauth`` view in your browser and you will get authenticated as
the ``adminuser`` user.

You can specify a different userid by providing it as an url parameter:
e.g. ``@@adminauth?userid=john``.


CAS Server URL
==============

The CAS Server URL options has to be provided via environment variables.

Example::

    ADMIN_AUTH_CAS_SERVER_URL=https://cas.example.com/

Admin users id
==============

You need to define what user the plugin should use as central admin user (default is admin).

Example::

    ADMIN_AUTH_USERID=admin

Copyright
=========

The package is based on ftw.zopemaster (GNU General Public License, version 2)


``wcs.adminauth`` is licensed under GNU General Public License, version 2.
