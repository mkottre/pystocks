pystocks
========

Pystocks is a simple utility that can be used to gather basic information about a certain stock. It gathers its data from Yahoo Finance.

Usage
========

Pystocks requires Python 3 and ystockquote >= 0.2.5 which is currently not available on PyPI so must be acquired through github.

	git clone git://github.com/cgoldberg/ystockquote.git
	cd ystockquote
	python setup.py install

After ystockquote is installed, pystocks should be able to run with the command:

	python pystocks.py
