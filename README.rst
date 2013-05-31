webexpy
=======

A very solid python wrapper around the Cisco WebEx XML API.  Focuses on the Site Center right now.  Super solid.

Install
-------

This package depends on grequests. If something goes wrong check if you have installed libevent-dev.

For example:

    sudo apt-get install libevent-dev

Usage
-----

Go to http://developer.cisco.com/web/webex-developer/try-webex-apis

anche choose a "Desired WebEx Web Conferencing ID" (for example: foo) and a password (for example: 12345).

Example code:

>>> from sanetime import time
>>> from webex.account import Account
>>> from webex.event import Event
>>> dict_conf = dict(username='testaccount', password='password', site_name='apidemoeu')
>>> account = Account(**dict_conf)
>>> now = time(s=time().s, tz='America/New_York')
>>> starts_at = now + 15*60*10**6
>>> ends_at = now + 30*60*10**6
>>> new_event = Event(account, title='Title', sessionName='session', confName='conf', \
...                   description='descr', starts_at=starts_at, ends_at=ends_at, \
...                   started_at=starts_at, ended_at=ends_at)
>>> new_event.create()
>>> account.get_listed_events(True)

