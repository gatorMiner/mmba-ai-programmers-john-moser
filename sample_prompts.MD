### sample_prompts.md

```markdown
# Sample Prompts and Templates
This file contains ready-to-use prompt templates and examples for the pipeline: image generation, narrative generation (LLM), RAG retrieval prompts, GAN training seed prompts, and a short HITL review checklist.

---

## 1. Image Prompt Template
Use this template for Stable Diffusion style generation. Replace bracketed tokens.

**Template**
```
Create a [style] portrait of "[character_name]" — [short_description]. Visual motifs: [motifs]. Color palette: [colors]. Mood: [mood]. Resolution: [width]x[height]. Produce [n_variations] variations. Output: high-resolution PNG, transparent background optional.
```

**Example**
```
Create a synthwave glitch portrait of "Grinshard" — satirical HR-like villain with a cracked smiley mask and surveillance balloons. Visual motifs: neon smiley, glitch overlays, canned laughter. Color palette: neon magenta, cyan, black. Mood: unsettling, satirical. Resolution: 2048x2048. Produce 4 variations. Output: high-resolution PNG.
```

---

## 2. Narrative Prompt Template (LLM with RAG context)
Use this template after retrieving lore chunks from the vector DB. Request structured JSON output.

**Template**
```
Using the following lore context retrieved via RAG: [LORE_CHUNKS], write a [min]-[max] word soliloquy for "[character_name]" that reads like a satirical manifesto. Return JSON with fields: title, soliloquy, unlockable_content_ipfs, tags (array), metadata_version, prompt_version. Keep language vivid and consistent with the provided lore.
```

**Example**
```
Using the following lore context retrieved via RAG: [lore_chunk_1, lore_chunk_2], write a 120-200 word soliloquy for "Grinshard" that reads like a satirical manifesto. Return JSON with fields: title, soliloquy, unlockable_content_ipfs, tags, metadata_version, prompt_version.
```

---

## 3. RAG Retrieval Prompt Template
Use this to fetch relevant lore chunks for a character.

**Template**
```
Find the top 5 lore chunks most relevant to the query: "[query]". Rank by semantic similarity and return chunk IDs and short excerpts only.
```

**Example**
```
Find the top 5 lore chunks most relevant to the query: "Grinshard origin ritual and propaganda motifs". Return chunk IDs and 1-2 sentence excerpts.
```

---

## 4. GAN Training Seed Prompt (for dataset curation)
Use this to describe the desired dataset and style for a GAN training job.

**Template**
```
Curate a dataset of [N] images for style "[style_name]". Desired characteristics: [list characteristics]. Exclude: [forbidden content]. Target resolution: [WxH]. Provide a short justification for dataset choices and a suggested augmentation pipeline.
```

**Example**
```
Curate a dataset of 5000 images for style "neon-glitch synthwave". Desired characteristics: high contrast neon palettes, glitch artifacts, portrait-centric composition, 1:1 aspect ratio. Exclude: real-person likenesses without consent. Target resolution: 1024x1024. Suggest augmentations: color jitter, random crop, horizontal flip, synthetic noise overlays.
```

---

## 5. HITL Review Checklist
Use this checklist in the review UI for human approvers.

- Visual alignment with prompt motifs (yes/no)
- Readability at target sizes (yes/no)
- No unsafe or copyrighted content (yes/no)
- Narrative coherence with lore (1–5)
- Recommended action: Approve / Request edit / Reject

---

## 6. Prompt Versioning Notes
- Always append `prompt_version` with ISO date and short tag (e.g., `v2025-11-28-a`) when saving a new prompt.
- Keep a changelog entry describing edits and SME rationale.

```

---
