# Syllabus Style Guide

## Naming
- Classes: CapitalCase
- Attributes: under_scores

## Docstrings
- First line is a real sentence with a period and everything.
    - just a short description
- Remainder is paragraphs.
- Models
    - All external relationships must be included under "related fields:"
        related fields:
            \`{field_name}\` from {app}.{model}
        note: {app} optional if {model} is local
