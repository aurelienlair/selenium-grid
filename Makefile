.DEFAULT_GOAL:=help
CUR_DIR:=$$(pwd)
export PIPENV_VENV_IN_PROJECT=true

help:
	@echo "❓ helps section"
	grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install-virtual-env: ## 🛠️ Install Python virtual environment
	@echo "🌐 installing python virtual environment"
	pipenv install

activate-virtual-env: ## 🔌 Activate Python virtual environment
	@echo "🔌 activating python virtual environment"
	pipenv shell

echo-virtual-env: ## 🗨️ Echo Python virtual environment
	@echo "🐍 Python virtual environment present in $(VIRTUAL_ENV)"

compose-logs: ## 📑 Show docker 🐳 containers logs
	@echo "📑 looking for docker 🐳 logs"
	@if [ "$(filter-out chrome firefox,$(strip $(param)))" = "" ]; then \
		echo "$(param)"; \
	else \
		docker-compose logs -f; \
	fi
	echo "here"

compose-down: ## 🛑 Shut down docker 🐳 services
	@echo "🛑 shutting down docker 🐳 services"
	docker-compose down

compose-up: ## 🏃 Start docker 🐳 services
	@echo "🏃 starting docker 🐳 services"
	docker-compose up -d

open-selenium-grid-dashboard: ## 📊 Open Selenium grid dashboard
	@echo "🕸️ opening Selenium grid dashboard"
	open http://selenium-hub:4444/ui

chromium-version: ## 🏃 Echo Chromium version 
	docker exec -it selenium-grid-chromium-1 bash -c 'chromium --version'

chromium-grid-run: ## ▶️ Run tests with Chromium
	@echo "✅🧪 running tests on Chromium with Selenium grid"
	BROWSER=chrome pytest tests/test_google_search.py

firefox-version: ## 🏃 Echo Firefox version 
	docker exec -it selenium-grid-firefox-1 bash -c 'firefox --version'

firefox-grid-run: ## ▶️ Run tests with Firefox
	@echo "✅🧪 running tests on Firefox with Selenium grid"
	BROWSER=firefox pytest tests/test_google_search.py

firefox-run: ## ▶️ Run tests with Firefox
	@echo "✅🧪 running tests on Firefox"
	pytest tests/test_google_search.py