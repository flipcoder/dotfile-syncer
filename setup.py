#!/usr/bin/env python3
import os, sys, shutil, configparser

if os.name == "nt":
    import _winapi

    home = os.environ["HOMEDRIVE"] + os.environ["HOMEPATH"]
else:
    home = os.environ["HOME"]


def confirm(question, default="y"):
    default = default.lower()
    if default == "y":
        options = "Y/n"
    else:
        options = "y/N"
    # TODO: make this a single character read (no endline)
    choice = input("%s (%s)? " % (question, options))
    choice = choice.lower()
    if choice == "":
        CHOICE = DEFAULT
    if choice == "a":
        always = True
    return choice == "y"


def getboolean(config, section, option, default=False):
    try:
        return config.getboolean(section, option)
    except configparser.NoSectionError:
        return default
    except configparser.NoOptionError:
        return default


def recursive_symlink(path):

    config = configparser.ConfigParser()

    # read config first
    for fn in os.listdir(path):
        if fn.lower() == "dotfiles.cfg":
            rel_path = os.path.normpath(os.path.join(path, fn))
            config.read(rel_path)

    for fn in os.listdir(path):
        if fn == ".git":
            continue
        if fn.lower() == "dotfiles.cfg":  # reserve filename for dotfiles config
            continue

        rel_path = os.path.normpath(os.path.join(path, fn))

        # if getboolean(config, fn, "pull"): # pull repos before we recurse
        #    recursive_pull(path)

        # recurse or link here?
        if os.path.isdir(rel_path) and not getboolean(config, fn, "link"):
            recursive_symlink(rel_path)
        else:
            link_path = os.path.join(home, rel_path)

            print("link path: ", link_path)
            if os.path.lexists(
                link_path
            ):  # and confirm("%s already exists. overwrite? " % link_path):
                if os.path.isdir(link_path) and not os.path.islink(link_path):
                    print("rmtree ", link_path)
                    shutil.rmtree(link_path)
                else:
                    print("os.remove ", link_path)
                    os.remove(link_path)

            try:
                os.makedirs(os.path.dirname(link_path))
            except FileExistsError:
                pass

            print("%s <- %s" % (os.path.abspath(rel_path), link_path))
            os.symlink(
                os.path.abspath(rel_path),
                link_path,
                target_is_directory=os.path.isdir(link_path),
            )


# def recursive_pull(path):
#    for fn in os.listdir(path):
#        rel_path = os.path.normpath(os.path.join(path, fn))

#        if fn == ".git":
#            back = os.getcwd()
#            os.chdir(path) # path above .git (rel_path == .../.git)
#            os.system("git pull")
#            os.chdir(back)

#        if os.path.isdir(rel_path):
#            recursive_pull(rel_path)

if __name__ == "__main__":
    if not confirm(
        "Warning: This program will create links, potentially "
        + "overwriting any dotfiles matching between your home directory and "
        "this program's subdirectory 'files'. " + "Do you wish to continue",
        "n",
    ):
        sys.exit(1)

    back = os.getcwd()
    os.chdir("files")
    recursive_symlink(os.path.join("."))
    os.chdir(back)
