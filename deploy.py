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
    def __init__(self, target_directory):
        self.target_dir = Path(target_directory).resolve()
        self.script_dir = Path(__file__).parent.resolve()
        self.guides_dir = self.script_dir / "guides"
        self.templates_dir = self.script_dir / "templates"
        
    def validate_environment(self):
        """Validate that the deployment environment is ready."""
        print("🔍 Validating deployment environment...")
        
        # Check if script directory has required files
        if not self.guides_dir.exists():
            raise FileNotFoundError(f"Guides directory not found: {self.guides_dir}")
            
        required_guides = [
            "llm-session-quick-start.md",
            "human-quick-commands.md", 
            "session-knowledge-compilation.md",
            "system-setup-instructions.md",
            "troubleshooting-comprehensive.md"
        ]
        
        missing_guides = []
        for guide in required_guides:
            if not (self.guides_dir / guide).exists():
                missing_guides.append(guide)
                
        if missing_guides:
            raise FileNotFoundError(f"Missing required guides: {missing_guides}")
            
        print("✅ Environment validation passed")
        
    def create_directory_structure(self):
        """Create the standard LM_context directory structure."""
        print("📁 Creating directory structure...")
        
        directories = [
            "LM_context",
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
        """Copy all system guide files to the target directory."""
        print("📋 Copying system guides...")
        
        guides_target = self.target_dir / "guides"
        guides_target.mkdir(exist_ok=True)
        
        for guide_file in self.guides_dir.glob("*.md"):
            target_file = guides_target / guide_file.name
            shutil.copy2(guide_file, target_file)
            print(f"  ✅ Copied: {guide_file.name}")
            
    def create_template_files(self):
        """Create template files for the new project."""
        print("📝 Creating template files...")
        
        # Create README.md
        readme_content = self.generate_project_readme()
        readme_path = self.target_dir / "LM_context" / "README.md"
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        print("  ✅ Created: LM_context/README.md")
        
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
        """Generate session handoff template."""
        return f"""# Project Session Handoff
**Last Updated:** {datetime.now().strftime('%B %d, %Y, %I:%M %p')}
**Current Iteration:** 1 - Project Setup & Initial Learning

## Context Freshness Status
- **Environment:** ✅ CURRENT (verified {datetime.now().strftime('%Y-%m-%d')}) - Development environment set up
- **Assumptions:** ⚠️ NEEDS_UPDATE - No hypotheses validated yet
- **Failed Solutions:** ✅ CURRENT (no failures yet) - New project setup
- **Working Solutions:** ⚠️ NEEDS_UPDATE - No solutions documented yet

**LLM Optimization:** Only read files marked ⚠️ NEEDS_UPDATE to save tokens

## Iteration Context
**Hypothesis Being Tested:** [CUSTOMIZE: Your current hypothesis or learning goal]

**Current Experiment:** [CUSTOMIZE: What you're currently working on]

**Progress:** 10% complete - Project structure created, ready to begin learning

## Immediate Next Actions (Priority Order)
1. **PRIORITY 1:** [CUSTOMIZE: Your most important next task]
2. **PRIORITY 2:** [CUSTOMIZE: Second priority task]
3. **PRIORITY 3:** [CUSTOMIZE: Third priority task]

## Current Working State
**Development Environment:** [CUSTOMIZE: Your development setup]
**Project Location:** `{self.target_dir}`
**Key Resources:** [CUSTOMIZE: Important documentation, tools, etc.]

## Blockers/Risks
- **None currently identified** - New project setup
- [CUSTOMIZE: Add any known blockers or risks]

## Definition of Done for Current Iteration
- [ ] [CUSTOMIZE: Specific, measurable completion criteria]
- [ ] [CUSTOMIZE: Additional completion criteria]
- [ ] [CUSTOMIZE: More completion criteria]

## Context for Next Session
**If Iteration 1 Complete:** [CUSTOMIZE: What should happen next]
**If Iteration 1 Continues:** [CUSTOMIZE: How to continue current work]

## Files to Read First in New Session
1. **CRITICAL:** `dynamic/current-iteration.md` - Active iteration status
2. **IMPORTANT:** `static/environment.md` - Development environment setup
3. **REFERENCE:** `guides/llm-session-quick-start.md` - Session procedures
4. **CONTEXT:** `README.md` - Project overview and goals

## Project Development Notes
- Project structure created using LLM Context Management System
- Ready to begin systematic learning and development
- All context management tools in place

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
    deployer = LLMContextDeployer(target_path)
    deployer.deploy()

if __name__ == "__main__":
    main()
