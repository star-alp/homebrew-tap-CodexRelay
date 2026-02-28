cask "codexrelay" do
  version "0.1.5"
  sha256 "7cbb6638837b4f1ee27ae4e1a5eb75f5e9a216763f2084f0fe9e3b59a29593cd"

  url "https://github.com/Red-noblue/Codex_Relay/releases/download/v#{version}/CodexRelay_#{version}_aarch64.dmg",
      verified: "github.com/Red-noblue/Codex_Relay/"
  name "CodexRelay"
  desc "Cross-device Codex CLI session transfer manager"
  homepage "https://github.com/Red-noblue/Codex_Relay"

  depends_on arch: :arm64

  app "CodexRelay.app"
end
