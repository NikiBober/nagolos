# Nágólós
Automatically adds stress marks to Ukrainian-language documents. Processes the entire input file using dictionary-based morphological analysis with context-aware disambiguation.

## Using

Supported formats: `.docx`, `.pdf`, `.epub`
### From command-line

```bash
$ python nagolos.py <filename> [options]
```

Options:
- `-o, --output <output_file>`: Specify output file path (default: `<filename>_nagolos.docx`)
- `-v, --verbose`: Enable verbose logging

Processed file will be saved as `<filename>_nagolos.docx` (or specified output file) 

### Installing
Requires Python 3.10 or later installed.

```bash
$ pip install -r requirements.txt
```