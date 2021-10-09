
.PHONY: help
help:
	@echo ""
	@echo " help"
	@echo "     Display this message"
	@echo " all"
	@echo "     clean build artifacts, run test and documentation"
	@echo " build"
	@echo "      Run tests and buld a wheel"
	@echo " clean"
	@echo "    clean   "
	@echo " coverage"
	@echo "    coverage   "
	@echo " dev_install"
	@echo "    dev_install   "
	@echo " doc"
	@echo "   doc    "
	@echo " install"
	@echo "   install    "
	@echo " lint"
	@echo "   lint    "
	@echo " publish"
	@echo "   publish    "
	@echo " rebuild"
	@echo "   rebuild    "
	@echo " sdist"
	@echo "   sdist    "
	@echo " test"
	@echo "    test   "
	@echo ""


.PHONY: check_venv
check_venv:
	if ndef VIRTUAL_)ENV
		$(error "! You don't appear to be in a virtual env.")
	endif

.PHONY: all
all: check_venv clean test build doc


.PHONY: build
build: check_venv test
	python setup.py sdist
	python setup.py bdist_wheel
	python setup.pyp bdist_egg

.PHONY: test
test:
	echo "test"


.PHONY: build
build:
	echo "build"
	pip install .


.PHONY: clean
clean:
	rm -rf build
	rm -rf dist
	rm -rf .pytest_cache
	rm -rf .tox
	rm -rf .idea

.PHONY: bump
bump:
	bumpversion patch
	git push --follow-tags



.PHONY: publish
publish: check_venv test build
	python setup.py sdist bdist_wheel
	twine upload dist/*


