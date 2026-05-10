#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""
Optional extra (not required to use the eufyMake printer):

Greyscale Mandelbrot height map for workflows that treat brightness as height
(e.g. some relief / texture experiments). Convention here: white = zero height,
black = full height. See repo README for visitor-focused printer guidance.

Dependencies: pip install -r requirements.txt (from repository root).

Licensed under the MIT License; see LICENSE-MIT in the repository root.
"""

import argparse
import numpy as np
from PIL import Image

# Print resolution (embedded in PNG; width/height pixels = PHYSICAL_IN × PRINT_DPI)
PRINT_DPI = 1440
# Square output side length [in]; e.g. 5.0 → 7200 px at 1440 dpi (reasonable render cost).
PHYSICAL_IN = 5.0
WIDTH = int(round(PHYSICAL_IN * PRINT_DPI))
HEIGHT = WIDTH

# Image & view (classic full set with margin)
XMIN, XMAX = -2.35, 1.05
YMIN, YMAX = -1.35, 1.35
MAX_ITER = 800
SUPERSAMPLE = 1  # set 2 for 2x internal resolution then downscale (smoother)


def mandelbrot_smooth(h: int, w: int) -> np.ndarray:
    y = np.linspace(YMIN, YMAX, h, dtype=np.float64)
    x = np.linspace(XMIN, XMAX, w, dtype=np.float64)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y

    z = np.zeros_like(C)
    div = np.full(C.shape, False, dtype=bool)
    smooth = np.full(C.shape, np.float64(MAX_ITER))

    for i in range(MAX_ITER):
        mask = ~div
        if not np.any(mask):
            break
        z[mask] = z[mask] * z[mask] + C[mask]
        escaped = np.abs(z) > 2.0
        new = escaped & ~div
        div |= escaped
        # Normalized iteration count (smooth)
        if np.any(new):
            sm = i + 1.0 - np.log(np.log(np.abs(z[new]) + 1e-15)) / np.log(2.0)
            smooth[new] = sm

    # Interior: still not diverged -> full depth (black in output)
    smooth[~div] = np.float64(MAX_ITER)

    interior = ~div
    return smooth.astype(np.float64), interior


def smooth_to_grey(
    smooth: np.ndarray,
    interior: np.ndarray,
    p_low: float = 2.0,
    p_high: float = 99.6,
    gamma: float = 0.88,
) -> np.ndarray:
    """Map smooth iteration to grey: far outside -> white; near boundary -> dark greys; interior -> black.

    Uses log1p(smooth) for *escaped* points: almost all exterior pixels escape in a handful of iterations
    (median ~3), so linear smooth/MAX_ITER stacks ~80% of pixels in 250–254 and looks binary.
    """
    L = np.log1p(np.maximum(smooth, 0.0))
    exterior = ~interior
    le = L[exterior]
    lo = float(np.percentile(le, p_low))
    hi = float(np.percentile(le, p_high))
    span = max(hi - lo, 1e-9)
    t = (np.clip(L, lo, hi) - lo) / span
    if gamma != 1.0:
        t = np.power(t, gamma)
    grey = np.empty_like(smooth, dtype=np.float64)
    grey[exterior] = (1.0 - t[exterior]) * 255.0
    grey[interior] = 0.0
    return np.round(np.clip(grey, 0.0, 255.0)).astype(np.uint8)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Mandelbrot greyscale height map PNG (optional tool; not needed for E1 printing)."
    )
    parser.add_argument(
        "-o",
        "--output",
        default="mandelbrot_heightmap.png",
        help="Output PNG path (default: mandelbrot_heightmap.png next to cwd)",
    )
    args = parser.parse_args()

    if SUPERSAMPLE > 1:
        h, w = HEIGHT * SUPERSAMPLE, WIDTH * SUPERSAMPLE
        sm, inside = mandelbrot_smooth(h, w)
        g = smooth_to_grey(sm, inside)
        img = Image.fromarray(g, mode="L")
        img = img.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    else:
        sm, inside = mandelbrot_smooth(HEIGHT, WIDTH)
        g = smooth_to_grey(sm, inside)
        img = Image.fromarray(g, mode="L")

    img.save(args.output, dpi=(PRINT_DPI, PRINT_DPI))
    print(args.output, img.size, f"{PRINT_DPI} dpi ~{PHYSICAL_IN:g} inch side")


if __name__ == "__main__":
    main()
