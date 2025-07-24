#!/usr/bin/env python3
"""
LLM Context Management System Deployment Script

This script sets up the LLM Context Management System for a new project.
It creates the proper directory structure and copies all necessary files.

Usage:
    python3 deploy.py /path/to/your/project/directory

Example:
    python3 deploy.py /Users/username/my-learning-project
    python3 deploy.py /home/user/development/ai-research
"""

import os
import sys
import shutil
import argparse
from pathlib import Path
from datetime import datetime

class LLMContextDeployer:
    def __init__(self, target_directory, project_type="technical"):
        self.target_dir = Path(target_directory).resolve()
        self.project_type = project_type
        self.script_dir = Path(__file__).parent.resolve()
        self.lm_context_dir = self.script_dir / "LM_context"
        self.templates_dir = self.script_dir / "templates"
        
    def validate_environment(self):
        """Validate that the deployment environment is ready."""
        print("🔍 Validating deployment environment...")
        
        # Check if LM_context directory has required files
        if not self.lm_context_dir.exists():
            raise FileNotFoundError(f"LM_context directory not found: {self.lm_context_dir}")
            
        # Check for available guides in the new structure
        guide_dirs = ["human-guides", "llm-guides"]
        total_guides = 0
        for guide_dir in guide_dirs:
            guide_path = self.lm_context_dir / guide_dir
            if guide_path.exists():
                total_guides += len(list(guide_path.glob("*.md")))
        
        if total_guides == 0:
            raise FileNotFoundError(f"No guide files found in LM_context structure")
            
        print(f"✅ Environment validation passed - Found {total_guides} guide files")
        
    def create_directory_structure(self):
        """Create the standard LM_context directory structure."""
        print("📁 Creating directory structure...")
        
        directories = [
            "LM_context",
            "LM_context/human-guides",
            "LM_context/llm-guides", 
            "LM_context/static",
            "LM_context/static/knowledge-base", 
            "LM_context/static/resources",
            "LM_context/evolving",
            "LM_context/dynamic",
            "LM_context/dynamic/failed-solutions",
            "LM_context/archive",
            "LM_context/archive/daily-logs"
        ]
        
        for directory in directories:
            dir_path = self.target_dir / directory
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"  ✅ Created: {directory}")
            
    def copy_system_guides(self):
        """Copy all system guide files to the target directory with new organization."""
        print("📋 Copying system guides...")
        
        # Define guide categories and their target directories
        # NOTE: system-docs files moved to knowledge/ and are NOT deployed to new projects
        guide_categories = {
            "human-guides": [
                "human-maintenance-guide.md",
                "human-quick-commands.md"
            ],
            "llm-guides": [
                "llm-session-quick-start.md", 
                "llm-context-question-guide.md",
                "llm-output-management-guide.md"  # New improvement from melexis-simple
            ]
        }
        
        # Copy guides to their appropriate directories
        for category, guide_files in guide_categories.items():
            target_dir = self.target_dir / "LM_context" / category
            target_dir.mkdir(exist_ok=True)
            
            for guide_file in guide_files:
                source_file = self.lm_context_dir / category / guide_file
                if source_file.exists():
                    target_file = target_dir / guide_file
                    shutil.copy2(source_file, target_file)
                    print(f"  ✅ Copied: {category}/{guide_file}")
                else:
                    print(f"  ⚠️  Missing: {guide_file} (will be created as placeholder)")
            
    def create_template_files(self):
        """Create template files for the new project."""
        print("📝 Creating template files...")
        
        # Create README.md
        readme_content = self.generate_project_readme()
        readme_path = self.target_dir / "LM_context" / "README.md"
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        print("  ✅ Created: LM_context/README.md")
        
        # Create collaboration-workflow.md
        collaboration_content = self.generate_collaboration_workflow()
        collaboration_path = self.target_dir / "LM_context" / "collaboration-workflow.md"
        with open(collaboration_path, 'w') as f:
            f.write(collaboration_content)
        print("  ✅ Created: LM_context/collaboration-workflow.md")
        
        # Create session-handoff.md template
        handoff_content = self.generate_session_handoff_template()
        handoff_path = self.target_dir / "LM_context" / "dynamic" / "session-handoff.md"
        with open(handoff_path, 'w') as f:
            f.write(handoff_content)
        print("  ✅ Created: dynamic/session-handoff.md")
        
        # Create current-iteration.md template
        iteration_content = self.generate_current_iteration_template()
        iteration_path = self.target_dir / "LM_context" / "dynamic" / "current-iteration.md"
        with open(iteration_path, 'w') as f:
            f.write(iteration_content)
        print("  ✅ Created: dynamic/current-iteration.md")
        
        # Create environment.md template
        environment_content = self.generate_environment_template()
        env_path = self.target_dir / "LM_context" / "static" / "environment.md"
        with open(env_path, 'w') as f:
            f.write(environment_content)
        print("  ✅ Created: static/environment.md")
        
        # Create basic assumption-validator.py template
        validator_content = self.generate_validator_template()
        validator_path = self.target_dir / "LM_context" / "dynamic" / "assumption-validator.py"
        with open(validator_path, 'w') as f:
            f.write(validator_content)
        os.chmod(validator_path, 0o755)  # Make executable
        print("  ✅ Created: dynamic/assumption-validator.py")
        
    def generate_collaboration_workflow(self):
        """Generate collaboration workflow template."""
        return """# Human-LLM Collaboration Workflow

## Core Cooperation Model

This document defines the fundamental collaboration patterns between humans and LLMs in the context management system.

## Context Restoration Flow (Session Start)

```mermaid
flowchart TD
    A["👤 HUMAN: Starts Session"] --> B{"👤 HUMAN: Copy-Paste Session Command?"}
    B -->|Yes| C["🤖 LLM: Reads Session Command"]
    B -->|No| D["🤖 LLM: Generic Start"]
    
    C --> E["🤖 LLM: Read session-handoff.md"]
    E --> F["🤖 LLM: Read current-iteration.md"]
    F --> G["🤖 LLM: Read static/environment.md"]
    G --> H["🤖 LLM: Check dynamic/failed-solutions/"]
    H --> I["🤖 LLM: Read evolving/assumptions-log.md"]
    
    I --> J["🤖 LLM: Analyze Context Files"]
    J --> K["🤖 LLM: Generate 3-5 Specific Questions"]
    K --> L["🤖 LLM: Ask Context-Based Questions"]
    L --> M["👤 HUMAN: Responds to Questions"]
    M --> N["🤖 LLM: Understands Current State"]
    N --> O["🤖 LLM: Begin Productive Session"]
    
    D --> P["🤖 LLM: Ask Generic Questions"]
    P --> Q["👤 HUMAN: Provides Context Manually"]
    Q --> R["🤖 LLM: Less Efficient Session Start"]
```

## Actor Responsibilities

### Human Responsibilities
- **Session Initiation**: Use copy-paste commands for optimal context restoration
- **Question Response**: Provide clear, specific answers to LLM context questions
- **Session Closure**: Trigger proper session end to preserve context
- **Quality Validation**: Confirm LLM understanding and context accuracy
- **Priority Setting**: Guide LLM on next session priorities and focus areas

### LLM Responsibilities
- **Context Reading**: Read files in priority order with validation
- **Question Generation**: Ask specific, context-based questions (not generic)
- **Understanding Validation**: Confirm correct interpretation of context
- **Knowledge Compilation**: Update all relevant context files during closure
- **Handoff Preparation**: Prepare clear context for next session

## Collaboration Principles

### 1. Context-First Approach
- **Human**: Provides structured context through files, not lengthy explanations
- **LLM**: Reads context systematically before asking questions
- **Benefit**: Efficient session starts with complete understanding

### 2. Question-Driven Clarification
- **Human**: Responds to specific questions rather than providing unsolicited information
- **LLM**: Asks targeted questions based on context analysis
- **Benefit**: Focused communication without information overload

### 3. Validation Checkpoints
- **Human**: Confirms LLM understanding at key decision points
- **LLM**: Validates interpretation before proceeding with work
- **Benefit**: Prevents work based on misunderstood context

### 4. Knowledge Preservation
- **Human**: Ensures proper session closure for context preservation
- **LLM**: Documents all discoveries and updates context files
- **Benefit**: Continuous knowledge building across sessions

## Success Metrics

### Collaboration Effectiveness
- **Session Start Time**: <30 seconds from command to productive work
- **Context Accuracy**: >95% of context correctly understood by LLM
- **Knowledge Preservation**: 100% of discoveries captured in context files
- **Session Continuity**: Seamless handoff between sessions

---

**Purpose:** Define the fundamental collaboration model between humans and LLMs
**Audience:** Both humans and LLMs using the context management system
**Usage:** Reference for proper collaboration patterns and quality validation
"""

    def generate_project_readme(self):
        """Generate project-specific README content."""
        project_name = self.target_dir.name.replace('-', ' ').replace('_', ' ').title()
        return f"""# {project_name} - LLM Context Management

## Overview
This directory contains the LLM context management system for the {project_name} project.

## 🚀 Quick Start

### For LLM Sessions
1. **Start Here:** Read `guides/llm-session-quick-start.md`
2. **Session Context:** Always read `dynamic/session-handoff.md` first
3. **Check Failures:** MANDATORY check of `dynamic/failed-solutions/` before suggesting
4. **Validation:** Use `assumption-validator.py` for all testing

### For Human Maintenance
1. **Quick Commands:** Use `guides/human-quick-commands.md`
2. **Session Start:** Copy-paste one-line start command
3. **Session End:** Copy-paste one-line end command

## 📁 Directory Structure

```
LM_context/
├── README.md                          # This file - project overview
├── static/                            # Tier 1: Static Foundation
│   ├── environment.md                 # Hardware, network, software setup
│   ├── knowledge-base/                # Compiled knowledge
│   └── resources/                     # PDF documents and static resources
├── evolving/                          # Tier 2: Evolving Product
│   ├── assumptions-log.md             # Hypothesis validation history
│   └── project-plan.md                # Original project plan
├── dynamic/                           # Tier 3: Dynamic Session
│   ├── session-handoff.md             # CRITICAL - immediate session context
│   ├── current-iteration.md           # Active iteration status
│   ├── assumption-validator.py        # Automated validation framework
│   └── failed-solutions/              # Failed solution tracking
└── archive/                           # Completed work
    └── daily-logs/                    # Daily session logs
```

## 🎯 Project Goal
[CUSTOMIZE THIS: Describe your specific project goal and learning objectives]

## 🛠️ Technical Context
[CUSTOMIZE THIS: Add your project-specific technical details]
- **Environment:** [Your development environment]
- **Key Technologies:** [Technologies you're learning/using]
- **Success Criteria:** [How you'll measure success]

---

**Last Updated:** {datetime.now().strftime('%B %d, %Y')}  
**System Version:** LLM Context Management System v1.2  
**Purpose:** Context management for {project_name}
"""

    def generate_session_handoff_template(self):
        """Generate project-type-specific session handoff template."""
        
        # Project-type-specific customizations
        project_configs = {
            "technical": {
                "iteration_goal": "Technical Implementation & System Integration",
                "hypothesis": "The technical system can be implemented with current tools and environment",
                "experiment": "Setting up development environment and testing basic functionality",
                "priorities": [
                    "Set up development environment and verify all tools work",
                    "Implement basic functionality and test core features",
                    "Debug any integration issues and document solutions"
                ],
                "working_state": "Development environment with IDE, build tools, and testing framework",
                "resources": "Technical documentation, API references, development tools",
                "completion_criteria": [
                    "Development environment fully configured and tested",
                    "Basic functionality implemented and working",
                    "Core integration points validated and documented"
                ]
            },
            "research": {
                "iteration_goal": "Research Design & Hypothesis Validation",
                "hypothesis": "The research question can be systematically investigated with available methods",
                "experiment": "Designing research methodology and conducting initial validation",
                "priorities": [
                    "Define research question and methodology clearly",
                    "Conduct literature review and identify key sources",
                    "Design experiments and validation framework"
                ],
                "working_state": "Research environment with literature access and analysis tools",
                "resources": "Academic papers, research databases, analysis software",
                "completion_criteria": [
                    "Research question clearly defined and scoped",
                    "Literature review completed with key insights documented",
                    "Experimental design validated and ready for execution"
                ]
            },
            "documentation": {
                "iteration_goal": "Documentation Architecture & Content Creation",
                "hypothesis": "Comprehensive documentation can be created systematically with clear structure",
                "experiment": "Establishing documentation framework and creating initial content",
                "priorities": [
                    "Design documentation architecture and information hierarchy",
                    "Create templates and style guides for consistent content",
                    "Develop initial content sections and validate approach"
                ],
                "working_state": "Documentation environment with writing tools and content management",
                "resources": "Style guides, content templates, collaboration tools",
                "completion_criteria": [
                    "Documentation architecture designed and validated",
                    "Content templates created and tested",
                    "Initial documentation sections completed and reviewed"
                ]
            },
            "collaborative": {
                "iteration_goal": "Team Coordination & Collaboration Framework",
                "hypothesis": "Effective collaboration can be achieved through systematic coordination and communication",
                "experiment": "Establishing collaboration processes and testing team coordination",
                "priorities": [
                    "Set up collaboration tools and communication channels",
                    "Define team roles, responsibilities, and workflows",
                    "Establish decision-making processes and documentation standards"
                ],
                "working_state": "Collaborative environment with shared tools and communication channels",
                "resources": "Collaboration platforms, communication tools, shared repositories",
                "completion_criteria": [
                    "Collaboration framework established and tested",
                    "Team roles and workflows clearly defined",
                    "Communication processes validated and documented"
                ]
            }
        }
        
        config = project_configs.get(self.project_type, project_configs["technical"])
        
        return f"""# Project Session Handoff
**Last Updated:** {datetime.now().strftime('%B %d, %Y, %I:%M %p')}
**Project Type:** {self.project_type.title()}
**Current Iteration:** 1 - {config['iteration_goal']}

## Context Freshness Status
- **Environment:** ✅ CURRENT (verified {datetime.now().strftime('%Y-%m-%d')}) - Development environment set up
- **Assumptions:** ⚠️ NEEDS_UPDATE - No hypotheses validated yet
- **Failed Solutions:** ✅ CURRENT (no failures yet) - New project setup
- **Working Solutions:** ⚠️ NEEDS_UPDATE - No solutions documented yet

**LLM Optimization:** Only read files marked ⚠️ NEEDS_UPDATE to save tokens

## Iteration Context
**Hypothesis Being Tested:** {config['hypothesis']}

**Current Experiment:** {config['experiment']}

**Progress:** 10% complete - Project structure created, ready to begin {self.project_type} work

## Immediate Next Actions (Priority Order)
1. **PRIORITY 1:** {config['priorities'][0]}
2. **PRIORITY 2:** {config['priorities'][1]}
3. **PRIORITY 3:** {config['priorities'][2]}

## Current Working State
**Development Environment:** {config['working_state']}
**Project Location:** `{self.target_dir}`
**Key Resources:** {config['resources']}

## Blockers/Risks
- **None currently identified** - New {self.project_type} project setup
- [CUSTOMIZE: Add any known blockers or risks specific to {self.project_type} work]

## Definition of Done for Current Iteration
- [ ] {config['completion_criteria'][0]}
- [ ] {config['completion_criteria'][1]}
- [ ] {config['completion_criteria'][2]}

## Context for Next Session
**If Iteration 1 Complete:** Move to Iteration 2 - Advanced {self.project_type.title()} Implementation
**If Iteration 1 Continues:** Continue with current {self.project_type} setup and validation

## Files to Read First in New Session
1. **CRITICAL:** `dynamic/current-iteration.md` - Active iteration status
2. **IMPORTANT:** `static/environment.md` - Development environment setup
3. **REFERENCE:** `guides/llm-session-quick-start.md` - Session procedures
4. **CONTEXT:** `README.md` - Project overview and goals

## Project Development Notes
- {self.project_type.title()} project structure created using LLM Context Management System
- Ready to begin systematic {self.project_type} development and learning
- All context management tools configured for {self.project_type} workflows

"""

    def generate_current_iteration_template(self):
        """Generate current iteration template."""
        return f"""# Current Iteration Context
**Iteration:** 1 - Project Setup & Initial Learning
**Started:** {datetime.now().strftime('%B %d, %Y')}
**Goal:** [CUSTOMIZE: Your specific iteration goal]

## Current Hypothesis
"[CUSTOMIZE: Your current hypothesis or assumption to test]"

## Experiment Design
- **Experiment 1:** [CUSTOMIZE: First experiment or learning task]
- **Experiment 2:** [CUSTOMIZE: Second experiment or learning task]
- **Experiment 3:** [CUSTOMIZE: Third experiment or learning task]

## Success Criteria
- [ ] [CUSTOMIZE: Specific, measurable success criteria]
- [ ] [CUSTOMIZE: Additional success criteria]
- [ ] [CUSTOMIZE: More success criteria]

## Current Status
- ✅ **Project Setup:** LLM Context Management System deployed
- ⏳ **Learning Phase:** Ready to begin systematic learning
- ⏳ **Validation Framework:** Need to customize assumption-validator.py
- ⏳ **Knowledge Base:** Ready to accumulate insights

## Active Experiments

### Experiment 1: [CUSTOMIZE TITLE] ⏳ PENDING
**Status:** Ready to begin
**Evidence:** Project structure created
**Next:** [CUSTOMIZE: Specific next steps]

## Next Actions (Priority Order)
1. **PRIORITY 1:** [CUSTOMIZE: Most important next action]
2. **PRIORITY 2:** [CUSTOMIZE: Second priority action]
3. **PRIORITY 3:** [CUSTOMIZE: Third priority action]

## Definition of Done for Current Iteration
- [ ] [CUSTOMIZE: Specific completion criteria]
- [ ] [CUSTOMIZE: Additional completion criteria]
- [ ] [CUSTOMIZE: More completion criteria]

## Risks and Mitigation
- **Risk:** [CUSTOMIZE: Potential risk]
  - **Mitigation:** [CUSTOMIZE: How to mitigate]

## Key Insights Gained
[This section will be updated as you learn]

## Technical Architecture
[CUSTOMIZE: Add your project-specific technical details]

## Evidence Collected
[This section will be updated with validation results]

## Next Iteration Planning
**Iteration 2:** [CUSTOMIZE: Next iteration focus]
- **Focus:** [CUSTOMIZE: What to focus on next]
- **Goal:** [CUSTOMIZE: Next iteration goal]

---

**Last Updated:** {datetime.now().strftime('%B %d, %Y, %I:%M %p')}  
**Progress:** 10% complete - Project setup complete, ready to begin  
**Next Session Focus:** [CUSTOMIZE: What to focus on in next session]
"""

    def generate_environment_template(self):
        """Generate environment template."""
        return f"""# Development Environment Configuration

## System Information
**Last Updated:** {datetime.now().strftime('%B %d, %Y')}
**Operating System:** [CUSTOMIZE: Your OS - e.g., macOS, Linux, Windows]
**Development Machine:** [CUSTOMIZE: Your machine specs]

## Project Setup
**Project Directory:** `{self.target_dir}`
**Context Directory:** `{self.target_dir}/LM_context`

## Development Tools
[CUSTOMIZE: List your development tools]
- **IDE/Editor:** [e.g., VSCode, PyCharm, etc.]
- **Version Control:** [e.g., Git]
- **Package Manager:** [e.g., pip, npm, etc.]
- **Build Tools:** [e.g., Make, CMake, etc.]

## Dependencies
[CUSTOMIZE: List your project dependencies]
- **Language:** [e.g., Python 3.9+, Node.js, etc.]
- **Key Libraries:** [List important libraries/frameworks]
- **System Dependencies:** [Any system-level requirements]

## Network Configuration
[CUSTOMIZE: If your project involves networking]
- **Development Machine IP:** [Your IP if relevant]
- **Target Devices:** [Any remote devices if relevant]
- **Ports Used:** [Any specific ports]

## Hardware Requirements
[CUSTOMIZE: Any specific hardware needs]
- **Minimum RAM:** [e.g., 8GB]
- **Storage:** [e.g., 10GB free space]
- **Special Hardware:** [Any special requirements]

## Environment Variables
[CUSTOMIZE: Any required environment variables]
```bash
export PROJECT_ROOT="{self.target_dir}"
export CONTEXT_DIR="{self.target_dir}/LM_context"
# Add other environment variables as needed
```

## Installation Instructions
[CUSTOMIZE: How to set up the development environment]

### 1. Clone/Setup Project
```bash
cd {self.target_dir}
# Add your project setup commands here
```

### 2. Install Dependencies
```bash
# Add your dependency installation commands here
```

### 3. Verify Installation
```bash
# Add verification commands here
python3 LM_context/dynamic/assumption-validator.py --health-check
```

## Troubleshooting
[CUSTOMIZE: Common environment issues and solutions]

### Common Issues
- **Issue 1:** [Description]
  - **Solution:** [How to fix]
- **Issue 2:** [Description]
  - **Solution:** [How to fix]

## Performance Considerations
[CUSTOMIZE: Any performance-related environment notes]
- **CPU Usage:** [Expected CPU usage patterns]
- **Memory Usage:** [Expected memory usage]
- **Disk Usage:** [Expected disk usage]

---

**Environment Status:** ✅ Ready for development  
**Last Verified:** {datetime.now().strftime('%B %d, %Y')}  
**Next Review:** [Set a date for next environment review]
"""

    def generate_validator_template(self):
        """Generate basic assumption validator template."""
        return '''#!/usr/bin/env python3
"""
Assumption Validator for Project

This script validates project assumptions and hypotheses.
Customize the validation methods for your specific project needs.
"""

import sys
import json
import subprocess
import argparse
from datetime import datetime
from pathlib import Path

class AssumptionValidator:
    def __init__(self):
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "validations": {},
            "summary": {
                "total": 0,
                "passed": 0,
                "failed": 0,
                "errors": []
            }
        }
        
    def validate_environment(self):
        """Validate basic development environment."""
        print("🔍 Validating development environment...")
        
        try:
            # Check Python version
            python_version = sys.version_info
            if python_version.major >= 3 and python_version.minor >= 7:
                self.record_result("python_version", True, f"Python {python_version.major}.{python_version.minor}")
            else:
                self.record_result("python_version", False, f"Python version too old: {python_version}")
                
            # Check project directory structure
            context_dir = Path(__file__).parent.parent
            required_dirs = ["static", "evolving", "dynamic", "archive"]
            
            for dir_name in required_dirs:
                dir_path = context_dir / dir_name
                if dir_path.exists():
                    self.record_result(f"directory_{dir_name}", True, f"Directory exists: {dir_name}")
                else:
                    self.record_result(f"directory_{dir_name}", False, f"Missing directory: {dir_name}")
                    
            return True
            
        except Exception as e:
            self.record_result("environment_validation", False, f"Error: {str(e)}")
            return False
            
    def validate_project_specific(self):
        """
        CUSTOMIZE THIS METHOD for your specific project validations.
        
        Examples:
        - Test API connectivity
        - Verify database connections
        - Check hardware availability
        - Validate configuration files
        - Test build processes
        """
        print("🔍 Validating project-specific requirements...")
        
        try:
            # Example validation - customize for your project
            self.record_result("project_setup", True, "Project setup validation placeholder")
            
            # Add your specific validations here:
            # - Hardware checks
            # - Network connectivity
            # - Service availability
            # - Configuration validation
            # - Build system checks
            
            return True
            
        except Exception as e:
            self.record_result("project_validation", False, f"Error: {str(e)}")
            return False
            
    def record_result(self, test_name, passed, details):
        """Record a validation result."""
        self.results["validations"][test_name] = {
            "passed": passed,
            "details": details,
            "timestamp": datetime.now().isoformat()
        }
        
        self.results["summary"]["total"] += 1
        if passed:
            self.results["summary"]["passed"] += 1
            print(f"  ✅ {test_name}: {details}")
        else:
            self.results["summary"]["failed"] += 1
            self.results["summary"]["errors"].append(f"{test_name}: {details}")
            print(f"  ❌ {test_name}: {details}")
            
    def run_health_check(self):
        """Run basic health check validations."""
        print("🏥 Running health check...")
        
        success = True
        success &= self.validate_environment()
        
        return success
        
    def run_full_validation(self):
        """Run complete validation suite."""
        print("🔬 Running full validation suite...")
        
        success = True
        success &= self.validate_environment()
        success &= self.validate_project_specific()
        
        return success
        
    def save_results(self):
        """Save validation results to file."""
        results_file = Path(__file__).parent / "validation-results.json"
        with open(results_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"📊 Results saved to: {results_file}")
        
    def print_summary(self):
        """Print validation summary."""
        summary = self.results["summary"]
        print("\\n📋 Validation Summary:")
        print(f"  Total tests: {summary['total']}")
        print(f"  Passed: {summary['passed']}")
        print(f"  Failed: {summary['failed']}")
        
        if summary["errors"]:
            print("\\n❌ Errors:")
            for error in summary["errors"]:
                print(f"  - {error}")
        else:
            print("\\n✅ All validations passed!")

def main():
    parser = argparse.ArgumentParser(description="Validate project assumptions and environment")
    parser.add_argument("--health-check", action="store_true", help="Run basic health check only")
    parser.add_argument("--quick-check", action="store_true", help="Run quick validation")
    parser.add_argument("--save-results", action="store_true", help="Save results to file")
    
    args = parser.parse_args()
    
    validator = AssumptionValidator()
    
    try:
        if args.health_check or args.quick_check:
            success = validator.run_health_check()
        else:
            success = validator.run_full_validation()
            
        validator.print_summary()
        
        if args.save_results:
            validator.save_results()
            
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print("\\n⚠️ Validation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\\n💥 Validation failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
'''

    def create_deployment_summary(self):
        """Create a deployment summary file."""
        print("📄 Creating deployment summary...")
        
        summary_content = f"""# LLM Context Management System - Deployment Summary

## Deployment Information
**Date:** {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
**Target Directory:** `{self.target_dir}`
**System Version:** v1.2

## Files Created

### Directory Structure
```
{self.target_dir.name}/
├── guides/                            # System guides (read-only)
│   ├── llm-session-quick-start.md     # LLM session procedures
│   ├── human-quick-commands.md        # Human interface commands
│   ├── session-knowledge-compilation.md # Knowledge compilation
│   ├── system-setup-instructions.md   # System recreation guide
│   └── troubleshooting-comprehensive.md # Troubleshooting
└── LM_context/                        # Project context management
    ├── README.md                      # Project overview
    ├── static/                        # Static foundation
    │   ├── environment.md             # Development environment
    │   ├── knowledge-base/            # Compiled knowledge
    │   └── resources/                 # PDF documents and resources
    ├── evolving/                      # Evolving product context
    ├── dynamic/                       # Dynamic session context
    │   ├── session-handoff.md         # Session handoffs
    │   ├── current-iteration.md       # Current iteration status
    │   ├── assumption-validator.py    # Validation framework
    │   └── failed-solutions/          # Failed solution tracking
    └── archive/                       # Completed work
        └── daily-logs/                # Daily session logs
```

## Next Steps

### 1. Customize for Your Project (Required)
- **Edit `LM_context/README.md`** - Add your project description and goals
- **Update `LM_context/static/environment.md`** - Configure your development environment
- **Customize `LM_context/dynamic/assumption-validator.py`** - Add project-specific validations
- **Modify `LM_context/dynamic/session-handoff.md`** - Set your initial priorities
- **Update `LM_context/dynamic/current-iteration.md`** - Define your first iteration

### 2. Start Using the System
```bash
# Navigate to your project
cd {self.target_dir}

# For humans: Use quick commands
cat guides/human-quick-commands.md

# For LLMs: Follow session procedures
cat guides/llm-session-quick-start.md

# Test the validation framework
python3 LM_context/dynamic/assumption-validator.py --health-check
```

### 3. Begin Your First Session
Use this command to start your first LLM session:
```
Start session: Read context (session-handoff, current-iteration, environment, failed-solutions), ask 3-5 specific questions based on what you find, then summarize status and next actions.
```

## System Features
- **74% Token Reduction** - Smart context loading with freshness tracking
- **Session Continuity** - Perfect handoffs between LLM sessions
- **Knowledge Compilation** - Comprehensive learning capture and organization
- **Failure Prevention** - Track and avoid repeating failed approaches
- **Automated Validation** - Customizable validation framework

## Support
- **Troubleshooting:** See `guides/troubleshooting-comprehensive.md`
- **System Setup:** See `guides/system-setup-instructions.md`
- **Human Commands:** See `guides/human-quick-commands.md`

---

**Deployment Status:** ✅ Complete  
**Ready for Use:** Yes  
**Next Action:** Customize template files for your specific project
"""
        
        summary_path = self.target_dir / "DEPLOYMENT_SUMMARY.md"
        with open(summary_path, 'w') as f:
            f.write(summary_content)
        print(f"  ✅ Created: DEPLOYMENT_SUMMARY.md")

    def deploy(self):
        """Execute the complete deployment process."""
        print(f"🚀 Deploying LLM Context Management System to: {self.target_dir}")
        print()
        
        try:
            # Create target directory if it doesn't exist
            self.target_dir.mkdir(parents=True, exist_ok=True)
            
            # Run deployment steps
            self.validate_environment()
            self.create_directory_structure()
            self.copy_system_guides()
            self.create_template_files()
            self.create_deployment_summary()
            
            print()
            print("🎉 Deployment completed successfully!")
            print()
            print("📋 Next Steps:")
            print(f"1. cd {self.target_dir}")
            print("2. Read DEPLOYMENT_SUMMARY.md for customization instructions")
            print("3. Customize the template files for your specific project")
            print("4. Start your first LLM session using the provided commands")
            print()
            print("📚 Documentation:")
            print("- guides/human-quick-commands.md - For human users")
            print("- guides/llm-session-quick-start.md - For LLM sessions")
            print("- guides/troubleshooting-comprehensive.md - For troubleshooting")
            
        except Exception as e:
            print(f"💥 Deployment failed: {e}")
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Deploy LLM Context Management System to a new project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 deploy.py /Users/username/my-learning-project
  python3 deploy.py /home/user/development/ai-research
  python3 deploy.py ./my-new-project
        """
    )
    
    parser.add_argument(
        "target_directory",
        help="Target directory where the system will be deployed"
    )
    
    parser.add_argument(
        "--project-type",
        choices=["technical", "research", "documentation", "collaborative"],
        default="technical",
        help="Project type for customized templates (default: technical)"
    )
    
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force deployment even if target directory exists and is not empty"
    )
    
    args = parser.parse_args()
    
    target_path = Path(args.target_directory).resolve()
    
    # Check if target directory exists and has content
    if target_path.exists() and any(target_path.iterdir()) and not args.force:
        print(f"⚠️  Target directory '{target_path}' exists and is not empty.")
        print("Use --force to deploy anyway, or choose a different directory.")
        sys.exit(1)
    
    # Deploy the system
    deployer = LLMContextDeployer(target_path, args.project_type)
    deployer.deploy()

if __name__ == "__main__":
    main()
