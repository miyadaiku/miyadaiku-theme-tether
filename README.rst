
Tether files for miyadaiku static site generator
========================================================

Provides `tether 1.4.5 <https://www.npmjs.com/package/tether>`__ files.


Installation
-------------------

Use pip command to install tether. 

::

   $ pip install miyadaiku.themes.tether


Configuraion
----------------------


In your config.yml file of your project, add following configuration at `themes` section.

::

   themes:
     - miyadaiku.themes.tether    # <---- add this line


Usage
----------------------

Add following code to your template files.

::

   <!-- include tether.js -->
   {{ tether.load_js(page) }}

