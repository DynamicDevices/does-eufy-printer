# does-eufy-printer — Mandelbrot height map for relief / lithophane prints

Grayscale **Mandelbrot** image and generator for tooling that treats **brightness as height** on the build plate:

- **White (255)** → **minimum** height (“zero”).
- **Black (0)** → **maximum** full height depth.

PNG is **`L` mode** (true greyscale); embeds **resolution metadata** (`dpi`) for tooling that honours it.

Upstream repository: **`git@github.com:DynamicDevices/does-eufy-printer.git`**

---

## What’s in here

| Item | Purpose |
|------|---------|
| `scripts/generate_mandelbrot_heightmap.py` | Computes smooth escape‑time Mandelbrot, tones to greyscale, saves PNG. |
| `mandelbrot_heightmap.png` | Checked‑in artefact (~5″ × 5″ nominal at **1440 dpi** embedded in PNG). |

---

## Design history (working notes)

The following summarizes the iterative requirements and fixes from the authoring session:

1. **Goal** — A **greyscale height map** (not discrete steps) derived from grey level for **FDM lithophane / displacement** workflows: printable texture height proportional to inverse brightness (lighter = thinner / lower).
2. **Subject** — **Mandelbrot set**, smooth/normalized escape time colouring.
3. **First tonal issue** — Mapping `smooth_iteration / MAX_ITER` made nearly all **exterior** pixels land in grey **249–254** (~78% by area) because median escape‑time depth outside the set is only a handful of iterations while `MAX_ITER` was hundreds. Visually **black-and-white**, unusable as a smooth ramp.
4. **Fix** — Exterior tonemapping switched to **`log1p(smooth_iteration)`** with **percentile stretching** (`p_low` / `p_high`) plus light **gamma**. **Interior** of the set is forced to **`grey = 0` (full height plateau)** separately from halo pixels.
5. **Print resolution** — Output embedded at **`PRINT_DPI = 1440`**, with **`WIDTH` / `HEIGHT` = `PHYSICAL_IN × PRINT_DPI`** (default **5 in** ⇒ **7200×7200** — long render).
6. **Physical interpretation sanity check** — Interior is intentionally a **flat maximum‑height plateau**; fine relief is primarily in the **outside** halo plus rare very dark escaped filaments (~full height ridges). Typical slicers need **invert** if they assume white = tallest.
7. **Repo split** — This tree was peeled out of **`vixdt`** so only Mandelbrot/print artefacts live here; product firmware layers stay elsewhere.

---

## Behaviour (how height maps mentally)

Roughly, for **escaped** pixels:

`log1p(smooth_escape)` → clip to percentile window → gamma → **`grey = (1 − t)×255`** (near boundary ⇒ darker ⇒ **taller** when black = tall).

For **non‑escaped** (inside the Mandelbrot set):

→ **`grey = 0`** (plateau).

---

## Dependencies

```text
numpy
pillow (PIL)
```

Example:

```bash
python3 -m pip install --user numpy pillow
```

---

## Regenerate PNG

Always run **from this directory** so outputs land beside the PNG:

```bash
cd /path/to/does-eufy-printer
python3 scripts/generate_mandelbrot_heightmap.py
```

Tune at top of **`generate_mandelbrot_heightmap.py`**:

- **`PRINT_DPI`** — DPI written into PNG (default **1440**).
- **`PHYSICAL_IN`** — nominal square side in inches (**pixels** = `PHYSICAL_IN × PRINT_DPI`).
- **`XMIN`/`XMAX`/`YMIN`/`YMAX`** — viewport in the complex plane.
- **`MAX_ITER`** — quality vs speed.
- **`p_low`, `p_high`, `gamma`** — halo stretch and contrast.
- **`SUPERSAMPLE`** — `2` oversamples internally then **Lanczos** down‑scales (smoother, slower).

Renders can take **minutes** at multi‑megapixel sizes.

---

## Git remote (`origin`)

Canonical **DynamicDevices** remote (configured as **`origin`** in local checkouts):

```text
git@github.com:DynamicDevices/does-eufy-printer.git
```
