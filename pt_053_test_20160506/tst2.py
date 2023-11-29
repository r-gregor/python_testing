#! /usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

headers = {	'from' : '<user@example.com>',
		'to' : '<someone_else@example.com>',
		'subject' : 'Test message'}

#  Now the header items can be accessed as a dictionary:
print('To: %s' % headers['to'])
print('From: %s' % headers['from'])
print('Subject: %s' % headers['subject'])
