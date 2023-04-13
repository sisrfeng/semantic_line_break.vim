import spacy

nlp = spacy.load('en_core_web_sm')
long_str =  "hi. 预备, 开始. par is a filter which copies its input to its output, changing all white characters (except newlines) to spaces, and  reformatting each paragraph. Paragraphs are separated by protected, blank, and bodiless lines (see the TERMINOLOGY section for definitions), and  optionally delimited by indentation (see the d option in the OPTIONS section). 快结束了, done"

doc = nlp( long_str)

for sent in doc.sents:
    clauses = sent.text.split(':')
    for clause in clauses:
        print(clause.strip())
#

# import textwrap
#
# def format_text_block(text_block):
#     # Set the width of the text block
#     width = 80
#
#     # Wrap the text block
#     wrapped_text = textwrap.wrap(text_block, width=width)
#
#     # Join the wrapped lines with a newline character
#     formatted_text = "\n".join(wrapped_text)
#
#     # Split the formatted text into clauses
#     clauses = formatted_text.split(", ")
#
#     # Join each clause with a newline character
#     formatted_clauses = "\n".join(clauses)
#
#     # Add indentation to each line
#     formatted_clauses = textwrap.indent(formatted_clauses, " " * 8)
#
#     # Add a newline character at the end of the formatted text
#     formatted_clauses += "\n"
#
#     return formatted_clauses
#
# text_block = "par is a filter which copies its input to its output, changing all white characters (except newlines) to spaces, and reformatting each paragraph. Paragraphs are separated by protected, blank, and bodiless lines (see the TERMINOLOGY section for definitions), and optionally delimited by indentation (see the d option in the OPTIONS section)."
# formatted_text = format_text_block(text_block)
# print(formatted_text)
