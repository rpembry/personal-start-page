from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'bookmarks.json').read_text())
(root/'bookmarks.js').write_text('window.START_BOOKMARKS = '+json.dumps(data,ensure_ascii=True)+';\n')
