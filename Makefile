PY := python3

all: schema demo

schema:
	$(PY) 1_make_schema.py

demo: 
	$(PY) demo.py

