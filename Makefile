python_version_full := $(wordlist 2,4,$(subst ., ,$(shell python --version 2>&1)))
python_version_major := $(word 1,${python_version_full})
python_version_minor := $(word 2,${python_version_full})
python_version_patch := $(word 3,${python_version_full})

all, chainsaw:
	@echo Using full library test...
	python test.py chainsaw

minify:
	@echo Using the minifier test...
	python test.py minify

loader:
	@echo Using the loader test...
	python test.py loader

install:
	@echo Installing requirements...
	@echo No requirements needed.
