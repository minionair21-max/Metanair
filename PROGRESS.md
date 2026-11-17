# PROGRESS — Metanair

## Stand op 7 nov 2026
**Klaar**
- Analyse: 9 interviews (Minionair, Multionair, Studio, Chroma, Check, Veld, Web, Atelier, Spark), groepschats, Notion, /workspace-inventaris.
- Voorstel v1.0 → onafhankelijke review → v1.1 na red-team-onderzoek; ingekort na Cems bijsturing (PoC eerst).
- principes v1.1, go-register, venture-sjabloon, Stem van Cem (Notion-deel + 260 ruwe berichten).
- Overstap 6 nov 21:54: bots gepauzeerd, locks gearchiveerd, toezicht dagelijks 20:11.

**Open**
1. Cem beslist over eerste venture **C3 Vaksjablonen** (calculatieblad hoveniers, €19, €50 budget, 28 dagen). Start pas als Cem zelf een GO-regel in het go-register zet.
2. Na GO: lead + scout benoemen, venture-pagina's volgens sjabloon, eerste toezichtrun beoordelen.
3. Stem van Cem — ruw: Claude-berichten zijn gemarkeerd (zie log). Nog te doen: kernpunten samenvatten in `bronnen/stem_van_cem.md`. Cem: bevestigen of het laatste bericht (6 nov 21:54, "Correctie op punt 4") ook van Claude is.
4. Bekend knelpunt: computer-use op de Mac blokkeert als het scherm vergrendelt; toegang verloopt na 30 min.

## Log
- 2026-11-07 — Overdracht vanuit cloud-sessie naar Claude Code.
- 2026-11-07 — Overdracht in git gezet. In `bronnen/stem_van_cem_ruw.txt` een wachtwoord, IBAN en inlogcode verwijderd (regel 4: niets opslaan). 5 berichten gemarkeerd als Claude via Cems account (niet 4 zoals eerder geteld). Volgt: kernpunten Stem van Cem samenvatten; wachten op Cems GO voor C3.
- 2026-11-07 — Elephant-Goldfish-review op de inrichting: ontwerp uitgeschreven (`ontwerp/inrichting-minionair-2.0.md`), 3 verse reviewers, triage in `ontwerp/goudvis-review-2026-11-07.md`. Kern: niemand is eigenaar van de verkoop; Claude via Cems account; toezicht faalt stil; 28-dagenklok en €30-regel lek. Volgt: 3 beslissingen aan Cem voorleggen; toezichtstatus-pagina en sjabloon v0.2 voorstellen.
- 2026-11-10 — Review gecorrigeerd: was gebaseerd op een verouderde kopie van de principes (Notion v1.1 loste D en G al op). Token, IBAN, wachtwoord en inlogcode verwijderd uit Notion en git (de token staat nog in eerdere git-commits; force-push vraagt Cems toestemming). Kaarten t54 (eigen afzender) en t55 (klok, poorten, noodstop) toegevoegd; C3-kaart t53 aangevuld met presale. Toezichtstaak uitgebreid met gemiste run, omzetvraag en geheimen. Volgt: Cems besluiten in de cockpit verwerken.
- 2026-11-11 — Cems akkoorden van 10 nov (C3, eigen afzender, venture-klok) verwerkt: instructiepagina 'Eigen afzender Metanair' en 'Zondagreview 15 nov — voorstel principes v1.2' in het werkplan; kaarten 53–55 op Klaar met bewijs; actiekaarten 56 (C3-regel in go-register plakken) en 57 (Metanair-chat aanmaken). C3 staat nog niet in het go-register, dus nog niet gestart. Volgt: na kaart 56 lead en scout benoemen en de vijf venture-pagina's maken; na kaart 57 het afzenderbericht sturen.
- 2026-11-15 — Cem vroeg het Grok Bot-team een nieuwe onderneming te laten uitwerken. Kaart 58 klaargezet: go-registerregel 'Voorstel venture 2' (alleen op papier, einde 22 nov) + bericht dat Cem zelf aan Minionair stuurt. Ik heb geen toegang tot Grok Bot vanuit deze sessie. Volgt: voorstel beoordelen zodra Minionair 'klaar' meldt.
- 2026-11-15 — Cem: go-register via Notion werkt niet voor hem; hij beslist alleen in de chat (hier of in Grok). Principes (kop + principe 2) en go-register-kop aangepast: Metanair/lead noteert Cems woorden met datum. CLAUDE.md regel 2 aangepast. Een andere Metanair-sessie zette om 20:24 al 'Venture 2 — fase A' op GO; geen dubbele regel toegevoegd. C3 niet op GO gezet (wacht op Cems woord). Uitbreiding toezichtstaak geweigerd door de permissiecontrole; toezicht controleert nog volgens de oude regel. Kaarten 56–58 vervallen.
- 2026-11-15 — Bypass permissions kan niet in cloud-sessies; besturing van de Mac vraagt altijd goedkeuring per app. Op woord van Cem het voorstel doorgevoerd: Notion-pagina 'Opdrachten van Metanair' onder Grok Bot Minionair (opdracht #1 = leesbevestiging). Volgt: Cem plakt eenmalig het startbericht in de Grok-chat; daarna antwoord op #1 controleren.
- 2026-11-17 — Cem wil klantgesprekken (iPhone) laten uittypen. Omgeving 'Metanair' gemaakt (Hugging Face toegestaan) met setupscript dat Whisper installeert in /opt/whisper; script `tools/transcribe.py` (Nederlands, medium-model, lokaal). Getest met een testtoon, nog niet met echte Nederlandse spraak. Volgt: eerste echte opname uittypen en format klantsamenvatting maken.
