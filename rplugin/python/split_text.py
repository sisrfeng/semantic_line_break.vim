import pynvim
import spacy

Autocmd: Called 4 times, file: split_text.py

@pynvim.plugin
class SplitTextPlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command("SplitText", range="", nargs="*", sync=True)
    def split_text(self, args, range):
        # Get the current buffer and cursor position
        buf = self.nvim.current.buffer
        row, col = self.nvim.current.window.cursor

        # Get the current paragraph as a single string
        start = end = row - 1
        while start > 0 and buf[start].strip():
            start -= 1
        while end < len(buf) and buf[end].strip():
            end += 1
        text = " ".join(buf[start+1:end])

        # Use spaCy to split the text by clauses
        doc = nlp(text)
        clauses = []
        for sent in doc.sents:
            clause = []
            for token in sent:
                clause.append(token.text)
                if token.is_punct or token.is_stop:
                    clauses.append(" ".join(clause))
                    clause = []
            if clause:
                clauses.append(" ".join(clause))

        # Replace the current paragraph with the split text
        buf[start+1:end] = clauses

        # Move the cursor to the original position
        self.nvim.current.window.cursor = (row, col)
