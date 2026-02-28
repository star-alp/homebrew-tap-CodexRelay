#!/usr/bin/env python3

from __future__ import annotations

import json
import os
import re
import sys
import urllib.request

UPSTREAM = "Red-noblue/Codex_Relay"
CASK_PATH = os.path.join("Casks", "codexrelay.rb")


def gh_json(url: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "codexrelay-tap-updater",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def gh_asset_text(asset_api_url: str) -> str:
    # Download release asset via API (more reliable than github.com direct download in some networks).
    req = urllib.request.Request(
        asset_api_url,
        headers={
            "Accept": "application/octet-stream",
            "User-Agent": "codexrelay-tap-updater",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def main() -> int:
    release = gh_json(f"https://api.github.com/repos/{UPSTREAM}/releases/latest")
    tag = (release.get("tag_name") or "").strip()
    if not tag:
        print("Missing tag_name in latest release", file=sys.stderr)
        return 2
    version = tag[1:] if tag.startswith("v") else tag

    assets = release.get("assets") or []
    sha_asset = next((a for a in assets if a.get("name") == "SHA256SUMS.txt"), None)
    if not sha_asset:
        print("Missing SHA256SUMS.txt asset in latest release", file=sys.stderr)
        return 3

    sha_text = gh_asset_text(sha_asset["url"])
    dmg_name = f"CodexRelay_{version}_aarch64.dmg"
    sha256 = None
    for line in sha_text.splitlines():
        # Format: "<sha>  ./path/to/file"
        parts = line.split()
        if len(parts) >= 2 and parts[0].lower() == parts[0] and dmg_name in parts[-1]:
            sha256 = parts[0]
            break
    if not sha256 or not re.fullmatch(r"[0-9a-f]{64}", sha256):
        print(f"Failed to locate sha256 for {dmg_name} in SHA256SUMS.txt", file=sys.stderr)
        return 4

    with open(CASK_PATH, "r", encoding="utf-8") as f:
        old = f.read()

    new = old
    new = re.sub(r'version\s+"[^"]+"', f'version "{version}"', new, count=1)
    new = re.sub(r'sha256\s+"[0-9a-f]{64}"', f'sha256 "{sha256}"', new, count=1)

    if new == old:
        print("No changes")
        return 0

    with open(CASK_PATH, "w", encoding="utf-8") as f:
        f.write(new)

    print(f"Updated {CASK_PATH}: version={version} sha256={sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

