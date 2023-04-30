run:
	docker run -it --rm -p 5000:5000 telecom_carrier

build:
	docker build --no-cache -t telecom_carrier .

pep8: black
	flake8 ./telecom_carrier --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 ./telecom_carrier --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

black:
	black  telecom_carrier -l79

test:
	docker run -it telecom_carrier pytest .