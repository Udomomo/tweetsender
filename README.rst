tweetsender
===========

.. image:: https://img.shields.io/github/license/Udomomo/tweetsender.svg
   :target: https://github.com/Udomomo/tweetsender/blob/master/LICENSE.txt
  
.. image:: http://img.shields.io/pypi/v/tweetsender.svg
   :target: https://pypi.python.org/pypi/tweetsender

tweet-only Twitter CLI

When to use
-----------

-  When you want to tweet while coding
-  But don’t want to be distracted by your friend’s posts

Installation
------------

Before installing, download and install python3. 3.6 or higher is
required. Installation is done with ``pip install`` command.
Installation to ``venv`` environment is recommended.

::

   python -m venv myenv
   source myenv/bin/activate
   pip install tweetsender

Creating a Twitter app
----------------------

Before posting tweet, you need to create your Twitter app at
https://apps.twitter.com. After creating an app, open “permissions” tab
and select “Read and Write”. You may need to link your phone number to
your Twitter account. Open “Keys and Access Tokens”, and check your
Consumer Key, Consumer Secret, Access Token, and Access Token Secret. Do
not post them online.

Config
------

If you use this CLI for the first time, you need to use ``tweet config``
and type your API keys. The keys are saved in
``.tweetsender_config.json`` on your home directory.

Usage
-----

-  ``tweet send`` \|\| ``tweet s``

   -  send tweet

-  ``tweet config``

   -  config your API keys

-  ``tweet -s``

   -  set your Twitter API Token

-  ``tweet -h``

   -  show help
