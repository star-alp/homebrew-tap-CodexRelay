cask "codexrelay" do
  version "0.1.2"
  sha256 "f99d759df37910d7616f0b7c2c6ea5d063c8ff9a0f7a2fecfb52b75dcbafd92a"

  url "https://github.com/Red-noblue/Codex_Relay/releases/download/v#{version}/CodexRelay_#{version}_aarch64.dmg",
      verified: "github.com/Red-noblue/Codex_Relay/"
  name "CodexRelay"
  desc "Cross-device Codex CLI session transfer manager"
  homepage "https://github.com/Red-noblue/Codex_Relay"

  depends_on arch: :arm64

  app "CodexRelay.app"
end

