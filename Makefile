all: clean build

build:
	pyinstaller --onefile main.spec

clean:
	rm -rf dist/ build/
