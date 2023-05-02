Introduction
============

This product provides administrative login functionality for Plone sites using
a central authentication server (CAS).

It's meant only for installations maintained by 4teamwork as it provides
administrative privileges for users that can authenticate with the 4teamwork
CAS.

It's goal is to make locally stored passwords for administrative accounts
obsolete and instead authenticate users with their personal, centrally managed
account when logging in with an administrative account to a Plone site.

This is helpful when running a lot of Plone sites and having multiple people
that need administrative access as there's no need to share and manage
administrative passwords.

Session authentication plugin
-----------------------------

A session authentication PAS plugin is automatically installed in the Zope root
user folder (acl_users) if needed as the root user folder does not provide any
session-based authentication on default installations. The plugin is based on
``plone.session``.

After installation of the session plugin the password of the user zopemaster
is reset to a random value to disable password-based login.


Installation
============

Add ``ftw.zopemaster`` to the list of eggs in your buildout, run buildout and
restart your instance.


Usage
=====

Open the ``@@zauth`` view in your browser and you will get authenticated as
the ``zopemaster`` user.

You can specify a different userid by providing it as an url parameter:
e.g. ``@@zauth?userid=john``.


Options
=======

Configuration options can be provided via the ``zope-conf-additional`` section.

Example::

    zope-conf-additional =
       <product-config wcs.adminuser>
           cas_server_url https://cas.example.com/
       </product-config>


Currently the following options are supported:

cas_server_url
  The URL of the central authentication server (CAS). Defaults to https://auth.4teamwork.ch


Links
=====

- Main project repository: https://git.4teamwork.ch/ftw/ftw.zopemaster
- Issue tracker: https://git.4teamwork.ch/ftw/ftw.zopemaster/issues


Copyright
=========

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``ftw.zopemaster`` is licensed under GNU General Public License, version 2.
