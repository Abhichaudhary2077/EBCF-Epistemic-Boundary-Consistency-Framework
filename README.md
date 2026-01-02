# EBCF — Epistemic Boundary & Consistency Framework

> **EBCF answers one question only:**  
> **“Is it honest to answer this question with what we currently know?”**

EBCF does **not** give answers.  
It decides **whether answering is epistemically allowed**.

---

## What Does “Epistemic” Mean (In This Project)?

In EBCF, **epistemic** simply means:

> **Related to knowledge — what is known, what is not known,  
> and whether something can be known at all with the given information.**

That’s it.  
No philosophy degree required.

---

## A Very Simple Explanation (For Anyone)

Imagine someone asks:

> “What is inside this closed box?”

If:
- you can’t see inside  
- you can’t open it  
- you have no sensors  

Then the **honest answer** is:

> “I don’t know.”

That moment — when you stop instead of guessing —  
is called an **epistemic boundary**.

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

EBCF evaluates four things:

1. **What you know** (observables)
2. **What you assume** (assumptions)
3. **What you are trying to do** (task)
4. **Whether understanding is actually improving**

If uncertainty:
- stops improving **and**
- the task is non-identifiable even in principle

➡️ **EBCF halts reasoning and explains why.**

---

## What EBCF Is NOT

EBCF is **not**:

- ❌ an AI model  
- ❌ a predictor  
- ❌ a solver  
- ❌ a diagnostic system  

It does **not** tell you *what is true*.

It tells you whether **claiming truth would be dishonest**.

---

## When Should You Use EBCF?

Use EBCF **before answering** when:

- ❓ information is incomplete
- ⚠️ wrong answers are costly
- 🧠 assumptions are hidden
- 🔬 scientific honesty matters
- 🤖 you want AI systems to refuse instead of hallucinate

Typical domains:
- medicine
- research
- machine learning
- simulations
- decision systems
- safety-critical logic

---

## When Should You NOT Use EBCF?

Do **not** use EBCF when:

- you just want a guess
- approximation is acceptable
- uncertainty doesn’t matter
- exploration > correctness

EBCF is **strict by design**.

---

## Minimal Usage Example (Any Python Developer)

```python
from ebcf import epistemic_check

result = epistemic_check(
    observables=["chest pain", "normal ECG"],
    missing=["blood test"]
)

print(result)








📘 Medical Reference Example (Non-Diagnostic)

EBCF includes a reference implementation for medical symptom reasoning.

⚠️ Important
This example does not diagnose, predict disease,
or replace medical professionals.

It only evaluates whether conclusions are epistemically justified.

Example: Chest Pain

Chest pain is a classic case where:

multiple serious and non-serious causes coexist

symptoms alone are often insufficient

false certainty can be dangerous

Reference flow behavior:

collects only directly observable symptoms

forbids disease labels or interpretations

explicitly surfaces missing clinical information

triggers an epistemic STOP when causes remain indistinguishable

If red-flag indicators appear, the system halts immediately and advises seeking urgent care.

What This Example Demonstrates

how observations are separated from assumptions

how missing information is made explicit

where and why epistemic reasoning must stop

why uncertainty can be irreducible without new data

This example is intentionally conservative and scope-limited.

It exists to show when not to reason, not how to diagnose.

Reuse in Other Domains

The same structure applies to:

debugging

scientific experiments

ML evaluation

system modeling

Only the question specification changes.
The EBCF core remains the same.