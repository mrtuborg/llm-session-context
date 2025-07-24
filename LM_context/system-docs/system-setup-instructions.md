# Agile Context Management System - Complete Setup Instructions

## Overview
This guide provides step-by-step instructions for any LLM to recreate the complete Agile context management system for maintaining continuity between sessions and optimizing token usage.

---

## 🎯 System Purpose
- **Maintain context** between LLM sessions without re-reading everything
- **Optimize token usage** through tiered file structure
- **Automate assumption validation** with reusable Python framework
- **Enable seamless handoffs** between different LLM sessions
- **Support hypothesis-driven development** with evidence tracking
- **Provide project type intelligence** with domain-specific optimization
- **Enable agile planning** with automatic schedule adaptation

## 🔄 Knowledge vs. Context Separation (CRITICAL)

### Core Principle
This system maintains a **strict separation** between project management context and learning artifacts:

- **`LM_context/`** = Session continuity, project management, automation framework
- **`knowledge/`** = Learning outcomes, technical guides, research documentation, tutorials

### What Goes Where

#### LM_context/ (Session Management Only)
- **Session handoffs** and iteration status
- **Assumption validation** scripts and results
- **Working solutions** (commands and proven approaches)
- **Project management** (backlog, risks, progress tracking)
- **System guides** (maintenance, setup instructions)

#### knowledge/ (Learning Artifacts Only)
- **Technical deep-dives** and architectural analysis
- **Troubleshooting guides** and debugging techniques
- **Learning articles** and research notes
- **Best practices** and design patterns discovered
- **Tutorial content** and educational materials
- **Performance analysis** and optimization studies

### Folder Structure Example
```
project-root/
├── LM_context/                    # Session continuity (this system)
│   ├── dynamic/session-handoff.md
│   ├── guides/system-setup-instructions.md  # NEVER DELETE
│   └── ...
├── knowledge/                     # Learning artifacts
│   ├── [project-domain]/
│   │   ├── pipeline-architecture-deep-dive.md
│   │   ├── plugin-development-guide.md
│   │   └── troubleshooting-comprehensive.md
│   ├── performance/
│   │   ├── cpu-optimization-analysis.md
│   │   └── memory-management-study.md
│   └── hardware/
│       ├── imx8mp-vpu-integration.md
│       └── [project]-technical-guide.md
└── [main-project-files]
```

### Reference Guidelines
- **Context files** may reference knowledge articles but never duplicate content
- **Knowledge articles** should be self-contained and comprehensive
- **Session handoffs** should link to relevant knowledge for quick access
- **Working solutions** should reference detailed explanations in knowledge/

### Maintenance Responsibilities
- **LM_context/**: Updated every session, kept lean and actionable
- **knowledge/**: Updated when learning occurs, comprehensive and detailed
- **Cross-references**: Maintained to ensure context can quickly access relevant knowledge

**IMPORTANT**: The `guides/system-setup-instructions.md` file should **NEVER be deleted** as it contains the complete system recreation instructions.

---

## 🎯 Step 0: Project Type Selection (NEW - v2.0)

### Project Type Intelligence
The system now supports **domain-specific optimization** based on project type. Choose the appropriate type for optimal LLM behavior and context organization:

#### **Technical Projects**
- **Focus:** Implementation, debugging, system integration
- **LLM Behavior:** Asks about programming languages, platforms, frameworks
- **Optimized Files:** environment.md (detailed), working-solutions.md (code-focused), failed-solutions/ (debugging)
- **Success Metrics:** Functional requirements, performance benchmarks, integration tests

#### **Research Projects**
- **Focus:** Hypothesis validation, evidence collection, systematic investigation
- **LLM Behavior:** Asks about research questions, methodology, hypotheses
- **Optimized Files:** assumptions-log.md (detailed), validation.md (methodology), external-resources.md (literature)
- **Success Metrics:** Experimental results, data quality, statistical significance

#### **Documentation Projects**
- **Focus:** Content creation, organization, knowledge management
- **LLM Behavior:** Asks about audience, scope, format requirements
- **Optimized Files:** project-plan.md (content architecture), external-resources.md (references), working-solutions.md (templates)
- **Success Metrics:** Content completeness, accuracy, user feedback

#### **Collaborative Projects**
- **Focus:** Team coordination, communication, shared decision-making
- **LLM Behavior:** Asks about team members, decision processes, communication channels
- **Optimized Files:** session-handoff.md (coordination), assumptions-log.md (decisions), working-solutions.md (team knowledge)
- **Success Metrics:** Team productivity, communication effectiveness, decision quality

### Project Type-Specific Session Commands
Based on your project type, use the appropriate session start command:

#### Technical Projects
```
Start technical session: Read context (session-handoff, current-iteration, environment, working-solutions), ask about programming language/platform/frameworks, focus on implementation and integration, summarize technical status and next development actions.
```

#### Research Projects
```
Start research session: Read context (session-handoff, current-iteration, assumptions-log, validation), ask about research question/methodology/hypothesis, focus on evidence collection and validation, summarize research status and next investigation actions.
```

#### Documentation Projects
```
Start documentation session: Read context (session-handoff, current-iteration, project-plan, external-resources), ask about audience/scope/format requirements, focus on content creation and organization, summarize documentation status and next writing actions.
```

#### Collaborative Projects
```
Start collaborative session: Read context (session-handoff, current-iteration, assumptions-log, working-solutions), ask about team members/decision process/communication channels, focus on coordination and knowledge sharing, summarize team status and next collaboration actions.
```

---

## 📁 Step 1: Create Directory Structure

From your project's root directory:

```bash
# Create the two main directories for context and knowledge
mkdir -p LM_context knowledge

# Create the tiered structure inside LM_context
mkdir -p LM_context/{static,evolving,dynamic,llm-guides,system-docs,archive}
mkdir -p LM_context/dynamic/failed-solutions
```
This establishes the core folder structure at the project root, separating session management (`LM_context`) from persistent knowledge (`knowledge`).

---

## 📝 Step 2: Create Static Foundation Files

### 2.1 Environment Configuration
**File:** `static/environment.md`

```markdown
# Project Environment Configuration

## Hardware Setup
- **Target Device:** [IP_ADDRESS] ([HARDWARE_DESCRIPTION])
- **Development Machine:** [DEV_IP] ([OS_TYPE])
- **Camera/Sensor:** [DEVICE_DESCRIPTION]
- **Network:** [NETWORK_CONFIG]

## Software Environment
- **Main Project Directory:** [PROJECT_PATH]
- **Context Directory:** [CONTEXT_PATH]
- **Build System:** [BUILD_SYSTEM]
- **Key Dependencies:** [DEPENDENCIES_LIST]

## Access Information
- **SSH Access:** ssh [user]@[target_ip]
- **Device Paths:** [DEVICE_PATHS]
- **Configuration Files:** [CONFIG_LOCATIONS]

## Network Configuration
- **Streaming Endpoints:** [ENDPOINTS]
- **Port Configuration:** [PORTS]
- **Firewall Settings:** [FIREWALL_INFO]

*Last Updated: [DATE]*
*Update Frequency: Only when hardware/network changes*
```

### 2.2 External Resources
**File:** `static/external-resources.md`

```markdown
# External Resources and Documentation

## Official Documentation
- **Primary Technology Docs:** [MAIN_TECH_DOCS]
- **API References:** [API_DOCS]
- **Hardware Manuals:** [HARDWARE_DOCS]

## Learning Resources
- **Tutorials:** [TUTORIAL_LINKS]
- **Examples:** [EXAMPLE_REPOS]
- **Community Resources:** [FORUMS_BLOGS]

## Development Tools
- **Build Tools:** [BUILD_TOOL_DOCS]
- **Debugging Tools:** [DEBUG_TOOL_DOCS]
- **Testing Frameworks:** [TEST_FRAMEWORK_DOCS]

## Reference Materials
- **Best Practices:** [BEST_PRACTICE_GUIDES]
- **Architecture Patterns:** [ARCHITECTURE_DOCS]
- **Performance Guidelines:** [PERFORMANCE_GUIDES]

*Last Updated: [DATE]*
*Update Frequency: When new resources discovered*
```

---

## 📋 Step 3: Create Evolving Product Files

### 3.1 Product Backlog
**File:** `evolving/product-backlog.md`

```markdown
# [PROJECT_NAME] - Product Backlog

## Epic: [MAIN_PROJECT_GOAL]
**Vision:** [PROJECT_VISION_STATEMENT]

---

## Iteration 1: [ITERATION_1_NAME]
**Goal:** [ITERATION_1_GOAL]
**Hypothesis:** "[ITERATION_1_HYPOTHESIS]"

### User Stories:
- **Story 1:** As a [USER_TYPE], I want [FUNCTIONALITY] so that [BENEFIT]
  - **Acceptance Criteria:** 
    - [CRITERION_1]
    - [CRITERION_2]
  - **Status:** ⏳ BACKLOG

---

## Definition of Done (Global)
- [ ] All acceptance criteria met
- [ ] Code tested and working
- [ ] Documentation updated
- [ ] Performance metrics validated
- [ ] Integration confirmed

## Out of Scope
- [OUT_OF_SCOPE_ITEMS]
```

### 3.2 Assumptions Log
**File:** `evolving/assumptions-log.md`

```markdown
# Assumptions & Hypotheses Validation Log

## Iteration 1: [ITERATION_NAME]
**Status:** ⏳ PLANNED

### H1: [FIRST_HYPOTHESIS]
**Status:** ⏳ NOT TESTED
**Evidence:** 
- [EVIDENCE_PLACEHOLDER]
**Impact:** [EXPECTED_IMPACT]

---

## Key Learning Outcomes

### Validated Concepts:
1. **[CONCEPT_1]:** [DESCRIPTION]

### Critical Success Factors:
1. **[FACTOR_1]:** [DESCRIPTION]

### Risk Mitigation Strategies:
1. **[STRATEGY_1]:** [DESCRIPTION]
```

### 3.3 Risk Assessment
**File:** `evolving/risk-assessment.md`

```markdown
# Risk Assessment and Mitigation

## High Priority Risks

### R1: [RISK_NAME]
**Probability:** [HIGH/MEDIUM/LOW]
**Impact:** [HIGH/MEDIUM/LOW]
**Description:** [RISK_DESCRIPTION]
**Mitigation:** [MITIGATION_STRATEGY]
**Status:** [ACTIVE/MITIGATED/MONITORING]

## Medium Priority Risks
[SIMILAR_FORMAT]

## Low Priority Risks
[SIMILAR_FORMAT]

## Risk Monitoring
- **Review Frequency:** [FREQUENCY]
- **Key Indicators:** [INDICATORS]
- **Escalation Criteria:** [CRITERIA]
```

### 3.4 Validation Criteria
**File:** `evolving/validation.md`

```markdown
# Success Criteria and Validation Metrics

## Project Success Criteria
- **Primary Goal:** [PRIMARY_SUCCESS_METRIC]
- **Performance Targets:** [PERFORMANCE_TARGETS]
- **Quality Standards:** [QUALITY_STANDARDS]

## Iteration Success Criteria
- **Iteration 1:** [ITERATION_1_CRITERIA]
- **Iteration 2:** [ITERATION_2_CRITERIA]

## Validation Methods
- **Automated Testing:** [AUTOMATED_TEST_DESCRIPTION]
- **Performance Measurement:** [PERFORMANCE_TEST_DESCRIPTION]
- **Integration Testing:** [INTEGRATION_TEST_DESCRIPTION]

## Acceptance Thresholds
- **Performance:** [PERFORMANCE_THRESHOLDS]
- **Reliability:** [RELIABILITY_THRESHOLDS]
- **Quality:** [QUALITY_THRESHOLDS]
```

---

## 🔄 Step 4: Create Dynamic Session Files

### 4.1 Current Iteration Context
**File:** `dynamic/current-iteration.md`

```markdown
# Current Iteration Context
**Iteration:** 1 - [ITERATION_NAME]
**Started:** [DATE]
**Goal:** [ITERATION_GOAL]

## Current Hypothesis
"[HYPOTHESIS_STATEMENT]"

## Experiment Design
- [EXPERIMENT_1]
- [EXPERIMENT_2]

## Success Criteria
- [ ] [CRITERION_1]
- [ ] [CRITERION_2]

## Current Status
- ⏳ [PENDING_ITEM]
- 🔄 [IN_PROGRESS_ITEM]
- ✅ [COMPLETED_ITEM]

## Active Experiments
1. **[EXPERIMENT_NAME]:** [DESCRIPTION]

## Next Actions (Priority Order)
1. **PRIORITY 1:** [ACTION_1]
2. **PRIORITY 2:** [ACTION_2]

## Blockers/Risks
- [CURRENT_BLOCKERS]

## Definition of Done for Current Iteration
- [ ] [DONE_CRITERION_1]
- [ ] [DONE_CRITERION_2]

## Transition to Next Iteration
**Next Iteration:** [NEXT_ITERATION_NUMBER] - [NEXT_ITERATION_NAME]
**Next Hypothesis:** "[NEXT_HYPOTHESIS]"
**Preparation Needed:** [PREPARATION_TASKS]
```

### 4.2 Session Handoff Template
**File:** `dynamic/session-handoff.md`

```markdown
# Agile Session Handoff
**Last Updated:** [DATE_TIME]
**Current Iteration:** [ITERATION_NUMBER] - [ITERATION_NAME]

## Iteration Context
**Hypothesis Being Tested:** "[CURRENT_HYPOTHESIS]"
**Current Experiment:** [CURRENT_EXPERIMENT]
**Progress:** [PROGRESS_PERCENTAGE]% complete - [STATUS_DESCRIPTION]

## Immediate Next Actions (Priority Order)
1. **PRIORITY 1:** [ACTION_1]
2. **PRIORITY 2:** [ACTION_2]
3. **PRIORITY 3:** [ACTION_3]

## Current Working State
**Target Device:** [TARGET_DEVICE_INFO]
**Development Machine:** [DEV_MACHINE_INFO]
**Working Directory:** [WORKING_DIRECTORY]

**Active Solutions:**
- **[SOLUTION_1]:** [STATUS_AND_DESCRIPTION]
- **[SOLUTION_2]:** [STATUS_AND_DESCRIPTION]

**Test Commands Ready:**
```bash
# [COMMAND_DESCRIPTION]
[COMMAND_1]

# [COMMAND_DESCRIPTION]
[COMMAND_2]
```

## Assumption Validation Framework
**CRITICAL:** Use the automated validation script for all assumption testing:

```bash
# Run all current validations
cd [CONTEXT_DIRECTORY]
python3 dynamic/assumption-validator.py

# Extended test
python3 dynamic/assumption-validator.py --[OPTION] [VALUE]
```

### MANDATORY: Updating Validation Script for New Assumptions
**When adding new hypotheses, LLM sessions MUST update the validation script:**

1. **Add new validation method:**
```python
def validate_hX_new_hypothesis(self) -> bool:
    """HX: Description of new hypothesis"""
    logging.info("Validating HX: New hypothesis description")
    
    # Test implementation
    test_cmd = "your_test_command_here"
    success, stdout, stderr = self.run_command(test_cmd, timeout=30)
    
    evidence = {
        "test_result": success,
        "output": stdout,
        "error": stderr if not success else ""
    }
    
    if success:
        self.log_result("HX", "VALIDATED", evidence, "Success message")
        return True
    else:
        self.log_result("HX", "FAILED", evidence, "Failure message")
        return False
```

2. **Add to run_all_validations method:**
```python
validations = [
    # ... existing validations ...
    ("HX", self.validate_hX_new_hypothesis),
]
```

3. **Update assumptions-log.md** with the new hypothesis
4. **Test the new validation** before proceeding

## Blockers/Risks
- [CURRENT_BLOCKERS]

## Definition of Done for Current Iteration
- [ ] [DONE_CRITERION_1]
- [ ] [DONE_CRITERION_2]

## Context for Next Session
**If Iteration Complete:** [NEXT_ITERATION_INSTRUCTIONS]
**If Iteration Continues:** [CONTINUATION_INSTRUCTIONS]

## Key Technical Context
- **[TECHNICAL_CONTEXT_1]:** [DESCRIPTION]
- **[TECHNICAL_CONTEXT_2]:** [DESCRIPTION]

## Files to Read First in New Session
1. **CRITICAL:** `dynamic/current-iteration.md` - Active iteration status
2. **IMPORTANT:** `evolving/assumptions-log.md` - Validation results and evidence
3. **REFERENCE:** `evolving/product-backlog.md` - Overall project context
4. **STATIC:** `static/environment.md` - Hardware and network configuration (if needed)

## Cost Optimization Notes
- Static files (`static/`) rarely need re-reading unless hardware changes
- Focus on dynamic files (`dynamic/`) for session context
- Use `evolving/assumptions-log.md` to avoid re-deriving proven solutions
- Leverage existing working scripts in main project directory
```

### 4.3 Working Solutions Template
**File:** `dynamic/working-solutions.md`

```markdown
# Proven Working Solutions
**Last Updated:** [DATE]
**Status:** Validated through automated testing

## [SOLUTION_1_NAME] (VALIDATED - [HYPOTHESIS_ID])
**Status:** ✅ WORKING - [STATUS_DESCRIPTION]
**Performance:** [PERFORMANCE_METRICS]
**Evidence:** Validated via assumption-validator.py

```bash
# [SOLUTION_DESCRIPTION]
[COMMAND_OR_CODE_BLOCK]
```

## [SOLUTION_2_NAME] (VALIDATED - [HYPOTHESIS_ID])
**Status:** ✅ WORKING - [STATUS_DESCRIPTION]
**Evidence:** [EVIDENCE_DESCRIPTION]

```bash
# [SOLUTION_DESCRIPTION]
[COMMAND_OR_CODE_BLOCK]
```

## Validation Script Commands
**Status:** ✅ WORKING - Automated testing framework
**Location:** `dynamic/assumption-validator.py`

```bash
# Run all validations
python3 dynamic/assumption-validator.py

# Extended test
python3 dynamic/assumption-validator.py --[OPTION] [VALUE]
```

## Performance Baselines (VALIDATED - [HYPOTHESIS_ID])
**Status:** ✅ CONFIRMED - Performance improvement documented
**Evidence:** [PERFORMANCE_EVIDENCE]

- **New Solution:** [NEW_METRICS]
- **Original Solution:** [ORIGINAL_METRICS]
- **Improvement:** [IMPROVEMENT_METRICS]

## Archive Notes
**Obsolete Solutions:** (Moved to archive when no longer needed)
- None currently - all solutions remain active

**Next Validation Needed:**
- [NEXT_VALIDATION_1]
- [NEXT_VALIDATION_2]

---

## Usage Instructions
1. **[USAGE_INSTRUCTION_1]**
2. **[USAGE_INSTRUCTION_2]**
3. **Update this file** when new solutions are validated
```

---

## 🐍 Step 5: Create Assumption Validation Framework

### 5.1 Python Validation Script
**File:** `dynamic/assumption-validator.py`

```python
#!/usr/bin/env python3
"""
[PROJECT_NAME] Assumption Validation Framework
Automated testing and validation of project hypotheses
"""

import subprocess
import time
import json
import psutil
import os
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('validation-results.log'),
        logging.StreamHandler()
    ]
)

class AssumptionValidator:
    def __init__(self, target_device="[TARGET_IP]", target_mac="[DEV_IP]"):
        self.target_device = target_device
        self.target_mac = target_mac
        self.results = {}
        self.start_time = datetime.now()
        
    def log_result(self, assumption_id: str, status: str, evidence: Dict, notes: str = ""):
        """Log validation result for an assumption"""
        self.results[assumption_id] = {
            "status": status,
            "evidence": evidence,
            "notes": notes,
            "timestamp": datetime.now().isoformat(),
            "validation_time": (datetime.now() - self.start_time).total_seconds()
        }
        logging.info(f"{assumption_id}: {status} - {notes}")

    def run_command(self, command: str, timeout: int = 30) -> Tuple[bool, str, str]:
        """Execute command and return success, stdout, stderr"""
        try:
            result = subprocess.run(
                command, shell=True, timeout=timeout,
                capture_output=True, text=True
            )
            return result.returncode == 0, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return False, "", f"Command timed out after {timeout}s"
        except Exception as e:
            return False, "", str(e)

    def measure_system_resources(self, duration: int = 10) -> Dict:
        """Measure CPU and memory usage over specified duration"""
        cpu_samples = []
        memory_samples = []
        
        for _ in range(duration):
            cpu_samples.append(psutil.cpu_percent(interval=1))
            memory_samples.append(psutil.virtual_memory().percent)
        
        return {
            "cpu_avg": sum(cpu_samples) / len(cpu_samples),
            "cpu_max": max(cpu_samples),
            "memory_avg": sum(memory_samples) / len(memory_samples),
            "memory_max": max(memory_samples),
            "samples": len(cpu_samples)
        }

    def validate_h1_first_hypothesis(self) -> bool:
        """H1: [FIRST_HYPOTHESIS_DESCRIPTION]"""
        logging.info("Validating H1: [FIRST_HYPOTHESIS_DESCRIPTION]")
        
        # Test implementation - CUSTOMIZE THIS
        test_cmd = "[YOUR_TEST_COMMAND]"
        success, stdout, stderr = self.run_command(test_cmd, timeout=30)
        
        evidence = {
            "test_result": success,
            "output": stdout,
            "error": stderr if not success else ""
        }
        
        if success:
            self.log_result("H1", "VALIDATED", evidence, "[SUCCESS_MESSAGE]")
            return True
        else:
            self.log_result("H1", "FAILED", evidence, "[FAILURE_MESSAGE]")
            return False

    # ADD MORE VALIDATION METHODS HERE AS NEEDED
    # def validate_h2_second_hypothesis(self) -> bool:
    #     """H2: [SECOND_HYPOTHESIS_DESCRIPTION]"""
    #     # Implementation here

    def run_all_validations(self) -> Dict:
        """Run all assumption validations"""
        logging.info("Starting comprehensive assumption validation")
        
        validations = [
            ("H1", self.validate_h1_first_hypothesis),
            # ADD MORE VALIDATIONS HERE
            # ("H2", self.validate_h2_second_hypothesis),
        ]
        
        results_summary = {}
        
        for assumption_id, validator_func in validations:
            try:
                result = validator_func()
                results_summary[assumption_id] = "VALIDATED" if result else "FAILED"
            except Exception as e:
                logging.error(f"Error validating {assumption_id}: {e}")
                results_summary[assumption_id] = "ERROR"
                self.log_result(assumption_id, "ERROR", {"exception": str(e)})
        
        return results_summary

    def save_results(self, filename: str = None):
        """Save validation results to JSON file"""
        if filename is None:
            filename = f"validation-results-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
        
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        logging.info(f"Results saved to {filename}")

    def print_summary(self):
        """Print validation summary"""
        print("\n" + "="*60)
        print("ASSUMPTION VALIDATION SUMMARY")
        print("="*60)
        
        for assumption_id, result in self.results.items():
            status_icon = "✅" if result["status"] == "VALIDATED" else "❌" if result["status"] == "FAILED" else "⚠️"
            print(f"{status_icon} {assumption_id}: {result['status']} - {result['notes']}")
        
        validated = sum(1 for r in self.results.values() if r["status"] == "VALIDATED")
        total = len(self.results)
        print(f"\nValidation Score: {validated}/{total} ({validated/total*100:.1f}%)")
        print("="*60)

def main():
    """Main execution function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="[PROJECT_NAME] Assumption Validator")
    parser.add_argument("--target-device", default="[TARGET_IP]", help="Target device IP")
    parser.add_argument("--target-mac", default="[DEV_IP]", help="Development machine IP")
    parser.add_argument("--output", help="Output JSON file for results")
    
    args = parser.parse_args()
    
    validator = AssumptionValidator(args.target_device, args.target_mac)
    
    # Run all validations
    summary = validator.run_all_validations()
    
    # Save and display results
    validator.save_results(args.output)
    validator.print_summary()

if __name__ == "__main__":
    main()
```

---

## 📚 Step 6: Create Guide Files

### 6.1 LLM Quick Start Guide
**File:** `guides/llm-session-quick-start.md`

```markdown
# LLM Session Quick Start Guide

## 🚀 Immediate Actions (First 30 seconds)

### 1. Read Session Context (CRITICAL)
```
1. READ: dynamic/session-handoff.md (immediate context)
2. READ: dynamic/current-iteration.md (active hypothesis)
3. REFERENCE: evolving/assumptions-log.md (validation history)
```

### 2. Identify Current Task
- **Current Iteration:** Check session-handoff.md for iteration number and hypothesis
- **Priority Actions:** Check "Immediate Next Actions" section
- **Blockers:** Check for any current blockers or risks

### 3. Verify System State
```bash
# Quick validation check
cd [CONTEXT_DIRECTORY]
python3 dynamic/assumption-validator.py
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

## 🔧 Essential Commands

### Validation Framework
```bash
# Location: [CONTEXT_DIRECTORY]
cd [CONTEXT_DIRECTORY]

# Quick validation (all current hypotheses)
python3 dynamic/assumption-validator.py

# Extended test
python3 dynamic/assumption-validator.py --[OPTION] [VALUE]
```

## ⚠️ Critical Rules

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
[CONTEXT_DIRECTORY]/
├── static/                    # Read only when hardware changes
│   ├── environment.md         # Hardware, network configuration
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

## 💡 Cost Optimization

### Token Usage Strategy
- **Primary:** dynamic/ files (always read)
- **Secondary:** evolving/ files (reference as needed)
- **Minimal:** static/ files (only when hardware changes)
- **Never:** archive/ files (completed work)

### Efficiency Tips
- Use assumptions-log.md to avoid re-deriving solutions
- Reference working-solutions.md for proven commands
- Use validation script instead of manual testing
- Keep session-handoff.md concise and actionable
```

### 6.2 Human Maintenance Guide
**File:** `guides/human-maintenance-guide.md`

```markdown
# Human Context Maintenance Guide

## Overview
This guide explains how to maintain the Agile context management system for optimal LLM session continuity and cost efficiency.

---

## End of Each Session Checklist

### 1. Update Session Handoff (CRITICAL)
**File:** `dynamic/session-handoff.md`
- [ ] Update "Last Updated" timestamp
- [ ] Update "Progress" percentage and status
- [ ] Update "Immediate Next Actions" with current priorities
- [ ] Update "Current Working State" if anything changed
- [ ] Update "Blockers/Risks" section
- [ ] Update "Definition of Done" checklist progress

### 2. Update Current Iteration Status
**File:** `dynamic/current-iteration.md`
- [ ] Update "Current Status" section with latest progress
- [ ] Update "Active Experiments" if new tests were started
- [ ] Update "Next Actions" priority order
- [ ] Update "Definition of Done" checklist

### 3. Update Assumptions Log (If Validation Occurred)
**File:** `evolving/assumptions-log.md`
- [ ] Add new evidence to existing hypotheses
- [ ] Update hypothesis status (TESTING → VALIDATED/FAILED)
- [ ] Add new hypotheses if iteration progressed
- [ ] Update "Evidence Collected" and "Evidence Needed" sections

### 4. Archive Completed Work
- [ ] If iteration completed, move detailed logs to `archive/iterationX-complete/`
- [ ] Keep only essential information in active files
- [ ] Update product backlog with completion status

---

## Assumption Validation Script Usage

### Script Location
```bash
[CONTEXT_DIRECTORY]/dynamic/assumption-validator.py
```

### Basic Usage Commands

#### 1. Run All Current Validations
```bash
cd [CONTEXT_DIRECTORY]
python3 dynamic/assumption-validator.py
```
**Output:** Validates all current hypotheses and generates summary report

#### 2. Save Results to Specific Files
```bash
# Save with custom filename
python3 dynamic/assumption-validator.py --output validation-results-iteration1.json

# Save with timestamp (automatic)
python3 dynamic/assumption-validator.py
# Creates: validation-results-YYYYMMDD-HHMMSS.json
```

#### 3. Get Help
```bash
python3 dynamic/assumption-validator.py --help
```

### Script Output Files

#### 1. JSON Results File
**Location:** `validation-results-YYYYMMDD-HHMMSS.json`
**Content:** Detailed validation results with evidence and timestamps

#### 2. Log File
**Location:** `validation-results.log`
**Content:** Detailed execution log with timestamps and debug information

### Interpreting Results

#### Status Values
- **VALIDATED** ✅ - Hypothesis confirmed with evidence
- **FAILED** ❌ - Hypothesis disproven or test failed
- **ERROR** ⚠️ - Technical error during testing
- **TESTING** 🔄 - Currently being validated (in progress)

---

## Weekly Maintenance Tasks

### 1. Review and Consolidate (Every Monday)
- [ ] Review `evolving/assumptions-log.md` for completed validations
- [ ] Consolidate similar evidence entries
- [ ] Archive old detailed logs to reduce file size
- [ ] Update `evolving/product-backlog.md` completion status

### 2. Clean Up Dynamic Files (Every Friday)
- [ ] Archive completed session handoff entries
- [ ] Clean up old validation result files (keep last 5)
- [ ] Remove obsolete working solutions from context
- [ ] Update file timestamps and progress indicators

### 3. Validate System Health (Bi-weekly)
```bash
# Run full validation to ensure system still works
cd [CONTEXT_DIRECTORY]
python3 dynamic/assumption-validator.py
```

---

## File Size Management

### Target File Sizes (for optimal LLM context)
- `dynamic/session-handoff.md`: < 2KB (focus on essentials)
- `dynamic/current-iteration.md`: < 1.5KB (current state only)
- `evolving/assumptions-log.md`: < 10KB (key evidence only)
- `evolving/product-backlog.md`: < 8KB (active stories only)

### When Files Get Too Large
1. **Archive completed iterations** to `archive/` directory
2. **Summarize old evidence** instead of keeping detailed logs
3. **Remove obsolete working solutions** that are no longer used
4. **Consolidate similar validation results**

---

## Cost Optimization Strategy

### Token Usage Guidelines
1. **Keep dynamic files small** (< 2KB each) for frequent reading
2. **Archive completed work** to reduce context size
3. **Use validation script results** instead of manual testing descriptions
4. **Reference proven solutions** rather than re-deriving them

### Context Efficiency Rules
1. **Static files** (`static/`) - Read only when hardware/environment changes
2. **Evolving files** (`evolving/`) - Reference for planning and validation history
3. **Dynamic files** (`dynamic/`) - Always read for current session context
4. **Archive files** (`archive/`) - Never read in active sessions
```

---

## 📖 Step 7: Create Main README

**File:** `README.md`

```markdown
# [PROJECT_NAME] - Agile Context Management System

## Overview
This directory contains a comprehensive Agile context management system designed to optimize LLM session continuity and cost efficiency for the [PROJECT_DESCRIPTION].

## 🎯 Project Goal
[PROJECT_GOAL_DESCRIPTION]

## 📁 Directory Structure

```
[CONTEXT_DIRECTORY]/
├── README.md                          # This file - system overview
├── static/                            # Tier 1: Static Foundation (rarely changes)
│   ├── environment.md                 # Hardware, network configuration
│   └── external-resources.md          # Documentation links and references
├── evolving/                          # Tier 2: Evolving Product (gradual changes)
│   ├── product-backlog.md             # User stories and iteration planning
│   ├── assumptions-log.md             # Hypothesis validation history
│   ├── risk-assessment.md             # Risk analysis and mitigation
│   └── validation.md                  # Success criteria and metrics
├── dynamic/                           # Tier 3: Dynamic Session (changes every session)
│   ├── session-handoff.md             # CRITICAL - immediate session context
│   ├── current-iteration.md           # Active iteration status and hypothesis
│   ├── assumption-validator.py        # Automated validation framework
│   └── working-solutions.md           # Proven commands and solutions
├── guides/                            # Meta-instructions and documentation
│   ├── llm-session-quick-start.md     # Quick start guide for LLM sessions
│   ├── human-maintenance-guide.md     # Comprehensive maintenance guide
│   └── system-setup-instructions.md   # Complete system recreation guide
└── archive/                           # Completed iterations (don't read in active sessions)
```

## 🚀 Quick Start for LLM Sessions

### 1. Essential Reading Order (First 30 seconds)
1. **CRITICAL:** `dynamic/session-handoff.md` - Immediate session context
2. **IMPORTANT:** `dynamic/current-iteration.md` - Active iteration and hypothesis
3. **REFERENCE:** `evolving/assumptions-log.md` - Validation history and evidence

### 2. Key Commands
```bash
# Navigate to context directory
cd [CONTEXT_DIRECTORY]

# Run all current validations
python3 dynamic/assumption-validator.py

# Get help
