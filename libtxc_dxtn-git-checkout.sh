#!/bin/sh

VERSION=1.0.1

git clone git://people.freedesktop.org/~mareko/libtxc_dxtn libtxc_dxtn
cd libtxc_dxtn

REVISION=$(git log | head -n1 | awk '{print $2}' | cut -c 1-8)

rm -fr .git
cd ..
tar -cjf libtxc_dxtn-${VERSION}-git${REVISION}.tar.bz2 libtxc_dxtn
rm -fr libtxc_dxtn
