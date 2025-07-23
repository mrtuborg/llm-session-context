# Human Quick Commands & Shortcuts

## 🚀 One-Line Session Commands

### Session Start (Copy-Paste)
```
Start session: Read context (session-handoff, current-iteration, environment, failed-solutions), ask 3-5 specific questions based on what you find, then summarize status and next actions.
```

### Session End (Copy-Paste)  
```
End session: Compile knowledge (update working-solutions.md, failed-solutions/, create daily log in archive/daily-logs/), update session-handoff.md and current-iteration.md, update knowledge base in static/knowledge-base/, ask closure questions about knowledge completeness and next priorities.
```

### Emergency Reset (Copy-Paste)
```
System reset: Run assumption-validator.py, read working-solutions.md, update session-handoff.md with current technical state.
```

## ⚡ Quick Status Checks

### Before Starting Session
```bash
# Quick system health check (30 seconds)
cd /path/to/your/project/LM_context
python3 dynamic/assumption-validator.py --stability-hours 0.1 && echo "✅ System Ready"
```

### After Session (Verify LLM Updates)
```bash
# Check if files were actually updated (10 seconds)
ls -la dynamic/session-handoff.md dynamic/current-iteration.md
grep -i "$(date +%Y-%m-%d)" dynamic/session-handoff.md || echo "⚠️ Session handoff not updated"
```

### Weekly Maintenance (5 minutes)
```bash
# Clean up and verify system health
find . -name "*.md" -size +10k -exec echo "Large file: {}" \;
python3 dynamic/assumption-validator.py --stability-hours 1
```

## 📋 Human Decision Templates

### When LLM Asks About Priorities
**Quick Responses:**
- `"Continue current iteration - focus on [specific task]"`
- `"Pivot to [new area] - current work is blocked"`  
- `"Run validation first - need to verify current state"`
- `"Emergency: fix [specific issue] immediately"`

### When LLM Asks About Time/Scope
**Quick Responses:**
- `"30 min session - quick progress only"`
- `"2 hour session - can tackle major tasks"`
- `"Just validation - run tests and update status"`
- `"Planning session - prepare next iteration"`

### When LLM Asks About Environment
**Quick Responses:**
- `"Environment unchanged - proceed as documented"`
- `"Network issue: target device IP changed to [new IP]"`
- `"Hardware problem: camera not accessible"`
- `"All systems normal - continue with current setup"`

## 🎯 Cost-Saving Shortcuts

### Avoid Re-Reading Large Files
**Instead of:** "Read the entire environment.md file"
**Say:** "Environment unchanged since last session - use cached context"

### Use Validation Script Results
**Instead of:** Describing manual tests
**Say:** "Run assumption-validator.py and use those results"

### Reference Previous Sessions
**Instead of:** Re-explaining context
**Say:** "Continue from session-handoff.md - no additional context needed"

### Batch Updates
**Instead of:** Multiple file updates
**Say:** "Update all context files at session end - batch the changes"

## 🔧 Emergency Procedures

### If LLM Seems Confused
```
Reset context: Read session-handoff.md only, ask one specific question about current priority, proceed with that task.
```

### If Session Goes Off-Track
```
Refocus: What's the #1 priority from session-handoff.md? Work on that only.
```

### If Files Seem Inconsistent
```
Validate system: Run assumption-validator.py, update session-handoff.md with actual current state.
```

## 📊 Success Metrics (Quick Check)

### Good Session Indicators
- [ ] LLM asked specific questions (not generic)
- [ ] Work focused on session-handoff priorities  
- [ ] Files updated with concrete progress
- [ ] Next session has clear direction

### Poor Session Indicators  
- [ ] LLM asked generic questions
- [ ] Work scattered across multiple areas
- [ ] Vague progress updates
- [ ] Unclear next steps

## 💡 Pro Tips

### Save Tokens
- Use short, specific responses to LLM questions
- Reference file names instead of describing content
- Say "continue as planned" when no changes needed
- Use validation script results instead of manual descriptions

### Save Time
- Keep session-handoff.md under 2KB for fast reading
- Use the one-line session commands above
- Batch all file updates at session end
- Run quick status checks before starting

### Maintain Quality
- Always verify LLM actually updated files
- Check that next actions are specific and actionable
- Ensure progress percentages reflect reality
- Keep failed-solutions updated when things don't work

---

**Last Updated:** July 23, 2025  
**Purpose:** Streamline human interaction with the LLM context system
