# LLM Session Quick Start Guide

## 🚀 Enhanced Immediate Actions (First 30 seconds)

### 1. Context Health Validation (NEW - CRITICAL)
```
1. VALIDATE: Check if all required context files exist
2. FRESHNESS: Check file timestamps and warn if stale (>7 days)
3. CONSISTENCY: Cross-check information between files for conflicts
4. BACKUP: Note current state before any changes
```

### 2. Read Session Context with Validation
```
1. READ: dynamic/session-handoff.md (immediate context)
2. READ: dynamic/current-iteration.md (active hypothesis)
3. READ: static/environment.md (hardware/software constraints - ESSENTIAL)
4. CHECK: dynamic/failed-solutions/ (MANDATORY before suggesting solutions)
5. REFERENCE: evolving/assumptions-log.md (validation history)
6. VALIDATE: Confirm understanding of context before proceeding
```

### 3. Generate Context-Specific Questions with Understanding Validation
After reading the context files, ask the human 3-5 specific questions based on what you discovered, then validate your understanding.

**IMPORTANT:** Use `guides/llm-context-question-guide.md` for detailed guidance on generating appropriate questions.

**Quick Question Framework:**
- **Analyze Context:** Identify status indicators, blockers, priorities, and environment changes
- **Generate Specific Questions:** Reference exact details from context files
- **Focus on Decisions:** Ask about actionable choices that affect the current session
- **Be Contextual:** Base questions on what you actually read, not generic templates

**Example Approach:**
1. Read session-handoff.md → Ask about specific blockers or priorities mentioned
2. Read current-iteration.md → Ask about hypothesis status and next steps
3. Read environment.md → Verify current setup and constraints
4. Check failed-solutions/ → Avoid suggesting previously failed approaches

### 3. Identify Current Task
- **Current Iteration:** Check session-handoff.md for iteration number and hypothesis
- **Priority Actions:** Check "Immediate Next Actions" section
- **Blockers:** Check for any current blockers or risks

### 4. Verify System State
```bash
# Quick validation check
cd /path/to/your/project/LM_context
python3 dynamic/assumption-validator.py --stability-hours 0.1
```

## 📋 Session Workflow

### For Continuing Current Iteration
1. **Check Progress:** Review current-iteration.md status
2. **Run Validation:** Use assumption-validator.py to verify current state
3. **Execute Priority Task:** Focus on highest priority action from session-handoff.md
4. **Update Context:** Update assumptions-log.md with new evidence
5. **Prepare Handoff:** Update session-handoff.md for next session

### For Starting New Iteration
1. **Complete Previous:** Ensure previous iteration is properly closed
2. **Update Backlog:** Mark completed stories in product-backlog.md
3. **Create New Context:** Update current-iteration.md with new hypothesis
4. **Add Validation:** Update assumption-validator.py with new test methods
5. **Set Handoff:** Update session-handoff.md with new iteration context

### For Ending Sessions with Enhanced Verification
**IMPORTANT:** Use `guides/llm-session-closure-guide.md` for detailed guidance on proper session closure.

**Enhanced Closure Framework:**
1. **Pre-Save Validation:** Assess what was completed and validate completeness
2. **Create Backup:** Create timestamped backup of all context files before updates
3. **Update Files with Verification:** Update all context files and verify each update succeeded
4. **Quality Validation:** Check that updated context meets quality standards
5. **Generate Closure Questions:** Ask context-specific questions about next session priorities
6. **Confirm Proper Closure:** Validate that all information was captured and next session is prepared

**File Update Verification Checklist:**
- [ ] session-handoff.md updated with next session priorities
- [ ] current-iteration.md updated with progress and status
- [ ] assumptions-log.md updated with new evidence/validation results
- [ ] working-solutions.md updated with any new working commands
- [ ] failed-solutions/ updated with any failed approaches
- [ ] knowledge-base/ updated with new insights (if applicable)
- [ ] daily log created in archive/daily-logs/

## 🔧 Essential Commands

### Validation Framework
```bash
# Location: /path/to/your/project/LM_context
cd /path/to/your/project/LM_context

# Quick validation (all current hypotheses)
python3 dynamic/assumption-validator.py

# Extended stability test
python3 dynamic/assumption-validator.py --stability-hours 1

# Full validation test
python3 dynamic/assumption-validator.py --stability-hours 24 --stability-only
```

### Working Solutions (Reference Only)
```bash
# Location: /path/to/your/main/project
cd /path/to/your/main/project

# Run project-specific tests (customize for your domain)
./scripts/run_tests.sh

# Basic functionality test (customize for your project)
./scripts/basic_test.sh
```

## ⚠️ Critical Rules

### CRITICAL: LM_context/ vs Project Knowledge Distinction

**What LM_context/ Contains (Session Management):**
- **Session state and handoffs** - Where you left off, what's next
- **Iteration tracking and progress** - Current goals, success criteria, completion status  
- **Working/failed solution patterns** - What works, what doesn't, why
- **Optimization guides and workflows** - How to work efficiently

**What Lives in Project Root (NOT in LM_context/):**
- **Source code and implementations** - Actual project deliverables
- **Technical documentation** - API docs, architecture guides, tutorials
- **Build systems and scripts** - Working project scripts and configurations
- **Domain expertise** - Complete knowledge bases and reference materials

**LLM Behavior Rules:**
- **DO:** Update LM_context/ files with session progress and solution patterns
- **DON'T:** Put complete tutorials, API documentation, or source code in LM_context/
- **DO:** Reference project files when needed, but keep context focused on session management
- **DON'T:** Duplicate project knowledge in context files - use references instead

**Example - GStreamer Project:**
```
✅ CORRECT in LM_context/: "Working solution: gst-launch-1.0 v4l2src ! tee ! udpsink"
❌ WRONG in LM_context/: Complete GStreamer plugin development tutorial

✅ CORRECT in LM_context/: "Failed: RTSP streaming (>200ms latency)"  
❌ WRONG in LM_context/: Full RTSP protocol specification

✅ CORRECT in LM_context/: "Next: Test multi-consumer tee performance"
❌ WRONG in LM_context/: Complete melexis_v4l2.h API documentation
```

### ALWAYS Use Validation Script
- **Never** manually test assumptions
- **Always** use `python3 dynamic/assumption-validator.py`
- **Update** script when adding new hypotheses

### Update Script for New Assumptions
When adding new hypothesis HX:
1. Add `validate_hX_new_hypothesis()` method
2. Add to `run_all_validations()` list
3. Test the new validation
4. Update assumptions-log.md

### File Update Priority
1. **HIGH:** dynamic/session-handoff.md (every session)
2. **MEDIUM:** dynamic/current-iteration.md (when progress made)
3. **MEDIUM:** evolving/assumptions-log.md (when validation done)
4. **LOW:** Other files (as needed)

## 📁 File Structure Reference

```
LM_context/
├── static/                    # Read only when environment changes
│   ├── environment.md         # Hardware, network, software config
│   └── external-resources.md  # Documentation links
├── evolving/                  # Reference for planning
│   ├── product-backlog.md     # User stories and iterations
│   ├── assumptions-log.md     # Hypothesis validation history
│   ├── risk-assessment.md     # Risk analysis
│   └── validation.md          # Success criteria
├── dynamic/                   # Always read for current context
│   ├── session-handoff.md     # CRITICAL - immediate context
│   ├── current-iteration.md   # Active iteration status
│   ├── assumption-validator.py # Automated testing framework
│   └── working-solutions.md   # Proven commands and solutions
├── guides/                    # Meta-instructions
│   ├── llm-session-quick-start.md # This file
│   └── human-maintenance-guide.md # Human maintenance
└── archive/                   # Completed work (don't read)
```

## 🎯 Success Indicators

### Good Session Start
- [ ] Session handoff context understood
- [ ] Current hypothesis identified
- [ ] Priority actions clear
- [ ] Validation script ready

### Productive Session
- [ ] Validation script used for all testing
- [ ] Evidence documented in assumptions-log.md
- [ ] Progress updated in current-iteration.md
- [ ] Next session prepared in session-handoff.md

## 🚨 Emergency Procedures

### If Context Is Unclear
1. Run validation script to assess current technical state
2. Check working-solutions.md for proven commands
3. Review assumptions-log.md for last validated state
4. Update session-handoff.md with findings

### If Validation Script Fails
1. Check environment connectivity and dependencies
2. Verify project setup and configuration
3. Check system installation and requirements
4. Review validation-results.log for errors

## 💡 Cost Optimization

### Token Usage Strategy
- **Primary:** dynamic/ files (always read)
- **Secondary:** evolving/ files (reference as needed)
- **Minimal:** static/ files (only when environment changes)
- **Never:** archive/ files (completed work)

### Efficiency Tips
- Use assumptions-log.md to avoid re-deriving solutions
- Reference working-solutions.md for proven commands
- Use validation script instead of manual testing
- Keep session-handoff.md concise and actionable

## 📞 Quick Reference

### Current Project Context
- **Development Environment:** [Customize for your project]
- **Main Project Directory:** [Your project path]
- **Context Files:** [Your LM_context path]
- **Key Technologies:** [Your project technologies]

### Proven Architecture
- **System Design:** [Your project architecture]
- **Performance Metrics:** [Your performance benchmarks]
- **Validation Framework:** Automated via assumption-validator.py
- **Success Criteria:** [Your project success metrics]

### Next Likely Tasks
- [Customize based on your project roadmap]
- [Add your typical next steps]
- [Include your common iteration goals]

---

**Last Updated:** July 23, 2025  
**Purpose:** Generic LLM session procedures for any project domain  
**Scope:** Reusable across all project types
