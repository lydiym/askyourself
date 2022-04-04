# Self-Documented Makefile see https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

PATCH_FILE_NAME:=BroadcastReceiver.patch
P4A_DIR:=.buildozer/android/platform/python-for-android
PATCHED_FILE:=$(P4A_DIR)/pythonforandroid/bootstraps/common/build/templates/BroadcastReceiver.tmpl.java
SHELL:=/bin/bash

.DEFAULT_GOAL:=help
.PHONY: help debug release clean

debug: ## Build debug version
	buildozer -v android debug

release: ## Build release version
	buildozer -v android release

clean: ## Cleanup all build files
	buildozer appclean

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
