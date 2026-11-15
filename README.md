# ClawdBase agent skills

Reusable instructions for AI agents that assess agents, skills and creators using Clawdbase.

## Skills

- [`agent-trust-assessment`](skills/agent-trust-assessment/SKILL.md) — resolve identities and distinguish public score snapshots from newly requested trust assessments.

Each skill follows the [Agent Skills format](https://agentskills.io/specification): a directory containing `SKILL.md` and optional supporting files. The `skills/` directory is a repository layout, not a universal auto-discovery location. To install, copy the entire skill directory, including `references/`, into the skills directory documented by your agent (for example, a project-level `.agents/skills/` if your client supports it). Reload or restart the agent if needed.

## Requirements and safety

The Clawdbase workflows require network access and a supported MCP connection or REST access key. A fresh score may consume an allowance or credits; search and scoring are different operations. Read the skill before use. A trust score is not proof that code is safe.

Never commit credentials, access keys, personal configuration, or private assessment results. Review all files and Git history before publication; `.gitignore` is not a secret scanner.

## Verify

Run `python3 -m unittest discover -s tests -v` for offline structural checks. For full specification validation, use `skills-ref validate skills/agent-trust-assessment` if the [reference validator](https://github.com/agentskills/agentskills/tree/main/skills-ref) is installed.

## Publishing

Credentials, remotes and commit identity are local configuration and must not be committed. Verify the intended GitHub account, commit identity, remote and files before committing or pushing. The ClawdBase project may use a different GitHub account from your other repositories; do not assume your global Git settings are appropriate.

## License

[MIT](LICENSE).
