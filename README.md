# Hamecohming Framework

> **OS-level AI governance that enforces boundaries — not opinions.**

AI safety should not depend on whether the model makes good decisions.  
It should depend on whether execution is permitted at the system level in the first place.

This framework enforces provenance, consent, and domain constraints at the **kernel execution boundary** — deterministically, without semantic interpretation.

---

## The Problem

Model-level alignment is probabilistic. It can be overridden by prompting, fine-tuning, or context manipulation.

The Hamecohming Framework moves the enforcement point **below** the model:

```text
User/Agent Request
      ↓
  Tag Check  ←  Provenance / Domain / Consent
      ↓
 OS Boundary  ←  No semantic interpretation. Deterministic enforcement.
      ↓
Permit Execution  ──or──  Structural Silence (deny by structure, not by judgment)
```

<img src="https://raw.githubusercontent.com/overthinker-jp/umecohming-hamecohming/main/os-layer-diagram.png" width="100%" />

---

## Core Logic

```c
if (!os.verify_domain_tag(process, action)) {
    deny_execution();  // No interpretation. No loopholes.
}
```

No model in the decision path. No prompt-injection attack surface. No "maybe".

---

## Components

| Component | Role |
|---|---|
| **Umecohming** | Attribute embedding & provenance tagging |
| **Hamecohming** | Institutional boundary definition |
| **Structural Silence** | Execution halt on unverified actions |
| **Transparency Incentives** | Redistribution logic tied to verified usage |

---

## Implementation

### Conceptual prototype (Python)

Demonstrates the boundary logic in a readable form.  
Not OS-level; intended as a specification reference.

```bash
python os/boundary.py
```

- Tag matching with tamper detection (SHA-256 rule hash)
- Structural Silence that actually halts execution (`sys.exit(1)`)
- Persistent audit log at `logs/boundary_audit.jsonl`

### Kernel-level enforcement (eBPF/LSM)

The production implementation enforces the same boundary conditions at the kernel syscall layer — before user-space code can execute.

```bash
# Load the LSM hook (requires root)
sudo python ebpf/loader.py
```

See `/ebpf/` for the kernel-space implementation.

> **Note:** The Python prototype is a conceptual demonstration.  
> Actual OS-level enforcement requires the eBPF implementation.

---

## Threat Model / Limitations

Conceptual prototype — not a secure enforcement layer.

- User-space execution → integrity can be bypassed in a compromised runtime
- `sys.exit(1)` → hard stop by design (no recovery path)
- Audit logs → writable and not tamper-resistant

Not flaws. Scope.

Real enforcement begins where user-space ends — at the kernel boundary (eBPF/LSM).

---

## Background

This framework emerged from a practical question:

*Why does AI safety rely on the model saying no — when the OS can simply deny execution?*

Informed by pharmacovigilance system design (adverse event detection without retraining) and applied to AI governance as an institutional architecture problem.

**90/9/1 model:**

- ~90% of AI interactions → probabilistic safety is sufficient
- ~9% → context-aware gray-zone handling
- <1% → OS-level hard stop, no exceptions

---

## Publications & Public Record

| Type | Link |
|---|---|
| Notion | [Open Notion](https://wise-antimatter-790.notion.site/35667dd80dba808da854cc0621a803ea) |

---

## Status

Active research. Independent. Not affiliated with any institution.  
Feedback and issues welcome.
