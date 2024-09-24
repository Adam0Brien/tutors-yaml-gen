# Tutors Course File System Generator

## Overview
This project is designed to create a structured file system for tutors courses based on a YAML configuration file. 

## Features
- **Automated Directory and File Creation**: Generates a hierarchical file structure for each `topic`, `unit`, and `talk` based on the YAML configuration.
- **Content Population**: Populates files with content defined `assets/markdown` that can be called in the YAML file, allowing for predefined instructional material and notes.
- **Asset Management**: Copies assets such as images, PDFs, and markdown from a specified assets directory to the corresponding locations in the generated file system.
- **Customizable Structure**: Allows for flexible course design by modifying the YAML structure, enabling the creation of different course layouts and content.



## How to Use
1. **Prepare the YAML File**: Define the course structure in a YAML file (`filesystem.yaml`), specifying directories, files, and markdown content.
2. **Place Assets in the Directory**: Ensure that all required assets (e.g., images, PDFs) are available in the `assets` directory.
3. **Run the Script**: `make clean && make run`
4. Transfer the generated filesystem to your tutors project and procede as normal

## Example yaml file
- This generates the folder structure for a single topic of a course, which contains a lecture with a slidedeck along with a talk with different sections

```yaml
calendar.yaml: []
course.md: ["# Course Overview", "This course provides a comprehensive understanding of Agile methodologies."]
'course.png': []
json:
  calendar.yaml: []
  'course.png': []
  index.html: []
  netlify.toml: []
  properties.yaml: []
  topic-01-introduction-to-agile:
    'agile.png': []
    'typical.md': ["# Introduction to Agile", "Agile is a set of principles that encourage adaptive planning."]
    unit-1:
      'main.md': ["# Unit 1: Introduction", "This unit introduces the core concepts of Agile and its benefits."]
      talk-1-agile-overview:
        'Agile&Scrum.pdf': []
        'agile.png': []
        'agile-overview.md': ["agile-overview"] ## assets/markdown/agile-overview.md
      book-a-scrum-board:
              archives:
                'archive.zip': []
              img:
                'scrum-board.png': []
              '00.Section1.md': ["scrum-overview"] ## assets/markdown/scrum-overview
              '01.Section2.md': ["using-scrum"] ## assets/markdown/using-scrum

```
