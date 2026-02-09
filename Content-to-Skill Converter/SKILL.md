---
name: content-to-skill
description: Transform tutorials, blog posts, articles, and documentation into high-quality Claude skills. Use when the user provides educational content (as file, URL, or text) and wants to convert it into a reusable skill. This skill analyzes the content structure, extracts key procedures, generates examples, and creates a complete skill package with SKILL.md, evaluation cases, and supporting files.
---

# Content-to-Skill Converter

This skill transforms educational content (tutorials, blog posts, articles, documentation) into production-ready Claude skills. It performs deep content analysis, extracts actionable procedures, and generates a complete skill package.

## When to Use This Skill

**Trigger conditions:**
- User provides a tutorial/guide and says "turn this into a skill"
- User uploads documentation and asks "make a skill from this"
- User pastes a blog post and wants to "skillify it"
- User provides a URL and asks to "convert this to a skill"
- User asks "can you create a skill based on this article?"

**Input formats supported:**
- Uploaded files: PDF, Markdown, TXT, DOCX, HTML
- URLs: Web pages, blog posts, documentation sites
- Pasted text: Direct content in the conversation

## Core Workflow

### Phase 1: Content Intake & Analysis

**Step 1: Receive Content**

Determine the input format:
- **File upload**: Use `view` tool to read the file from `/mnt/user-data/uploads/`
- **URL**: Use `web_fetch` tool to retrieve the web page content
- **Pasted text**: Process directly from conversation

**Step 2: Deep Content Analysis**

Analyze the content to understand:

1. **Content Type Classification**
   - Technical tutorial (code-heavy, step-by-step)
   - Conceptual guide (theory, principles, best practices)
   - Procedural documentation (workflows, processes)
   - Reference material (API docs, specifications)
   - Mixed/hybrid content

2. **Structure Mapping**
   - Identify main sections and subsections
   - Locate examples, code snippets, diagrams
   - Find prerequisites, dependencies, requirements
   - Extract key concepts and terminology
   - Identify decision points and variations

3. **Actionable Extraction**
   - What specific tasks does this enable?
   - What are the step-by-step procedures?
   - What are common pitfalls or mistakes?
   - What are the success criteria?
   - What edge cases or variations exist?

**Step 3: Confirm Understanding with User**

Present a structured summary:

```
I've analyzed the content. Here's what I found:

**Content Type**: [Technical Tutorial / Conceptual Guide / etc.]

**Main Topic**: [Brief description]

**Key Procedures Identified**:
1. [Procedure 1]
2. [Procedure 2]
3. [Procedure 3]

**Examples Found**: [Number] code examples / [Number] case studies

**Complexity Level**: [Beginner / Intermediate / Advanced]

Does this accurately capture the content? Is there anything specific you want emphasized or excluded?
```

Wait for user confirmation before proceeding.

### Phase 2: Skill Design

**Step 4: Define Skill Scope**

Ask the user clarifying questions:

1. **Skill Name**: What should this skill be called? (suggest a name based on content)
2. **Trigger Scope**: When should Claude use this skill?
   - Only for exact matches (narrow)
   - For related questions (medium)
   - For broad category (wide)
3. **Target Users**: Who will use this skill? (affects tone and detail level)
4. **Key Capabilities**: What should the skill enable Claude to do?

Generate 3-5 options for each question based on content analysis.

Use the `ask_user_input_v0` tool to collect preferences efficiently.

**Step 5: Structure Planning**

Based on content type and user preferences, plan the skill structure:

**For Technical Tutorials**:
- Prerequisites and setup
- Step-by-step procedures
- Code examples with annotations
- Common errors and troubleshooting
- Best practices and anti-patterns
- Evaluation test cases

**For Conceptual Guides**:
- Core concepts and definitions
- Frameworks and mental models
- Application guidelines
- Example scenarios
- Decision trees for when to apply
- Evaluation test cases

**For Procedural Documentation**:
- Process overview and goals
- Detailed step sequences
- Decision points and branching
- Quality checks and validation
- Edge cases and exceptions
- Evaluation test cases

**For Reference Material**:
- Structured reference information
- Usage patterns and examples
- Parameter/option explanations
- Common use cases
- Evaluation test cases

### Phase 3: Skill Generation

**Step 6: Generate SKILL.md**

Create the main skill file following this template:

```markdown
---
name: [skill-name]
description: [2-3 sentence description that clearly states: what this skill does, when Claude should use it, and key triggers. Be specific about triggers to ensure proper activation.]
---

# [Skill Title]

[1-2 paragraph overview explaining the skill's purpose and capabilities]

## When to Use This Skill

**Trigger conditions:**
- [Specific phrase or pattern 1]
- [Specific phrase or pattern 2]
- [Specific phrase or pattern 3]
- [Context or situation]

**Do NOT use this skill when:**
- [Anti-pattern 1]
- [Anti-pattern 2]

## Core Procedures

### [Main Procedure 1 Name]

**Purpose**: [What this procedure accomplishes]

**Prerequisites**:
- [Prerequisite 1]
- [Prerequisite 2]

**Steps**:

1. **[Step 1 Title]**
   - [Detailed instruction]
   - [Rationale or important note]
   - Example: `[code or example]`

2. **[Step 2 Title]**
   - [Detailed instruction]
   - Common pitfall: [Warning]
   
[Continue for all steps...]

**Success Criteria**:
- [How to verify completion]
- [Expected outcomes]

**Troubleshooting**:
- Problem: [Issue]
  - Solution: [Fix]

### [Main Procedure 2 Name]

[Same structure as above]

## Examples

### Example 1: [Scenario Name]

**Context**: [Setup/situation]

**Task**: [What needs to be done]

**Solution**:
```[language]
[Code or detailed example]
```

**Explanation**: [Why this works, key points]

### Example 2: [Scenario Name]

[Same structure]

## Best Practices

- **[Practice 1]**: [Explanation and reasoning]
- **[Practice 2]**: [Explanation and reasoning]

## Common Mistakes to Avoid

- **Mistake**: [What not to do]
  - **Why**: [The problem this causes]
  - **Instead**: [Correct approach]

## Edge Cases and Variations

### [Edge Case 1]
**Situation**: [When this occurs]
**Approach**: [How to handle]

## Additional Resources

[If the original content contains useful references, links, or related material]

## Notes for Claude

[Any meta-instructions about how Claude should apply this skill, tone to use, level of detail, etc.]
```

**Step 7: Create Evaluation Cases**

Generate comprehensive evaluation test cases:

Create `evals/evals.json`:

```json
{
  "evals": [
    {
      "id": 0,
      "prompt": "[Test prompt that should trigger this skill]",
      "expectations": [
        "[Expected behavior 1]",
        "[Expected behavior 2]",
        "[Expected behavior 3]"
      ],
      "files": []
    },
    {
      "id": 1,
      "prompt": "[Different test scenario]",
      "expectations": [
        "[Expected behavior]"
      ],
      "files": []
    }
  ]
}
```

**Evaluation case guidelines**:
- Create 5-10 test cases covering different aspects
- Include basic cases (happy path)
- Include edge cases and variations
- Include negative cases (shouldn't trigger)
- Each case should have 2-5 clear expectations
- Expectations should be verifiable and specific

**Step 8: Generate Supporting Files (if needed)**

Based on content, create additional files:

- **`examples/`**: Directory with example files if content includes code/data samples
- **`references/`**: Directory with reference material or quick-lookup tables
- **`templates/`**: Directory with reusable templates extracted from content
- **`README.md`**: User-facing documentation about the skill

### Phase 4: Quality Assurance

**Step 9: Self-Review**

Review the generated skill against quality criteria:

**Clarity Checklist**:
- [ ] Skill description clearly states what, when, and why
- [ ] Trigger conditions are specific and unambiguous
- [ ] Procedures have clear steps and success criteria
- [ ] Examples are relevant and well-explained
- [ ] Technical terms are defined or contextualized

**Completeness Checklist**:
- [ ] All major procedures from source content are captured
- [ ] Important edge cases are documented
- [ ] Common mistakes and troubleshooting included
- [ ] Examples cover different scenarios
- [ ] Evaluation cases test key capabilities

**Usability Checklist**:
- [ ] Structure is logical and easy to navigate
- [ ] Instructions are actionable (not just descriptive)
- [ ] Tone is appropriate for target users
- [ ] Code examples are tested/validated (if applicable)
- [ ] Cross-references and links work

**Step 10: Present to User**

Show the generated skill structure:

```
I've created a skill package based on the content. Here's what's included:

📄 **SKILL.md** - Main skill file ([X] lines)
   - [Y] core procedures
   - [Z] examples
   - Best practices and common mistakes

📁 **evals/** - Test cases
   - [N] evaluation cases covering [aspects]

[📁 **examples/** - Code/data samples] (if applicable)
[📁 **references/** - Reference material] (if applicable)

The skill will trigger when users:
- [Trigger 1]
- [Trigger 2]
- [Trigger 3]

Would you like me to:
1. Show you the complete SKILL.md file
2. Make adjustments to scope or triggers
3. Add more examples or edge cases
4. Run the evaluation tests
```

Use the `ask_user_input_v0` tool for user's next action.

**Step 11: Iterate Based on Feedback**

Based on user feedback:
- **Expand**: Add more details, examples, or edge cases
- **Refine**: Clarify instructions, improve structure
- **Adjust scope**: Narrow or broaden trigger conditions
- **Test**: Run evaluation cases to verify behavior

Continue iterating until user is satisfied.

### Phase 5: Finalization

**Step 12: Package and Export**

Once approved, prepare the final skill package:

1. **Organize files** in proper structure:
```
skill-name/
├── SKILL.md
├── evals/
│   ├── evals.json
│   └── files/ (if needed)
├── examples/ (if applicable)
├── references/ (if applicable)
└── README.md (optional)
```

2. **Create in `/home/claude/`** first, then **copy to `/mnt/user-data/outputs/`**

3. **Generate installation instructions**:

Create a `README.md` with:
- Skill overview and purpose
- Installation instructions (where to place files)
- How to verify it's working
- Example usage
- Troubleshooting tips

4. **Provide user with download**:

Use `present_files` tool to share all skill files.

**Step 13: Usage Guidance**

Provide clear instructions:

```
✅ Your skill is ready!

**To use this skill:**

1. [Installation instructions - depends on where user wants to deploy]
2. [Activation instructions]
3. [How to test it's working]

**Example usage:**
Try asking Claude: "[example trigger prompt]"

**Evaluation:**
[Instructions on how to run the eval tests]

Would you like help testing the skill or making any final adjustments?
```

## Skill Extraction Strategies

### For Code-Heavy Tutorials

**Focus on**:
- Exact command sequences and syntax
- Configuration file structures
- API call patterns
- Error messages and their solutions
- Version-specific differences
- Setup and teardown procedures

**Extract**:
- Code blocks with full context
- Comments explaining "why" not just "what"
- Dependency specifications
- Environment requirements

### For Conceptual Content

**Focus on**:
- Core principles and frameworks
- Decision-making criteria
- When to apply vs. when not to apply
- Trade-offs and considerations
- Mental models and analogies

**Extract**:
- Key definitions
- Comparison tables
- Decision trees
- Illustrative examples

### For Process Documentation

**Focus on**:
- Step sequencing and dependencies
- Decision points and branching logic
- Validation and quality checks
- Rollback and error recovery
- Stakeholder interactions

**Extract**:
- Workflow diagrams (describe in text)
- Checklists
- Template documents
- Approval criteria

## Quality Guidelines

### Writing Style for Generated Skills

**Be Specific**: Replace vague instructions with concrete steps
- ❌ "Configure the system appropriately"
- ✅ "Set the `max_retries` parameter to 3 in config.yaml"

**Be Action-Oriented**: Use imperative verbs
- ❌ "The file should be created"
- ✅ "Create the file using..."

**Provide Context**: Explain the "why" for non-obvious steps
- ✅ "Run `npm install` before building. This ensures all dependencies are available for the build process."

**Structure for Scannability**: Use headers, lists, and code blocks
- Break long procedures into numbered steps
- Use bullet points for lists of items
- Use code blocks with language tags

**Include Examples**: Show, don't just tell
- Provide concrete examples for abstract concepts
- Include both simple and complex cases
- Show common variations

### Common Pitfalls to Avoid

1. **Overly Broad Triggers**: 
   - ❌ "Use when user asks about programming"
   - ✅ "Use when user asks to implement OAuth 2.0 authentication flow"

2. **Missing Prerequisites**:
   - Always list what needs to be in place before starting

3. **Assuming Context**:
   - Don't assume knowledge not in the original content
   - Define technical terms

4. **Incomplete Error Handling**:
   - Include troubleshooting for common failures
   - Provide diagnostic steps

5. **Generic Examples**:
   - Make examples realistic and specific
   - Base examples on actual use cases from content

## Advanced Features

### Handling Multi-Part Content

If source content spans multiple articles or sections:

1. **Analyze each piece separately** to identify themes
2. **Find commonalities** and create unified procedures
3. **Preserve variations** as edge cases or alternatives
4. **Cross-reference** related sections

### Incorporating Visual Content

If source includes diagrams, screenshots, or visual aids:

1. **Describe visual content** in detail within the skill
2. **Extract the insight** the visual conveys
3. **Create text-based representations** (ASCII art, structured descriptions)
4. **Note when visuals are essential** vs. supplementary

### Handling Version-Specific Content

If content is tied to specific versions:

1. **Note version requirements** clearly in prerequisites
2. **Document version differences** in edge cases
3. **Provide migration paths** if multiple versions covered
4. **Flag deprecated approaches** with alternatives

## Meta-Skills for Claude

When applying this generated skill:

- **Recognize context**: Look for trigger phrases but also understand user intent
- **Adapt tone**: Match formality level to user and task
- **Provide right detail level**: More detail for beginners, concise for experts
- **Link to original**: Mention source content when helpful for deeper context
- **Stay current**: If skill content might be outdated, verify with web search
- **Combine with other skills**: This skill may work alongside others (e.g., docx, code execution)

## Workflow Variations

### Quick Conversion Mode

If user explicitly wants fast conversion:
1. Skip confirmation steps
2. Use default structure based on content type
3. Generate 3-5 basic eval cases
4. Present complete package immediately

### Interactive Refinement Mode

If user wants involvement:
1. Confirm understanding after analysis
2. Ask about scope and triggers
3. Show drafts of each section for approval
4. Iterate on examples and edge cases
5. Review eval cases together

### Batch Processing Mode

If user provides multiple content sources:
1. Analyze all sources together
2. Identify overlaps and contradictions
3. Create unified skill or separate skills as appropriate
4. Generate comparison matrix if creating separate skills

## Tips for Effective Skill Creation

**Start with Core Value**: What's the #1 thing this skill enables?

**Think About Discovery**: How will users know to use this skill?

**Optimize for Learning**: First-time users should be able to follow along

**Plan for Iteration**: Skills improve with usage and feedback

**Test Thoroughly**: Run the eval cases yourself before delivery

**Document Limitations**: Be clear about what the skill doesn't cover

**Maintain Traceability**: Keep links to source material for updates

---

## Example Transformation

Here's a before/after to illustrate the transformation:

### Input: Blog Post Snippet

```
"When implementing retry logic, you should always use exponential backoff.
This means increasing the wait time between retries. For example, wait 1s,
then 2s, then 4s. This prevents overwhelming the server."
```

### Output: Skill Section

```markdown
### Implementing Retry Logic with Exponential Backoff

**Purpose**: Prevent overwhelming servers during transient failures by progressively increasing wait times between retry attempts.

**When to use**:
- API requests that may fail due to rate limiting
- Network requests with intermittent connectivity
- Database operations during high load

**Steps**:

1. **Define retry parameters**
   - `max_retries`: Maximum number of attempts (typically 3-5)
   - `base_delay`: Initial wait time in seconds (typically 1s)
   - `backoff_factor`: Multiplier for each retry (typically 2)

2. **Implement the exponential backoff formula**
   ```python
   wait_time = base_delay * (backoff_factor ** attempt_number)
   ```
   
   Example progression with base_delay=1s, backoff_factor=2:
   - Attempt 1: wait 1s  (1 * 2^0)
   - Attempt 2: wait 2s  (1 * 2^1)
   - Attempt 3: wait 4s  (1 * 2^2)
   - Attempt 4: wait 8s  (1 * 2^3)

3. **Add jitter to prevent thundering herd**
   ```python
   import random
   wait_time = base_delay * (backoff_factor ** attempt) + random.uniform(0, 1)
   ```
   Prevents multiple clients from retrying at exactly the same time.

**Success Criteria**:
- Retry attempts increase wait time exponentially
- Maximum retry limit is respected
- Operations eventually succeed or fail definitively

**Common Mistakes**:
- ❌ Using fixed delay between all retries → Can overwhelm server
- ❌ Unlimited retries → Can cause indefinite hangs
- ❌ No jitter → Creates synchronized retry storms

**Edge Cases**:
- **Very slow operations**: Consider longer base_delay (5-10s)
- **Rate-limited APIs**: Match backoff to reset windows
- **Critical operations**: May need different strategy (circuit breaker)
```

---

## Closing Notes

This skill transforms passive content into active capabilities. The goal is not just to copy information, but to make it actionable and accessible through Claude's conversational interface.

Quality over speed: Take time to understand the content deeply and structure it well. A well-crafted skill serves users for years.
