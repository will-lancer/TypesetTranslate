from pathlib import Path
import sys

from PIL import Image, ImageDraw


source = Path(sys.argv[1])
destination = Path(sys.argv[2])
destination.mkdir(parents=True, exist_ok=True)
pages = sorted(source.glob("page-*.png"))

columns = 3
rows = 4
cell_width = 520
cell_height = 390
pages_per_sheet = columns * rows

for sheet_index, offset in enumerate(
    range(0, len(pages), pages_per_sheet), start=1
):
    sheet = Image.new(
        "RGB", (cell_width * columns, cell_height * rows), "white"
    )
    draw = ImageDraw.Draw(sheet)
    for cell_index, page_path in enumerate(
        pages[offset : offset + pages_per_sheet]
    ):
        with Image.open(page_path) as page:
            width, height = page.size
            crop = page.crop((0, int(height * 0.53), width, height))
            crop.thumbnail((cell_width - 20, cell_height - 34))
            x = (cell_index % columns) * cell_width + 10
            y = (cell_index // columns) * cell_height + 28
            sheet.paste(crop.convert("RGB"), (x, y))
            draw.text(
                (x, 7 + (cell_index // columns) * cell_height),
                page_path.stem,
                fill="black",
            )
    sheet.save(destination / f"bottom-contact-{sheet_index}.png")
