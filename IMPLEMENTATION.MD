### IMPLEMENTATION.md — Minimal Setup Guide

#### Purpose
Quick, copy-ready instructions to run a local dev instance of the pipeline, validate outputs, and wire basic CI/CD. Keep secrets out of source control and use the environment variables listed below.

---

### Prerequisites
- **Node.js** 18+ or **Python** 3.10+ depending on chosen service implementations.  
- **Git** for repository management.  
- **Docker** recommended for local vector DB or self-hosted Stable Diffusion.  
- Cloud accounts as needed: OpenAI API key, IPFS pinning service, Polygon wallet and RPC provider, Thirdweb/Manifold credentials.

---

### Environment variables
Set these in your environment or secrets manager (do not commit to repo).

- **OPENAI_API_KEY** — OpenAI LLM key.  
- **IMAGE_API_KEY** — Hosted Stable Diffusion provider key (if using hosted).  
- **IPFS_PIN_KEY** — Pinning service API key.  
- **WEB3_RPC_URL** — Polygon RPC endpoint.  
- **WALLET_PRIVATE_KEY** — Wallet key for minting (store in secrets manager).  
- **THIRDWEB_API_KEY** — Thirdweb or minting SDK key.  
- **VECTOR_DB_API_KEY** — Pinecone/Weaviate/Milvus key.  
- **OBSERVABILITY_DSN** — Tracing/monitoring endpoint (optional).

Example local export (Linux/macOS):
```bash
export OPENAI_API_KEY="sk-xxxx"
export IMAGE_API_KEY="img-xxxx"
export IPFS_PIN_KEY="pin-xxxx"
export WEB3_RPC_URL="https://polygon-rpc.example"
export WALLET_PRIVATE_KEY="0x..."
export THIRDWEB_API_KEY="tw-xxxx"
export VECTOR_DB_API_KEY="vec-xxxx"
export OBSERVABILITY_DSN="https://otel.example"
```

---

### Local development quickstart
1. **Clone repo**
```bash
git clone <your-repo-url>
cd <repo-name>
```
2. **Install dependencies**
- Node service:
```bash
cd services/orchestrator
npm install
```
- Python service:
```bash
cd services/llm
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
3. **Run local dev services**
- Start vector DB (Docker example):
```bash
docker run --name vectordb -p 8200:8200 pinecone/local:latest
```
- Start orchestrator and LLM service (example):
```bash
# in separate terminals
npm run dev   # orchestrator
python app.py # LLM orchestrator
```
4. **Smoke test**
- Use provided sample prompt endpoint to submit a test prompt and confirm:
  - LLM returns structured JSON matching `metadata_schema.json`.  
  - Image generator returns candidate images (URLs or local files).  
  - IPFS upload returns a content identifier (CID).  
  - Minting service returns a transaction hash on Polygon.

Example curl test (replace endpoint and payload):
```bash
curl -X POST http://localhost:3000/api/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Create a synthwave portrait of Grinshard","prompt_version":"v1"}'
```

---

### Running pipeline steps manually
- **Generate images** (orchestrator endpoint):
```bash
POST /api/images { "prompt": "...", "n": 4 }
```
- **Run RAG retrieval**:
```bash
POST /api/rag { "query": "Grinshard origin ritual" }
```
- **Generate narrative**:
```bash
POST /api/narrative { "lore_chunks": [...], "character": "Grinshard" }
```
- **Package metadata and upload to IPFS**:
```bash
POST /api/package { "image_cid": "ipfs://...", "metadata": {...} }
```
- **Mint on Polygon**:
```bash
POST /api/mint { "metadata_uri": "ipfs://...", "tier": "rare" }
```

(Implementations should return JSON with status, CID, and transaction hash for each step.)

---

### CI/CD basics with GitHub Actions
- **Trigger**: push to `main` or PR to `main`.  
- **Jobs**:
  - **lint/test** — run unit tests and schema validation.  
  - **deploy** — deploy serverless functions or container images to staging.  
  - **release** — tag prompt/schema changes and optionally trigger a sample generation job.  
- **Secrets**: store API keys and wallet private key in GitHub Secrets; never commit them.

Example job snippet (conceptual):
```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install
        run: npm ci
      - name: Run tests
        run: npm test
  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Deploy functions
        run: ./scripts/deploy.sh
```

---

### Optional GAN training and integration
- **Dataset**: prepare curated images and store in a secure bucket.  
- **Training**: use a GPU instance or managed ML service; version checkpoints and export sample generations.  
- **CI/CD hook**: when a new checkpoint is published, run automated sample generation and FID/IS evaluation; if metrics pass and SME approves, promote checkpoint to production.  
- **Inference**: expose a lightweight inference endpoint that the orchestrator can call for discriminator scoring or style generation.

---

### Testing and validation
- **Unit tests** for prompt manager and schema validation.  
- **Integration tests** that run a full pipeline on a small sample prompt and assert:
  - LLM output conforms to JSON schema.  
  - Image candidate count and format.  
  - IPFS upload returns CID.  
  - Mint transaction confirmed on Polygon testnet.  
- **Regression tests**: store ground-truth prompt-output pairs and run nightly comparisons.

---

### Secrets and safety checklist
- Use a secrets manager for private keys and API tokens.  
- Enforce input validation and output filtering before publishing unlockables.  
- Add rate limits and cost guards for model and image API calls.  
- Require SME approval for any automated on-chain metadata changes.

---
