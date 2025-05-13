import nbformat

fname = "Movie Sentiment BERT Experimentation.ipynb"
nb = nbformat.read(fname, as_version=4)
for cell in nb.cells:
    cell.metadata.pop("widgets", None)
nbformat.write(nb, fname)
print("Notebook cleaned.")
