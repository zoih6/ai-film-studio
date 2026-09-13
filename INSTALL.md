# Install AI Film Studio

AI Film Studio is a reusable agent skill and plugin. The canonical repository is:

> `https://github.com/zoih6/ai-film-studio`

For a generic agent that supports repository-based skills, provide the URL together with this instruction:

```text
Install the AI Film Studio skill/plugin from https://github.com/zoih6/ai-film-studio.
Read the repository's AGENTS.md for maintenance guidance, then use SKILL.md as the canonical behavior and start at workflows/intent-router.md.
```

## Claude Code

```bash
claude plugin marketplace add https://github.com/zoih6/ai-film-studio
claude plugin install ai-film-studio@ai-film-studio
```

If the installed Claude Code version accepts a GitHub repository directly, use:

```bash
claude plugin marketplace add zoih6/ai-film-studio
claude plugin install ai-film-studio@ai-film-studio
```

Verify:

```bash
claude plugin list
claude plugin validate .
```

## Codex

```bash
codex plugin marketplace add zoih6/ai-film-studio --ref main
codex plugin add ai-film-studio@ai-film-studio
```

Verify:

```bash
codex plugin list
```

## Generic Agent Skills Standard

Clone or download the repository, then install the repository directory as a skill. The canonical file is:

```text
SKILL.md
```

The compatibility path is also available at:

```text
skills/ai-film-studio/SKILL.md
```

After installation, invoke it with a natural-language request such as:

```text
Use AI Film Studio. Create a 15-second Arabic commercial for a specialty coffee brand for Reels, including a brief, big idea, shot cards, image prompts, motion prompts, audio plan, end card, and quality checks.
```

## Manual local installation

For tools that load skills from a local directory:

```bash
mkdir -p ~/.claude/skills/ai-film-studio
cp SKILL.md ~/.claude/skills/ai-film-studio/SKILL.md
cp -R workflows references schemas styles quality examples ~/.claude/skills/ai-film-studio/
```

## Update

Pull the latest repository and reinstall or refresh the plugin/skill using the same route. Do not edit the compatibility copies independently; `SKILL.md` is the source of truth.

## Uninstall

Use the host's plugin removal command, or remove the manually installed directory:

```bash
rm -rf ~/.claude/skills/ai-film-studio
```

## First-run checklist

1. Read `SKILL.md`.
2. Route the request through `workflows/intent-router.md`.
3. Load only the selected workflow and its required references.
4. Preserve style locks and entity continuity.
5. Run the relevant quality gates before delivery.
