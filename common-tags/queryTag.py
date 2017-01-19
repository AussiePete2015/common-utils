#!/usr/bin/env python

__copyright__ = '(c) 2016 DataNexus Inc.  All Rights Reserved.'
__license__ = 'APLv2.0'
__author__ = 'ckeller@datanexus.org'
__version__ = '0.1'

def match_tags (line, args):
    
    app_repo = line.split(',')[0]
    app_repo = app_repo[app_repo.find(':')+1:]    
    app_name = app_repo[app_repo.rfind('/')+1:]
    app_tag=line.split(',')[1].lstrip()
    app_tag = app_tag[app_tag.find(':')+1:]
    
    if str(args.url).lower() == str(app_repo).lower(): return (app_tag)
    if str(args.application).lower() == app_name.lower(): return (app_tag)
    if str(args.tag).lower() == app_tag.lower(): return (app_name)
    
    return None
    
def read_file (args):
    import sys
    
    """read file into in-memory hash"""
   
    try:
        with open(args.db, 'r') as f:
            while True:
                app_line = f.readline()
                if app_line == '': break
                app_line = app_line.partition('#')[0].rstrip()
                if not app_line == '':
                    result = match_tags(app_line, args)
                    if result is not None: print result
    except IOError:
        print "'database %s' not found...exiting" % args.db
        sys.exit(1)
    
def main():
    """Main function"""
    
    import argparse
    import os
        
#     print os.path.dirname(os.path.abspath(__file__)).join("/tagsDB")
    
    parser = argparse.ArgumentParser(description='Query common tag database')
    parser.add_argument('--url', dest='url', help='return the tag associated with the URL')
    parser.add_argument('--app', dest='application',help='return the tag associated with the repository application name')
    parser.add_argument('--tag', dest='tag',help='return the repository application name associated with the tag')
    parser.add_argument('--db', dest='db', default=os.path.dirname(os.path.abspath(__file__)) + "/tagsDB", help='defaults to: %s' % os.path.dirname(os.path.abspath(__file__))+ "/tagsDB")
    
    read_file(parser.parse_args())
    
if __name__ == '__main__': 
    main()
    