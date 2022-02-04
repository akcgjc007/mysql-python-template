PY := python3

all: 1 2

1:
	$(PY) 1_make_schema.py

2: 
	$(PY) 2_insert_entries.py

