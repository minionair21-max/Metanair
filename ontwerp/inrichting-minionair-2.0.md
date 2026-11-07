# Ontwerp — inrichting Minionair 2.0 (stand 7 nov 2026)
Geschreven door de olifant (Metanair) voor een review door goudvissen: dit document moet op zichzelf te begrijpen zijn.

## 1. Doel en kader
- Eigenaar: Cem, B2B-marketingstrateeg in Amsterdam. Heeft 1–2 uur per avond (19–22u), wil maximaal 3 beslissingen per avond nemen, denkt visueel.
- Doel: autonoom laten draaiende ventures → proof of concept → samen ~€800 netto per maand.
- Stuur van Cem (6 nov): eerst een proof of concept. B2B, B2C, e-commerce en SaaS krijgen evenveel kans. Klein en wendbaar, geen bureaucratie of compliance vóór de eerste sales.
- Harde grenzen: geen producten op basis van persoonsgegevens van particulieren; nooit communiceren uit Cems naam; geen wachtwoorden, kaartgegevens of inlogcodes door agents laten invullen of opslaan.
- Budget voor AI-abonnementen: €150–300 per maand.

## 2. Waarom er een nieuwe inrichting is (de oude, okt–nov 2026)
- ~10 bots in Grok Bot op een Mac mini: Minionair (COO), Multionair (Acting CEO), acht operators (Studio, Check, Veld, Chroma, Atelier, Web, Spark, Kas), plus drie groepschats.
- Eén venture (SIX DIGITS, kleurproducten via print-on-demand). Resultaat na een maand: €0 omzet, ~€100 aan ads, 74 klikken en 0 keer in winkelwagen.
- Gevonden oorzaken: regels in ~527 losse lock-bestanden; "Cem is akkoord" doorgegeven door bots zonder register; vier bots en Claude voor één creatieve post; coördinatie optimaliseerde op activiteit in plaats van omzet; geen externe meetlat; geen evaluatiemoment; CEO/COO-lagen van hetzelfde model gaven geen echte controle.
- Overstap op 6 nov 21:54: Multionair en de acht operators gepauzeerd (niet gewist); locks gearchiveerd; SIX DIGITS op HOLD.

## 3. De nieuwe inrichting

### 3.1 Rollen
| Rol | Wie | Mag | Mag niet |
|---|---|---|---|
| Eigenaar | Cem | GO/HOLD/NEE zetten in het go-register; principes wijzigen (alleen bij de zondagreview); kill-criteria wijzigen | — |
| Architect en toezicht | Claude als "Metanair" (Claude Code, cloud-sessies, Notion-koppeling) | systeem ontwerpen, voorstellen doen, toezicht houden, berichten aan bots sturen die Cem goedkeurde of die binnen een bestaande GO vallen | principes of go-register wijzigen; ventures uitvoeren; wachtwoorden invullen |
| Lead (per venture) | één bot in Grok Bot | als enige schrijven in de venturebestanden; taken uitvoeren | extra bots inschakelen; geld ≥€30 zonder GO |
| Scout (per venture) | één bot in Grok Bot | lezen, onderzoeken, rapport aanleveren aan de lead | schrijven in venturebestanden |
| Dagelijks toezicht | geplande Claude-taak, elke dag 20:11 | controleren op regelafwijkingen, claims zonder bewijs, stilte en bewijs van voortgang | ingrijpen; alleen melden |

### 3.2 Bron van waarheid (Notion)
- **principes** (10 regels; zie bijlage A). Elke bot leest dit bij de start van elk werkblok.
- **go-register** (tabel: onderdeel, status, sinds, door, grens). Alleen Cem schrijft. Wat niet op GO staat, staat op HOLD. "Cem is akkoord" in een chat telt niet.
- **Per venture vijf bestanden** (venture-sjabloon): venture.md (wat, voor wie, prijs, kill-criteria, budget), taken.md (enige opdrachtlijst), trechter.md (één regel per week: bezoekers → aanvragen → betaald), log.md (alleen de lead), lessen.md.
- Privé voor Metanair: werkplan en logboek, plus deze git-repo (CLAUDE.md, PROGRESS.md, bronnen/).
- "Stem van Cem": Cems eigen woorden en besluiten op datum, zodat bijsturing niet verloren gaat.

### 3.3 Ritme
- Lead start elk werkblok: principes → go-register → venture → taken. Werkt één taak af, schrijft log en taken bij.
- Elke dag 20:11 een toezichtsrun door Claude.
- Elke zondag een review met Cem: lessen lezen en eventueel de principes wijzigen.
- Cem ziet alles in een cockpit (een HTML-dashboard; de data staat in een losse database bij dat dashboard).

### 3.4 Geld en kill
- Venturekaart (Revolut), €50 per venture in fase 1, €200 in fase 2.
- Uitgaven onder €30 mogen met een logregel; vanaf €30 alleen met GO.
- Eerst de trechter, dan de euro: geen advertentiegeld zonder een pagina waarvan bewezen is dat hij werkt.
- Kill na 28 dagen zonder eerste betaling.

### 3.5 Huidige stand go-register
| Onderdeel | Status |
|---|---|
| SIX DIGITS (alles) | HOLD |
| Top-10 onderzoek (Multionair) | GO — alleen onderzoek (Multionair is wel gepauzeerd) |
| RPW-bewijspakket | NEE |
| Pion-wachtlijst | GO — alleen aanmelding |
| Nieuwe inrichting (Claude bouwt) | GO — per stap een kaart in de cockpit |

### 3.6 Eerste venture (voorstel, nog geen GO)
**C3 Vaksjablonen**: een calculatieblad voor hoveniers, €19, budget €50, 28 dagen. Start pas als Cem zelf een GO-regel zet. Daarna worden een lead en een scout benoemd en de vijf venture-pagina's aangemaakt.

## 4. Technische realiteit en bekende knelpunten
- Grok Bot draait op een Mac mini. Claude bereikt die via computer-use. Dat blokkeert als het scherm vergrendelt, en de toegang verloopt na 30 minuten.
- Notion staat op het gratis plan (beperkte queries).
- De bots hebben eigen geheugen (bijv. ~220 journal-items per bot), dat ongemeten blijft. Het geheugen is géén bron van waarheid.
- De oude cockpit-data staat in een artifact-database, los van Notion. Er zijn dus twee plekken met status.
- Claude stuurde berichten aan bots via Cems account in de hoofdchat. Daardoor ziet een bot die berichten als "van Cem".
- Elke Claude-sessie begint zonder geheugen. Continuïteit hangt af van CLAUDE.md, PROGRESS.md en Notion.

## 5. Ontwerpkeuzes die de olifant bewust maakte
1. Liever minimaal (één lead, één scout) dan een team: extra agents leveren vooral coördinatielast op.
2. Eén schrijver per venture om tegenstrijdige besluiten te voorkomen.
3. Een go bestaat alleen als regel in een register, niet in een gesprek.
4. Een externe meetlat (euro's, trechter) in plaats van activiteit.
5. Toezicht door een ander model (Claude) dan de uitvoerders (Grok Bot), om dezelfde blinde vlekken te vermijden.
6. Een vaste killdatum in plaats van een open evaluatie.

## Bijlage A — principes (v1, akkoord Cem 6 nov)
1. Doel: per venture eerst één betalende klant, dan pas groei. Succes = euro's, niet activiteit.
2. Bezetting per venture: precies één lead en één scout. Geen extra bots, geen CEO/COO-laag.
3. Eén schrijver: alleen de lead schrijft in de venturebestanden.
4. Go komt alleen van Cem, en staat alleen in het go-register.
5. Nieuwste besluit wint, met datum; het oude wordt doorgestreept.
6. Eerst de trechter, dan de euro.
7. Geld: <€30 mag met log; ≥€30 alleen met go. €50 (fase 1), €200 (fase 2).
8. Hold is hold: geen nieuwe taken, geen spend, niets wissen.
9. Nooit uit Cems naam communiceren; outreach via de eigen mailbox van de venture.
10. Taal: Nederlands naar Cem, kort.
