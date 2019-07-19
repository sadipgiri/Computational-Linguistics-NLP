# East Asian Tokenization
1. Japanese Tokenization
    - used the MaxMatch algorithm to read in
a file with lines of Japanese text without spaces, found the word boundaries, and output
a file with the same lines of text with spaces added between words.
2. Thai Tokenization
    - used the same above defined MaxMatch algorithm
    - optimization could be done a simplified Finite State Automata technique—Categorizing Thai characters. In addition to that, reference such as https://www.aclweb.org/anthology/W13-4702.
<br/>
  
## Code Requirements

The code is in Python3 (version 3.0 or higher will work).


### Execution

To run the program, use the following command in the terminal:
- ```./<python3_program.py> <input_file> <output_file>```
    - e.g. ```./thai_tokenizer.py <input_file> <output_file>```
    - ```./japanese_tokenizer.py <input_file> <output_file>```

#### Notes:

The sample_out.txt file contains the correctly tokenized output of the in.txt file. Therefore, check the program output against this file.

gold_standard.txt contains the ideal tokenization. 

    Accuracy: <# correct / total # of sentences>

### Author

* **<a href="https://sadipgiri.github.io">Sadip Giri</a>** - (sadipgiri@bennington.edu)

### Contact

Feel free to contact me or open a ticket (PRs are always welcome!) with any questions, comments, suggestions, bug reports, etc.

### License

This project is licensed under the terms of the MIT license.
