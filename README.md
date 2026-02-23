# nagolos
Automatically adds stress marks to Ukrainian-language documents. Processes the entire input file using dictionary-based morphological analysis with context-aware disambiguation.

## Using

Supported formats: `.docx`, `.pdf`
### From command-line

```bash
$ python main.py <filename>
```
Processed file will be saved as `<filename>_nagolos` 

### Installing
Requires Python installed.

```bash
$ pip install -r requirements.txt
```