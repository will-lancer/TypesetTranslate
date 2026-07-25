from pathlib import Path
import sys

from PIL import Image, ImageDraw


source = Path(sys.argv[1])
destination = Path(sys.argv[2])
destination.mkdir(parents=True, exist_ok=True)
pages = sorted(source.glob("page-*.png"))

thumb_size = (240, 340)
cell_size = (260, 375)
pages_per_sheet = 15

for sheet_index, offset in enumerate(
    range(0, len(pages), pages_per_sheet), start=1
):
    sheet = Image.new(
        "RGB", (cell_size[0] * 5, cell_size[1] * 3), "white"
    )
    draw = ImageDraw.Draw(sheet)
    for cell_index, page_path in enumerate(
        pages[offset : offset + pages_per_sheet]
    ):
        with Image.open(page_path) as page:
            page.thumbnail(thumb_size)
            x = (cell_index % 5) * cell_size[0] + 10
            y = (cell_index // 5) * cell_size[1] + 24
            sheet.paste(page.convert("RGB"), (x, y))
            draw.text(
                (x, 5 + (cell_index // 5) * cell_size[1]),
                page_path.stem,
                fill="black",
            )
    sheet.save(destination / f"contact-{sheet_index}.png")
