#!/usr/bin/env python3
"""
Reference Audit Script for REN-01 Manuscript
Checks citations in tex file against bib file and verifies key references
"""

import re
import os

print("=" * 70)
print("REN-01 REFERENCE AUDIT")
print("=" * 70)

# Read the tex file
with open('ren01.tex', 'r') as f:
    tex_content = f.read()

# Read the bib file
with open('references39.bib', 'r') as f:
    bib_content = f.read()

# Extract all citations from tex file
cite_pattern = r'\\cite\{([^}]+)\}'
citations_raw = re.findall(cite_pattern, tex_content)

# Split multiple citations (e.g., \cite{A,B,C})
all_citations = []
for cite in citations_raw:
    for c in cite.split(','):
        all_citations.append(c.strip())

unique_citations = sorted(set(all_citations))
print(f"\n1. CITATION ANALYSIS")
print("-" * 50)
print(f"Total citation instances: {len(all_citations)}")
print(f"Unique citations: {len(unique_citations)}")

# Extract all bib entries
bib_pattern = r'@\w+\{([^,]+),'
bib_entries = re.findall(bib_pattern, bib_content)
bib_entries = [b.strip() for b in bib_entries]

print(f"Bib file entries: {len(bib_entries)}")

# Check for missing citations
print(f"\n2. MISSING CITATIONS CHECK")
print("-" * 50)
missing = []
for cite in unique_citations:
    if cite not in bib_entries:
        missing.append(cite)

if missing:
    print(f"Citations in tex but NOT in bib ({len(missing)}):")
    for m in missing:
        print(f"  [MISSING] {m}")
else:
    print("All citations found in bib file!")

# Check for unused bib entries
print(f"\n3. UNUSED BIB ENTRIES CHECK")
print("-" * 50)
unused = []
for entry in bib_entries:
    if entry not in unique_citations:
        unused.append(entry)

if unused:
    print(f"Bib entries NOT cited in tex ({len(unused)}):")
    for u in unused[:10]:  # Show first 10
        print(f"  [UNUSED] {u}")
    if len(unused) > 10:
        print(f"  ... and {len(unused) - 10} more")
else:
    print("All bib entries are used!")

# Key references to verify
print(f"\n4. KEY REFERENCE VERIFICATION")
print("-" * 50)

key_refs = {
    'OpenNeuro2024': 'OpenNeuro dataset ds000245 (n=45 PD subjects)',
    'PubChem2024': 'PubChem CID 66553195 (TRV130/oliceridine)',
    'Poewe2017': 'Parkinson disease review (Nature Reviews Disease Primers)',
    'Kalia2015': 'Parkinsons disease (Lancet)',
    'Friston2010': 'Free-energy principle (Nature Reviews Neuroscience)',
    'DeWire2013': 'G protein-biased MOR ligand (J Pharmacol Exp Ther)',
    'Manglik2016': 'Structure-based opioid discovery (Nature)',
}

print("Checking key references:")
for ref, desc in key_refs.items():
    if ref in bib_entries:
        print(f"  [OK] {ref}: {desc}")
    else:
        print(f"  [MISSING] {ref}: {desc}")

# Extract and display key bib entries
print(f"\n5. KEY BIB ENTRY DETAILS")
print("-" * 50)

def extract_bib_entry(bib_content, key):
    pattern = rf'@\w+\{{{key},[^@]*'
    match = re.search(pattern, bib_content, re.DOTALL)
    if match:
        return match.group(0).strip()
    return None

for ref in ['OpenNeuro2024', 'PubChem2024']:
    entry = extract_bib_entry(bib_content, ref)
    if entry:
        print(f"\n{ref}:")
        # Extract title and year
        title_match = re.search(r'title\s*=\s*\{([^}]+)\}', entry)
        year_match = re.search(r'year\s*=\s*\{?(\d{4})\}?', entry)
        if title_match:
            print(f"  Title: {title_match.group(1)[:60]}...")
        if year_match:
            print(f"  Year: {year_match.group(1)}")
    else:
        print(f"\n{ref}: NOT FOUND IN BIB FILE")

# Citation frequency analysis
print(f"\n6. CITATION FREQUENCY ANALYSIS")
print("-" * 50)

from collections import Counter
cite_counts = Counter(all_citations)
print("Most cited references:")
for cite, count in cite_counts.most_common(10):
    print(f"  {cite}: {count} times")

# Check for potential issues
print(f"\n7. POTENTIAL ISSUES")
print("-" * 50)

issues = []

# Check for self-citations (if any pattern suggests it)
# Check for very old references
old_refs = []
for entry in bib_entries:
    entry_text = extract_bib_entry(bib_content, entry)
    if entry_text:
        year_match = re.search(r'year\s*=\s*\{?(\d{4})\}?', entry_text)
        if year_match:
            year = int(year_match.group(1))
            if year < 1990:
                old_refs.append((entry, year))

if old_refs:
    print(f"References older than 1990 ({len(old_refs)}):")
    for ref, year in sorted(old_refs, key=lambda x: x[1])[:5]:
        print(f"  {ref} ({year})")

# Check for 2024/2025 references (may need verification)
recent_refs = []
for entry in bib_entries:
    entry_text = extract_bib_entry(bib_content, entry)
    if entry_text:
        year_match = re.search(r'year\s*=\s*\{?(\d{4})\}?', entry_text)
        if year_match:
            year = int(year_match.group(1))
            if year >= 2024:
                recent_refs.append((entry, year))

if recent_refs:
    print(f"\nRecent references (2024+) - verify these exist:")
    for ref, year in recent_refs:
        print(f"  {ref} ({year})")

# Summary
print(f"\n" + "=" * 70)
print("REFERENCE AUDIT SUMMARY")
print("=" * 70)
print(f"Total unique citations: {len(unique_citations)}")
print(f"Total bib entries: {len(bib_entries)}")
print(f"Missing from bib: {len(missing)}")
print(f"Unused in bib: {len(unused)}")
print(f"Key references verified: {sum(1 for r in key_refs if r in bib_entries)}/{len(key_refs)}")

if missing:
    print(f"\n[!] WARNING: {len(missing)} citations are missing from the bib file")
    print("    These will appear as '?' in the compiled PDF")
print("=" * 70)
