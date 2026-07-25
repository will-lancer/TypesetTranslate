from pathlib import Path
import sys

from PIL import Image


source = Path(sys.argv[1])

for path in sorted(source.glob("page-*.png")):
    with Image.open(path) as image:
        gray = image.convert("L")
        width, height = gray.size
        hits = []
        for y in range(height // 2, height - 40):
            longest = run = 0
            for x in range(20, width // 2):
                if gray.getpixel((x, y)) < 210:
                    run += 1
                    longest = max(longest, run)
                else:
                    run = 0
            if longest >= 35:
                hits.append((y, longest))
        if hits:
            print(path.name, hits[:8])
