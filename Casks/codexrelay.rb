cask "codexrelay" do
  version "0.1.6"
  sha256 "74237241012f518e053e0766f4606049503babdefcbc9e8ed7a3910f4abfec1a"

  url "https://github.com/Red-noblue/Codex_Relay/releases/download/v#{version}/CodexRelay_#{version}_aarch64.dmg",
      verified: "github.com/Red-noblue/Codex_Relay/"
  name "CodexRelay"
  desc "Cross-device Codex CLI session transfer manager"
  homepage "https://github.com/Red-noblue/Codex_Relay"

  depends_on arch: :arm64

  app "CodexRelay.app"
end
