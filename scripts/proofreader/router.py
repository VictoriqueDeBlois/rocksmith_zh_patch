"""Local routing. Priority: SKIP, C, E, D, B, F, A, G."""
import re

from scripts.localization import PLACEHOLDER_RE

# Extend the shared expression without changing existing translation tools.
TOKENS = re.compile(PLACEHOLDER_RE.pattern + r"|\{\d+\}")
CATEGORIES = tuple("ABCDEFG")

def words(pattern, text):
    return bool(re.search(r"\b(?:" + pattern + r")\b", text, re.I))

def route(source, translation=""):
    text = TOKENS.sub("", source).strip()
    if not re.search(r"[A-Za-z]", text):
        return "SKIP"
    if re.fullmatch(r"\d+\s*[xX]\s*\d+|[A-G][#♯b♭]?(?:m|maj|min|dim|aug|sus|add)?\d*(?:/[A-G][#b]?)?", text, re.I):
        return "SKIP"
    if re.fullmatch(r"[A-Z]{2,}[-]?\d+[A-Z\d-]*", text) or re.fullmatch(r"(?:MARSHALL|ORANGE|VOX|FENDER)\s+[A-Z]+[-]?\d+[A-Z\d-]*", text):
        return "SKIP"
    if re.fullmatch(r"(?:Rocksmith(?: 2014)?|Ubisoft|Steam|PSN|Xbox LIVE|PlayStation|Real Tone Cable)[®™]?", text, re.I):
        return "SKIP"
    if re.match(r"^(?:Epiphone|Gibson|Fender|Ibanez|Gretsch)[®™]\s*", text) and len(text) < 80 and not words(r"with|is|has|features", text):
        return "SKIP"
    teaching = words(r"practice|technique|picking|let's|finger|fretting|tremolo|harmonics?|intonated|capo|strumming|bend|fretboard|strings?", text)
    system_storage = words(r"HDD|disk space|storage|save data", text)
    if not system_storage and (words(r"score|at least|in a single game|for a single game|collect|destroy|destroyed|streak|achievement", text)
            or re.match(r"^(?:Beat|Win|Reach|Earn|Steal|Shoot|Jump|Leap|Survive|Level Up|Successfully hit)\b", text, re.I)
            or (not teaching and (words(r"in a row", text) or re.search(r"超过|连续|一局内", translation)))):
        return "C"
    if words(r"chord tone|electronic tuner", text):
        return "B"
    if words(r"cabs?|cabinet|box|amps?|amplifier|combo|tone|pedal|fuzz|overdrive|wah|drive|electronic|pad|speaker driver|session drums|preset|head|open-back|chorus effect|delay|pickup|\d+x\d+|voiced for|pitch-shift|vibrato effect|flanger|limiter", text):
        return "E"
    if words(r"Xbox|PSN|PlayStation|LIVE|matchmaking|host|party|profiles?|online|multiplayer|group leader|network|NAT|WLAN|Ethernet", text) or (not teaching and words(r"match|sessions?", text) and not words(r"session mode|in a session|session blue", text)):
        return "D"
    if (teaching or words(r"slides?|bends?|frets?|fretboard|strings?|chords?|pick|picking|mute|muting|palm|techniques?|arpeggio|slap|pop|scales?|downbeat|upbeat|Phrygian|session mode", text) or re.search(r"指法|按弦|扫弦|拨弦|推弦|滑音", translation)) and not words(r"selected item|center circle", text):
        return "B"
    if len(text) > 20 and words(r"title|menu|continue|exit|error|load|loading|save|saving|settings|select|selected|press|failed|unable|subtitles|volume", text):
        return "F"
    if len(text) <= 20:
        return "A"
    return "G"
