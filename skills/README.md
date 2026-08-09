# Skills — Brand creative pipeline (`brand-gdrive` branch)

**Storage:** Client artifacts on Google Drive (`gdrive/clients/{slug}/`). Skills and templates in this repo. See [brand-social-creative-pipeline/references/google-drive-storage.md](./brand-social-creative-pipeline/references/google-drive-storage.md).

Skills for the Swayam weekly cloud agent (paths on Drive when using this branch).

## Invoke order (weekly run)

| Phase | Skill | Path |
|-------|-------|------|
| 1 Research | reddit-posts | [reddit-posts/SKILL.md](./reddit-posts/SKILL.md) |
| 2 Copy | caption-writer-sms, post-writer-sms, whatsapp-skill | [caption-writer-sms](./caption-writer-sms/SKILL.md), [post-writer-sms](./post-writer-sms/SKILL.md), [whatsapp-skill](./whatsapp-skill/SKILL.md) |
| 2 Context | social-media-context-sms | Read `gdrive/clients/swayam/plans/{run_date}/social-media-context.md` on Drive |
| 3–4 Creative | brand-social-creative-pipeline | [brand-social-creative-pipeline/SKILL.md](./brand-social-creative-pipeline/SKILL.md) |
| Hooks (optional) | hook-writer-sms | [hook-writer-sms/SKILL.md](./hook-writer-sms/SKILL.md) |
| Bootstrap (brand setup) | design-brand-guardian | [design-brand-guardian/SKILL.md](./design-brand-guardian/SKILL.md) |
| Bootstrap (Pinterest refs) | pinterest-reference-fetch | [brand-social-creative-pipeline/references/pinterest-reference-fetch/SKILL.md](./brand-social-creative-pipeline/references/pinterest-reference-fetch/SKILL.md) |
| Bootstrap (reference layout prompt) | reference-creative-prompt | [brand-social-creative-pipeline/references/reference-creative-prompt/SKILL.md](./brand-social-creative-pipeline/references/reference-creative-prompt/SKILL.md) |
| Publish (after image) | firestore-creative-publish | [brand-social-creative-pipeline/references/firestore-creative-publish/SKILL.md](./brand-social-creative-pipeline/references/firestore-creative-publish/SKILL.md) |
| Caption score (before publish) | caption-score | [brand-social-creative-pipeline/references/caption-score/SKILL.md](./brand-social-creative-pipeline/references/caption-score/SKILL.md) |
| Bootstrap (profile research) | creator-profile-teardown | [creator-profile-teardown/SKILL.md](./creator-profile-teardown/SKILL.md) |

## Swayam brand assets (on Google Drive)

| File | Purpose |
|------|---------|
| `gdrive/clients/swayam/BRAND_DNA.json` | Invariant brand tokens |
| `gdrive/clients/swayam/BRAND_DNA_SCHEMA.json` | Brand DNA schema |
| `gdrive/clients/swayam/CREATIVE_DNA_SCHEMA.json` | Per-creative DNA schema |
| `gdrive/clients/swayam/plans/{run_date}/social-media-context.md` | Voice, audience, pillars |

Schema templates (repo): `brand-social-creative-pipeline/templates/`

## Prompt merge

See [brand-social-creative-pipeline/references/prompt-merge.md](./brand-social-creative-pipeline/references/prompt-merge.md).

## Bootstrap skills (quarterly / new client)

- **design-brand-guardian** — Phase 1 brand identity (`BRAND_IDENTITY.md` on Drive)
- **pinterest-reference-fetch** — Phase 1b: 5 Pinterest layout pins → `gdrive/clients/{slug}/references/pinterest/{run_date}/`
- **creator-profile-teardown** — Instagram/social profile analysis before strategy
