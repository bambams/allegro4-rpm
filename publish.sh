#!/usr/bin/env bash

root=${1:-$HOME/src/allegro/4-rpm}
rpm_tree=${2:-$HOME/rpm}
other_rpm_tree="`echo $rpm_tree | sed -r 's,\brpm\b,rpmbuild,'`"

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

spec=allegro.spec
version=`grep -A 1 changelog "$spec" |
        tail -n 1 |
        sed -r 's,.*([0-9]+\.[0-9]+\.[0-9]+-[0-9]+),\1,'`

remote=castopulence.org
dest="/var/www/rpm/allegro/$version/"

srpm="allegro-$version.fc13.src.rpm"
sha1="$root/SHA1SUM"

echo "Publishing $version to $host:$dest..."
read -p "Continue (Y/n) " answer

if [ "$answer" != y -a "$answer" != Y ]; then
    echo "Aborting..." 1>&2
    exit 1
fi


if [ ! -d "$rpm_tree" ]; then
    if [ "$rpm_tree" != "$HOME/rpm" ]; then
        echo "Aborting..." 2>&1
        exit 1
    fi
    echo "Failed to find '$rpm_tree' tree... Trying 'rpmbuild'..." 1>&2
    if [ -d "$other_rpm_tree" ]; then
        rpm_tree="$other_rpm_tree"
    else
        echo "Failed to find '$other_rpm_tree' tree... Skipping removal." 1>&2
    fi
fi

if [ -d "$rpm_tree" ]; then
    read -p "Remove '$rpm_tree' tree? (Y/n) " answer
    if [ "$answer" == y -o "$answer" == Y ]; then
        rm -fR "$rpm_tree"
    fi
fi

./init.sh

if [ ! -d "$rpm_tree" ]; then
    echo "Can't find '$rpm_tree' tree... Aborting..." 1>&2
    exit 1
fi

read -p "Rebuild? (Y/n) [n] " answer;

if [ "$answer" == y -o "$answer" == Y ]; then
    /usr/bin/make
fi

(cd "$rpm_tree/SRPMS" &&
        /usr/bin/sha1sum "$srpm" 1>"$sha1") &&
        /usr/bin/sha1sum "$spec" 1>>"$sha1" &&
        /usr/bin/ssh "$remote" /bin/mkdir -p "$dest"
        /usr/bin/scp "$sha1" "$remote:$dest" &&
        /usr/bin/scp "$spec" "$remote:$dest" &&
        (cd "$rpm_tree/SRPMS" &&
        /usr/bin/scp "$srpm" "$remote:$dest")

