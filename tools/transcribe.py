"""Gespreksopname (m4a/mp3/wav) -> Nederlands transcript met tijdstempels.
Gebruik: python tools/transcribe.py <audiobestand> [model]   (model: small | medium; standaard medium)
Draait lokaal met Whisper (faster-whisper); de audio gaat nergens anders heen."""
import sys, time
from faster_whisper import WhisperModel

audio = sys.argv[1]
model = WhisperModel(sys.argv[2] if len(sys.argv) > 2 else "medium", device="cpu", compute_type="int8")
t = time.time()
segments, info = model.transcribe(audio, language="nl", vad_filter=True)
for s in segments:
    print(f"[{int(s.start // 60):02d}:{int(s.start % 60):02d}] {s.text.strip()}", flush=True)
print(f"# duur {info.duration / 60:.1f} min, rekentijd {(time.time() - t) / 60:.1f} min", file=sys.stderr)
