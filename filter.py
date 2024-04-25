import sys
import nbformat
import yaml
from pathlib import Path

# read notebook from stdin
nb = nbformat.reads(sys.stdin.read(), as_version=4)

# read cell 0 as yaml
metadata = yaml.load(nb.cells[0].source.replace('---', ''), Loader=yaml.FullLoader)
title = metadata.get('title', 'Notebook Title')
do_insert_colab_badge = metadata.get('insert_colab_badge', False)

if do_insert_colab_badge:
    cwd = Path.cwd().name
    nb_path = next(Path.cwd().glob("*.ipynb")).relative_to(Path.cwd().parent)
    colab_link = f"https://colab.research.google.com/github/nateraw/naterawdotcom/blob/main/{nb_path}"
    colab_badge = f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_link})"

    # Create the title and badge markdown
    title_and_badge = f"# {title}\n\n{colab_badge}"

    # Insert a new markdown cell at index 1 with the title and badge
    new_markdown_cell = nbformat.v4.new_markdown_cell(source=title_and_badge)
    nb.cells.insert(1, new_markdown_cell)

# write notebook to stdout
nbformat.write(nb, sys.stdout)
