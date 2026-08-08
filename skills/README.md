# Skills — Swayam weekly creative pipeline

Skills for the [Swayam weekly cloud agent](../docs/swayam/swayam-weekly-automation.md).

## Invoke order (weekly run)

| Phase | Skill | Path |
|-------|-------|------|
| 1 Research | reddit-posts | [reddit-posts/SKILL.md](./reddit-posts/SKILL.md) |
| 2 Copy | caption-writer-sms, post-writer-sms, whatsapp-skill | [caption-writer-sms](./caption-writer-sms/SKILL.md), [post-writer-sms](./post-writer-sms/SKILL.md), [whatsapp-skill](./whatsapp-skill/SKILL.md) |
| 2 Context | social-media-context-sms | Read [docs/swayam/social-media-context-sms.md](../docs/swayam/social-media-context-sms.md) |
| 3–4 Creative | brand-social-creative-pipeline | [brand-social-creative-pipeline/SKILL.md](./brand-social-creative-pipeline/SKILL.md) |
| Hooks (optional) | hook-writer-sms | [hook-writer-sms/SKILL.md](./hook-writer-sms/SKILL.md) |
| Bootstrap (brand setup) | design-brand-guardian | [design-brand-guardian/SKILL.md](./design-brand-guardian/SKILL.md) |
| Bootstrap (profile research) | creator-profile-teardown | [creator-profile-teardown/SKILL.md](./creator-profile-teardown/SKILL.md) |

## Swayam brand assets

| File | Purpose |
|------|---------|
| [docs/swayam/BRAND_DNA.json](../docs/swayam/BRAND_DNA.json) | Invariant brand tokens |
| [docs/swayam/BRAND_DNA_SCHEMA.json](../docs/swayam/BRAND_DNA_SCHEMA.json) | Brand DNA schema |
| [docs/swayam/CREATIVE_DNA_SCHEMA.json](../docs/swayam/CREATIVE_DNA_SCHEMA.json) | Per-creative DNA schema |
| [docs/swayam/social-media-context-sms.md](../docs/swayam/social-media-context-sms.md) | Voice, audience, pillars |

## Prompt merge

See [brand-social-creative-pipeline/references/prompt-merge.md](./brand-social-creative-pipeline/references/prompt-merge.md).

## Bootstrap skills (quarterly / new client)

- **design-brand-guardian** — Phase 1 brand identity (`BRAND_IDENTITY.md`)
- **creator-profile-teardown** — Instagram/social profile analysis before strategy
