# EBCF — Epistemic Boundary & Consistency Framework

> **EBCF answers one question only:**  
> **“Is it honest to answer this question with what we currently know?”**

It does **not** give answers.  
It decides **whether answering is allowed**.

---

## What Does “Epistemic” Mean Here?

In this project, **epistemic** simply means:

> **Related to knowledge — what is known, what is not known,  
> and whether something can be known at all with the given information.**

That’s it.  
No philosophy degree required.

---

## A Very Simple Explanation (For Anyone)

Imagine someone asks you:

> “What is inside this closed box?”

If:
- you can’t see inside  
- you can’t open it  
- you have no sensors  

Then the **honest answer** is:

> “I don’t know.”

That moment — when you stop instead of guessing —  
that is an **epistemic boundary**.

**EBCF is code that detects that moment automatically.**

---

## Why EBCF Exists

Most systems (including AI systems):

- keep answering even when they shouldn’t
- hide uncertainty
- sound confident while guessing

**EBCF exists to prevent that.**

> Uncertainty is not failure.  
> Pretending uncertainty does not exist is failure.

---

## What EBCF Does (Precisely)

EBCF checks four things:

1. **What you know** (observables)
2. **What you assume** (assumptions)
3. **What you are trying to do** (task)
4. **Whether understanding is actually improving**

If uncertainty:
- stops improving **and**
- the task cannot be solved even in principle

➡️ **EBCF stops the system and explains why.**

---

## What EBCF Is NOT

EBCF is **not**:

- ❌ an AI model  
- ❌ a predictor  
- ❌ a solver  
- ❌ a decision-maker  

It does **not** tell you *what* is true.

It tells you whether **claiming truth would be dishonest**.

---

## When Should You Use EBCF?

Use EBCF **before answering** when:

- ❓ Information is incomplete
- ⚠️ Wrong answers are costly
- 🧠 Assumptions are hidden
- 🔬 You care about scientific honesty
- 🤖 You want AI systems to refuse instead of hallucinate

Typical domains:
- medicine
- research
- machine learning
- simulations
- decision systems
- safety-critical logic

---

## When Should You NOT Use EBCF?

Do NOT use EBCF when:

- you just want a guess
- approximation is acceptable
- uncertainty doesn’t matter
- exploration > correctness

EBCF is **strict by design**.

---

## Minimal Usage Example (For Any Python Developer)

"""python
from ebcf import epistemic_check

result = epistemic_check(
    observables=["chest pain", "normal ECG"],
    missing=["blood test"]
)

print(result)


output:
EpistemicResult(
  allowed=False,
  confidence=0.9,
  reason="Non-identifiable under current observables"
)
"""

## Graphical Interface (For Everyone)

EBCF includes a minimal graphical interface for non-technical users.

Run:

```bash
python ebcf_gui.py
