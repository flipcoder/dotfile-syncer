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
- Run ./setup.py (with python3) to create/renew the links.

Additionally, if you have individual files or dirs you want linked INSTEAD of
the whole directory they are contained in, create a dotfiles.cfg next to them.
For each file or folder, add them like this to the dotfiles.cfg ffile (ini format):
```
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
instead of ~/.vim itself.

