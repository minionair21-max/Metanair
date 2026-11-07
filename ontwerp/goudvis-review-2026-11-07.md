# Goudvis-review — inrichting Minionair 2.0 (7 nov 2026)

**Methode (Elephant-Goldfish):** de olifant (Metanair, met alle context) schreef `inrichting-minionair-2.0.md`. Drie goudvissen, verse agents zonder voorkennis, lazen alléén dat document. Elk had een eigen invalshoek: (1) weg naar de eerste euro, (2) operationeel falen, (3) zeggenschap en risico. Daarna weegt de olifant de bevindingen. Een bevinding die door meerdere goudvissen onafhankelijk is gevonden, weegt het zwaarst.

## Waar alle drie op uitkwamen

| # | Bevinding | Gevonden door | Oordeel olifant |
|---|---|---|---|
| A | **Claude praat via Cems account**: bots zien Metanair als Cem, dus "Cem is akkoord telt niet" is niet af te dwingen | 1, 2, 3 | **Klopt, hoog.** Dit is precies het oude go-verwarringspatroon. |
| B | **Toezicht faalt stil en meet activiteit**: de computer-use naar de Mac blokkeert, een run die niet draait merkt niemand op, de bevindingen gaan van run tot run verloren, en de run vraagt nergens naar omzet | 1, 2, 3 | **Klopt, hoog.** |
| C | **De 28-dagenklok heeft geen start**, GO's hebben geen einddatum en fase 2 is niet gedefinieerd | 1, 2, 3 | **Klopt, hoog.** De killregel is zo niet te handhaven. |
| D | **Geldregel lekt**: "<€30 met log" geldt per uitgave en stapelt dus op; bovendien is onduidelijk wie de kaart gebruikt als agents geen kaartgegevens mogen invullen | 1, 2, 3 | **Klopt, hoog.** |
| E | **Twee plekken met status** (Notion en de cockpit-database); er staat niet welke plek wint | 1, 2, 3 | **Klopt, midden.** |

## Sterk punt van één goudvis

| # | Bevinding | Oordeel olifant |
|---|---|---|
| F | **Niemand is eigenaar van de verkoop** (goudvis 1). Bevoegdheden zijn goed geregeld, maar mailbox, betaallink en verkoopkanaal hebben geen eigenaar, en tot dag 28 bestaat er geen tussenmeting. | **Klopt, hoog: de belangrijkste les.** Het ontwerp regelt vooral wat níét mag. |
| G | **"Klaar" heeft geen bewijsveld** in taken.md (goudvis 2) | Klopt. Neem het op in het venture-sjabloon. |
| H | **Gepauzeerde bots hergebruiken** brengt hun oude geheugen terug (goudvis 2) | Klopt. Lead en scout moeten nieuwe bots zijn. |
| I | **C3 heeft geen bewijs van vraag** (goudvis 1) | Klopt. Test met een presale vóór de bouw. |

## Verworpen of rechtgezet

| Bevinding | Waarom niet |
|---|---|
| "Pion-wachtlijst verzamelt persoonsgegevens" | Leesfout, door een gat in het document. Pion is een agent-platform; het gaat om Cems eigen aanmelding. In het document moet dit wél uitgelegd worden. |
| "Principe 5 (nieuwste besluit wint) botst met wijzigen alleen op zondag" | Geen botsing. Principe 5 gaat over besluiten; principes wijzigen alleen op zondag. Wel verduidelijken. |
| "Maak het go-register technisch alleen-lezen" | Gratis Notion kan dit niet fijn genoeg. Alternatief: het toezicht controleert de paginageschiedenis en meldt elke wijziging die niet van Cem komt. |
| "Alle vreemde termen uitleggen (RPW, C3)" | Terecht voor het document, maar zonder invloed op het systeem. |

## Wat Metanair zelf oppakt (binnen de bestaande GO "Nieuwe inrichting")
1. **Toezichtstatus-pagina** in Notion: laatste run, open bevindingen en opvolging. Elke run leest die pagina eerst en werkt hem als laatste bij. Een run die niet heeft gedraaid, telt als **rood**. De run leest Notion, niet de Mac.
2. **Toezichtsvraag nummer één:** "welke taak bracht vandaag een klant dichter bij betalen?"
3. **Venture-sjabloon v0.2 (voorstel):** elke taak krijgt een veld "klaar is…" en een bewijsveld (URL, screenshot of transactie); de eerste taak is altijd een verkooptaak; tussenpoorten op dag 3, 7 en 14; de trechter dagelijks bijhouden.
4. **De cockpit wordt een alleen-lezen weergave van Notion.** Een verschil tussen de twee is een bevinding.
5. Ontwerpdocument verduidelijken (Pion, principe 5, NEE als status).

## Max 3 beslissingen voor Cem
1. **Afzender.** Krijgt Metanair in Grok Bot een eigen account of kanaal? Bots voeren een opdracht dan alleen uit als die naar een regel in het go-register verwijst. *(Voorstel: ja. Cem maakt het account zelf aan, want daar is een login voor nodig.)*
2. **Geld en klok.** De €30-grens wordt cumulatief per venture. Elke venture krijgt een virtuele Revolut-kaart met een limiet gelijk aan het budget; Cem beheert die. De 28-dagenklok start op de GO-datum, en de GO-regel krijgt die einddatum. *(Voorstel: ja. Wordt een nieuwe principe-tekst, zondagreview.)*
3. **C3 met presale eerst.** Een GO voor 7 dagen presale-test: lead en scout (nieuwe bots) benaderen hoveniers met een betaallink vóór de bouw. Ook de noodstop hoort hierbij: mag Metanair een venture op HOLD zetten (alleen stoppen, nooit starten)? *(Voorstel: ja op beide.)*

Open, door Cem af te ronden: het Top-10-onderzoek staat op GO, maar Multionair is gepauzeerd. Zet die regel op "vervallen" of wijs het werk toe.
