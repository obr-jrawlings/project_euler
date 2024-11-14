-include .env
export

# Installation and configuration commands
python-setup:
	@pyenv update
	@pyenv install $(PYTHON_VERSION)
	@pyenv local $(PYTHON_VERSION)
	@echo "Python $(PYTHON_VERSION) installed and set locally."

reqs:
	@call.venv\Scripts\activate && python -m pip install --upgrade pip setuptools wheel
	@call.venv\Scripts\activate && python -m pip install -r requirements.txt
	@echo "======================="
	@echo "Virtual environment successfully created with requirements installed"
	@echo "To activate the venv type '.venv\Scripts\activate'"

venv:
	@make python-setup
	@python3 -m venv .venv
	@echo "Virtual environment '.venv' created."
	@make reqs
