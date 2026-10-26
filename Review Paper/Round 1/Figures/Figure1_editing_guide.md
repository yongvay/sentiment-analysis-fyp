# Editing Figure 1

The file `Figure1_compounding_chain.svg` is plain text. You do not need a graphics program to change the
wording — Notepad will do it.

---

## Route 1 — change the words (easiest)

Open the `.svg` in **Notepad** or **VS Code**. Every label looks like this:

```xml
<text class="n" x="108" y="48" text-anchor="middle">Linguistic structure</text>
```

Change only the part **between `>` and `</text>`**. Leave everything else alone.

### Where each label lives

| Line | What it is |
|---|---|
| 17 | Box 1 title — Linguistic structure |
| 18–20 | Box 1 body, three lines |
| 23 | Box 2 title — Systematic disagreement |
| 24–26 | Box 2 body |
| 29 | Box 3 title — Automation |
| 30–32 | Box 3 body |
| 35 | Box 4 title — Shared blind spot |
| 36–38 | Box 4 body |
| 41 | Box 5 title — Extreme class skew |
| 42–44 | Box 5 body |
| 47 | Box 6 title — Reliability hard to establish |
| 48–50 | Box 6 body |
| 59–64 | The link numbers 1 to 6 beside the arrows |
| 66–67 | The return-edge label, two lines |
| 69–73 | The italic note block on the left, five lines |

### Two rules

**SVG does not wrap text.** Each line is a separate `<text>` element. If you want a box to say something
longer, spread it across the three body lines that are already there — do not type a long sentence into one.

**Watch the width.** Boxes are 196 units wide. Roughly:

- Title line (bold, 12.5px): about **26 characters** before it overflows
- Body line (11px): about **30 characters**

If a title must be longer, do what line 47 already does and add `style="font-size:11.4px"` inside the tag.

---

## Route 2 — move things around

Use **Inkscape** (free, inkscape.org). Open the `.svg`, drag boxes, then File → Save.

Each box is a `<rect>` plus its `<text>` lines, and they are **not grouped**, so dragging a box in Inkscape
leaves its text behind. Select the rectangle and its text lines together before moving. If you move a box,
the arrow into it will not follow — arrows are the `<path class="ed">` lines and their coordinates are fixed.

Honestly, if the layout needs to change, it is faster to ask me to regenerate it.

---

## Route 3 — check your work

Drag the `.svg` onto a **Chrome or Edge** window. It renders immediately. Save the file, press F5, see the
change. No installation required.

---

## Putting it into Word

**Insert the SVG directly, not the PNG.** Word 2016 and later support it:

> Insert → Pictures → This Device → select `Figure1_compounding_chain.svg`

The figure stays vector, so it prints sharply at any size and survives the conference PDF conversion. The
PNG is a fallback for older Word versions or if a co-author's machine refuses the SVG.

Set the width to the full text column, roughly 14.6 cm in this template. The template requires a minimum
figure width of 6 cm, so there is plenty of headroom. Caption goes **6pt below** the figure, per template §7.

---

## If you edit the SVG, regenerate the PNG

Only needed if you are using the PNG rather than the SVG. Either:

- **Inkscape:** File → Export → PNG, set DPI to 300, Export
- **Ask me:** send the edited SVG back and I will re-render it

---

## The figure is greyscale-safe

Fills are `#f5f5f3` for the two entry boxes and `#e4e4e0` for the four cycle boxes. That difference is
deliberate — it marks which boxes form the closed loop — and it survives a black-and-white print. If you
change the fills, keep the two shades distinguishable in greyscale.
