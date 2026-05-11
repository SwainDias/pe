# Q19. Information Extraction using Named Entity Recognition (NER)

text = """
Apple Inc. was founded by Steve Jobs and Steve Wozniak in Cupertino, California in 1976.
The company is headquartered in the United States and its CEO Tim Cook earns over $10 million annually.
In January 2024, Apple released new products at an event in San Francisco.
"""

# =============================================
# PART A - spaCy (requires: python -m spacy download en_core_web_sm)
# =============================================

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

print("=== PART A: spaCy ===\n")

for ent in doc.ents:
    print(ent.text, "->", ent.label_, "(" + spacy.explain(ent.label_) + ")")


# =============================================
# PART B - Hardcoded NER (no external models)
# =============================================

import re
from collections import defaultdict

# Hardcoded entity dictionary
entity_patterns = {
    "Apple Inc.": "ORG",
    "Steve Jobs": "PERSON",
    "Steve Wozniak": "PERSON",
    "Cupertino": "GPE",
    "California": "GPE",
    "1976": "DATE",
    "United States": "GPE",
    "Tim Cook": "PERSON",
    "$10 million": "MONEY",
    "January 2024": "DATE",
    "Apple": "ORG",
    "San Francisco": "GPE",
}

print("\n=== PART B: Hardcoded NER Parsing ===\n")

found_entities = []

# Parse text manually using pattern matching
for entity in entity_patterns:
    if re.search(re.escape(entity), text):
        label = entity_patterns[entity]
        found_entities.append((entity, label))
        print(entity, "->", label)

# Group entities by type
groups = defaultdict(list)

for entity, label in found_entities:
    groups[label].append(entity)

print("\nGrouped by type:")

for label in groups:
    print(label, ":", groups[label])