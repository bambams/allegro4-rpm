RPM_BUILD_ROOT=${HOME}/rpm

.PHONY: all check

all: build check
	
build:
	rm -fR ${RPM_BUILD_ROOT}/RPMS
	rpmbuild -ba allegro.spec

check:
	rpmlint ${RPM_BUILD_ROOT}/RPMS/*/allegro-*.rpm

