# Example: Converting a Tutorial to a Skill

This example demonstrates how the content-to-skill converter transforms a tutorial into a functional skill.

## Source Tutorial: "Git Workflow Best Practices"

### Original Content

```markdown
# Git Workflow Best Practices

## Creating Feature Branches

When working on a new feature, always create a dedicated branch:

1. Pull the latest changes from main: `git pull origin main`
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit regularly
4. Push your branch: `git push -u origin feature/your-feature-name`

Never commit directly to the main branch!

## Writing Good Commit Messages

A good commit message should:
- Start with a verb in present tense (Add, Fix, Update)
- Be concise but descriptive
- Reference issue numbers if applicable

Good example: "Add user authentication with JWT"
Bad example: "stuff"

## Code Review Process

Before merging:
1. Create a pull request
2. Request reviews from at least 2 team members
3. Address all comments
4. Ensure CI/CD passes
5. Squash commits before merging

Common mistakes:
- Merging without approval
- Leaving merge conflicts unresolved
- Not updating documentation
```

## Generated Skill

### SKILL.md (excerpt)

```markdown
---
name: git-workflow
description: Guide users through professional Git workflows including feature branching, commit message conventions, and code review processes. Use when users ask about Git best practices, how to create branches, write commits, or manage pull requests. Triggers on questions about Git workflow, branching strategies, or team collaboration with Git.
---

# Git Workflow Best Practices

This skill helps users follow professional Git workflows for team collaboration.

## When to Use This Skill

**Trigger conditions:**
- User asks "how should I create a Git branch?"
- User mentions "Git workflow" or "branching strategy"
- User asks about commit message standards
- User needs help with pull request process
- User asks "what's the right way to use Git?"

**Do NOT use this skill when:**
- User needs basic Git commands (that's general knowledge)
- User asks about Git installation or configuration
- Question is about GitHub/GitLab features, not Git workflow

## Core Procedures

### Creating Feature Branches

**Purpose**: Isolate feature development from the main codebase to enable parallel work and easier code review.

**Prerequisites**:
- Git repository initialized
- Access to remote repository
- Main branch is stable

**Steps**:

1. **Sync with latest main**
   ```bash
   git pull origin main
   ```
   - Ensures your starting point is current
   - Prevents merge conflicts later
   - Common pitfall: Skipping this step leads to out-of-date branches

2. **Create descriptive feature branch**
   ```bash
   git checkout -b feature/user-authentication
   ```
   - Naming convention: `feature/`, `bugfix/`, `hotfix/`
   - Use kebab-case: `feature/add-payment-gateway`
   - Include issue number if applicable: `feature/123-user-auth`

3. **Make changes and commit regularly**
   - Commit logical chunks of work
   - Each commit should be a complete, working change
   - Don't wait until "everything is done"

4. **Push feature branch to remote**
   ```bash
   git push -u origin feature/user-authentication
   ```
   - The `-u` flag sets upstream tracking
   - Enables pull request creation
   - Creates backup of your work

**Success Criteria**:
- Branch created with descriptive name
- Synced with latest main before starting
- Changes pushed to remote repository

**Troubleshooting**:
- Problem: "Branch already exists"
  - Solution: Use `git checkout feature/name` to switch to it, or choose different name

- Problem: Diverged from main after starting
  - Solution: Regularly rebase: `git rebase main`

### Writing Effective Commit Messages

**Purpose**: Create clear project history that helps teammates understand changes and helps future debugging.

**Standards**:

1. **Use imperative present tense**
   - ✅ "Add user authentication"
   - ✅ "Fix login validation bug"
   - ✅ "Update dependencies to latest versions"
   - ❌ "Added authentication" (past tense)
   - ❌ "Adds authentication" (third person)

2. **Structure: Type + Brief Description**
   ```
   Add JWT-based user authentication

   - Implement token generation on login
   - Add middleware for protected routes
   - Include token refresh mechanism
   
   Closes #234
   ```

3. **Keep subject line under 50 characters**
   - Forces conciseness
   - Displays well in Git logs
   - Detailed explanation goes in body

**Common Mistake**:
- ❌ Vague messages like "fix stuff", "update", "changes"
- **Why**: Impossible to understand what changed without reading code
- **Instead**: Be specific about what and why

**When to reference issues**:
- Always include issue number if available
- Use "Closes #123" to auto-close issues
- Helps track which commits address which issues

### Code Review Process

**Purpose**: Ensure code quality, share knowledge, and catch bugs before they reach production.

**Prerequisites**:
- Feature branch pushed to remote
- Changes are complete and tested locally
- Code follows project standards

**Steps**:

1. **Create pull request**
   - Title should summarize the change
   - Description should explain what, why, and how
   - Reference related issues
   - Add screenshots for UI changes

2. **Request reviews**
   - Minimum 2 reviewers (team standard)
   - Choose people familiar with the affected code
   - Tag them directly for faster response

3. **Respond to feedback**
   - Address all comments (even if you disagree)
   - Make requested changes in new commits
   - Explain your reasoning if pushing back
   - Mark conversations as resolved

4. **Ensure CI/CD passes**
   - All tests must pass
   - Code coverage meets threshold
   - Linting and formatting checks pass
   - Build succeeds

5. **Squash and merge**
   ```
   git rebase -i main  # Squash commits locally
   ```
   - Combines related commits into one
   - Creates cleaner project history
   - Keep logical separation if needed

**Success Criteria**:
- All reviewers approved
- All CI checks green
- No unresolved conversations
- Conflicts resolved

**Common Mistakes**:

- **Merging without approval**
  - Why: Bypasses quality checks and team oversight
  - Instead: Wait for required approvals

- **Leaving merge conflicts unresolved**
  - Why: Breaks the main branch for everyone
  - Instead: Resolve conflicts in your branch first

- **Not updating documentation**
  - Why: Code and docs become out of sync
  - Instead: Update docs in the same PR

## Edge Cases and Variations

### Working with Long-Running Features

**Situation**: Feature takes weeks/months to complete

**Approach**:
- Regularly rebase on main to stay current
- Consider feature flags to merge incrementally
- Break into smaller PRs if possible

### Emergency Hotfixes

**Situation**: Critical bug needs immediate fix

**Approach**:
```bash
git checkout -b hotfix/critical-login-bug main
# Make minimal fix
# Fast-track review process
# Merge and deploy immediately
```

## Notes for Claude

When helping users with Git workflow:
- Emphasize the "why" behind practices, not just the "how"
- Adjust formality based on team context (startup vs enterprise)
- Consider project size (solo vs large team) when recommending practices
- If user's team has different standards, respect those
- Provide commands but also explain what they do
```

### evals/evals.json (excerpt)

```json
{
  "evals": [
    {
      "id": 0,
      "prompt": "What's the right way to create a feature branch in Git?",
      "expectations": [
        "Skill is triggered",
        "Explains to pull latest main first",
        "Shows git checkout -b command with naming convention",
        "Mentions pushing branch to remote",
        "Includes rationale for each step"
      ]
    },
    {
      "id": 1,
      "prompt": "How do I write good commit messages?",
      "expectations": [
        "Skill is triggered",
        "Recommends imperative present tense",
        "Provides good vs bad examples",
        "Mentions 50 character limit for subject",
        "Explains when to reference issues"
      ]
    }
  ]
}
```

## Key Transformations

The content-to-skill converter made these improvements:

1. **Added Clear Triggers**: Specified exactly when the skill should activate
2. **Structured Procedures**: Broke down steps with clear purposes and rationale
3. **Enhanced Examples**: Added more context and explanation to code examples
4. **Included Edge Cases**: Covered long-running features and hotfixes
5. **Added Troubleshooting**: Anticipated common problems and solutions
6. **Created Evaluation Cases**: Tests to verify skill works correctly
7. **Added Meta-Instructions**: Guided Claude on how to apply the skill

## Usage

To use this generated skill, Claude would:

**User**: "What's the best way to handle Git branches in a team?"

**Claude** (using the skill):
> When working on a team, you should use feature branches to isolate your work. Here's the workflow:
>
> First, sync with the latest main branch:
> ```bash
> git pull origin main
> ```
>
> Then create a descriptive feature branch:
> ```bash
> git checkout -b feature/your-feature-name
> ```
>
> The naming convention helps organize branches - use `feature/` for new features, `bugfix/` for fixes, and `hotfix/` for urgent production fixes.
>
> [Continues with detailed guidance from the skill...]

## Benefits

The skill enables:
- ✅ Consistent Git practices across conversations
- ✅ Detailed, step-by-step guidance
- ✅ Context-aware recommendations
- ✅ Proactive error prevention
- ✅ Reusable knowledge capture
