#!/usr/bin/env python3
"""
LLM Context System Framework Sync Tool

This script helps sync improvements from real project usage back to the framework
with intelligent questioning to avoid unintentional framework corruption.

Usage:
    python3 sync-framework-improvements.py --source /path/to/project --target /path/to/framework
    python3 sync-framework-improvements.py --analyze-only /path/to/project
"""

import os
import sys
import json
import argparse
import difflib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class FrameworkSyncTool:
    def __init__(self, source_project: str, target_framework: str, analyze_only: bool = False):
        self.source_project = Path(source_project).resolve()
        self.target_framework = Path(target_framework).resolve()
        self.analyze_only = analyze_only
        
        # Define framework-relevant files and their categories
        self.framework_files = {
            # Core LLM guides that should be synced
            "llm-guides": [
                "llm-session-quick-start.md",
                "llm-context-question-guide.md",
                "llm-output-management-guide.md"  # New improvement from melexis
            ],
            
            # Human guides that should be synced
            "human-guides": [
                "human-quick-commands.md",
                "human-maintenance-guide.md"
            ],
            
            # System documentation that should be synced
            "system-docs": [
                "context-flow-diagrams.md",
                "cost-optimization-analysis.md",
                "session-knowledge-compilation.md",
                "system-setup-instructions.md",
                "troubleshooting-comprehensive.md"
            ],
            
            # Evolving framework specifications
            "evolving": [
                "foundational-elements-specification.md"  # Major improvement from melexis
            ],
            
            # Template files that might have improvements
            "templates": [
                "collaboration-workflow.md",
                "README.md"
            ]
        }
        
        # Project-specific files that should NOT be synced to framework
        self.project_specific_exclusions = [
            "static/environment.md",  # Project-specific environment
            "static/external-resources.md",  # Project-specific resources
            "static/resources/",  # Project-specific PDFs and resources
            "dynamic/session-handoff.md",  # Project-specific session state
            "dynamic/current-iteration.md",  # Project-specific iteration
            "dynamic/working-solutions.md",  # Project-specific solutions
            "dynamic/failed-solutions/",  # Project-specific failures
            "dynamic/assumption-validator.py",  # Project-specific validation
            "evolving/assumptions-log.md",  # Project-specific assumptions
            "evolving/product-backlog.md",  # Project-specific backlog
            "evolving/project-plan.md",  # Project-specific plan
            "evolving/risk-assesment.md",  # Project-specific risks
            "evolving/validation.md",  # Project-specific validation
            "archive/",  # Project-specific archive
            "knowledge/"  # Project-specific knowledge
        ]
        
    def analyze_improvements(self) -> Dict:
        """Analyze what improvements exist in the source project."""
        print("🔍 Analyzing improvements in source project...")
        
        improvements = {
            "new_files": [],
            "modified_files": [],
            "structural_changes": [],
            "potential_framework_enhancements": []
        }
        
        source_lm_context = self.source_project / "LM_context"
        target_lm_context = self.target_framework / "LM_context"
        
        if not source_lm_context.exists():
            print(f"❌ Source LM_context not found: {source_lm_context}")
            return improvements
            
        if not target_lm_context.exists():
            print(f"❌ Target LM_context not found: {target_lm_context}")
            return improvements
            
        # Check for new files
        for category, files in self.framework_files.items():
            for file_name in files:
                source_file = source_lm_context / category / file_name
                target_file = target_lm_context / category / file_name
                
                if source_file.exists() and not target_file.exists():
                    improvements["new_files"].append({
                        "category": category,
                        "file": file_name,
                        "source_path": str(source_file),
                        "target_path": str(target_file)
                    })
                elif source_file.exists() and target_file.exists():
                    # Check for modifications
                    if self._files_different(source_file, target_file):
                        improvements["modified_files"].append({
                            "category": category,
                            "file": file_name,
                            "source_path": str(source_file),
                            "target_path": str(target_file)
                        })
        
        # Check for structural improvements
        improvements["structural_changes"] = self._analyze_structural_changes()
        
        # Identify potential framework enhancements
        improvements["potential_framework_enhancements"] = self._identify_framework_enhancements()
        
        return improvements
        
    def _files_different(self, file1: Path, file2: Path) -> bool:
        """Check if two files are different."""
        try:
            with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
                return f1.read() != f2.read()
        except Exception as e:
            print(f"⚠️ Error comparing files {file1} and {file2}: {e}")
            return False
            
    def _analyze_structural_changes(self) -> List[Dict]:
        """Analyze structural changes in the project."""
        changes = []
        
        source_lm_context = self.source_project / "LM_context"
        target_lm_context = self.target_framework / "LM_context"
        
        # Check for new directories
        for item in source_lm_context.rglob("*"):
            if item.is_dir():
                relative_path = item.relative_to(source_lm_context)
                target_equivalent = target_lm_context / relative_path
                
                if not target_equivalent.exists():
                    changes.append({
                        "type": "new_directory",
                        "path": str(relative_path),
                        "description": f"New directory structure: {relative_path}"
                    })
        
        return changes
        
    def _identify_framework_enhancements(self) -> List[Dict]:
        """Identify potential framework enhancements from project usage."""
        enhancements = []
        
        # Check for new guide files
        source_guides = self.source_project / "LM_context" / "llm-guides"
        if source_guides.exists():
            for guide_file in source_guides.glob("*.md"):
                if guide_file.name not in self.framework_files["llm-guides"]:
                    enhancements.append({
                        "type": "new_guide",
                        "file": guide_file.name,
                        "path": str(guide_file),
                        "description": f"New LLM guide discovered: {guide_file.name}"
                    })
        
        # Check for enhanced foundational elements
        source_foundational = self.source_project / "LM_context" / "evolving" / "foundational-elements-specification.md"
        target_foundational = self.target_framework / "LM_context" / "evolving" / "foundational-elements-specification.md"
        
        if source_foundational.exists() and target_foundational.exists():
            if self._files_different(source_foundational, target_foundational):
                enhancements.append({
                    "type": "foundational_elements_enhancement",
                    "file": "foundational-elements-specification.md",
                    "description": "Foundational elements specification has been enhanced"
                })
        
        return enhancements
        
    def interactive_sync(self, improvements: Dict) -> None:
        """Interactively sync improvements with user confirmation."""
        print("\n🔄 Starting interactive sync process...")
        
        # Handle new files
        if improvements["new_files"]:
            print(f"\n📄 Found {len(improvements['new_files'])} new files:")
            for new_file in improvements["new_files"]:
                self._handle_new_file(new_file)
        
        # Handle modified files
        if improvements["modified_files"]:
            print(f"\n✏️ Found {len(improvements['modified_files'])} modified files:")
            for modified_file in improvements["modified_files"]:
                self._handle_modified_file(modified_file)
        
        # Handle structural changes
        if improvements["structural_changes"]:
            print(f"\n🏗️ Found {len(improvements['structural_changes'])} structural changes:")
            for change in improvements["structural_changes"]:
                self._handle_structural_change(change)
        
        # Handle framework enhancements
        if improvements["potential_framework_enhancements"]:
            print(f"\n🚀 Found {len(improvements['potential_framework_enhancements'])} potential framework enhancements:")
            for enhancement in improvements["potential_framework_enhancements"]:
                self._handle_framework_enhancement(enhancement)
                
    def _handle_new_file(self, new_file: Dict) -> None:
        """Handle a new file with user interaction."""
        print(f"\n📄 New file found: {new_file['category']}/{new_file['file']}")
        
        # Show file preview
        try:
            with open(new_file['source_path'], 'r', encoding='utf-8') as f:
                content = f.read()
                preview = content[:500] + "..." if len(content) > 500 else content
                print(f"Preview:\n{preview}")
        except Exception as e:
            print(f"⚠️ Could not preview file: {e}")
            
        # Ask user decision
        while True:
            choice = input(f"\nAdd this file to framework? [y/n/s(kip)/p(review)]: ").lower().strip()
            
            if choice == 'y':
                self._copy_file_to_framework(new_file)
                break
            elif choice == 'n':
                print("❌ Skipping file")
                break
            elif choice == 's':
                print("⏭️ Skipping file")
                break
            elif choice == 'p':
                self._show_full_file_content(new_file['source_path'])
            else:
                print("Please enter y, n, s, or p")
                
    def _handle_modified_file(self, modified_file: Dict) -> None:
        """Handle a modified file with user interaction."""
        print(f"\n✏️ Modified file: {modified_file['category']}/{modified_file['file']}")
        
        # Show diff
        self._show_file_diff(modified_file['target_path'], modified_file['source_path'])
        
        # Ask user decision
        while True:
            choice = input(f"\nUpdate framework file with these changes? [y/n/s(kip)/d(iff again)]: ").lower().strip()
            
            if choice == 'y':
                self._copy_file_to_framework(modified_file)
                break
            elif choice == 'n':
                print("❌ Skipping file")
                break
            elif choice == 's':
                print("⏭️ Skipping file")
                break
            elif choice == 'd':
                self._show_file_diff(modified_file['target_path'], modified_file['source_path'])
            else:
                print("Please enter y, n, s, or d")
                
    def _handle_structural_change(self, change: Dict) -> None:
        """Handle a structural change with user interaction."""
        print(f"\n🏗️ Structural change: {change['description']}")
        
        choice = input(f"Apply this structural change to framework? [y/n]: ").lower().strip()
        
        if choice == 'y':
            if change['type'] == 'new_directory':
                target_dir = self.target_framework / "LM_context" / change['path']
                target_dir.mkdir(parents=True, exist_ok=True)
                print(f"✅ Created directory: {target_dir}")
        else:
            print("❌ Skipping structural change")
            
    def _handle_framework_enhancement(self, enhancement: Dict) -> None:
        """Handle a framework enhancement with user interaction."""
        print(f"\n🚀 Framework enhancement: {enhancement['description']}")
        
        if enhancement['type'] == 'new_guide':
            print(f"New guide file: {enhancement['file']}")
            self._show_full_file_content(enhancement['path'])
            
            choice = input(f"Add this guide to the framework? [y/n]: ").lower().strip()
            if choice == 'y':
                # Copy to framework guides
                source_file = Path(enhancement['path'])
                target_file = self.target_framework / "LM_context" / "llm-guides" / enhancement['file']
                self._copy_file(source_file, target_file)
                
                # Update framework file lists
                self._update_framework_file_lists(enhancement['file'], "llm-guides")
                
        elif enhancement['type'] == 'foundational_elements_enhancement':
            print("Foundational elements specification has been enhanced")
            self._show_file_diff(
                str(self.target_framework / "LM_context" / "evolving" / "foundational-elements-specification.md"),
                str(self.source_project / "LM_context" / "evolving" / "foundational-elements-specification.md")
            )
            
            choice = input(f"Update foundational elements specification? [y/n]: ").lower().strip()
            if choice == 'y':
                source_file = self.source_project / "LM_context" / "evolving" / "foundational-elements-specification.md"
                target_file = self.target_framework / "LM_context" / "evolving" / "foundational-elements-specification.md"
                self._copy_file(source_file, target_file)
                
    def _copy_file_to_framework(self, file_info: Dict) -> None:
        """Copy a file to the framework."""
        source_file = Path(file_info['source_path'])
        target_file = Path(file_info['target_path'])
        
        self._copy_file(source_file, target_file)
        
    def _copy_file(self, source: Path, target: Path) -> None:
        """Copy a file with backup."""
        if not self.analyze_only:
            # Create backup if target exists
            if target.exists():
                backup_path = target.with_suffix(target.suffix + f".backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}")
                target.rename(backup_path)
                print(f"📦 Backup created: {backup_path}")
            
            # Ensure target directory exists
            target.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy file
            with open(source, 'r', encoding='utf-8') as src, open(target, 'w', encoding='utf-8') as tgt:
                tgt.write(src.read())
            
            print(f"✅ Copied: {source} → {target}")
        else:
            print(f"🔍 Would copy: {source} → {target}")
            
    def _show_file_diff(self, file1_path: str, file2_path: str) -> None:
        """Show diff between two files."""
        try:
            with open(file1_path, 'r', encoding='utf-8') as f1:
                file1_lines = f1.readlines()
            with open(file2_path, 'r', encoding='utf-8') as f2:
                file2_lines = f2.readlines()
                
            diff = difflib.unified_diff(
                file1_lines, file2_lines,
                fromfile=f"framework/{Path(file1_path).name}",
                tofile=f"project/{Path(file2_path).name}",
                lineterm=''
            )
            
            print("\n📊 Diff:")
            for line in diff:
                if line.startswith('+'):
                    print(f"\033[92m{line}\033[0m")  # Green
                elif line.startswith('-'):
                    print(f"\033[91m{line}\033[0m")  # Red
                elif line.startswith('@@'):
                    print(f"\033[94m{line}\033[0m")  # Blue
                else:
                    print(line)
                    
        except Exception as e:
            print(f"⚠️ Could not show diff: {e}")
            
    def _show_full_file_content(self, file_path: str) -> None:
        """Show full content of a file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"\n📄 Full content of {Path(file_path).name}:")
                print("=" * 50)
                print(content)
                print("=" * 50)
        except Exception as e:
            print(f"⚠️ Could not show file content: {e}")
            
    def _update_framework_file_lists(self, filename: str, category: str) -> None:
        """Update framework file lists to include new files."""
        # This would update deploy.py and other framework files to include the new file
        print(f"📝 Note: Remember to update deploy.py to include {filename} in {category}")
        
    def generate_sync_report(self, improvements: Dict) -> None:
        """Generate a detailed sync report."""
        report_path = self.target_framework / f"sync-report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# Framework Sync Report\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Source Project:** {self.source_project}\n")
            f.write(f"**Target Framework:** {self.target_framework}\n\n")
            
            f.write(f"## Summary\n\n")
            f.write(f"- New files: {len(improvements['new_files'])}\n")
            f.write(f"- Modified files: {len(improvements['modified_files'])}\n")
            f.write(f"- Structural changes: {len(improvements['structural_changes'])}\n")
            f.write(f"- Framework enhancements: {len(improvements['potential_framework_enhancements'])}\n\n")
            
            # Detail each category
            if improvements['new_files']:
                f.write(f"## New Files\n\n")
                for new_file in improvements['new_files']:
                    f.write(f"- **{new_file['category']}/{new_file['file']}**\n")
                    f.write(f"  - Source: {new_file['source_path']}\n")
                    f.write(f"  - Target: {new_file['target_path']}\n\n")
            
            if improvements['modified_files']:
                f.write(f"## Modified Files\n\n")
                for modified_file in improvements['modified_files']:
                    f.write(f"- **{modified_file['category']}/{modified_file['file']}**\n")
                    f.write(f"  - Source: {modified_file['source_path']}\n")
                    f.write(f"  - Target: {modified_file['target_path']}\n\n")
            
            if improvements['structural_changes']:
                f.write(f"## Structural Changes\n\n")
                for change in improvements['structural_changes']:
                    f.write(f"- **{change['type']}:** {change['description']}\n\n")
            
            if improvements['potential_framework_enhancements']:
                f.write(f"## Framework Enhancements\n\n")
                for enhancement in improvements['potential_framework_enhancements']:
                    f.write(f"- **{enhancement['type']}:** {enhancement['description']}\n\n")
        
        print(f"📊 Sync report generated: {report_path}")

def main():
    parser = argparse.ArgumentParser(
        description="Sync improvements from project usage back to framework",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze improvements only
  python3 sync-framework-improvements.py --analyze-only /Users/vn/ws/melexis-simple
  
  # Interactive sync from melexis project to framework
  python3 sync-framework-improvements.py --source /Users/vn/ws/melexis-simple --target /Users/vn/ws/LLM_Context_System
  
  # Generate report only
  python3 sync-framework-improvements.py --source /Users/vn/ws/melexis-simple --target /Users/vn/ws/LLM_Context_System --report-only
        """
    )
    
    parser.add_argument(
        "--source",
        help="Source project directory with improvements"
    )
    
    parser.add_argument(
        "--target", 
        help="Target framework directory to sync to"
    )
    
    parser.add_argument(
        "--analyze-only",
        help="Only analyze improvements without syncing (provide source path)"
    )
    
    parser.add_argument(
        "--report-only",
        action="store_true",
        help="Generate report only, don't sync"
    )
    
    args = parser.parse_args()
    
    # Determine operation mode
    if args.analyze_only:
        if not Path(args.analyze_only).exists():
            print(f"❌ Source project not found: {args.analyze_only}")
            sys.exit(1)
        
        # Analyze only mode
        sync_tool = FrameworkSyncTool(args.analyze_only, "", analyze_only=True)
        improvements = sync_tool.analyze_improvements()
        
        print(f"\n📊 Analysis Results:")
        print(f"- New files: {len(improvements['new_files'])}")
        print(f"- Modified files: {len(improvements['modified_files'])}")
        print(f"- Structural changes: {len(improvements['structural_changes'])}")
        print(f"- Framework enhancements: {len(improvements['potential_framework_enhancements'])}")
        
        if improvements['new_files']:
            print(f"\n📄 New Files:")
            for new_file in improvements['new_files']:
                print(f"  - {new_file['category']}/{new_file['file']}")
        
        if improvements['modified_files']:
            print(f"\n✏️ Modified Files:")
            for modified_file in improvements['modified_files']:
                print(f"  - {modified_file['category']}/{modified_file['file']}")
        
        if improvements['potential_framework_enhancements']:
            print(f"\n🚀 Framework Enhancements:")
            for enhancement in improvements['potential_framework_enhancements']:
                print(f"  - {enhancement['description']}")
                
    elif args.source and args.target:
        if not Path(args.source).exists():
            print(f"❌ Source project not found: {args.source}")
            sys.exit(1)
        
        if not Path(args.target).exists():
            print(f"❌ Target framework not found: {args.target}")
            sys.exit(1)
        
        # Full sync mode
        sync_tool = FrameworkSyncTool(args.source, args.target, analyze_only=args.report_only)
        improvements = sync_tool.analyze_improvements()
        
        if args.report_only:
            sync_tool.generate_sync_report(improvements)
        else:
            sync_tool.interactive_sync(improvements)
            sync_tool.generate_sync_report(improvements)
            
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
