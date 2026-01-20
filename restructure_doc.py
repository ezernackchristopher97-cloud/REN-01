#!/usr/bin/env python3
"""
Restructure REN-01 manuscript:
- Main body ends with Conclusion (after Discussion)
- Future Work and other supplementary material goes to Appendix
"""

with open('ren01.tex', 'r') as f:
    content = f.read()

# Find the key sections
lines = content.split('\n')

# Find line indices for key sections
discussion_start = None
future_work_start = None
conclusion_start = None
bibliography_start = None
end_document = None

for i, line in enumerate(lines):
    if '\\section{Discussion}' in line:
        discussion_start = i
    elif '\\section{Future Work}' in line:
        future_work_start = i
    elif '\\section{Conclusion}' in line:
        conclusion_start = i
    elif '\\bibliographystyle{' in line:
        bibliography_start = i
    elif '\\end{document}' in line:
        end_document = i

print(f"Discussion starts at line: {discussion_start}")
print(f"Future Work starts at line: {future_work_start}")
print(f"Conclusion starts at line: {conclusion_start}")
print(f"Bibliography starts at line: {bibliography_start}")
print(f"End document at line: {end_document}")

# Extract sections
# Everything before Future Work (including Discussion)
main_body = lines[:future_work_start]

# Future Work section (from Future Work to Conclusion)
future_work = lines[future_work_start:conclusion_start]

# Conclusion section (from Conclusion to Bibliography)
conclusion = lines[conclusion_start:bibliography_start]

# Bibliography and end
bibliography = lines[bibliography_start:]

# New structure:
# 1. Main body (up to end of Discussion)
# 2. Conclusion (moved here)
# 3. Appendix containing Future Work
# 4. Bibliography

new_content = []

# Add main body (everything up to Future Work)
new_content.extend(main_body)

# Add Conclusion right after Discussion
new_content.extend(conclusion)

# Add Appendix with Future Work
new_content.append('')
new_content.append('\\appendix')
new_content.append('')

# Convert Future Work section to appendix
for line in future_work:
    if '\\section{Future Work}' in line:
        new_content.append('\\section{Future Work and Extensions}')
    else:
        new_content.append(line)

# Add bibliography
new_content.extend(bibliography)

# Write the restructured content
with open('ren01.tex', 'w') as f:
    f.write('\n'.join(new_content))

print("Document restructured successfully!")
print(f"New structure:")
print(f"  - Main body sections 1-10 (Introduction through Discussion)")
print(f"  - Section 11: Conclusion")
print(f"  - Appendix A: Future Work and Extensions")
print(f"  - References")
