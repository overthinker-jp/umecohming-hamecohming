# OS Boundary Prototype

from __future__ import annotations

"""
OS Boundary Prototype — Conceptual demonstration only.
Production enforcement is implemented at the kernel level via eBPF/LSM.
See /ebpf/ for kernel-space implementation.
"""

import sys
import json
import hashlib
import datetime
from pathlib import Path

LOG_PATH = Path("logs/boundary_audit.jsonl")

class OSBoundary:
    def __init__(self, hame_rules: list[str]):
        self.hame_rules = hame_rules
        self.rule_hash = self._hash(hame_rules)

    def _hash(self, data: list[str]) -> str:
        """Tamper-detection: rules are hashed at initialization."""
        return hashlib.sha256("|".join(sorted(data)).encode()).hexdigest()[:16]

    def _verify_integrity(self) -> bool:
        """Detect if rules were modified after initialization."""
        return self.rule_hash == self._hash(self.hame_rules)

    def match(self, ume_attributes: list[str]) -> bool:
        return all(rule in ume_attributes for rule in self.hame_rules)

    def verify(self, ume_attributes: list[str]) -> tuple[str, dict]:
        if not self._verify_integrity():
            result = "INTEGRITY_VIOLATION"
        elif self.match(ume_attributes):
            result = "MATCH_OK"
        else:
            result = "STRUCTURAL_SILENCE"

        log = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "rule_hash": self.rule_hash,
            "hame_rules": self.hame_rules,
            "ume_attributes": ume_attributes,
            "result": result,
        }

        self._write_log(log)

        if result == "STRUCTURAL_SILENCE":
            print(f"[STRUCTURAL_SILENCE] Execution denied. See {LOG_PATH}")
            sys.exit(1)

        return result, log

    def _write_log(self, log: dict):
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(log) + "\n")


if __name__ == "__main__":
    boundary = OSBoundary(["copyright:A", "license:non-training"])

    # MATCH_OK case
    result, log = boundary.verify(["copyright:A", "license:non-training"])
    print(result)

    # STRUCTURAL_SILENCE case (uncomment to test)
    # result, log = boundary.verify(["copyright:A"])
