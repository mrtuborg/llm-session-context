# Comprehensive Troubleshooting Guide

## Overview
This guide provides detailed troubleshooting procedures for the LLM Context Management System, covering common issues, diagnostic techniques, and resolution strategies for any project type.

## 🚨 Emergency Procedures

### System Completely Broken
```bash
# 1. Check basic file structure
ls -la static/ evolving/ dynamic/ archive/

# 2. Verify critical files exist
ls -la dynamic/session-handoff.md dynamic/current-iteration.md

# 3. Run validation script if available
python3 dynamic/assumption-validator.py --quick-check

# 4. Check file permissions
find . -name "*.md" -not -readable -exec echo "Unreadable: {}" \;
```

### LLM Sessions Completely Unfocused
```bash
# Reset to minimal context
echo "EMERGENCY RESET - Read session-handoff.md only, focus on #1 priority" > emergency-context.txt

# Check session handoff clarity
wc -l dynamic/session-handoff.md  # Should be under 100 lines
grep -i "priority\|next\|action" dynamic/session-handoff.md
```

## 🔧 Context System Debugging

### File Consistency Issues
```bash
# Check for file size problems
find . -name "*.md" -size +50k -exec echo "Large file: {} $(wc -l < {})" \;

# Check for empty critical files
find dynamic/ -name "*.md" -size 0 -exec echo "Empty file: {}" \;

# Verify file timestamps
ls -lt dynamic/ | head -5  # Should show recent updates
```

### Session Handoff Problems
```bash
# Check handoff file quality
grep -c "TODO\|TBD\|unclear" dynamic/session-handoff.md  # Should be 0

# Verify specific actions exist
grep -i "next action\|priority\|immediate" dynamic/session-handoff.md

# Check for vague language
grep -i "maybe\|possibly\|might\|could" dynamic/session-handoff.md
```

## 📊 Performance Diagnostics

### Token Usage Analysis
```bash
# Estimate file sizes for token calculation
find . -name "*.md" -exec wc -c {} + | sort -n

# Check for redundant content
find . -name "*.md" -exec grep -l "duplicate content pattern" {} \;

# Monitor context freshness
grep -r "Last Updated" . | grep -v "$(date +%Y-%m-%d)"
```

### Session Efficiency Problems
```bash
# Check session duration patterns
grep -r "session.*minutes\|session.*hours" archive/daily-logs/

# Analyze question quality
grep -c "generic\|vague\|unclear" dynamic/session-handoff.md

# Review iteration completion rates
grep -c "✅\|completed\|done" evolving/assumptions-log.md
```

## 🔍 Common Issues and Solutions

### Issue: LLM Asks Generic Questions
**Symptoms:**
- Questions like "What would you like to work on?"
- No reference to specific project context
- Repeated questions across sessions

**Diagnosis:**
```bash
# Check session handoff specificity
grep -i "specific\|exact\|precise" dynamic/session-handoff.md

# Verify context freshness
ls -la dynamic/session-handoff.md  # Should be recently modified
```

**Solutions:**
1. **Update session handoff** with specific, actionable priorities
2. **Add concrete next steps** with exact commands or tasks
3. **Include specific questions** the LLM should ask
4. **Reference specific files** and line numbers when possible

### Issue: Context Files Too Large
**Symptoms:**
- Files over 10KB in size
- LLM sessions slow to start
- Token usage exceeding limits

**Diagnosis:**
```bash
# Find large files
find . -name "*.md" -size +10k -exec ls -lh {} \;

# Check for repetitive content
find . -name "*.md" -exec grep -c "repeated pattern" {} \;
```

**Solutions:**
1. **Archive completed work** to archive/ directory
2. **Consolidate similar content** across files
3. **Use references** instead of duplicating information
4. **Split large files** into focused, smaller files

### Issue: Validation Script Failures
**Symptoms:**
- Script exits with errors
- No validation results generated
- Environment setup problems

**Diagnosis:**
```bash
# Check script syntax
python3 -m py_compile dynamic/assumption-validator.py

# Verify dependencies
python3 -c "import sys; print(sys.version)"

# Check file permissions
ls -la dynamic/assumption-validator.py
```

**Solutions:**
1. **Fix syntax errors** using Python linter
2. **Install missing dependencies** for your project domain
3. **Update script permissions** to executable
4. **Customize validation methods** for your specific project

### Issue: Knowledge Not Preserved
**Symptoms:**
- Repeated work across sessions
- Lost insights and solutions
- No learning accumulation

**Diagnosis:**
```bash
# Check knowledge base updates
ls -la static/knowledge-base/

# Verify working solutions tracking
wc -l dynamic/working-solutions.md

# Check daily logs creation
ls -la archive/daily-logs/
```

**Solutions:**
1. **Update knowledge base** after each session
2. **Document working solutions** with exact commands
3. **Create daily logs** with session summaries
4. **Cross-reference** related solutions and insights

## 🛠️ System Maintenance

### Weekly Health Checks
```bash
# File size monitoring
find . -name "*.md" -size +10k -exec echo "Review size: {}" \;

# Context freshness check
find . -name "*.md" -mtime +7 -exec echo "Stale file: {}" \;

# Validation script health
python3 dynamic/assumption-validator.py --health-check

# Archive old content
find archive/ -name "*.md" -mtime +30 -exec echo "Archive candidate: {}" \;
```

### Monthly System Optimization
```bash
# Consolidate knowledge base
grep -r "duplicate insight" static/knowledge-base/

# Clean up failed solutions
find dynamic/failed-solutions/ -name "*.md" -mtime +60

# Update system guides
diff guides/ /path/to/latest/system/guides/

# Performance analysis
grep -r "token.*reduction\|session.*time" .
```

## 📋 Diagnostic Checklists

### Before Each Session
- [ ] Session handoff file updated within 24 hours
- [ ] Current iteration has specific, measurable goals
- [ ] Validation script runs without errors
- [ ] No files over 10KB without justification
- [ ] Failed solutions documented for current work area

### After Each Session
- [ ] Session handoff updated with concrete next steps
- [ ] Working solutions documented with exact commands
- [ ] Knowledge base updated with new insights
- [ ] Daily log created in archive/
- [ ] Current iteration progress updated with evidence

### Weekly Maintenance
- [ ] All files under size limits
- [ ] No stale content over 1 week old
- [ ] Validation script health verified
- [ ] Knowledge base consolidated and organized
- [ ] Archive cleaned of old, irrelevant content

## 🆘 When All Else Fails

### Complete System Reset
```bash
# 1. Backup current state
cp -r . ../backup-$(date +%Y%m%d)

# 2. Reset to minimal context
echo "System reset - start fresh with basic project context" > dynamic/session-handoff.md

# 3. Run basic validation
python3 dynamic/assumption-validator.py --basic-check

# 4. Rebuild from working solutions
grep -r "✅.*working" dynamic/working-solutions.md
```

### Emergency Context Recovery
```bash
# 1. Check git history for last good state
git log --oneline -10

# 2. Restore from backup if available
ls -la ../backup-*

# 3. Rebuild from project-specific working directory
# (This will be project-specific - check your main project directory)

# 4. Use system setup instructions to recreate
# Follow guides/system-setup-instructions.md
```

## 📞 Getting Help

### Self-Diagnosis Questions
1. **What specific error or behavior are you seeing?**
2. **When did this problem first appear?**
3. **What was the last working state you remember?**
4. **Have you made any recent changes to the system?**
5. **Are there any error messages or logs available?**

### Information to Gather
- **File sizes and timestamps** of critical context files
- **Error messages** from validation scripts or LLM sessions
- **Recent changes** to project environment or setup
- **Session patterns** that might indicate systemic issues

### Recovery Strategies
1. **Start Simple** - Use minimal context and build up
2. **Use Validation** - Let automated checks guide diagnosis
3. **Check History** - Look for last known good state
4. **Rebuild Systematically** - Follow setup instructions step by step

---

**Last Updated:** July 23, 2025  
**Purpose:** Comprehensive troubleshooting for LLM Context Management System  
**Scope:** Generic procedures applicable to any project domain
