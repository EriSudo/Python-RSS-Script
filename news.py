#! /usr/bin/env python

import feedparser
print '-----------------------------------------------------'

print 'The Intercept'

print '-----------------------------------------------------'

d = feedparser.parse('https://theintercept.com/feed/?lang=en')

print d['entries'][0]['title'] 

print d.entries[0]['link'] 

print d['entries'][1]['title'] 

print d.entries[1]['link'] 

print d['entries'][2]['title'] 

print d.entries[2]['link'] 

print d['entries'][3]['title'] 

print d.entries[3]['link'] 

print d['entries'][4]['title'] 

print d.entries[4]['link'] 
