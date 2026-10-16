# Betty Ep01 — Prompt Template v1

**prompt_version:** `v1.0.0-betty-ep01`
**Source:** manual Meta AI run, curated 2026-10-16. The exact Meta AI prompt text was not preserved; the template below is reconstructed from the locked archetype traits and the selected output.

## Archetype template (CONSTANT across all Rogues Gallery characters)

The makeup expression never changes. Only the face underneath does.

- **Base:** pale chalk-white makeup base
- **Grin:** wide fixed red grin with extended smile lines
- **Eyes:** wide staring eyes with heavy black outline around the eyes
- **Era styling:** 1950s nostalgic
- **Render style:** stylized watercolor graphic-novel illustration — non-photoreal, illustrated (required for safety)

## Variable layer (per character / episode)

- Gender, age, hair style and color
- Costume and props
- Setting and background signage

## Image prompt template

```text
Create a stylized watercolor graphic-novel portrait of "[character_name]" — [gender], [age], [hair]. Wearing [costume]. Makeup (constant): pale chalk-white base, wide fixed red grin with extended smile lines, wide staring eyes with heavy black outline around the eyes. Era: 1950s nostalgic. Setting: [setting]. Style: illustrated watercolor, non-photoreal, graphic novel. Mood: cheerful menace. Generate 4 variations.
```

## Betty Ep01 instance

```text
Create a stylized watercolor graphic-novel portrait of "Betty" — young woman, brown ponytail, red polka-dot bandana, teal soda-shop uniform with white apron and BETTY name tag. Makeup (constant): pale chalk-white base, wide fixed red grin with extended smile lines, wide staring eyes with heavy black outline around the eyes. Era: 1950s nostalgic. Setting: soda shop interior, SODAS 25c / MALTS / MILKSHAKES sign behind. Style: illustrated watercolor, non-photoreal, graphic novel. Mood: cheerful menace. Generate 4 variations.
```

## Variety pack (rejected candidates, kept for style reference)

1. `images/variety_housewife_victory_rolls.webp` — housewife, victory rolls
2. `images/variety_fedora_man.webp` — man, fedora, pinstripe suit
3. `images/betty_polka_dots_original.webp` — Betty, polka dots (original)

Selected anchor: `images/betty_soda_shop_selected.webp` — ponytail, red polka-dot bandana, teal uniform, SODAS 25c MALTS MILKSHAKES background.

## Prompt versioning

- `v1.0.0-betty-ep01` — initial archetype template locked from manual Meta AI run (2026-10-16). Constant = makeup expression; variable = face, costume, setting.
- Future characters reuse the CONSTANT block verbatim; only the variable layer changes.
