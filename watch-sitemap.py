#!/usr/bin/env python3
"""
File Watcher for Sitemap Auto-Generation
Watches for HTML file changes and regenerates sitemap.xml automatically
"""

import time
import subprocess
import sys
from pathlib import Path
from datetime import datetime

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    print("❌ watchdog package not found.")
    print("\nTo enable auto-update, install watchdog:")
    print("   pip3 install watchdog")
    print("\nAlternatively, manually run the sitemap generator after changes:")
    print("   python3 generate-sitemap.py")
    sys.exit(1)


class HTMLFileHandler(FileSystemEventHandler):
    """Handler for HTML file changes"""

    def __init__(self):
        self.last_regenerated = 0
        self.cooldown = 2  # seconds to wait before regenerating again

    def on_any_event(self, event):
        """Called when any file system event occurs"""
        # Only process HTML files
        if event.is_directory:
            return

        if event.src_path.endswith('.html'):
            current_time = time.time()

            # Prevent rapid regeneration (debounce)
            if current_time - self.last_regenerated < self.cooldown:
                return

            self.last_regenerated = current_time

            # Determine event type
            event_type = event.event_type
            file_name = Path(event.src_path).name

            print(f"\n{'='*60}")
            print(f"🔔 {event_type.upper()}: {event.src_path}")
            print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"{'='*60}")

            # Regenerate sitemap
            try:
                print("🔄 Regenerating sitemap...")
                result = subprocess.run(
                    ['python3', 'generate-sitemap.py'],
                    capture_output=True,
                    text=True
                )

                if result.returncode == 0:
                    print(result.stdout)
                else:
                    print(f"❌ Error: {result.stderr}")

            except Exception as e:
                print(f"❌ Failed to regenerate sitemap: {e}")


def main():
    """Start watching for file changes"""
    print("👀 Freight Labs Sitemap Auto-Generator")
    print("=" * 60)
    print("Watching for HTML file changes...")
    print("Press Ctrl+C to stop")
    print("=" * 60)

    event_handler = HTMLFileHandler()
    observer = Observer()

    # Watch current directory and all subdirectories
    observer.schedule(event_handler, '.', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n👋 Stopping file watcher...")
        observer.stop()

    observer.join()
    print("✅ File watcher stopped")


if __name__ == '__main__':
    main()
