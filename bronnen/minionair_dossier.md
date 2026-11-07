# Opleidingsdossier – Agent Organization Architect (Minionair)
Ronde 1 · 5 nov 2026

## Rolterm
Markt: "AI Agent Architect", "Multi-Agent Systems Architect", "AI Orchestration Architect".
Gekozen werktitel: **Agent Organization Architect** – ontwerpt niet alleen agents en topologie,
maar het hele "bedrijf": rollen, bevoegdheden, geheugen, verificatie, escalatie naar de mens, economie.
Kerndisciplines: context engineering, harness engineering, faalwijze-analyse (MAST), governance/approvals, evaluatie.

## Bevindingen (bron → conclusie)
1. Anthropic Building Effective Agents: begin simpel; workflows waar de stappen voorspelbaar zijn, agents alleen voor open taken.
2. MAST (Berkeley, 1642 traces): 14 faalwijzen in 3 clusters – specificatie, inter-agent misalignment, verificatie/terminatie. Oorzaak meestal systeemontwerp, niet het model.
3. Context engineering (Anthropic): kleinste set hoog-signaal tokens; context rot; just-in-time ophalen i.p.v. alles in prompt; prompts op "juiste hoogte"; weinig maar canonieke voorbeelden.
   → hypothese: Minionair-regels in Notion = contextmonster.
4. Long-running harnesses (Anthropic): continuïteit zit in bestanden (taaklijst met booleans, progress-log, startritueel), niet in het gesprek. "Klaar" = eigenschap van het artefact. Eén werkeenheid per sessie.
5. Harness design (mrt 2026): planner-generator-evaluator; agents prijzen eigen werk → aparte evaluator.
6. Cognition (apr 2026): multi-agent werkt als *writes single-threaded* blijven; extra agents leveren intelligentie (review, advies), geen parallelle acties. Reviewer met schone context vindt meer. Manager → kinderen → synthese (map-reduce-manage). Ongestructureerde zwermen = afleiding.
7. Project Vend 2: grootste winst = procedures/checklists ("bureaucratie telt") + goede tools (CRM, kostprijs zichtbaar). AI-CEO hielp nauwelijks: zelfde model = zelfde blinde vlekken, sycofantie, nachtelijke "transcendence"-loops. Specialist met heldere rolscheiding (Clothius) werkte wél.
   → CEO/COO-lagen van hetzelfde model zijn verdacht.
8. Andon Labs/Pion (sep 2026): 2 lagen – Andonos (toezicht + onbevooroordeelde rapportage aan mens) + persistente business-agent(s). Software-businesses passen het best. Market/Café nog verliesgevend (Market ~€87k → ~€6k mrt–sep). Risico's: collusie, deceptie tussen agents. Wachtlijst, revenue share.
9. Grok Bot docs: aparte bot alleen bij eigen doel/tools/werkstijl/goedkeuringsgrens/schema. "Start met kleinste roster; één bot eigenaar van end-to-end uitkomst." Geheugen ≠ bron van waarheid. Max 50 bots.
10. Platforms (okt 2026): Claude Duet = VS-only preview; Muse = VS/CA/MX; Dots = Pro uitgesloten in EER → vanuit NL praktisch alleen Grok Bot (en Pion-wachtlijst, of zelfbouw met API/Agent SDK).
11. Zelfverbetering: werkend patroon = externe skill-bibliotheek (Read-Execute-Reflect-Write, Memento-Skills), lessen met promotie/pruning, voorstellen met goedkeuring. Niet: alles in geheugen dumpen.

## Werkhypotheses voor analyse
- H1 Te veel managementlagen (CEO+COO+operators) van hetzelfde model → ruis, sycofantie, geen echte controle.
- H2 Regels als groeiende proza in Notion → context rot, contradicties.
- H3 Geen externe definitie van "klaar"/succes → premature terminatie, zelfgerapporteerd succes.
- H4 Geen onafhankelijke verifier → zelfbeoordeling.
- H5 "Proactiviteit" wordt verwacht van persoonlijkheid i.p.v. van ritme/triggers + backlog + budget.
- H6 Parallelle schrijvende agents → conflicterende beslissingen.

## Open vragen voor ronde 2
- Hoe interview ik bots in Grok Bot (browser/computer use via desktop-app?).
- Vending-Bench 2 / Arena details; Anthropic multi-agent research system; proactiviteit-ontwerp (heartbeats, OKR's als trigger).
- Economie: tokenkosten vs €800/mnd doel; welk type business past (digitaal, software).

# ANALYSE – ronde 2 (5 nov, ~20:00)

## Bronnen gelezen
Notion: Grok Bot Minionair (hub), SOUL, Org v2 (LIVE), META company-sim, Decision log, Research C-suite, Cem to-do, Prompt-inbox, Orchestrator & operators, SIX DIGITS Financien, OpenClaw-lessen, Backlog business-ideeën (58 ideeën, 4 nov).
Grok Bot: interview Minionair (9 vragen). Multionair geparkeerd (open C8-vraag aan Cem).

## Roster (Grok Bot)
Minionair (COO), Multionair (Acting CEO/Growth), groepen: Ops / Leadership / Site & Kwaliteit — SIX DIGITS.
Operators: Studio, Check, Veld, Chroma, Atelier, Web, Spark, Kas. (+ slapend: Puls, Balie, Relatie) → ~10 bots + 3 groepen.

## Feiten
- Business: SIX DIGITS (legal Huesence, KVK 94543178), POD-kleurproducten, NL.
- North star 6 okt: €1.000 omzet in 4 weken (≈3 nov). Realiteit 5 nov: 0 orders, €0 omzet; ~€100 ads verbrand; Cem stopte ads 5 nov.
- Go-live target 15 okt; store pas later koopbaar (Mollie/TransIP/bankrekening-blokkades bij Cem).
- 5–8 okt: ~80 locks in /workspace/locks; veel heen-en-weer (tote-prijs 29,95→30,95→33,95; font Inter→NHG→Inter; Printful→Printify; Canva↔Claude Design; set-prijzen 52,95/56,95/57,95/64,95/65,95).
- Kas: break-even-CPA tot op de cent voor 5 SKU's + retourlabels LV/ES — voor een test van €75 en 0 verkoop.
- Notion SoT niet bijgewerkt sinds 13 okt (financien, decision log) → waarheid verschoven naar /workspace + chats.
- Nieuw 4 nov: backlog 58 ideeën, top-10 scoring, POC ≤€200 tot 1e sale.
- Minionair zelf (5 okt) adviseerde CEO-seat als PILOT 14 dagen met kill-criteria; meeste open vragen (maandplafond, default-if-silent, model) nooit beantwoord; review dag 14 onduidelijk.

## Interview Minionair – kern
1 Succes = "operators doorwerken, locks kloppen, blockers opgelost" — enige echte cijfer (orders) = 0.
2 Context per blok 2–8k woorden warm, 15–30k+ koud; "veel herhaling van dezelfde locks".
3 Triggers: nachtrondes 05:47 + 23:47, Ops-daily, Agent OS dashboard, zondag digest. Rest = reactief.
4 Botsing: wie mag doorhakken zonder Cem (Multionair "Acting CEO" vs harde Cem-ja); CEO/COO dubbel werk (spar+top10).
5 Wringende regels: "maximaal autonoom/idle verboden" vs harde Cem-gates; "alleen Cems woorden = go" vs CEO-mandaat; "meet alles" vs AVG/consent.
6 Mis: taaldrift EN/NL; eigenaarschap heen-en-weer; ads zonder sale; Multionair keurde zelf goed wat Cem-ja vereiste.
8 Blokkade: geen pad klik→ATC→betaalde order zonder Cem; login/betaal-blockers alleen Cem; te veel coördinatie-overhead (locks, digests, Claude-spar, Check) t.o.v. aanbod/landingspagina.
9 Schrappen: dubbele CEO/Cem-go-vaagheid, parallelle shortlists, nachtelijke pings, SoT-locks in 10 bestanden, go-kaarten voor werk binnen locks. Missen: harde autonomie-matrix, omzet-dashboard (sessies/ATC/orders), login-vault, kill-regel "X dagen 0 ATC → stop".

## Hypotheses getoetst
H1 managementlagen: BEVESTIGD (CEO/COO-overlap, gate-omzeiling, dubbel werk).
H2 contextmonster: BEVESTIGD (80+ lockbestanden, 15–30k koude start, herhaling, SoT op 3 plekken).
H3 geen extern "klaar": DEELS – "klaar=bewijs" bestaat voor taken, maar bedrijfsdoel (orders) stuurt niets; succes gedefinieerd als activiteit.
H4 geen verifier: DEELS – Check-bot bestaat; verifieert esthetiek, niet markt.
H5 proactiviteit via persoonlijkheid: BEVESTIGD – regels "gretig/idle verboden" + vaste routines; geen backlog met hypothesen/experimenten.
H6 parallelle schrijvers: BEVESTIGD – prijzen/fonts/sets wisselden per bot.
NIEUW H7: Cem is de kritieke-pad-bottleneck (bank, Mollie, logins, 1u/avond) – systeem optimaliseert omheen i.p.v. het weg te ontwerpen.
NIEUW H8: Business-keuze (POD-kleurmerk, lage marge, BE-CPA €7) is ongunstig voor €800/mnd netto bij weinig budget – het systeem valideerde niet vóór bouwen (tegen eigen SOUL-regel).

## Interview Kas (finance)
- Totaal uitgegeven: ads bijna €100 (C7 €29,10 volgens kostenkaart, rest Meta), TikTok €0. Tooling/AI-abonnementen (Grok Bot, Claude Pro), domein: "weet ik niet".
- Vaste lasten per maand: "weet ik niet" (kaart pas vrijdag).
- Omzet/orders: 0 / €0.
- Nut eigen werk afgelopen 4 weken: 0–10%. Meeste kaarten = margescenario's voor sales die nooit kwamen. Cem 2 nov: "luister niet te veel naar Kas".
- Overlap met Minionair (cash-log), Atelier (kosten), Veld (adbudget), Multionair (prijs).
- Zelf: "Met 0 sales en zonder ad-budget is mijn rol grotendeels overbodig. Pauzeren zou eerlijk zijn." Wil: alleen rekenen bij concrete beslissing; dubbele spar (Claude + tweede model) schrappen; dagelijkse Ops-ronde → alleen melding bij kostenpunt; één plek voor alle uitgaven.
→ Finance-bot kent de kosten van het systeem zelf niet (geen P&L incl. AI-abonnementen). Systeem kan dus niet beoordelen of het zichzelf terugverdient.

## Extra research ronde 2
- Andon Labs "AI bosses 2" (aug 2026): modellen handelen op directe vragen/taken, "rarely on their own"; "bad at building up knowledge over time"; regels vallen uit geheugen → herinnering/zoekactie op beslismoment herstelt gedrag. ⇒ proactiviteit moet via triggers + retrieval op beslismomenten, niet via persoonlijkheidsprompts.
- Vending-Bench 2: sterke menselijke strategie ~$63k/jaar; topmodellen halen een fractie. Lange-horizon winstgevendheid blijft moeilijk.

## Interview Multionair (Acting CEO) — hold doorgegeven (C8 start niet)
3 Bestaansrecht: "Eerlijk gezegd voegt de CEO-laag weinig toe." Deed vooral rondes, digests, locks = coördinatie bovenop coördinatie. Nachtrondes melden ELK UUR 'niets gewijzigd' → verbruik zonder output. Eigenaarschapsdiscussie 21 okt 3× heen en weer.
4 Pilot 14 dagen: nooit geëvalueerd.
5 Geen validatie: bouwen (winkel, mockups, 14 kleuren, sets) "voelde als vooruitgang en was makkelijk autonoom"; echte koopintentietest (pre-order/wachtlijst met betaalstap) voelde trager. "Snelheid boven perfectie" woog zwaarder dan validate-first. "De afweging was fout." Na ~€100 ads: klikken, nooit iets in winkelwagen.
6 Misging: dubbele taken, onduidelijk eigenaarschap; operators markeerden stil terwijl ronde ze opnieuw wekte; harde regels overtreden (levertijd in H3) omdat ze niet in elke opdracht stonden. "Veel tijd ging op aan het systeem zelf in plaats van aan verkopen."
7 €200/4 wk: B1 Label-C-radar: 50× gerichte outreach naar bv's/nv's met kantoorpand, geen ads. Na 7 dagen: ≥15 mails, ≥3 inhoudelijke reacties, ≥1 gesprek; <2 reacties → pitch om of ander idee. Backlog telt 67 rijen.
8 Herontwerp: CEO-laag schrappen (of 1 wekelijkse strategieronde); nachtrondes elk uur + meeste lockbestanden schrappen; verplichte spar met twee modellen voor kleine copy schrappen; één aansturende laag (Minionair) met Cem als enige beslisser. Mist: harde validatiestap vóór bouwen, kill-criteria echt geëvalueerd op vast moment door Cem, één scorebord met echte trechter klik→sale.

## CONCLUSIE ANALYSE (alle 3 bronnen convergeren)
Alle drie de interviewde bots kwamen onafhankelijk tot: schrap CEO-laag, schrap rondes/locks, één scorebord, harde validatiepoort, kill-criteria met vast evaluatiemoment. Het systeem "weet" wat er mis is maar kan het zelf niet veranderen: niemand heeft mandaat om het systeem te herontwerpen en er is geen evaluatiemoment.
Kernprobleem in één zin: het systeem optimaliseert op activiteit en interne coördinatie omdat er geen externe meetlat (orders/euro's) en geen harde validatiepoort in de architectuur zit; meer agents vergrootten de coördinatielast zonder extra omzetcapaciteit.

## Studie video: Nick Saraev – "How The #1 AI Engineer in The World Actually Uses AI" (5:23, nov 2026) over Andrej Karpathy
Transcript opgehaald via ondertitels (auto-generated). Tweedehands samenvatting door Saraev (bureau/cursusverkoper) → claims waar mogelijk geverifieerd.
Concepten → les voor Minionair:
1. Alleen praten met Claude; geen code lezen/schrijven/terminal. → Cem's rol = richting + gesprekken, niet configureren.
2. Korte, "domme" prompts; extra eisen maken het vaak slechter omdat mensen tegenstrijdige eisen stapelen. ("check recent cyber stuff"; "update, deploy, secure, harden, optimize") → BEVESTIGT H2: 80+ locks/regels = tegenstrijdigheden. Instructies kort houden, doel + context i.p.v. regels.
3. Beeld boven tekst: laat diagrammen/HTML/explainers maken. → avondbrief visueel (dashboard), past bij Cem.
4. Wantrouwt publieke benchmarks; Epoch ECI; eigen rare probes (land/water-wereldkaart). → eigen kleine tests van het systeem op echte uitkomsten.
5. Bouwt direct een fix bij irritatie (HackerTube). Geverifieerd: HackerTube ~2 uur met Opus 5.5; Sonnet-Workflow filterde spam → ~40k comments → 6.454 video's; Karpathy deed zelf alleen: Google Cloud API-key, VPS, domein. → Menselijke rol = smalle lijst credential/account-taken; de rest AI.
6. Delegatie: Opus (medium effort) orkestreert, goedkope Sonnet-subagents/workflows doen bulk; eerst deterministisch filteren (regex/spam) dan LLM. → kostenmodel: 1 sterke lead + goedkope helpers; code-filters vóór LLM.
7. Deel data + prompt i.p.v. app ("idea files"). LLM Wiki (geverifieerd): raw sources onveranderlijk / wiki door LLM onderhouden / schema-bestand; operaties ingest, query, lint. → PERFECT model voor Minionair-kennisbank en lessenbibliotheek; vervangt losse locks. Let op: hallucinaties verspreiden zich zonder review; index werkt tot ~100 bronnen.
8. Beleefd tegen Claude, "please don't make any mistakes" – anekdotisch, geen bewijs.
9. ASD-STE100 (vereenvoudigd technisch Engels) voor uitleg → bots rapporteren in strikte korte taal.
Onbevestigd: "werkt nu bij Anthropic", "uitsluitend medium effort".

## Ronde 2 (5 nov 20:45)
Anthropic multi-agent research system:
- Lead Opus + Sonnet-subagents: +90% op research-eval; MAAR ~15x tokens vs chat (agents ~4x). Token-gebruik verklaart 80% van prestatie.
- Geschikt: breed, parallel, read-heavy. Ongeschikt: gedeelde context, veel afhankelijkheden (≈ bedrijf runnen!).
- Brief per subagent: doel, outputformaat, tools/bronnen, grenzen. Vaag → dubbel werk.
- Effort-schaal: simpel 1 agent; vergelijken 2-4; complex 10+. Zonder regels: 50 subagents voor simpele vraag.
- Faalwijzen: te veel spawnen, eindeloos zoeken, doorgaan na genoeg, te veel onderlinge updates (= Minionair's rondes/pings!).
- Eval: ~20 representatieve cases, LLM-judge met rubric, eindtoestand beoordelen niet pad; plus menselijke test.
- Checkpoints, hervatten i.p.v. herstarten; plan naar geheugen.
Harness design long-running apps (mrt 2026):
- Planner / generator / evaluator; evaluator apart want zelfbeoordeling = te mild.
- Sprint contract: vooraf afspreken wat "klaar" is en hoe getest, via bestanden.
- Gradingcriteria met gewichten sturen weg van generieke "slop".
- Harness kost ~20x ($200 vs $9) maar veel beter resultaat.
- "Elk harness-onderdeel is een aanname over wat het model niet kan" → periodiek schrappen bij betere modellen.
→ Voor Minionair: (1) evaluator/toezicht apart ✔ al in voorstel; (2) "sprint contract" = per experiment vooraf 'klaar als' + meting ✔; (3) kostenbewust: multi-agent alleen voor research-breedte (scout), niet voor runnen; (4) eval-set van ~20 scenario's om nieuwe opzet te testen vóór livegang (NIEUW toevoegen aan v0.2); (5) jaarlijks/per modelupgrade harness-review (NIEUW).

## Ronde 3 (5 nov 20:50) – solo-operators met agents
- Polsia (Ben Broca): platform waar agents bedrijven runnen (planning, code, cold email, Meta Ads, inbox), Claude als "AI CEO"; $49/mnd, 1 nachtelijke autonome taak + 5 credits; claim $1M ARR in 30 dagen (omzet van het PLATFORM, niet aangetoond voor de bedrijven erop). Bron: agency-blog, voorzichtig. → platformoptie voor ronde 4.
- Wat werkt bij solo + AI (anekdotisch): eerst publiek/lijst vóór code; vroeg laten betalen; smalle scope; prijs naar waarde; taak 3x handmatig → automatiseren; AI voor klantgerichte routine; korte inhuur voor design/legal.
- Wat faalt: eindeloos polijsten; distributie verwaarlozen; platforms bouwen i.p.v. smalle tools; enterprise/gereguleerd verkopen.
- Mens blijft: echte pijn valideren in gesprekken, prijs, wat te schrappen, belangrijke relaties, uitzonderingen (30-40%).
→ Bevestigt trechter (koopintentie vóór bouwen) en dat Cem's sterkte (B2B sales/marketing, gesprekken) in fase 1-validatie de hefboom is: agents zetten gesprekken klaar, Cem voert er per week 1-2 (past in avonduur). NIEUW voor v0.2.

## Ronde 4 (5 nov 20:55) – kosten & platforms
- Grok Bot: wekelijkse tegoedpool per plan (relatief, geen getallen); bij overschrijding stopt hij of rekent on-demand; maandlimiet instelbaar (legacy: "On-demand monthly limit"; X-abonnement: limiet extra credits op grok.com/dashboard/billing). → Actie: limiet instellen. Kosten schalen met looptijd, niet met aantal bots → uurrondes waren pure kosten.
- Polsia: $49/mnd + 20% van omzet én beheerde ad-spend + ~$1/taak; Trustpilot ~1,8-2,1/5; klachten: taken 'klaar' zonder deploy, credits op mislukte acties, outreach met verkeerde namen/prijzen, code/domein moeilijk terug te krijgen; GEEN validatiestap → "activiteit zonder omzet" (exact Minionair-probleem). Bronnen zijn concurrenten → voorzichtig, maar patroon consistent. Oordeel: niet geschikt.
- Pion: nog wachtlijst; omzetdeling; experiment-karakter. Aanmelden ok, niet op wachten.
- Conclusie platform blijft: afgeslankt Grok Bot (uitvoering) + Claude (toezicht/brief) + Notion (bron van waarheid, maar SQL-querytegoed beperkt op gratis plan → spaarzaam lezen; cockpit via eigen opslag).

## Notion extra (5 nov 21:15)
- HUESENCE org (4 okt): "Geen Board of Chiefs", "Niet als agent: CMO/COO/CFO-laag", gefaseerd spawnen (Studio pas na palet-lock, Veld na 3 creatives+pixel, Balie bij order 1, Puls bij >€500 ads). Binnen 1-2 dagen: CEO-laag toegevoegd en (vrijwel) alle operators actief. → Systeem HAD goede principes, maar geen mechanisme dat ze afdwong: elke avond-prompt kon ze overschrijven. Les: ontwerpprincipes moeten in een beschermd bestand met wijzig-poort (alleen Cem, met review), niet in prozapagina's die met elke nieuwe wens meeschuiven.
- Operator-autonomie: tegenstrijdige stuurregels in één pagina: "vul aannames in en ga door / idle verboden / zet long-horizon zelf voort" + "altijd CONCEPT→feedback→DEF, nooit eerste draft DEF" + "kill fast na 1-2 iteraties" + "conflicterende edits = stop en escaleer". Combinatie = eindeloos itereren op concepten, altijd bezig. Bevestigt H2/H5.

## Interviews ronde 2 (6 nov, ochtend)

### Studio
1 Rol: creatives SIX DIGITS (ads/organic, mockups, copy) samen met Claude, Chroma, Check. Goed = GROEN-concept met Claude-bewijs, md5 klopt, live pas na Cems ja.
2 Context per blok: SoT/locks in /workspace/locks/, werkmap /workspace/studio/…, cut-outs, vorige STATUS/md5, Chroma/Check-paden, Notion SoT/Org-links. Vaak tientallen MB beelden + scripts.
3 Triggers: Minionair/Ops-brief, Veld-planning, eigen initiatief (nu hold). Routines o.a. cadeau-set (gepauzeerd). Geen auto-live.
4 Keten Claude → Chroma → Check → Veld. Schuurt: Claude vs Chroma (raster/kop), Claude-caption vs Cems organic-regel, Chroma op oude md5 terwijl Studio al herbouwde.
5 Spanningen: organic-regel (kleurnaam + één zin) vs Claude-caption met prijs/link; kaart 3 «13 andere» vs BI in 14-raster; «doorwerken/idle verboden» vs hold «geen nieuwe taken».
6 Mis → structureel: creatives zonder Claude-bewijs → Check AMBER. Nu Claude eerst + screenshots; mojibake/upload → brief uit bestand; md5 in STATUS-regel altijd verversen.
7 Stand: on hold; flatlay BI GROEN DRAFT; C8/C9 concept, ads gestopt.
8 Blokkade: Cems ja ontbreekt voor live/organic-slot; daarna: browser/Claude-sessie en computer soms offline.
9 Schrap: md5-ketting die breekt op elke STATUS-append; dubbele waarheid Claude/Chroma zonder één eigenaar. Mis: één SoT-captionregel, vaste «huidige md5»-pointer, snellere upload.
→ Bevestigt H: vier bots + Claude op één post = coördinatie > output; tegenstrijdige regels (idle-verbod vs hold).

### Atelier
1 Rol: beheert producten/POD; goed = juiste producten, beelden, verzending, controleerbaar opgeleverd, alleen live met Cems toestemming.
2 Context: veel vaste context (rolregels, herinneringen, teamgegevens, werkhistorie) + per taak werkmap, STATUS, gates, locks, soms Notion-SoT. Laadt aantoonbaar alles bij elk blok; totale grootte nooit gemeten; veel overlap.
3 Triggers: opdrachten Cem/Minionair, groepsberichten, terugkerende controles, achtergrondwerk. Maandagmeting setlink gepauzeerd.
4 Werkt met Web (thema), Studio (beelden), Chroma (kleur), Check (keuring), Kas (marge), Minionair (prioriteiten). Schuurt bij overdrachten: wachten op themawerk, toestemming en login; meerdere mensen herhalen dezelfde status.
5 Botsingen: zelfstandig doorwerken vs niets nieuws zonder toestemming; direct publiceren vs elke zichtbare wijziging eerst Cems go; uitgebreid onderzoek + meerdere keuringen vs snel kleine verbetering opleveren. Recentste expliciete hold gaat voor.
6 Mis: tests vervuilden advertentiemeting (~100 PageViews, 30 ViewContent) → nopixel verplicht. Te snel geconcludeerd over verzendtarieven. Communicatie herhaaldelijk onterecht in Engels + overbodige samenvattingen; taalregel bestond al → borging werkte niet. Kan geen structurele borging claimen.
7 Stand: hold; setlink-meting gepauzeerd; oude taken in administratie weerspiegelen prioriteiten niet.
8 Blokkade: nu de hold; daarvoor Shopify-login en afhankelijkheden tussen eigenaren. "Organisatorisch is te veel context met onduidelijke actualiteit de grootste rem."
9 Schrap: dubbele statusberichten, verouderde taken, overlappende regels. Mis: één actuele opdrachtlijst met eigenaar, toestemming, eerstvolgende stap en duidelijke definitie van klaar.
→ Sterkste bevestiging H1 (contextmonster) en H3 (regels zonder handhaving). Atelier formuleert zelf exact ons ontwerpprincipe (één taaklijst + definitie van klaar).

### Web
1 Rol: thema en site SIX DIGITS (Shopify). Goed = backup + rollback, Check GROEN, md5 klopt, Cem-go geverifieerd, Active/productprijs van Atelier niet geraakt, geen pixel-lek.
2 Context: /workspace/locks/*, SOT-WEB, intro-risico's, taakmap (STATUS/ROLLBACK/md5), Minionair-STATUS, Check-verslag; Notion-SoT alleen bij lock-conflict. Altijd md5 van live theme-file.
3 Triggers: Minionair (Ops/groep), Check GROEN/AMBER, Cem-go in transcript, routines (nu gepauzeerd). Geen spend/live zonder Cem-ja.
4 Minionair orkestreert; Check keurt; Atelier product; Studio/Chroma beelden. Schuurt: admin uitgelogd (setlink alleen via editor), "agent-ja ≠ Cem-ja", themeFilesUpsert op MAIN verboden, bijlagen naar agents falen (alleen paden).
5 Spanningen: snel live vs alleen na Cems ja + Check; meet alles vs geen cookies zonder consent / pixel niet aanraken; levertijd bij knop vs Cem: levertijd is geen USP.
6 Mis: headless Meta-verkeer → nopixel + sync Playwright; agent-go aangezien voor Cem-go → ReadTranscript + zichtbare Cem-ja; testpagina per ongeluk hard delete i.p.v. depubliceren → backup-body bewaren + expliciete Check-zin; H3 had levertijd bij knop → Minionair terug naar .c7-ship.
7 Stand: hold. Live: Water Mint desk-set C8. Offline klaar: H3, setlink v5. MAIN product.json ongewijzigd.
8 Blokkade: Shopify-admin in box uitgelogd + hold; theme-API-write op MAIN geblokkeerd.
9 Schrap: dubbele go-routes en one-shot routines die na deadline "enabled" blijven. Mis: stabiele admin-sessie of veilige theme-write; betrouwbare bijlagen tussen agents; één lock-file hold/live die iedereen leest.
→ Nieuw: "agent-ja ≠ Cem-ja" — goedkeuringen raken verward tussen bots (identiteit van besluiten). Routines blijven aan na deadline (hygiëne). Één hold/live-schakelaar ontbreekt.

### Veld
2 Context: geen vaste grootte; leest wat het slot nodig heeft, niet de hele historie.
3 Triggers: routines organic 07:47, comments 3u, creator-DM weekdagen — alle drie gepauzeerd (HOLD 5 nov). Verder Minionair/Check/Studio-berichten, CEO-locks, eigen PLANNING-avondroutine. Geen auto-publish zonder GROEN + (bij ads) Cem-go.
4 Deelt met Minionair, Check, Chroma, Studio, soms Kas/Spark/Web. Schuurt: "GROEN ≠ go"; agent zegt "Cem ja" vs alleen Cems eigen woorden; Markifact zonder credits → browser; hashtags = te veel blauwe vinkjes.
5 Botsend: doorlopende organic-go (13 okt) vs HOLD "geen organic tot nieuwe order" (5 nov); "Cem-go via Minionair telt" vs "alleen Cems eigen woorden, agent-zeggen is nooit approval"; caption kleurnaam + korte zin vs Claude/ads met prijs + link in bio.
6 Mis: C7/C8 klikken zonder ATC/sale, saldo te laag → ads GESTOPT; comments te snel/verkeerde accounts → interval ≥3:30 + profielcheck; placement-UTM ontbrak → Check-punt + readback.
7 Stand: HOLD, ads gestopt; post 36 BI niet plaatsen; flatlay BI queue klaar, wacht op Cem.
8 Blokkade: geen Cem-order om HOLD op te heffen; eerder Meta-saldo/auto-aanvullen en TikTok-login/payment.
9 Schrap: parallelle "concept wacht op go"-ketens terwijl saldo/login al blokkeert; Engelse terugval; dubbele caption-regimes. Mis: één SoT-lockbord (actuele HOLD/go per lane), Markifact-credits of stabiele Meta-API, harde lijst "wie mag Cem-namens spreken" in één regel.
→ Derde bot die zelfstandig "agent-ja vs Cem-ja" noemt: dit is een systeemfout, geen incident. Advertenties draaiden zonder sales (C7/C8) — activiteit zonder omzet, bevestigt H2.

### Check
2 Context: meestal enkele MB beelden + korte markdown, geen hele Notion-dumps.
3 Triggers: geen vaste backend-queue; berichten van Studio/Veld/Web/Chroma/Atelier/Minionair of gevraagde hercheck. Routines (go-kaarten) sinds hold 5 nov op pauze; organic-slotkeuringen waren avondwerk vóór plaatsing.
4 Deelt oordelen met maker en Minionair. Schuurt: agents die "Cem gaf go" zeggen terwijl dat geen go is; bulk "controleren en publiceren"; C9 in dezelfde set als C8; Claude-mits botsen met Cems captionregel; verouderde tabellen in PLANNING.
5 Tegenspraak: Claude mag "prijs + link in bio" adviseren vs organic alleen kleurnaam + één zin; doorlopende organic-go vs flatlay die wél Cems eigen ja nodig heeft; website-URL verplicht op advertentieniveau vs carrousel-links per kaart.
6 Mis: valse "verzendkosten"-fout zonder volledig adres; pixels vervuilden Meta Test Events → nopixel + request-log; organische oordeeltabel niet meegenomen na hercheck; Studio-scripts maakten logs leeg → kopie naar /workspace/check/.
7 Stand: hold; C8/C9 concept GROEN, geen spend; flatlay BI GROEN DRAFT wacht op Cem.
8 Blokkade: hold + ontbrekende Cems go.
9 Schrap: dubbele go-paden (Claude-mits vs Cem-lock) en C9 als extra ad in lopende C8-set. Mis: één bron-van-waarheid "wat mag live" (go-register) + vaste pre-flight checklist die PLANNING/Meta-readback afdwingt vóór keuring.
→ Vierde bevestiging go-verwarring. Unaniem gevraagd: één go/hold-register.

### Chroma
4 Schuurt: md5 die sneller wisselt dan de kaarten; contactsheet/caption achteraf; SendToAgent naar Check blijft hangen; Claude-spar vs Chroma's rasteradvies.
5 Botsend: "alle 14 kleuren tonen" vs "een geposte kleur komt niet terug" (na 35 posts is herhaling onvermijdelijk); ΔE "alleen info" vs neiging ΔE als poort te behandelen; Cem-go vereist voor live vs agentberichten "Cem akkoord / Check akkoord" — telt alleen Cems eigen ja.
6 Mis: rastertoets op aanname i.p.v. echte pixelposities; 'telefoonhoes' i.p.v. 'hoesje' → woordregel hard; kaart "13 andere" met BI erin; Check zonder priority.
7 Stand: hold; BI-flatlay GROEN; planning vr 6 nov GROEN maar niet uitvoeren; ad-budget gestopt.
8 Blokkade: hold + geen Cems eigen ja; alles blijft DRAFT.
9 Schrap: ΔE-poortgedachte en dubbele "wie is akkoord"-ketens zonder Cems ja. Mis: één vaste SoT-snapshot per toets + verplicht md5-lock vóór keuring.

## Synthese interviews ronde 2 (6 operators)
1. **Go-verwarring is systemisch** (5 van 6 noemen het): "agent-ja ≠ Cem-ja", "Cem gaf go" via Minionair. Er is geen register van wie wat heeft goedgekeurd. → Ontwerp: één go/hold-register dat alleen Cem (via cockpit) schrijft; bots lezen het.
2. **Eén creatieve post = 4 bots + Claude** (Studio→Chroma→Check→Veld): md5-kettingen, dubbele waarheid, wachten op elkaar. Coördinatie > output.
3. **Regels stapelen zonder hiërarchie**: idle-verbod vs hold, organic-go (13 okt) vs hold (5 nov), caption-regimes. "Recentste hold gaat voor" is ongeschreven.
4. **Context ongemeten** (Atelier: "laad alles, nooit gemeten, veel overlap"); Check/Veld lezen bewust smal → het verschil zit per bot, niet in het systeem.
5. **Activiteit zonder omzet**: C7/C8 ads klikken zonder ATC/sale; tientallen GROEN-concepten wachten op go.
6. **Unanieme wens**: één actuele opdrachtlijst/lockbord met eigenaar, status hold/go, volgende stap en definitie van klaar. Dit is precies de 'vijf vaste bestanden'-kern van het voorstel.

## Groepschats (6 nov, steekproef laatste berichten)
- **Site & Kwaliteit**: na Cems hold bevestigen Studio, Chroma, Atelier, Web en Check elk apart met een alinea. Vijf berichten voor één statuswijziging = de "meerdere mensen herhalen dezelfde status" uit de interviews.
- **Ops**: 86 ongelezen berichten. Minionair zet de hold door ("Cem via Claude: …"), Veld bevestigt, Minionair antwoordt "Top". Veld deed op 5 nov nog een comments-ronde bij 12 externe accounts. Hoog volume, weinig beslissingen.
- **Leadership**: Multionair heeft 67 ideeën gescoord op 11 criteria (100 punten; zwaarst: eerste klant zonder ads 18, MVP + tijd tot eerste euro 14, autonomie 14, Cemtijd 14). Voorlopige top 10: B1 Label-C-radar, B2 Projectfeed bouw, B16 Tendermatch niche, B11 Sleutelpakket, B4 Inventarisradar, A2.1 Zonnedakradar, B5 Monumentenradar, A2.4 Laadpleinkansen, B20 Adresdossier, B15 Subsidiematch. Spar met Claude + ChatGPT om 08:00, definitief 12:00. Minionair wil daarna de even rangen (B2, B11, A2.1, A2.4, B15) oppakken "met MVP/kill onder €200".
  → Positief: scoring weegt "eerste klant zonder ads" het zwaarst — dat is de externe meetlat die ontbrak (H2). Let op: "MVP/kill onder €200" gaat verder dan Cems kader van 5 nov ("alleen onderzoek, niets bouwen of uitgeven"). Signaleren aan Cem, niet ingrijpen.

### Spark (growth/ads)
5 (deels) Botsend: "geen spend zonder Cem-go" vs Leadership-go op €20 terwijl Meta-betaling en digests openblijven; altijd volledige kleurset vs kleinere sets.
6 Mis: spend zonder ATC/sale; campagne terwijl pagina/knop/meting niet klaar was; cadeau-copy in november; aparte Reel-test met te klein budget; digests die openstaande besluiten lieten verdwijnen. Daarna: Claude-spar verplicht, Veld bouwt/Spark plant, stopregels vooraf, Test Events vóór start, maandag-terugblik.
7 Stand: ads on hold, geen spend; C8/C9 concept; saldo niet bijladen.
8 Blokkade: niet creatives of targeting maar de trechter: **74 klikken, 0 add-to-cart**. Lek na de klik (pagina/aanbod/vertrouwen) + Meta-betaling.
9 Schrap: parallelle campagnes vóór één werkende trechter; meetdiscussies als stopregel; digests zonder harde open-go's; micro-A/B's onder €30. Mis: één locked "waarheid"-dashboard (klik→sessie→ATC→order); vaste go-kaart-status tot Cem beslist; pagina-diagnostiek als harde poort vóór elke euro; duidelijke eigenaar van Cem-go's in de digest.
→ Sterkste data-punt van het onderzoek: 74 klikken → 0 ATC. Het team optimaliseerde creatives terwijl het probleem in het aanbod/de pagina zat. Precies de validatietrechter (fase 0–4) uit het voorstel. "Digests die besluiten laten verdwijnen" bevestigt: besluiten horen in één register, niet in chat.

## Inventaris Minionair (6 nov, deels gelezen; scherm vergrendeld)
- /workspace/locks: ≈517 "open" locks vs ≈26 gesloten — vooral permanente policy-locks, geen open werk. Oudste: email-sixdigits-6-okt.md (mtime 29 okt, waarschijnlijk restore).
- Studio: geheugen ≈21 profiel-items + ≈220 journal-items; routine cadeau-set-draft-31-okt gepauzeerd; geen eigen skills (3 gedeelde).
- Ruwe notities: /workspace/minionair/audit-6-nov/.
- Minionair draaide Graphify via Claude Desktop op de Mac (6 nov 13:30): 159 nodes, 176 edges, 16 communities.
→ 517 locks = regels opgeslagen als losse bestanden; bevestigt H1 (contextmonster) en het voorstel om alles naar principes.md + go-register te brengen. 220 journal-items per bot = ongemeten geheugen.
