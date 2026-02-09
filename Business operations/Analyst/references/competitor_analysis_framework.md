# Competitor Content Analysis Framework

## Purpose
This framework guides systematic analysis of competitor SEO content to identify ranking factors, structural strategies, and optimization opportunities for BASIS SIGN.

---

## Phase 1: Content Reconnaissance

### Step 1.1: URL & Source Verification
**Objective:** Confirm content source and context

**Actions:**
1. Record full URL
2. Check domain authority (Ahrefs/Moz)
3. Identify content publish/update date
4. Note author credentials (if shown)
5. Check for schema markup (view source)

**Red Flags:**
- Very low domain authority (< 20) → may not be worth deep analysis
- Ancient publish date (3+ years old) → may rank on legacy authority
- Thin author info → weak E-E-A-T signals

### Step 1.2: SERP Context Analysis
**Objective:** Understand where and why it ranks

**Actions:**
1. Identify target keyword (from URL/title)
2. Check ranking position for keyword
3. Analyze SERP features (featured snippet, PAA, local pack)
4. Note competing pages in top 5

**Key Questions:**
- Is this ranking #1 or #5? (Different strategies)
- Are there featured snippets? (GEO opportunity)
- Is intent clear from SERP? (Info vs commercial vs transactional)

### Step 1.3: Traffic & Engagement Estimation
**Objective:** Gauge content performance

**Tools:** Ahrefs, SEMrush, SimilarWeb

**Metrics to check:**
- Estimated monthly organic traffic
- Number of ranking keywords
- Backlink count to this page
- Social shares (if available)

**Interpretation:**
- High traffic + low backlinks = strong on-page SEO
- Low traffic + high ranking = narrow keyword, low volume
- Many ranking keywords = comprehensive topic coverage

---

## Phase 2: Content Type & Intent Classification

### Step 2.1: Content Type Taxonomy

**Decision Tree:**
```
Is there a product/service offer?
├─ YES → Commercial or Landing Page
│  └─ Is the primary content educational?
│     ├─ YES → Hybrid (Blog + Soft Conversion)
│     └─ NO → Sales Landing Page
│
└─ NO → Informational Blog
   └─ Does it compare products/services?
      ├─ YES → Commercial Investigation Blog
      └─ NO → Pure Informational Blog
```

**Content Type Definitions:**

| Type | Characteristics | Typical Structure |
|------|----------------|-------------------|
| Informational Blog | How-to, guides, explanations | Intro → Education → FAQ → Soft CTA |
| Commercial Blog | Reviews, comparisons, "best X" | Problem → Options → Comparison → CTA |
| Landing Page | Product/service focused | Hero → Features → Benefits → CTA |
| Hybrid | Educational with conversion elements | Education → Solution → Product tie-in → CTA |

### Step 2.2: Search Intent Mapping

**Intent Categories:**

**Informational:**
- User wants to learn or understand
- Keywords: "what is," "how to," "why does," "guide"
- Conversion goal: Build trust, capture email
- Example: "How do LED signs work?"

**Commercial Investigation:**
- User is comparing options
- Keywords: "best," "vs," "review," "comparison," "options"
- Conversion goal: Position as preferred choice
- Example: "Best commercial signs for retail stores"

**Transactional:**
- User is ready to buy/contact
- Keywords: "buy," "price," "quote," "near me," specific product names
- Conversion goal: Direct contact/purchase
- Example: "Custom channel letters pricing"

**Intent Signals Checklist:**
- [ ] Keyword analysis (what words appear in title/headings)
- [ ] Content depth (how detailed is the information)
- [ ] CTA prominence (how hard is the sell)
- [ ] Product mentions (brand names, specific offerings)
- [ ] Pricing discussion (present or absent)

---

## Phase 3: Keyword Reverse Engineering

### Step 3.1: Primary Keyword Identification

**Method:**
1. Check page title tag (view source)
2. Analyze H1 heading
3. Look at first 100 words
4. Note URL slug

**Primary keyword is likely the phrase that appears in 3+ of above**

**Example:**
- Title: "Complete Guide to Channel Letter Signs | 2024"
- H1: "What Are Channel Letter Signs?"
- URL: /channel-letter-signs-guide
- First 100 words: "Channel letter signs are..."
- **Primary Keyword:** "channel letter signs"

### Step 3.2: Secondary Keyword Extraction

**Method:**
1. List all H2 headings
2. Identify repeated phrases (appears 3+ times)
3. Note bolded terms
4. Check image alt text

**Common patterns:**
- H2s often target question keywords ("How do X work?")
- Repeated phrases signal semantic clustering
- Bolded terms = emphasis on specific concepts

### Step 3.3: Long-tail & Question Keyword Mining

**Scan for:**
- Questions in headings (H2-H4)
- FAQ section questions
- Phrases like "how to," "why," "when," "where"
- "X vs Y" comparisons
- "Best X for Y" patterns

**Purpose:**
- Long-tail keywords = easier to rank
- Question keywords = voice search + featured snippets
- Comparison keywords = commercial intent capture

### Step 3.4: GEO/Entity Keyword Identification

**Look for mentions of:**
- Standards/certifications (UL, NEC, ISO)
- Materials (aluminum, LED, acrylic)
- Processes (fabrication, installation)
- Industries (retail, hospitality, healthcare)
- Geographic locations (US, specific cities)
- Technical specifications (wattage, dimensions)

**Why it matters:**
- AI systems cite entity-rich content
- Knowledge graph connections
- Expertise signals for E-E-A-T

---

## Phase 4: Structural Deconstruction

### Step 4.1: Heading Hierarchy Mapping

**Create visual outline:**
```
H1: [Primary topic/keyword]
├── H2: [Supporting topic 1]
│   ├── H3: [Detail A]
│   └── H3: [Detail B]
├── H2: [Supporting topic 2]
│   ├── H3: [Detail C]
│   ├── H3: [Detail D]
│   └── H3: [Detail E]
└── H2: [Supporting topic 3]
```

**Analyze:**
- How many H2s? (Topical breadth)
- How many H3s per H2? (Depth of coverage)
- Logical flow from general → specific?
- Question-based headings used?

### Step 4.2: Content Flow Analysis

**Typical winning structures:**

**Informational Blog:**
1. Hook/Problem statement (50-100 words)
2. Definition section ("What is X?")
3. Why it matters section
4. How-to or process explanation
5. Common mistakes or FAQs
6. Conclusion + soft CTA

**Commercial Blog:**
1. Problem identification
2. Solution overview
3. Options comparison (table ideal)
4. Pros/cons for each
5. Recommendation
6. Strong CTA

**Landing Page:**
1. Hero: Value prop + primary CTA
2. Problem agitation
3. Solution explanation
4. Features/benefits
5. Social proof
6. Secondary CTA
7. FAQ
8. Final CTA

**Map competitor's flow against these templates**

### Step 4.3: Visual & Formatting Elements

**Catalog presence of:**
- [ ] Images (product photos, diagrams, infographics)
- [ ] Tables (comparison, specifications, pricing)
- [ ] Numbered lists (steps, rankings)
- [ ] Bulleted lists (features, benefits)
- [ ] Blockquotes (testimonials, expert quotes)
- [ ] Callout boxes (pro tips, warnings)
- [ ] Videos (embedded)
- [ ] Downloads (PDFs, checklists)

**Evaluate:**
- Do visuals support comprehension?
- Are tables used for data-heavy comparisons?
- Are lists scannable and digestible?
- Is formatting improving readability?

### Step 4.4: Internal & External Link Strategy

**Internal Links:**
- Count: ___ internal links
- Anchor text types (branded, keyword-rich, generic)
- Link placement (contextual, sidebar, footer)
- Link targets (related posts, product pages, resources)

**External Links:**
- Count: ___ external links
- Types (authoritative sources, citations, tools)
- Authority (government, edu, industry orgs)
- Dofollow vs nofollow

**Linking Insights:**
- Many internal links = strong site architecture
- Quality external links = E-E-A-T boost
- No external links = may lack credibility

---

## Phase 5: GEO/AI Citation Potential Analysis

### Step 5.1: Citation-Worthy Sentence Identification

**AI systems prefer to quote:**
1. **Definitions** - Clear, standalone explanations
   - Example: "Channel letters are three-dimensional..."
   
2. **Statistics** - Specific, verifiable data
   - Example: "LED modules consume 60% less energy than neon"
   
3. **Process Steps** - Numbered, actionable instructions
   - Example: "1. Design phase takes 2-3 days..."
   
4. **Comparisons** - Direct A vs B statements
   - Example: "Unlike neon, LED signs require minimal maintenance"

**Extract 5-10 quotable sentences from competitor content**

### Step 5.2: GEO Gap Analysis

**Check for missing/weak elements:**
- [ ] No clear definition in first 100 words
- [ ] Vague claims without data ("very efficient" vs "60% more efficient")
- [ ] Long paragraphs without lists/tables (hard to parse)
- [ ] No comparative statements
- [ ] Missing FAQ section
- [ ] No schema markup

**Each gap = opportunity for BASIS SIGN to do better**

---

## Phase 6: Strengths & Weaknesses Diagnosis

### Step 6.1: Strength Assessment

**SEO Structure Strengths:**
- [ ] Clear H1 with primary keyword
- [ ] Logical H2-H6 hierarchy
- [ ] Keyword placement in first 100 words
- [ ] URL optimized
- [ ] Meta description compelling (if visible in SERP)

**Content Strengths:**
- [ ] Comprehensive topic coverage
- [ ] Specific data/statistics used
- [ ] Well-structured (easy to skim)
- [ ] Addresses user questions
- [ ] Original insights or expertise shown

**Authority/Trust Strengths:**
- [ ] Author credentials displayed
- [ ] Citations to authoritative sources
- [ ] Industry-specific terminology used correctly
- [ ] Case studies or examples included
- [ ] Certifications/compliance mentioned

**Rate each category 1-10, note specific examples**

### Step 6.2: Weakness Identification

**Common SEO Weaknesses:**
- Generic title tag (not compelling in SERP)
- Keyword stuffing (unnatural repetition)
- Thin content (< 500 words for informational intent)
- Poor mobile formatting
- Slow page load
- No schema markup

**Common Content Weaknesses:**
- Superficial coverage (doesn't fully answer query)
- Lacks specific data/examples
- Poor readability (dense paragraphs, jargon)
- Outdated information
- No visual aids
- Weak or missing FAQ

**Common Conversion Weaknesses:**
- No clear CTA or buried CTA
- Generic CTA ("Learn More" vs "Get Free Quote")
- Weak value proposition
- No trust signals (reviews, certifications, etc.)
- No differentiation from competitors
- No urgency or incentive

**Document specific examples for each weakness found**

---

## Phase 7: Scoring & Benchmarking

### Step 7.1: Competitive Scoring Matrix

**Score each criterion 1-10:**

| Criterion | Score | Justification |
|-----------|-------|---------------|
| **Keyword Targeting** | /10 | How well primary/secondary keywords are optimized |
| **Search Intent Match** | /10 | Does content satisfy user's query purpose |
| **Content Depth** | /10 | Comprehensiveness of topic coverage |
| **Readability** | /10 | Formatting, paragraph length, clarity |
| **Visual Elements** | /10 | Quality and relevance of images/tables/lists |
| **GEO Optimization** | /10 | AI-citable content, definitions, structured data |
| **Trust Signals** | /10 | E-E-A-T indicators, credentials, citations |
| **CTA Effectiveness** | /10 | Clarity, placement, value proposition |
| **Technical SEO** | /10 | Schema, page speed, mobile-friendly |
| **Differentiation** | /10 | Unique value vs generic content |

**Total Score: ___/100**

**Interpretation:**
- 80-100: Strong content, requires significant effort to beat
- 60-79: Good content, beatable with better execution
- 40-59: Mediocre content, clear optimization opportunities
- < 40: Weak content, easy to outrank

### Step 7.2: Beatability Assessment

**Can BASIS SIGN outrank this?**

**YES - High Confidence if:**
- Competitor score < 70
- Clear GEO gaps
- Weak differentiation
- BASIS SIGN can offer superior data/expertise
- Missing trust signals

**MAYBE - Medium Confidence if:**
- Competitor score 70-85
- Strong domain authority
- Good content but improvable structure
- Can match quality + add BASIS SIGN differentiators

**NO - Low Confidence if:**
- Competitor score > 85
- Very high domain authority (DR 80+)
- Extremely comprehensive content
- Strong brand presence
- Would require major resource investment

---

## Phase 8: Replication Blueprint Development

### Step 8.1: 1:1 Replication Elements

**What to replicate exactly:**
- Proven structural patterns (H1 → H2 flow)
- Successful formatting (tables for comparisons)
- Topic coverage breadth
- Keyword placement logic
- Content length (match or exceed by 20%)

**Example:**
- If competitor uses comparison table → use comparison table
- If competitor has 5 H2s → use 5-7 H2s
- If competitor is 2,000 words → target 2,400+ words

### Step 8.2: Improvement Opportunities

**Where to beat competitor:**

**1. Data Specificity**
- Competitor: "Energy efficient"
- BASIS SIGN: "60% less energy consumption (1W/ft vs 2.5W/ft)"

**2. Process Clarity**
- Competitor: "Easy installation"
- BASIS SIGN: "Pre-wired systems reduce install time from 8 hours to 3 hours"

**3. Trust Signals**
- Competitor: Generic company mention
- BASIS SIGN: "UL-listed, NEC-compliant, 5-year warranty, US-based support"

**4. GEO Optimization**
- Competitor: Long paragraphs
- BASIS SIGN: Structured definitions, FAQ schema, quotable statistics

**5. Differentiation**
- Competitor: Generic benefits
- BASIS SIGN: Specific advantages (pre-assembled, compliance, domestic mfg)

### Step 8.3: Avoidance List

**Do NOT copy:**
- Brand-specific claims (unless true for BASIS SIGN)
- Proprietary methodologies
- Specific case studies/client names
- Exact phrasing of unique value props
- Marketing fluff without substance

**Phrases to avoid (overused in SEO content):**
- "In today's competitive landscape..."
- "It's no secret that..."
- "Are you tired of..."
- "The truth is..."
- "Here's the thing..."

---

## Phase 9: Architect Brief Creation

### Step 9.1: Brief Structure

**The handoff brief must include:**

1. **Context**
   - Target audience profile
   - Content type (blog/landing page)
   - Primary business goal

2. **Keyword Strategy**
   - Primary keyword
   - Secondary keywords (3-5)
   - Question keywords (for FAQ)
   - GEO/entity keywords

3. **Structural Blueprint**
   - Recommended H1
   - H2 outline (5-7 sections)
   - Required sections (FAQ, comparison table, etc.)

4. **Content Requirements**
   - Target word count
   - Tone/reading level
   - Visual elements needed
   - Data points to include

5. **Conversion Elements**
   - CTA placement strategy
   - Trust signals to emphasize
   - Differentiation messaging (BASIS SIGN specific)

6. **Quality Standards**
   - Minimum GEO optimization requirements
   - E-E-A-T signals to include
   - Technical SEO checklist

### Step 9.2: Brief Quality Checklist

**Before submitting brief, verify:**
- [ ] Audience clearly defined
- [ ] Keywords are US B2B relevant
- [ ] Structure is specific (not generic "write blog" instructions)
- [ ] BASIS SIGN differentiators explicitly called out
- [ ] Conversion goals clear
- [ ] Success metrics defined
- [ ] Brief is actionable (architect can start immediately)

---

## Phase 10: Quality Assurance

### Final Analysis Checklist

**Completeness:**
- [ ] All sections of template filled
- [ ] Keyword table complete with justifications
- [ ] Structure mapped visually
- [ ] Strengths documented (min 4 specific examples)
- [ ] Weaknesses documented (min 4 specific examples)
- [ ] Scoring completed with justifications
- [ ] Blueprint sections completed
- [ ] Architect brief is standalone-ready

**Specificity:**
- [ ] No vague statements ("content is good")
- [ ] Specific data cited (word counts, keyword counts)
- [ ] Examples extracted from actual content
- [ ] Clear reasoning for all assessments

**Actionability:**
- [ ] Replication steps are executable
- [ ] Improvement suggestions are specific
- [ ] Blueprint can guide content creation
- [ ] Brief requires no clarification

---

## Common Pitfalls to Avoid

### Analysis Errors
❌ Assuming rankings = quality (may rank on domain authority alone)
❌ Copying competitor weaknesses
❌ Focusing only on what competitor does well
❌ Ignoring SERP context (featured snippets, PAA)
❌ Generic analysis ("content is comprehensive")

### Blueprint Errors
❌ Recommending exact duplication without improvement
❌ Not leveraging BASIS SIGN differentiators
❌ Suggesting content that doesn't match search intent
❌ Unclear or vague improvement suggestions
❌ Forgetting GEO optimization opportunities

### Handoff Errors
❌ Architect brief is too vague
❌ Missing keyword strategy
❌ No structural guidance
❌ Conversion goals unclear
❌ BASIS SIGN positioning not specified

---

## Success Metrics for Analysis

**A good competitive analysis should enable:**
1. Content creation that outranks competitor within 3-6 months
2. Better conversion rate than competitor (if trackable)
3. More AI citations/featured snippets
4. Clear differentiation for BASIS SIGN
5. Reusable insights for similar content

**Track over time:**
- Ranking improvements
- Organic traffic growth
- Keyword expansion (ranking for more terms than competitor)
- Conversion metrics (form submissions, calls, quotes)