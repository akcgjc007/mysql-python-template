PY := python3

all: 1 2

1:
	$(PY) 1_make_schema.py
	@echo "---Schema created successfully."

2: 
	$(PY) 2_insert_entries.py
	@echo "---Demo entries added successfully."

start: 
	sudo service mysql start

stop:
	sudo service mysql stop

restart:
	sudo service mysql restart

status:
	sudo service mysql status
