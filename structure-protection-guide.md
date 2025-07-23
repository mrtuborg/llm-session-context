# LLM Context System Structure Protection Guide
**Generator System:** LLM_Context_System
**Last Updated:** July 23, 2025
**Purpose:** Prevent breaking established context structure across projects

## 🚨 Critical: Protected Structure Pattern

### 📁 Standard LLM Context Structure (Never Modify):
```
LM_context/
├── README.md                          # Project overview and system integration
├── static/                            # Tier 1: Static Foundation
│   ├── environment.md                 # Hardware/network configuration
│   ├── external-resources.md          # Documentation links
│   └── resources/                     # PDF documents and references
├── evolving/                          # Tier 2: Evolving Product
│   ├── product-backlog.md             # User stories and iterations
│   ├── assumptions-log.md             # Hypothesis validation history
│   ├── project-plan.md                # Original project plan
│   └── validation.md                  # Success criteria
├── dynamic/                           # Tier 3: Dynamic Session
│   ├── session-handoff.md             # Session context and handoffs
│   ├── current-iteration.md           # Active iteration status
│   ├── working-solutions.md           # Proven solutions
│   └── failed-solutions/              # Failed solution tracking
├── guides/                            # Generated guides (copied from this system)
└── archive/                           # Completed iterations and logs
    ├── daily-logs/                    # Session logs
    └── planning/                      # Archived planning documents
```

## 🛡️ Protection Rules for All Projects

### Rule 1: Never Delete Core Directories
**Forbidden in any project:**
- Deleting `static/`, `evolving/`, `dynamic/`, `guides/`, `archive/`
- Renaming core structure directories
- Moving critical files like `session-handoff.md`, `current-iteration.md`

### Rule 2: Generator Guides Are Read-Only
**In project LM_context/guides/:**
- Never modify guides copied from this generator
- Update at generator source, then copy to projects
- Treat as immutable reference material

### Rule 3: Archive, Don't Delete
**Correct approach across all projects:**
- Move outdated files to appropriate `archive/` subdirectories
- Create dated subdirectories for organization
- Preserve context history for learning

## 🔧 Generator Maintenance

### Adding New Guides:
1. Create guide in `/Users/vn/ws/LLM_Context_System/guides/`
2. Update this protection guide with new guide name
3. Copy to active projects: `cp guides/* /path/to/project/LM_context/guides/`

### Updating Existing Guides:
1. Modify in generator system first
2. Copy updated version to all active projects
3. Never modify guides directly in project directories

## 📋 Project Setup Checklist

When setting up LLM Context System in new project:

- [ ] Create standard directory structure
- [ ] Copy all guides from generator: `cp /Users/vn/ws/LLM_Context_System/guides/* LM_context/guides/`
- [ ] Initialize core files (README.md, session-handoff.md, current-iteration.md)
- [ ] Set up archive structure
- [ ] Document project-specific context needs

## 🚨 Emergency Recovery Commands

### For Any Project:
```bash
# Restore guides from generator
cp /Users/vn/ws/LLM_Context_System/guides/* LM_context/guides/

# Recreate standard structure
mkdir -p LM_context/{static,evolving,dynamic,guides,archive/{daily-logs,planning}}
mkdir -p LM_context/static/resources
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
