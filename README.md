# Decentralized Biometric OSINT Protocol 🛡️🔗

An enterprise-grade, zero-trust Open Source Intelligence (OSINT) engine designed for hackathons. It autonomously aggregates digital footprints, cross-verifies identities using deep learning biometrics, and immutably anchors evidence to the Ethereum blockchain.

## Architectural Overview

Standard search engines rely on visual semantics that often trigger false positives based on clothing, background environments, or privacy filters. This protocol solves that problem through a **Multi-Tier Zero-Trust Pipeline**:

1. **Biometric Feature Extraction (`RetinaFace` & `FaceNet`):** Maps the high-dimensional facial geometry of the target scan, isolating it from background noise.
2. **Multi-Tier OSINT Cascade:** Queries uncensored visual matching engines (`Yandex Images`) and metadata text fallback search to harvest candidate profile links across major platforms (GitHub, LinkedIn, Twitter/X, Instagram).
3. **Independent AI Re-Verification:** Autonomously downloads candidate profile thumbnails and executes deep-metric cosine distance checks. Only candidates meeting strict mathematical confidence thresholds are approved.
4. **Decentralized Web3 Anchoring:** Pushes the verified identity URL, confidence score, and a SHA-256 cryptographic hash of the biometric vector to an Ethereum Sepolia Smart Contract.
5. **Genesis Fallback Protection:** For private or unindexed subjects, the engine bypasses public search gaps and anchors a secure cryptographic proof on-chain without throwing runtime exceptions.

---

## Repository Structure

```text
├── api/
│   └── main.py              # FastAPI asynchronous core engine & routes
├── contracts/
│   └── BiometricOSINT.sol   # Solidity smart contract for Sepolia anchoring
├── .env.example             # Environment configuration template
└── requirements.txt         # Project Python dependencies