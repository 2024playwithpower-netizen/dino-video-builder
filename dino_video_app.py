import streamlit as st
from datetime import date

st.set_page_config(page_title="Daily Dinosaur Video Engine", layout="centered")

st.title("Daily Dinosaur Video Engine")
st.caption("Yesterday’s Sketchbook — 25s videos")

DINOSAURS = [
    "Spinosaurus", "Allosaurus", "Giganotosaurus",
    "Baryonyx", "Suchomimus", "Carnotaurus",
    "Therizinosaurus", "Utahraptor", "Dilophosaurus",
    "Acrocanthosaurus"
]

today = str(date.today())
index = hash(today) % len(DINOSAURS)
dino = DINOSAURS[index]

st.subheader("Today’s Dinosaur")
st.success(dino)

st.subheader("25s Narration")
narration = f"""
This dinosaur didn’t hunt on land alone.
It waited silently beneath the water.
{dino} was a giant predator of ancient rivers and swamps.
Its long, narrow jaws were built to catch massive fish, snapping shut with terrifying speed.
Unlike other giant dinosaurs, it could swim with powerful, steady strokes.
Where land met water, {dino} ruled alone — a predator unlike any other.
""".strip()

st.text_area("", narration, height=200)

st.subheader("Video Prompts")
prompts = f"""
0–5s: Dark prehistoric swamp, fog above still water, cinematic wide shot.
5–10s: {dino} partially submerged, crocodile-like snout breaking water.
10–15s: Close-up jaws snapping shut, fish scattering.
15–20s: {dino} swimming powerfully, sail cutting water.
20–25s: {dino} roaring at sunset, cinematic end.
""".strip()

st.text_area("", prompts, height=180)

st.subheader("Posting Bundle")
posting = f"""
Title: This Dinosaur Hunted From the Water

Description:
A dinosaur that ruled rivers, not land.
{dino} was built to hunt from the water.
Subscribe to Yesterday’s Sketchbook for cinematic dinosaur stories.

Pinned Comment:
Did you know {dino} could swim? YES or NO
""".strip()

st.text_area("", posting, height=220)

st.caption("Caption Color: #F2F2F2 | Stroke: #000000 | Highlight: #FFC857")
