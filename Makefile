NPM := npm
PYTHON := python
FRONTEND_DIR := ./src/apps/dispenser/frontend

all: clean

.PHONY: clean
clean:
	pyclean --verbose .

.PHONY: build/dispenser-backend
build/dispenser-backend:
	$(PYTHON) -m venv .venv
	pip install --no-cache-dir -r requirements.txt

.PHONY: build/dispenser-frontend
build/dispenser-frontend:
	cd $(FRONTEND_DIR) && $(NPM) install three
	cd $(FRONTEND_DIR) && $(NPM) install vite

.PHONY: run/dispenser-backend
run/dispenser-backend:
	$(PYTHON) main.py --context dispenser-backend

.PHONY: run/dispenser-frontend
run/dispenser-frontend:
	cd $(FRONTEND_DIR) && npx vite