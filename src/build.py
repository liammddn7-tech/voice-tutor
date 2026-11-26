# Builds the app: inlines the bundled Anthropic SDK so the page is one file.
#   ../voice-tutor.html  -> single file for the PC
#   ../site/             -> the phone version to host (index.html, manifest, service worker, icons)
import pathlib, shutil
here = pathlib.Path(__file__).parent
app = (here / "app.html").read_text()
sdk = (here / "anthropic-sdk-1.8.0.js").read_text().replace("</script", "<\\/script")
imp = 'import Anthropic from "https://cdn.jsdelivr.net/npm/@anthropic-ai/sdk@1.8.0/+esm";'
assert imp in app
app = app.replace(imp, "const Anthropic = window.AnthropicSDK.default;")
app = app.replace('<script type="module">', "<script>\n" + sdk + "\n</script>\n<script type=\"module\">", 1)
(here.parent / "voice-tutor.html").write_text(app)
site = here.parent / "site"; site.mkdir(exist_ok=True)
(site / "index.html").write_text(app)
for f in ["manifest.webmanifest", "sw.js", "icon-192.png", "icon-512.png"]:
    shutil.copy(here / f, site / f)
print("built", len(app))
