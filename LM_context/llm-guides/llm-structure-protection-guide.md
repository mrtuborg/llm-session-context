# LLM Context System Structure Protection Guide
**Generator System:** LLM_Context_System
**Last Updated:** July 23, 2025
**Purpose:** Prevent breaking established context structure across projects

## 🎯 When LLMs Should Use This Guide

### Mandatory Reading Scenarios:
1. **Before any file operations** - Creating, moving, deleting, or renaming files in LM_context/
2. **When human requests "cleanup"** - Before reorganizing or restructuring context files
3. **During session end** - Before updating context files to ensure proper structure
4. **When encountering missing files** - Before recreating or restoring context structure
5. **Before suggesting structural changes** - When human asks about improving organization

### Automatic Triggers:
- **File not found errors** in LM_context/ → Read this guide before suggesting fixes
- **Human mentions "broken context"** → Read this guide to understand recovery procedures
- **Session handoff failures** → Check structure against this guide's requirements
- **Before any `mkdir`, `mv`, `rm` commands** in LM_context/ → Validate against protected structure

## 🚨 LLM Action Protocol

### Before Any Structure Changes:
1. **STOP** - Read this entire guide first
2. **VALIDATE** - Check proposed changes against protected structure
3. **CONFIRM** - Ask human for explicit approval of any structural modifications
4. **DOCUMENT** - Update this guide if new patterns emerge

### Emergency Response:
If LM_context/ structure is broken:
1. **IMMEDIATE** - Read this guide's recovery commands
2. **ASSESS** - Determine what's missing or corrupted
3. **RESTORE** - Use emergency recovery commands
4. **VERIFY** - Run assumption-validator.py to confirm structure

## 🚨 Critical: Protected Structure Pattern

### 📁 Standard LLM Context Structure (Never Modify):
```
LM_context/
├── README.md                          # Project overview and system integration
├── collaboration-workflow.md          # Human-LLM collaboration patterns
├── human-guides/                      # Human interface guides
│   ├── human-maintenance-guide.md     # System maintenance procedures
│   └── human-quick-commands.md        # Copy-paste commands for humans
├── llm-guides/                        # LLM session guides
│   ├── llm-session-quick-start.md     # LLM session procedures
│   ├── llm-context-question-guide.md  # Context-based questioning
│   └── llm-structure-protection-guide.md # This file - structure protection
├── static/                            # Tier 1: Static Foundation
│   ├── environment.md                 # Hardware/network configuration
│   ├── knowledge-base/                # Compiled knowledge
│   └── resources/                     # PDF documents and references
├── evolving/                          # Tier 2: Evolving Product
│   ├── assumptions-log.md             # Hypothesis validation history
│   └── project-plan.md                # Original project plan
├── dynamic/                           # Tier 3: Dynamic Session
│   ├── session-handoff.md             # Session context and handoffs
│   ├── current-iteration.md           # Active iteration status
│   ├── assumption-validator.py        # Automated validation framework
│   └── failed-solutions/              # Failed solution tracking
└── archive/                           # Completed iterations and logs
    └── daily-logs/                    # Session logs
```

## 🛡️ Protection Rules for All Projects

### Rule 1: Never Delete Core Directories
**Forbidden in any project:**
- Deleting `static/`, `evolving/`, `dynamic/`, `guides/`, `archive/`
- Renaming core structure directories
- Moving critical files like `session-handoff.md`, `current-iteration.md`

### Rule 2: Generator Guides Are Read-Only
**In project LM_context/human-guides/ and LM_context/llm-guides/:**
- Never modify guides copied from this generator
- Update at generator source, then copy to projects
- Treat as immutable reference material

### Rule 3: Archive, Don't Delete
**Correct approach across all projects:**
- Move outdated files to appropriate `archive/` subdirectories
- Create dated subdirectories for organization
- Preserve context history for learning

## 🔧 How This Guide Gets to Projects

### Automatic Deployment:
This guide is automatically copied to new projects when humans run:
```bash
python3 /Users/vn/ws/LLM_Context_System/deploy.py /path/to/new/project
```

### LLM Access Pattern:
1. **Human deploys** LLM Context System to their project
2. **This guide gets copied** to `project/LM_context/llm-guides/llm-structure-protection-guide.md`
3. **LLM reads this guide** when triggered by scenarios listed above
4. **LLM follows protection rules** to maintain structure integrity

### Generator Maintenance (For System Developers):
1. **Update source:** Modify in `/Users/vn/ws/LLM_Context_System/LM_context/llm-guides/`
2. **Deploy updates:** Use deploy.py to copy updated guides to projects
3. **Never modify directly:** Don't edit guides in individual projects

## 📋 LLM Usage Checklist

When LLM encounters structure-related tasks:

- [ ] **BEFORE file operations:** Read this guide's protection rules
- [ ] **CHECK structure:** Validate against the standard pattern above
- [ ] **ASK permission:** Get human approval for any structural changes
- [ ] **USE recovery commands:** If structure is broken, use commands below
- [ ] **VERIFY result:** Run assumption-validator.py after changes

## 🚨 Emergency Recovery Commands

### For Any Project (LLM can suggest these to humans):
```bash
# Restore guides from generator (human runs this)
python3 /Users/vn/ws/LLM_Context_System/deploy.py . --force

# Recreate missing directories
mkdir -p LM_context/{static,evolving,dynamic,archive/daily-logs}
mkdir -p LM_context/static/{knowledge-base,resources}
mkdir -p LM_context/dynamic/failed-solutions

# Restore from git if available
git checkout HEAD~1 -- LM_context/
```

## 🎯 Philosophy: Context vs Knowledge

### LLM Context System Manages:
- Session state and handoffs
- Iteration tracking and progress
- Working/failed solution patterns
- Optimization guides and workflows

### Project Knowledge Lives Elsewhere:
- Technical documentation in project docs/
- Domain expertise in appropriate project directories
- Learning materials in personal knowledge systems
- Code and implementation in src/ and related directories

---

**The LLM Context System is infrastructure - protect it like any critical system component! 🛡️**
