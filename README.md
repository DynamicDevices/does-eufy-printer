# eufyMake printer at DoES Liverpool

Simple notes for **anyone visiting [DoES Liverpool](https://doesliverpool.com/)** who wants to use the **[eufyMake](https://www.eufymake.com/) E1** — a desktop **UV inkjet** printer that can build **raised, full‑colour “3D texture”** on flat objects (and more with add‑ons you may not have on site).

You do **not** need a technical background. When something below says “software” or “file”, think “the app on the laptop” and “the thing you save before printing”.

**Loan and introductions:** **eufyMake** have **lent** this printer to **[DoES Liverpool](https://doesliverpool.com/) makerspace** for **one year**. DoES are **organising introduction and induction events** for people who want to try the printer or learn the basics — many sessions are **bookable on Eventbrite**. Example: **[Introduction to the eufyMake E1 UV texture printer](https://www.eventbrite.co.uk/e/introduction-to-the-eufymake-e1-uv-texture-printer-tickets-1988761821143)** *(search Eventbrite or ask DoES for other dates if that listing has passed).*

You can also check **[doesliverpool.com](https://doesliverpool.com/)** events and ask when you visit the space.

**Events and running costs:** The **introduction events are free** to book. Using the printer **afterwards is not free**: DoES ask people to **pay for usage** so **ink and other running costs** are covered. The **anticipated** charge is on the order of **about £1 per millilitre of ink** used — check with DoES for the **exact** rule when you visit, because pricing may be refined over time. In practice that **goes a long way**: **simple flat prints** (mostly a thin layer of ink) are usually **cheap**, while **textured / “3D texture” prints** cost **more** because the machine builds height with **many layers** of ink.

**Laptop, network, and apps at DoES:** In the makerspace there is a **laptop connected to this printer** that **you are welcome to use**. The printer is on the **DoES network**. eufyMake provides a **phone app** as well as **desktop software**; the **desktop application is more fully featured**, so for serious jobs or learning the full workflow it is better to use the **desktop app** (on the DoES laptop or your own machine) than the phone app alone.

---

## What this machine is (in plain language)

- **It is not a normal paper printer.** It jets **UV‑cured ink** onto things like plastic, wood, metal, ceramic, acrylic, and many other surfaces (always check the manufacturer’s guidance for your exact item).
- **It can print tall enough layers that you can feel the design** — embossing, brush‑stroke effects, textures. Marketing often calls this **“3D‑texture UV printing”**; the ink hardens under UV light.
- **Typical workflow:** prepare a design in **eufyMake’s software**, place your object on the bed, let the printer measure height where needed, then print.

Official overview and specs: [eufyMake E1 product page](https://www.eufymake.com/products/eufymake-e1).

---

## Example from DoES: Mandelbrot on a coaster

**Jackie Pease** ran this job on the DoES **eufyMake** printer: a **Mandelbrot set** (a famous mathematical fractal) on a **round coaster-sized disc**. The print shows **crisp edges** and **fine branching detail** around the black shape, on a **light grey** base — a good real-world sign that the machine can hold **high‑contrast artwork** and **intricate lines**.

![Mandelbrot fractal printed on a circular coaster at DoES Liverpool — print by Jackie Pease](assets/jackie-pease-mandelbrot-coaster.png)

*Photo: successful test print by Jackie Pease.  
If you want to try something similar, the repo includes an optional script (`scripts/generate_mandelbrot_heightmap.py`) that can produce a **greyscale height map** for texture-style workflows — most people will prepare art directly in **eufyMake Studio** instead.*

---

## Before you touch the printer

1. **Talk to someone at DoES first**  
   Makerspace tools are usually **induction-led**. Don’t assume you can walk up and use the machine alone. **Book an introduction** where offered — DoES often list these on **[Eventbrite](https://www.eventbrite.co.uk/)** (e.g. [this eufyMake E1 intro session](https://www.eventbrite.co.uk/e/introduction-to-the-eufymake-e1-uv-texture-printer-tickets-1988761821143)); new listings may appear for later dates. Otherwise ask at a **maker evening / workshop** or during your visit **where the printer lives, whether it’s in use, and what the local rules are** (booking, materials, cleanup).

2. **Read the manufacturer’s safety notes on UV ink**  
   Ink and cleaning supplies need **sensible handling** (skin/eye contact, ventilation, storage). Start here:  
   [All About eufyMake UV Ink](https://www.eufymake.com/blogs/news/all-about-eufymake-uv-ink).

3. **Plan what you are printing on**  
   **Not every object is suitable** (size, shape, surface, how it sits on the bed). If you are unsure, ask at DoES *before* you commit time to a design.

---

## What to bring (or have ready)

- **An idea** — logo, photo, graphic, or something from eufyMake’s “Make It Real” style tools (see links below).
- **Your own laptop (optional)** — there is already a **laptop at DoES wired up to the printer** you can use; bring yours if you prefer to work in your own files or software setup.
- **The object you want to print on** — **clean**, **dry**, and **allowed under local and manufacturer guidance**.
- **Patience the first time** — first prints often teach you about bed alignment, height measurement, and ink use.

---

## Simple path from “idea” to “printed object”

These are **high‑level** steps; the on‑screen software changes over time, so treat the **official app and guides** as the source of truth.

| Step | You… |
|------|------|
| 1 | **Install or open** the current **eufyMake printer software** (often **eufyMake Studio** — from [eufymake.com](https://www.eufymake.com/) **Software / Support**). **At DoES** you can use the **desktop app on the space laptop** already connected to the machine; the **phone app** exists but **does less** than the desktop version. |
| 2 | **Create or import** your design. Many people start from a photo or artwork; the tools can help with **layers / texture height** and colour. |
| 3 | **Choose material / preset** that matches what you are printing on (or follow DoES’s local profile if one exists). |
| 4 | On the printer: **place the object** carefully, **clear the area** of loose items, and follow the **on‑printer / app prompts** (height scan, positioning, etc.). |
| 5 | **Print**, stay nearby especially for the **first layers**, and note any **cleanup** steps (waste, wipes, lids — follow local and manufacturer instructions). |
| 6 | **Ask for help** if the job looks wrong (smearing, wrong height, head strikes). Stopping early is cheaper than damaging the head. |

Intro‑level context from the manufacturer:  
[UV printing beginner’s guide (buying / concepts)](https://www.eufymake.com/blogs/buying-guides/how-to-choose-a-uv-printer).

---

## Software and learning resources (official)

| What | Link |
|------|------|
| Main site (product, software downloads, support) | [eufymake.com](https://www.eufymake.com/) |
| Mobile vs desktop | eufyMake offers a **phone app** and **desktop** software; the **desktop app is more fully featured** — use desktop (e.g. on the DoES laptop) for the full workflow. |
| Web “Make It Real” creative area (as linked from product pages) | [makeitreal-beta.eufymake.com](https://makeitreal-beta.eufymake.com/) |
| Blog / tutorials | [eufyMake blogs](https://www.eufymake.com/blogs/news) |
| Community (social) | [eufyMake Facebook group](https://www.facebook.com/groups/eufymakeuvprintere1) (linked from manufacturer site) |
| Manufacturer support email (from their FAQ) | `support@eufymake.com` |

If a link changes, start from **eufymake.com** and use their **Support** / **Software** menus.

---

## When something goes wrong

- **Pause or stop** if you hear odd noises, see the head drag, or smell anything unusual — then **get someone at DoES**.
- **Don’t open consumables** you don’t need, and **don’t guess** on cleaning fluids — wrong chemistry can wreck the machine.
- For **warranty / hardware faults**, you’ll need **whoever owns the machine** to contact **eufyMake support**; visitors usually can’t do that on someone else’s behalf.

---

## About this Git repository

This repo is mainly **documentation** for DoES visitors. It also contains an **optional technical extra**: a small Python script that generates a **greyscale height map** (for experiments where brightness is treated as height in other tools). Most people using the E1 will **never** need it; it’s kept for members who like that workflow.

- **Visitor guide:** this `README` (you’re reading it).
- **Optional script:** `scripts/generate_mandelbrot_heightmap.py` — see comments at the top of that file. Dependencies: `requirements.txt`.

Upstream Git remote (if you contribute changes): `git@github.com:DynamicDevices/does-eufy-printer.git`

**Licensing:** This repo is **dual-licensed**. **Code** (`scripts/`, `requirements.txt`) is under the **[MIT License](LICENSE-MIT)**. **Documentation and images** (e.g. this README, `assets/`) are under **[CC BY 4.0](LICENSE-CC-BY-4.0.txt)** — share and adapt if you give appropriate credit (see `LICENSE` for the split, and credit Jackie Pease for the sample photo as noted above).

---

*DoES organisers: if you have a **fixed location**, **booking link**, or **local induction doc**, add a short subsection under “Before you touch the printer” so visitors see one clear place for Liverpool-specific rules.*
