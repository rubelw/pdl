
.PHONY: help
help:
	@echo ""
	@echo " help"
	@echo "     Display this message"
	@echo " clean"
	@echo "    clean   "
	@echo " coverage"
	@echo "    coverage   "
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
    if test "$(VIRTUAL_ENV)" == ""; then \
        echo "VIRTUAL_ENV not set"; \
        exit 1; \
    fi


.PHONY: test
test:
	pytest



.PHONY: clean
clean:
	rm -rf build
	rm -rf dist
	rm -rf .pytest_cache
	rm -rf .tox
	rm -rf tests/__pycache__

.PHONY: bump
bump:
	bumpversion patch
	git push --follow-tags



.PHONY: publish
publish: check_venv test
	python setup.py sdist bdist_wheel
	twine upload dist/*


