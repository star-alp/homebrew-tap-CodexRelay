cask "codexrelay" do
  version "0.1.7"
  sha256 "4a98ea119cbb737fcc9fe2c562b21c6d351ed05402d87565f69d6a8ff1c2eec0"

  url "https://github.com/Red-noblue/Codex_Relay/releases/download/v#{version}/CodexRelay_#{version}_aarch64.dmg",
      verified: "github.com/Red-noblue/Codex_Relay/"
  name "CodexRelay"
  desc "Cross-device Codex CLI session transfer manager"
  homepage "https://github.com/Red-noblue/Codex_Relay"

  depends_on arch: :arm64

  app "CodexRelay.app"
end
