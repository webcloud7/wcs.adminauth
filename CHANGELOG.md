# Changelog

<!--
   You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst
-->

<!-- towncrier release notes start -->

## 2.0.0 (2026-02-23)


### Breaking changes:

- Migrate build system to cookieplone template with pyproject.toml, uv, and ruff.
  Replace setup.py/buildout with pyproject.toml (hatchling), uv for dependency
  management, ruff for linting/formatting, and mxdev for Plone constraints.
  Move source to src/ layout, remove Python 2 artifacts (six, pkg_resources),
  update CI to Plone 6.1 with Python 3.12/3.13, and add towncrier for changelog. [#migration](https://github.com/webcloud7/wcs.adminauth/issues/migration)
