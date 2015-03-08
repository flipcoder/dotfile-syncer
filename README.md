# dotfile-syncer

This script creates symlinks between system dotfiles and a single synced folder.
It is intended for Linux, but may be used with other POSIX-compatible systems.

It works with Dropbox, Btsync, and compatible syncing programs.

Make sure you have backups of your home directory and any dotfiles before usage.
As with any script, I cannot guarentee this program is bug-free, however I use it myself without problem.

## Usage

- Store this folder in a synced directory (Dropbox, Btsync, etc.)
- Create 'files' directory next to this script and readme file.
- Put your dotfiles in the 'files' directory that you've created, assuming they
will be created relative to your home directory (files/.link -> ~/.link).
- Run ./setup.py (with python2) to create/renew the links.

Additionally, if you have individual files or dirs you want linked INSTEAD of
the whole directory they are contained in, create a dotfiles.cfg next to them.
For each file or folder, add them like this to the dotfiles.cfg (ini format):
``
    [NAME_HERE]
    link=true
```
Where "NAME_HERE" is the name of the item.

For example, files/.vim/dotfiles.cfg may contain:
```
[snippets]
link=true
[colors]
link=true
```

This indicates ~/.vim/snippets ~/.vim/colors will be created as their own links,
instead ~/.vim itself.

## LICENSE

The MIT License (MIT)

Copyright (c) 2013 Grady O'Connell

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

