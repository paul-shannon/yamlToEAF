default:
	@echo python3 -m venv ~/github/slexil2/py3105
	@echo source ~/github/slexil2/py3105/bin/activate
	@echo targets: all [basic-2-lines, 2-lines-one-lacks-morphemes]

all: basic-2-lines   2-lines-one-lacks-morphemes

basic-2-lines:
	python ~/github/yamlToEAF/toEAF.py bearAndAnt-2-complete-lines.yaml

2-lines-one-lacks-morphemes:
	python ~/github/yamlToEAF/toEAF.py bearAndAnt-2-lines-1-lacks-morphemes.yaml


