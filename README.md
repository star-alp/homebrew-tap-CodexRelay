# CodexRelay Homebrew Tap

This repository provides a Homebrew Cask for installing **CodexRelay**.

Project: https://github.com/Red-noblue/Codex_Relay

## Install

```bash
brew tap star-alp/tap-codexrelay
brew install --cask --no-quarantine codexrelay
```

If macOS still blocks the app, you can remove the quarantine attribute:

```bash
sudo xattr -dr com.apple.quarantine /Applications/CodexRelay.app
```

