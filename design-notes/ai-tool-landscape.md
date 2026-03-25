# GEAP 103: AI Tool Landscape Notes

**Date:** 2026-03-08
**Context:** Planning session reviewing what AI tools students will actually have access to in September 2026, and whether the course's tool layer is robust enough for students who can't or won't pay for premium subscriptions.

---

## Tool inventory for non-paying students

| Tool | Source | Covers |
|------|--------|--------|
| M365 Copilot | Humber institutional license | Word, Excel, PowerPoint (Weeks 2, 5, 6, 9) |
| GitHub Copilot Pro | GitHub Student Developer Pack (free) | Git workflows, coding, PR descriptions (Weeks 3, 7, 8, 11-14) |
| GitHub Codespaces | GitHub Student Developer Pack (free) | Cloud dev environment (weak-hardware backstop) |
| ChatGPT / Claude free tiers | Self-serve | General chat, troubleshooting, brainstorming |

**Conclusion:** This is a strong baseline. The two Copilots (M365 and GitHub) together cover nearly every task type in the course without students paying anything. Students who also pay for Claude or ChatGPT will have a smoother experience, but the assessment structure (articulation, documentation, communication -- not technical sophistication) means they aren't graded on what money buys.

---

## GitHub Student Developer Pack: key items for GEAP 103

From the Pack (verified 2026-03-08):

- **GitHub Copilot Pro** -- free while a student. AI pair programmer in VS Code. Covers the coding and Git side that M365 Copilot doesn't touch.
- **GitHub Codespaces** -- free Pro-level access. Cloud dev environment in the browser. Partial answer to hardware diversity (students with underpowered laptops can work in Codespaces). Won't run local LLMs, but handles Git and coding tasks.
- **GitHub Desktop** -- free for everyone. Simpler Git GUI.
- **VS Code** -- free for everyone.

Other Pack items potentially relevant: Notion (collaboration), 1Password (security habits), JetBrains (alternative IDE).

---

## Local models (Qwen, Llama, etc.)

### The "use AI to install AI" insight

Initial concern was that installing a local model (Ollama + Qwen or similar) is too complex for B1 learners. But the course's own thesis undermines that objection: the whole point is that students use AI to do technical things. Having Copilot walk a student through `brew install ollama && ollama pull qwen2.5` is a legitimate GEAP 103 exercise in task articulation and troubleshooting (CLOs 1, 5).

### Practical status

- **Not needed as load-bearing infrastructure.** The M365 Copilot + GitHub Copilot Pro combination covers the course's task types.
- **Good optional exercise.** "Use AI to install a local AI" exercises CLOs 1, 5, and creates natural mismatch (instructions won't work identically on every machine).
- **Hardware is the real constraint, not setup.** Students with 8GB RAM on older machines will struggle with even 7B models regardless of how smooth the installation is. Students with Apple Silicon or 16GB+ will be fine.
- **The attempt has value even if it fails.** A student who tries, hits a wall, writes a help request (CLO 6), and falls back to cloud tools has done meaningful learning.

### By September 2026

Local model capabilities are improving rapidly. On-device AI is being built into OS layers (Apple Intelligence, etc.). The hardware floor for useful local models is dropping. Expect the landscape to be more favourable than today, but don't design the course to depend on it.

---

## Open questions to resolve before September

1. **Verify M365 Copilot scope.** Does Humber's M365 Education license include full Copilot in Word/Excel/PowerPoint, or just the basic Copilot chat? Enterprise and Education licensing differ. If students don't get Copilot integrated into the Office apps, the entire tool layer for Weeks 2, 5, 6, 9 needs rethinking. **Check with IT now.**

2. **GitHub Education verification process.** How long does it take for Humber students to get verified? Build onboarding time into Week 3 (or earlier) so students have GitHub Copilot Pro active before they need it.

3. **Free tier durability.** ChatGPT's free tier has been getting more generous over time. Check the state of play in May/June 2026 before finalising any student-facing guides.

4. **Codespaces for hardware equity.** Could Codespaces be the default recommendation for students with weak hardware, rather than asking them to install local tools? Lower friction, but requires reliable internet.
