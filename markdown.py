# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# gm

# <codecell>

#! /usr/bin/python

import dominate # 'pip install dominate' must be run once before this
from dominate.tags import *
import re # Only needed because dominate doesn't let us set tab indentation
import tempfile
import webbrowser

def generate_html(title, paragraphs):
    page = dominate.document(title=title)
    with page:
        for paragraph in paragraphs:
            p(paragraph)
    return str(page)

def read_paragraphs():
    to_return = {'title': '', 'paragraphs': []}
    to_return['title'] = raw_input("Enter a title:\n")
    print "Enter your paragraph.  Enter a blank line to finish."
    for line in iter(raw_input, ''):
        to_return['paragraphs'].append(line)
    return to_return

if __name__ == '__main__':
    user_input = read_paragraphs()
    html_output = generate_html(user_input['title'], user_input['paragraphs'])
    with tempfile.NamedTemporaryFile(mode='w+t', suffix='.html', delete=False) as out:
        # HACK: This is silly, but dominate doesn't provide a way to change the
        # number of spaces used for a tab, but since it gives us exactly half
        # as many as we want, we can double-up on spaces at start of line and
        # get what we want
        out.write(re.sub(r'^(\s*)', r'\1\1', html_output, flags=re.MULTILINE))
    webbrowser.open(out.name)

# <codecell>


