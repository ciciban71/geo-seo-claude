"""Serbian Latin translation strings for GEO PDF report."""

STRINGS = {
    # Cover page
    'report_title': 'GEO izveštaj o analizi',
    'report_subtitle': 'Revizija optimizacije za generativne pretraživače za <b>{brand_name}</b>',
    'label_website': 'Veb sajt',
    'label_date': 'Datum analize',
    'label_score': 'GEO ocena',
    'score_of_100': '/100',

    # Score tiers
    'tier_excellent': 'Odlično',
    'tier_good': 'Dobro',
    'tier_moderate': 'Umereno',
    'tier_below_avg': 'Ispod proseka',
    'tier_needs_attention': 'Potrebna pažnja',

    # Section headers
    'section_executive_summary': 'Izvršni rezime',
    'section_score_breakdown': 'Raspodela GEO ocena',
    'section_platform_readiness': 'Spremnost AI platformi',
    'section_crawler_access': 'Status pristupa AI pretraživača',
    'section_findings': 'Ključni nalazi',
    'section_action_plan': 'Prioritizovan plan akcije',
    'section_methodology': 'Dodatak: Metodologija',
    'section_glossary': 'Rečnik pojmova',

    # Table headers
    'col_component': 'Komponenta',
    'col_score': 'Ocena',
    'col_weight': 'Težina',
    'col_weighted': 'Ponderisano',
    'col_platform': 'AI platforma',
    'col_status': 'Status',
    'col_crawler': 'Pretraživač',
    'col_recommendation': 'Preporuka',
    'col_term': 'Termin',
    'col_definition': 'Definicija',

    # Score components
    'comp_citability': 'AI citiranost i vidljivost',
    'comp_brand': 'Signali autoriteta brenda',
    'comp_content': 'Kvalitet sadržaja i E-E-A-T',
    'comp_technical': 'Tehničke osnove',
    'comp_schema': 'Strukturirani podaci',
    'comp_platform': 'Optimizacija platformi',
    'comp_overall': 'UKUPNO',

    # Chart labels (short)
    'chart_citability': 'Citiranost',
    'chart_brand': 'Brend',
    'chart_content': 'Sadržaj',
    'chart_technical': 'Tehnika',
    'chart_schema': 'Šema',
    'chart_platform': 'Platforme',

    # Descriptions
    'platform_desc': 'Ove ocene odražavaju verovatnoću da će svaka AI platforma za pretragu citirati vaš sadržaj. Ocena ispod 50 ukazuje na značajne prepreke za citiranje na toj platformi.',
    'crawler_desc': 'Blokiranje AI pretraživača sprečava AI platforme da citiraju vaš sadržaj. Tabela ispod prikazuje koji AI pretraživači trenutno mogu da pristupe vašem sajtu.',

    # Action plan sub-headers
    'quick_wins_title': 'Brze pobede (ove nedelje)',
    'quick_wins_desc': 'Veliki uticaj, mali napor \u2014 mogu se odmah primeniti.',
    'medium_term_title': 'Srednjoročna poboljšanja (ovog meseca)',
    'medium_term_desc': 'Značajan uticaj, umeren napor \u2014 zahteva promene sadržaja ili tehničke promene.',
    'strategic_title': 'Strateške inicijative (ovog kvartala)',
    'strategic_desc': 'Dugoročna konkurentska prednost \u2014 zahteva kontinuirano ulaganje.',

    # Header/footer
    'header_text': 'GEO-SEO izveštaj o analizi',
    'footer_generated': 'Generisano {date}',
    'footer_page': 'Strana {page}',
    'footer_confidential': 'Poverljivo',

    # Severity labels
    'severity_critical': 'KRITIČNO',
    'severity_high': 'VISOKO',
    'severity_medium': 'SREDNJE',

    # Fallbacks
    'fallback_exec_summary': 'Ovaj izveštaj predstavlja nalaze sveobuhvatne revizije optimizacije za generativne pretraživače (GEO) sprovedene na <b>{brand_name}</b> ({url}). Analiza je procenila spremnost veb sajta za pretraživače pokretane veštačkom inteligencijom uključujući Google AI Overviews, ChatGPT, Perplexity, Gemini i Bing Copilot. Ukupna GEO ocena spremnosti je <b>{geo_score}/100</b>, što sajt stavlja u kategoriju <b>{tier}</b>.',
    'fallback_no_crawlers': '<i>Pokrenite /geo crawlers da popunite ovaj odeljak podacima o pristupu AI pretraživača.</i>',
    'fallback_no_findings': '<i>Pokrenite punu /geo reviziju da popunite nalaze.</i>',

    # Methodology
    'methodology_text': 'Ova GEO revizija je sprovedena {date} analizirajući {url}. Analiza je procenila veb sajt kroz šest dimenzija: AI citiranost i vidljivost (25%), signali autoriteta brenda (20%), kvalitet sadržaja i E-E-A-T (20%), tehničke osnove (15%), strukturirani podaci (10%) i optimizacija platformi (10%).',
    'methodology_platforms': '<b>Procenjene platforme:</b> Google AI Overviews, ChatGPT Web Search, Perplexity AI, Google Gemini, Bing Copilot',
    'methodology_standards': '<b>Referentni standardi:</b> Google smernice za ocenjivače kvaliteta pretrage (dec 2025), Schema.org specifikacija, Core Web Vitals (pragovi za 2026), llms.txt novi standard, RSL 1.0 okvir za licenciranje',

    # Crawler table data
    'status_allowed': 'Dozvoljeno',
    'status_blocked': 'Blokirano',
    'status_unknown': 'Nepoznato',
    'rec_keep_allowed': 'Zadržati dozvolu',
    'rec_unblock': 'Deblokirati za vidljivost',

    # Disclaimer
    'disclaimer': 'Ovaj izveštaj je generisan alatom za analizu GEO-SEO Claude Code. Ocene i preporuke su zasnovane na automatizovanoj analizi i industrijskim standardima. Rezultate treba validirati testiranjem specifičnim za svaku platformu.',

    # Glossary entries
    'glossary_entries': [
        ['GEO', 'Optimizacija za generativne pretraživače \u2014 optimizacija sadržaja za citiranje u AI pretrazi'],
        ['AIO', 'AI pregledi \u2014 odgovori generisani veštačkom inteligencijom u Google rezultatima pretrage'],
        ['E-E-A-T', 'Iskustvo, ekspertiza, autoritet, pouzdanost'],
        ['SSR', 'Renderovanje na serveru \u2014 generisanje HTML-a na serveru za pristup pretraživača'],
        ['CWV', 'Osnovni veb pokazatelji \u2014 Google-ove metrike iskustva na stranici (LCP, INP, CLS)'],
        ['INP', 'Interakcija do sledećeg iscrtavanja \u2014 metrika odziva (zamenila FID mart 2024)'],
        ['JSON-LD', 'JavaScript notacija za povezane podatke \u2014 preferiran format strukturiranih podataka'],
        ['sameAs', 'Schema.org svojstvo koje povezuje entitet sa njegovim profilima na drugim platformama'],
        ['llms.txt', 'Predloženi standardni fajl za usmeravanje AI sistema o sadržaju sajta'],
        ['IndexNow', 'Protokol za trenutno obaveštavanje pretraživača o promenama sadržaja'],
    ],

    # Default action plan items
    'default_quick_wins': [
        'Dozvoliti svim AI pretraživačima prvog nivoa u robots.txt (GPTBot, ClaudeBot, PerplexityBot)',
        'Dodati datume objavljivanja i poslednjeg ažuriranja na sve stranice sadržaja',
        'Dodati potpise autora sa akreditivima na blog postove i članke',
        'Kreirati llms.txt fajl za usmeravanje AI sistema ka vašem ključnom sadržaju',
        'Dodati sameAs svojstva u šemu organizacije za povezivanje sa svim profilima na platformama',
    ],
    'default_medium_term': [
        'Restrukturirati 10 najvažnijih stranica sa naslovima zasnovanim na pitanjima i blokovima direktnih odgovora',
        'Implementirati sveobuhvatnu Organization + Article + Person šemu oznaka',
        'Optimizovati blokove sadržaja za AI citiranost (134-167 reči samostalnih pasusa)',
        'Obezbediti renderovanje na serveru za sve javne stranice sadržaja',
        'Implementirati IndexNow protokol za brzinu indeksiranja Bing/Copilot',
    ],
    'default_strategic': [
        'Izgraditi prisustvo na Wikipedia/Wikidata kroz medijsku pokrivenost i značaj',
        'Razviti aktivnu strategiju angažovanja Reddit zajednice u relevantnim podredditima',
        'Kreirati YouTube strategiju sadržaja usklađenu sa upitima AI pretrage',
        'Uspostaviti program objavljivanja originalnih istraživanja/podataka za jedinstvenu citiranost',
        'Izgraditi tematski autoritet kroz sveobuhvatne klastere sadržaja',
    ],
}
