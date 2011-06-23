#!/usr/bin/env bash

root=${1:-$HOME/src/allegro/4-rpm}
rpm_tree=${2:-$HOME/rpm}
src_path="$rpm_tree/SOURCES/allegro-4.4.2.tar.gz"
src_sha1=ae0c15d2cb6b0337ef388dc98cefc620883720df
src_url=http://downloads.sourceforge.net/project/alleg/allegro/4.4.2/allegro-4.4.2.tar.gz

if [ "`echo $root | grep '^/'`" != "$root" -o $? != 0 ]; then
    echo "Your project root path '$root' doesn't appear to be " 1>&2
    echo "absolute. I quit." 1>&2
    exit 1
fi

if [ "`/bin/pwd`" != "$root" ]; then
    echo "This script is designed to be used from the root of the " 1>&2
    echo "project. You can override that path by passing an " 1>&2
    echo "argument to the script. For example:" 1>&2
    echo "  ./init.sh \`pwd\`" 1>&2
    exit 1
fi

if [ ! -d .git ]; then
    echo "Ummm, I don't see .git here. This script isn't very smart so"
    echo "I'd recommend that you use it as it was intended."
    read -p "Try anyway? (Y/n) " answer
    if [ "$answer" != y -a "$answer" != Y ]; then
        echo "Aborting..." 1>&2
        exit 1
    fi
fi

if [ -d "$rpm_tree" ]; then
    echo "It seems rpm tree '$rpm_tree' already exists..."
    read -p "Would you like me to setup tree anyway? (Y/n) " answer
    if [ "$answer" != y -a "$answer" != Y ]; then
        skip_setuptree=1
    fi
fi

if [ ! "$skip_setuptree" == 1 ]; then
    echo "Setting up rpm tree..."
    /usr/bin/rpmdev-setuptree
fi

if [ ! -d "$rpm_tree" ]; then
    echo "Failed to find '$rpm_tree' tree... Trying 'rpmbuild'..." 1>&2
    echo "In the future you can save time by specifying the rpm " 1>&2
    echo "build tree as the second argument to this script." 1>&2
    "$0" "$root" "`echo $rpm_tree | sed -r 's,\brpm\b,rpmbuild,'`"
    exit $?
fi

echo "Creating .spec symlinks in '$rpm_tree/SPECS'..."
for f in $root/*.spec; do
    /bin/ln -fs "$f" "$rpm_tree/SPECS/"
done

if [ -f "$src_path" ]; then
    echo "Source tarball exists... Checking SHA1..."
    if [ `/usr/bin/sha1sum "$src_path" | sed -r 's/^([^ ]*).*/\1/'` == "$src_sha1" ]; then
        echo "SHA1 matches..."
        skip_src=1
    else
        echo "SHA1 doesn't match..."
        read -p "Would you like me to fetch the source for you? (Y/n) " answer
        if [ "$answer" != y -a "$answer" != Y ]; then
            skip_src=1
        fi
    fi
fi

if [ ! "$skip_src" == 1 ]; then
    echo "Fetching source tarball..."
    /usr/bin/wget -O "$src_path" "$src_url"
fi

