#!/usr/bin/env python3
"""
Comprehensive micro-edits for REN-01 manuscript
Following binding instructions from pasted_content_9.txt
"""

import re

def apply_edits(content):
    changes = []
    
    # 1. Fix "therapeutic superiority" overclaim
    old = "demonstrating therapeutic superiority"
    new = "demonstrating enhanced model stability in simulation"
    if old in content:
        content = content.replace(old, new)
        changes.append(("Line 459", old, new, "Remove overclaim"))
    
    # 2. Fix "REN-01 treatment" to "REN-01 condition"
    old = "REN-01 treatment ($\\chi$"
    new = "REN-01 condition ($\\chi$"
    if old in content:
        content = content.replace(old, new)
        changes.append(("Conclusion", old, new, "Reframe as simulation condition"))
    
    # 3. Fix "therapeutic mechanism" to "model mechanism"
    old = "MOR agonism as dominant therapeutic mechanism"
    new = "MOR agonism as the dominant mechanism in the model"
    if old in content:
        content = content.replace(old, new)
        changes.append(("Multiple", old, new, "Reframe as model mechanism"))
    
    # 4. Fix "therapeutic intervention" to "simulated intervention"
    old = "REN-01 therapeutic intervention"
    new = "simulated REN-01 intervention"
    if old in content:
        content = content.replace(old, new)
        changes.append(("Figure 1c", old, new, "Clarify simulation context"))
    
    # 5. Fix "restored dopamine" to "elevated dopamine proxy"
    old = "restored dopamine ($\\psi_D$"
    new = "elevated dopamine proxy ($\\psi_D$"
    if old in content:
        content = content.replace(old, new)
        changes.append(("Figure 4", old, new, "Use proxy language"))
    
    # 6. Strengthen quaternion abstraction disclaimer in Figure 2
    old = "Chains represent ensemble statistics across stochastic realizations and do not correspond to deterministic trajectories."
    new = "Chains represent ensemble statistics across stochastic realizations and do not correspond to deterministic trajectories, physical rotations, or measurable neural coordinates."
    if old in content:
        content = content.replace(old, new)
        changes.append(("Figure 2", "Added disclaimer", "physical rotations, measurable neural coordinates", "Strengthen abstraction"))
    
    # 7. Fix "trajectory" language in Figure 2 caption
    old = "Green trajectory (healthy)"
    new = "Green algebraic chain (healthy)"
    if old in content:
        content = content.replace(old, new)
        changes.append(("Figure 2", old, new, "Replace trajectory with algebraic chain"))
    
    old = "Red trajectory (degenerative)"
    new = "Red algebraic chain (degenerative)"
    if old in content:
        content = content.replace(old, new)
        changes.append(("Figure 2", old, new, "Replace trajectory with algebraic chain"))
    
    old = "Blue trajectory (REN-01)"
    new = "Blue algebraic chain (REN-01)"
    if old in content:
        content = content.replace(old, new)
        changes.append(("Figure 2", old, new, "Replace trajectory with algebraic chain"))
    
    # 8. Fix "establishes" overclaim
    old = "These results establish the quaternionic field model"
    new = "These results support the quaternionic field model"
    if old in content:
        content = content.replace(old, new)
        changes.append(("Validation Summary", old, new, "Soften claim"))
    
    # 9. Fix "confirms" to "suggests" where appropriate
    old = "confirming statistically distinct basins"
    new = "indicating statistically distinct basins in simulation"
    if old in content:
        content = content.replace(old, new)
        changes.append(("Figure 5c", old, new, "Soften claim"))
    
    # 10. Fix "confirms" in validation summary
    old = "Validation studies confirm:"
    new = "Validation studies indicate:"
    if old in content:
        content = content.replace(old, new)
        changes.append(("Validation Summary", old, new, "Soften claim"))
    
    # 11. Add "in simulation" qualifier to regime claims
    old = "confirming regime stability under parameter uncertainty"
    new = "indicating regime stability under parameter uncertainty in simulation"
    if old in content:
        content = content.replace(old, new)
        changes.append(("R3 section", old, new, "Add simulation qualifier"))
    
    # 12. Fix "therapeutic approach" in conclusion
    old = "REN-01 represents a therapeutic approach"
    new = "REN-01 represents a proposed modeling approach"
    if old in content:
        content = content.replace(old, new)
        changes.append(("Conclusion", old, new, "Reframe as modeling approach"))
    
    # 13. Fix "demonstrates" to "simulations show"
    old = "demonstrate three distinct dynamical regimes"
    new = "show three distinct dynamical regimes in simulation"
    if old in content:
        content = content.replace(old, new)
        changes.append(("Abstract/Conclusion", old, new, "Add simulation qualifier"))
    
    # 14. Fix "Therapeutic Outcomes" in figure caption
    old = "Therapeutic Outcomes (symptom alleviation and dopamine axis stability)"
    new = "Simulated Outcomes (model-predicted symptom proxy and dopamine axis stability)"
    if old in content:
        content = content.replace(old, new)
        changes.append(("Figure 1 caption", old, new, "Clarify simulation context"))
    
    # 15. Fix ± encoding to LaTeX
    content = re.sub(r'(\d+)\s*±\s*(\d+)', r'$\1 \\pm \2$', content)
    
    # 16. Fix × to LaTeX \times
    content = re.sub(r'(\d+)×', r'\1$\\times$', content)
    
    return content, changes

def main():
    with open('/home/ubuntu/REN-01-repo/ren01.tex', 'r') as f:
        content = f.read()
    
    content, changes = apply_edits(content)
    
    with open('/home/ubuntu/REN-01-repo/ren01.tex', 'w') as f:
        f.write(content)
    
    print(f"Applied {len(changes)} changes:")
    for c in changes:
        print(f"  {c[0]}: {c[1][:40]}... -> {c[2][:40]}...")

if __name__ == "__main__":
    main()
