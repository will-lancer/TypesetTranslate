from pathlib import Path

from PIL import Image, ImageDraw


root = Path(__file__).parent / "final-render"
pages = sorted(root.glob("page-*.png"))
thumb_size = (280, 396)
cell_size = (300, 430)

for sheet_index, offset in enumerate(range(0, len(pages), 16), start=1):
    sheet = Image.new("RGB", (cell_size[0] * 4, cell_size[1] * 4), "white")
    draw = ImageDraw.Draw(sheet)
    for cell_index, page_path in enumerate(pages[offset : offset + 16]):
        with Image.open(page_path) as page:
            page.thumbnail(thumb_size)
            x = (cell_index % 4) * cell_size[0] + 10
            y = (cell_index // 4) * cell_size[1] + 24
            sheet.paste(page.convert("RGB"), (x, y))
            draw.text((x, 5 + (cell_index // 4) * cell_size[1]), page_path.stem, fill="black")
    sheet.save(root / f"contact-{sheet_index}.png")
