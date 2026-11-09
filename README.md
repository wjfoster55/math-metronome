# Math Metronome

A mathematical rhythm playground built for Will: stacked cycles, grouping patterns
(e.g. 15/16 as 4+4+4+3), Euclidean spreads, polyrhythms, and forward / reversed /
both-together (crab) playback of the same rhythm math.

- One big Play button, presets that load instantly — built so the user mostly *listens*.
- Patterns save on the device, and export as a short code (also carried in the page URL
  after `#`) so Muse can hand the user a ready-loaded pattern by link, and the user can
  hand patterns back to Muse as codes.
- Plain static page served by a tiny Python server (`server.py`, uses `$PORT`).

Run locally: `python3 server.py` then open http://localhost:8080
