# Agile Course File System Generator

## Overview
This project is designed to create a structured file system for an Agile course based on a YAML configuration file. It automates the creation of directories, files, and content using predefined assets and markdown text specified in the YAML. The generated structure supports course material organization, making it easier for tutors to manage and deliver Agile-related topics.

## Features
- **Automated Directory and File Creation**: Generates a hierarchical file structure for each topic, unit, and talk based on the YAML configuration.
- **Content Population**: Populates markdown files with content defined in the YAML file, allowing for predefined instructional material and notes.
- **Asset Management**: Copies assets such as images, PDFs, and other resources from a specified assets directory to the corresponding locations in the generated file system.
- **Customizable Structure**: Allows for flexible course design by modifying the YAML structure, enabling the creation of different course layouts and content.



## How to Use
1. **Prepare the YAML File**: Define the course structure in a YAML file (`filesystem.yaml`), specifying directories, files, and markdown content.
2. **Place Assets in the Directory**: Ensure that all required assets (e.g., images, PDFs) are available in the `assets` directory.
3. **Run the Script**: `make clean && make run`
4. Transfer the generated filesystem to your tutors project and procede as normal

