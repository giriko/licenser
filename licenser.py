#!/usr/bin/env python

from argparse import ArgumentParser as parser
from datetime import date
import os.path

def add_license():
    p = parser(description='quickly add an open-source license to your project')

    p.add_argument('-l', dest='license', required=True, help='license to add')
    p.add_argument('-e', dest='email', required=True, help='your email address')
    p.add_argument('-n', dest='name', required=True, help='your name')
    p.add_argument('-p', dest='project', required=True, help='project name')
    p.add_argument('--no', action='store_true', required=False, help='removes file extension')

    args = p.parse_args()

    author = args.name + ' <' + args.email + '>'
    year = str(date.today().year)
    project = args.project
    ext = '' if args.no else '.txt'

    try:
        license = open(os.path.join(os.path.abspath("./Licenses/"),args.license)).read()
    except KeyError:
        p.exit(1, 'fatal: license %s does not exist\n' % args.license)

    license = license.format(author=author, year=year, project=project)
    with open('LICENSE' + ext, 'w') as f:
        f.write(license)
if __name__ == '__main__':
    add_license()
