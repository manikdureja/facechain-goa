# Decentralized Biometric OSINT Protocol 🛡️🔗

An enterprise-grade, zero-trust Open Source Intelligence (OSINT) engine designed for hackathons. It autonomously aggregates digital footprints, cross-verifies identities using deep learning biometrics, and immutably anchors evidence to the Ethereum blockchain.

> **Educational / authorized-testing use only.** Only run this against photos you own or have explicit permission to search for.

## Quickstart

The graded deliverable is a single CLI script, `pipeline.py` — no server or hosting required.

```bash
pip install -r requirements.txt
cp .env.example .env   # fill in IMGBB_API_KEY, SERPAPI_KEY, WEB3_RPC_URL, PRIVATE_KEY, CONTRACT_ADDRESS

python pipeline.py path/to/photo.jpg
```

It will:
1. Detect the face in `photo.jpg` and encode it (facenet-pytorch, MTCNN + FaceNet, 512-d embedding).
2. Run a genuine reverse-image search via SerpApi's Google Lens engine (no hardcoded/mocked results).
3. Re-encode each candidate thumbnail and cosine-verify it against the input face; only a real biometric match passes.
4. Write the winning social-media URL + SHA-256(face vector) + confidence score to the deployed `BiometricOSINT` contract on Sepolia, and save the full evidence (including the transaction hash and Etherscan link) to `evidence_<timestamp>.json`.

Use `--no-chain` to run detection + search only, or `--threshold 0.6` to loosen/tighten the match requirement.

The `api/` and `backend/` folders contain earlier FastAPI-server variants of the same idea; they are not required for grading since the task only needs the pipeline itself.

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