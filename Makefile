.PHONY: run clean
# Generate the filesystem
run:
	python3 main.py


# clean the filesystem
clean:
	rm -rf generated_filesystem

