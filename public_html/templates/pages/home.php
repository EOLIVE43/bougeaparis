<?php
/**
 * Page d'accueil / — refonte stratégique SEO (mai 2026)
 *
 * 9 sections :
 *   1. Hero éditorial (above-the-fold, pas d'image)
 *   2. Module trafic temps réel (partial traffic-banner)
 *   3. 5 entrées du site (cards Lucide)
 *   4. Vitrine stations LOT 1 (6 cards image + tagline)
 *   5. Top lieux à visiter par métro (8 POIs, format .visiter-poi-card)
 *   6. Le réseau en chiffres (partial key-stats-grid)
 *   7. Pourquoi BougeaParis (4 USP + info-callout)
 *   8. FAQ globale (partial faq-accordion + FAQPage schema.org)
 *   9. Maillage interne enrichi (5 cards thématiques)
 *
 * Conventions :
 * - Tous les chiffres tarifaires en lecture dynamique getTarif() ;
 *   source unique data/tarifs.json mise à jour chaque janvier.
 * - Tous les chiffres non-tarifaires en dur, sourcés dans commentaires HTML.
 * - CSS dédié /assets/css/home.css + partials réutilisés (info-callout,
 *   key-stats-grid, faq-accordion, traffic-banner).
 */

$tpl->addStylesheet('/assets/css/home.css');

// -------------------- SEO --------------------
$tpl->seo
    ->setTitle('Transports Paris, guide station par station')
    ->setDescription('Le guide indépendant des transports parisiens : métro, RER, bus, tramway. À chaque station, plans, horaires, sorties et lieux à visiter autour. Trafic temps réel.')
    ->setCanonical('/')
    ->setOgType('website')
    ->setOgImage('/assets/img/logo/og-image.png');

// -------------------- Données : 6 stations vitrine LOT 1 --------------------
// Taglines harmonisées à ~14-16 mots chacune (2 lignes max desktop) pour
// homogénéiser la hauteur des cards. Correction 2026-05-12 #14.
$vitrineStations = [
    [
        'name'    => 'Châtelet',
        'slug'    => 'chatelet',
        'lines'   => ['M1', 'M4', 'M7', 'M11', 'M14'],
        'tagline' => 'La station la plus fréquentée du métro parisien, carrefour de cinq lignes au cœur de Paris.',
        'hidden_mobile' => false,
    ],
    [
        'name'    => 'Charles-de-Gaulle–Étoile',
        'slug'    => 'charles-de-gaulle-etoile',
        'lines'   => ['M1', 'M2', 'M6', 'RER A'],
        'tagline' => "Sous l'Arc de Triomphe, carrefour entre les Champs-Élysées et la Place de l'Étoile.",
        'hidden_mobile' => false,
    ],
    [
        'name'    => 'Concorde',
        'slug'    => 'concorde',
        'lines'   => ['M1', 'M8', 'M12'],
        'tagline' => "Sous la place de la Concorde, point central de l'axe historique parisien.",
        'hidden_mobile' => false,
    ],
    [
        'name'    => 'Palais Royal–Musée du Louvre',
        'slug'    => 'palais-royal-musee-du-louvre',
        'lines'   => ['M1', 'M7'],
        'tagline' => "Accès direct au plus grand musée du monde et au jardin du Palais-Royal.",
        'hidden_mobile' => false,
    ],
    [
        'name'    => 'Tuileries',
        'slug'    => 'tuileries',
        'lines'   => ['M1'],
        'tagline' => "Au cœur du jardin royal historique, entre le Louvre et la Concorde.",
        'hidden_mobile' => true,
    ],
    [
        'name'    => 'La Défense–Grande Arche',
        'slug'    => 'la-defense-grande-arche',
        'lines'   => ['M1', 'RER A', 'T2'],
        'tagline' => "Terminus ouest de la ligne 1, sous la Grande Arche et le quartier d'affaires.",
        'hidden_mobile' => true,
    ],
];

// -------------------- Données : 8 Top POIs (sélection cohérente LOT 1) --------------------
// Image URLs sourcées depuis Wikimedia Commons (présents dans data/stations/*.json — nearby_pois).
// Descriptions courtes éditoriales (validées par Ludovic, conformes aux corrections #3b 2026-05-12).
$topPois = [
    [
        'name'         => 'Musée du Louvre',
        'image_url'    => 'https://commons.wikimedia.org/wiki/Special:FilePath/Cour%20Napol%C3%A9on%20at%20night%20-%20Louvre.jpg?width=800',
        'description'  => 'Le plus grand musée du monde et la pyramide de verre de Pei. Sortie directe depuis la station, sans remonter en surface.',
        'station_name' => 'Palais Royal–Musée du Louvre',
        'station_slug' => 'palais-royal-musee-du-louvre',
        'station_lines'=> ['M1', 'M7'],
    ],
    [
        'name'         => 'Cathédrale Notre-Dame',
        'image_url'    => 'https://commons.wikimedia.org/wiki/Special:FilePath/Notre-Dame%20de%20Paris%202013-07-24.jpg?width=800',
        'description'  => "Chef-d'œuvre de l'art gothique sur l'île de la Cité. À environ 10 minutes à pied depuis Châtelet en traversant le Pont au Change.",
        'station_name' => 'Châtelet',
        'station_slug' => 'chatelet',
        'station_lines'=> ['M1', 'M4', 'M7', 'M11', 'M14'],
    ],
    [
        'name'         => 'Arc de Triomphe',
        'image_url'    => 'https://commons.wikimedia.org/wiki/Special:FilePath/Arc%20de%20Triomphe%2C%20Paris%2021%20October%202010.jpg?width=800',
        'description'  => "Monumental arc commandé par Napoléon, sommet de l'axe historique. Sortie en surface directement sur la Place de l'Étoile.",
        'station_name' => 'Charles-de-Gaulle–Étoile',
        'station_slug' => 'charles-de-gaulle-etoile',
        'station_lines'=> ['M1', 'M2', 'M6', 'RER A'],
    ],
    [
        'name'         => 'Place de la Concorde',
        'image_url'    => 'https://commons.wikimedia.org/wiki/Special:FilePath/Place%20de%20la%20Concorde%20from%20the%20Eiffel%20Tower%2C%20Paris%20April%202011.jpg?width=800',
        'description'  => 'Plus célèbre place de Paris, au cœur des Rives de la Seine classées UNESCO depuis 1991, avec l’obélisque de Louxor en son centre. Sortie directe depuis la station.',
        'station_name' => 'Concorde',
        'station_slug' => 'concorde',
        'station_lines'=> ['M1', 'M8', 'M12'],
    ],
    [
        'name'         => 'Jardin des Tuileries',
        'image_url'    => 'https://commons.wikimedia.org/wiki/Special:FilePath/Grande%20Roue%20de%20Paris%20-%20Louvre%20et%20Jardins%20des%20Tuileries.jpg?width=800',
        'description'  => 'Jardin royal historique de 25 hectares entre le Louvre et la Concorde. Accessible également depuis Concorde et Palais-Royal.',
        'station_name' => 'Tuileries',
        'station_slug' => 'tuileries',
        'station_lines'=> ['M1'],
    ],
    [
        'name'         => 'Sainte-Chapelle',
        'image_url'    => 'https://commons.wikimedia.org/wiki/Special:FilePath/Szensapel.jpg?width=800',
        'description'  => "Joyau gothique du XIIIᵉ siècle et ses vitraux exceptionnels, à l'intérieur du Palais de Justice sur l'île de la Cité.",
        'station_name' => 'Châtelet',
        'station_slug' => 'chatelet',
        'station_lines'=> ['M1', 'M4', 'M7', 'M11', 'M14'],
    ],
    [
        'name'         => 'Centre Pompidou',
        'image_url'    => 'https://commons.wikimedia.org/wiki/Special:FilePath/Paris%20Montmartre%20Blick%20aufs%20Centre%20Georges-Pompidou.jpg?width=800',
        'description'  => "Musée d'art moderne et contemporain dans le bâtiment iconique de Piano et Rogers. À 8 minutes à pied de Châtelet.",
        'station_name' => 'Châtelet',
        'station_slug' => 'chatelet',
        'station_lines'=> ['M1', 'M4', 'M7', 'M11', 'M14'],
    ],
    [
        'name'         => 'Grande Arche de la Défense',
        'image_url'    => 'https://commons.wikimedia.org/wiki/Special:FilePath/Grande%20Arche%2C%20France%20-%20April%202011.jpg?width=800',
        'description'  => "Monumental cube ouvert moderne (1989), réplique géante de l'Arc de Triomphe alignée sur l'axe historique parisien.",
        'station_name' => 'La Défense–Grande Arche',
        'station_slug' => 'la-defense-grande-arche',
        'station_lines'=> ['M1', 'RER A', 'T2'],
    ],
];

// -------------------- Données : 8 FAQ globales + Schema.org FAQPage --------------------
// NOTE : les valeurs tarifaires sont interpolées ci-dessous via getTarif() dans
// les chaînes des réponses $faqs[*]['a'] (lecture dynamique au moment du render
// de cette page, source unique data/tarifs.json mise à jour chaque janvier).
$tMtr  = getTarif('ticket_metro_train_rer', 'price');
$tBT   = getTarif('ticket_bus_tram', 'price');
$tBTn  = getTarif('ticket_bus_tram', 'name');
$tMtrN = getTarif('ticket_metro_train_rer', 'name');
$nDay  = getTarif('navigo_decouverte', 'daily_price');
$nDayL = getTarif('navigo_decouverte', 'daily_label');
$nWk   = getTarif('navigo_decouverte', 'weekly_price');
$nWkL  = getTarif('navigo_decouverte', 'weekly_label');
$nMo   = getTarif('navigo_decouverte', 'monthly_price');
$nMoL  = getTarif('navigo_decouverte', 'monthly_label');
$nEasy = getTarif('navigo_easy', 'price');
$nDec  = getTarif('navigo_decouverte', 'price');
$tAero = getTarif('aeroports', 'price');

$faqs = [
    [
        'q' => 'Quel ticket choisir pour visiter Paris ?',
        'a' => "Pour un séjour touristique à Paris, plusieurs options existent. Le <strong>{$tMtrN}</strong> ({$tMtr}) couvre métro, RER et Transilien, tandis que le <strong>{$tBTn}</strong> ({$tBT}) est dédié aux trajets en surface. Au-delà de 5 trajets dans la journée, le <strong>forfait Navigo Jour</strong> ({$nDay} toutes zones) devient plus économique. Pour un séjour de 4 jours ou plus, le <strong>forfait Navigo Hebdomadaire</strong> ({$nWk}) couvre tout le réseau du lundi au dimanche. Ces forfaits se chargent sur la carte <strong>Navigo Easy</strong> ({$nEasy}, anonyme) ou <strong>Navigo Découverte</strong> ({$nDec}, avec photo).",
    ],
    [
        'q' => 'Quelle différence entre métro et RER ?',
        // Sources : RATP officiel (16 lignes métro, 308 stations) ; distance moyenne 400-600 m entre stations RATP ; 5 lignes RER (A-E, A/B RATP, C/D/E SNCF) ; Châtelet-Étoile RER A direct ~5 min RATP, M1 ~15 min sur 7 arrêts.
        'a' => "Le <strong>métro</strong> dessert exclusivement Paris intra-muros et sa proche couronne, avec un arrêt tous les 400 à 600 mètres. Il compte 16 lignes et plus de 300 stations, exploitées par la RATP. Le <strong>RER</strong> (Réseau Express Régional) traverse l'agglomération avec 5 lignes (A, B, C, D, E) qui relient Paris à la grande banlieue, avec des stations beaucoup plus espacées et des trains plus rapides. Concrètement, dans Paris, le RER fait office de « métro express » pour traverser la ville en quelques minutes : Châtelet–Étoile en RER A prend environ 5 minutes contre 15 minutes par le métro M1 (7 arrêts). Côté tarif, le même <strong>{$tMtrN}</strong> donne accès aux deux réseaux pour les trajets intra-Paris.",
    ],
    [
        'q' => 'Comment se rendre aux aéroports CDG et Orly en transport ?',
        // Sources : tarif unifié 14 € IDFM officiel + Wikipédia tarification IDF + RATP officiel ; T7 tramway → Bus-Tram ; Roissybus arrêt 1er mars 2026 confirmé ; durées RATP : RER B ~35 min, M14 ~25 min, OrlyVal+RER B ~30 min, T7 ~30 min.
        'a' => "Depuis le 1er janvier 2025, les liaisons aéroports utilisent un <strong>tarif unique unifié</strong> à <strong>{$tAero}</strong>, valable indifféremment sur les 4 services en transport en commun. Pour <strong>Roissy–Charles-de-Gaulle</strong>, le <strong>RER B</strong> est l'option la plus directe (Châtelet, Gare du Nord, Saint-Michel), environ 35 minutes. Le <strong>Roissybus</strong> historique au départ de l'Opéra a été <strong>supprimé le 1er mars 2026</strong> : à privilégier désormais le RER B ou le taxi. Pour <strong>Orly</strong>, le <strong>métro 14</strong> prolongé jusqu'à l'aéroport (depuis 2024) est l'option la plus rapide en 25 minutes ; l'<strong>OrlyVal</strong> combiné au RER B via Antony est une alternative en 30 minutes, au même <strong>{$tAero}</strong> unifié. Le <strong>tramway T7</strong> relie aussi Orly à Villejuif–Louis Aragon (M7) en 30 minutes pour un simple <strong>{$tBTn}</strong> ({$tBT}) — option économique mais plus lente, et avec une correspondance.",
    ],
    [
        'q' => 'Le métro fonctionne-t-il la nuit à Paris ?',
        // Sources : horaires métro RATP (5h30 → 1h05 dim-jeu, → 2h15 ven-sam-veilles) ; Noctilien ~50 lignes bus de nuit RATP.
        'a' => "Le <strong>métro parisien</strong> circule de <strong>5h30 environ jusqu'à 1h05</strong> du dimanche au jeudi, et <strong>jusqu'à 2h15</strong> les vendredis, samedis et veilles de jours fériés. Il n'y a <strong>pas de service métro de nuit complet</strong> comme à New York ou Tokyo. Pour les déplacements nocturnes entre 0h30 et 5h30, le réseau <strong>Noctilien</strong> prend le relais : une cinquantaine de lignes de <strong>bus de nuit</strong> au départ des principales gares parisiennes (Gare de l'Est, Châtelet, Saint-Lazare, Gare de Lyon, Montparnasse). Les Noctilien utilisent le même titre de transport que le réseau de jour ({$tBTn} ou forfait Navigo).",
    ],
    [
        'q' => 'Où acheter un ticket de métro à Paris ?',
        // Sources : RATP (distributeurs, guichets, apps officielles Bonjour RATP + IDFM) ; tabacs partenaires.
        'a' => "Plusieurs options s'offrent à vous pour acheter un <strong>ticket de métro à Paris</strong>. Les <strong>distributeurs automatiques</strong> sont présents dans toutes les stations, ils acceptent <strong>carte bancaire et espèces</strong> et proposent l'ensemble des titres. Les <strong>bureaux de tabac partenaires</strong> vendent également les tickets papier et rechargent les cartes Navigo Easy. Enfin, les <strong>guichets agents</strong> subsistent dans les principales stations mais avec des horaires d'ouverture restreints. Pour les voyageurs réguliers, la <strong>carte Navigo Easy</strong> ({$nEasy}) rechargeable au voyage est la solution la plus pratique.",
    ],
    [
        'q' => 'Le métro est-il accessible aux personnes à mobilité réduite ?',
        // Sources : RATP accessibilité officiel ; M14 100% accessible, autres lignes partiellement aménagées (Saint-Paul, Bérault…) ; RER A/B largement aménagés ; tramway 100% ; bus RATP 100% (plancher bas + rampe).
        'a' => "L'<strong>accessibilité PMR</strong> est inégale sur le réseau parisien. Le <strong>métro historique</strong> (lignes 1 à 13) reste <strong>partiellement accessible</strong> en raison de son héritage de la fin du XIXᵉ siècle (escaliers, couloirs étroits, profondeur des quais). La <strong>ligne 14</strong>, conçue à partir de 1998, est l'<strong>unique ligne intégralement accessible</strong> aux personnes à mobilité réduite avec ascenseurs sur toutes les stations. Les autres lignes sont <strong>partiellement aménagées</strong>, avec une <strong>politique de mise en accessibilité progressive</strong> (certaines stations comme Saint-Paul ou Bérault sont équipées). Le <strong>RER</strong> est mieux loti, en particulier les lignes A et B dont la plupart des gares sont aménagées. Le <strong>tramway</strong> est <strong>100 % accessible</strong> (planchers bas, quais à hauteur du véhicule). Les <strong>bus</strong> RATP disposent tous d'un plancher bas et d'une rampe d'accès pour fauteuils roulants.",
    ],
    [
        'q' => 'Combien coûte un ticket de métro à Paris en 2026 ?',
        'a' => "Depuis la <strong>refonte tarifaire de 2025</strong>, le ticket t+ historique a été supprimé et remplacé par deux titres distincts. Le <strong>{$tMtrN}</strong> ({$tMtr}) est valable pour le métro, le RER et le Transilien, <strong>toutes zones confondues</strong>. Le <strong>{$tBTn}</strong> ({$tBT}) est dédié aux trajets en bus et en tramway. Pour les trajets vers les aéroports CDG et Orly, un <strong>ticket unifié spécial aéroport</strong> à <strong>{$tAero}</strong> s'applique à tous les services (RER B, métro 14, OrlyVal, OrlyBus). Le <strong>carnet de 10 tickets</strong> n'existe plus depuis 2025.",
    ],
    [
        'q' => 'Comment fonctionne le pass Navigo Découverte ?',
        'a' => "Le <strong>Navigo Découverte</strong> est une <strong>carte personnelle</strong> au tarif de {$nDec} (achat unique, à vie), qui nécessite une <strong>photo d'identité</strong> et le nom du porteur. Une fois la carte obtenue, vous y chargez le <strong>forfait de votre choix</strong> depuis n'importe quel automate, application ou guichet : <strong>{$nDayL}</strong> à {$nDay}, <strong>{$nWkL}</strong> à {$nWk} (lundi-dimanche), ou <strong>{$nMoL}</strong> à {$nMo} (1er au dernier jour du mois calendaire). Tous les forfaits couvrent désormais l'<strong>ensemble des zones (1 à 5)</strong> depuis 2026, y compris les liaisons vers les <strong>aéroports CDG et Orly</strong>, sans supplément.",
    ],
];

// Schema.org FAQPage : génère un seul bloc JSON-LD avec toutes les questions
$faqSchema = [
    '@context' => 'https://schema.org',
    '@type'    => 'FAQPage',
    'mainEntity' => array_map(function ($f) {
        // Pour le schema, on strip les balises HTML de la réponse (Google indexe le texte brut)
        return [
            '@type'          => 'Question',
            'name'           => $f['q'],
            'acceptedAnswer' => [
                '@type' => 'Answer',
                'text'  => strip_tags($f['a']),
            ],
        ];
    }, $faqs),
];
$tpl->seo->addSchema($faqSchema);

// -------------------- Données : Réseau en chiffres (Section 6) --------------------
// Sources : RATP officiel (16 lignes métro, 13 lignes tramway), SNCF (8 lignes Transilien H/J/K/L/N/P/R/U), réseau régional ~350 lignes bus RATP+Optile.
$networkStats = [
    ['number' => '16',   'label' => 'lignes de métro'],
    ['number' => '5',    'label' => 'lignes de RER'],
    ['number' => '13',   'label' => 'lignes de tramway'],
    ['number' => '8',    'label' => 'lignes de Transilien'],
    ['number' => '350+', 'label' => 'lignes de bus', 'sublabel' => 'en Île-de-France'],
];

// -------------------- Données : 4 entrées du site (Section 3) --------------------
// La card "Tarifs" est retirée (correction 2026-05-12). Le lien reste accessible
// via la nav principale + la maintenance des partials info-callout.
$entries = [
    [
        'icon'  => 'train-front',
        'title' => 'Se déplacer',
        'desc'  => 'Tous les modes de transport franciliens en un seul guide. <strong>Métro</strong>, <strong>RER</strong>, <strong>bus</strong>, <strong>tramway</strong>, <strong>Transilien</strong>, <strong>aéroports</strong> : plans, lignes, fonctionnement.',
        'cta'   => 'Explorer les modes →',
        'url'   => '/se-deplacer/',
    ],
    [
        'icon'  => 'landmark',
        'title' => 'Visiter',
        'desc'  => 'Les lieux phares de Paris classés par catégorie : <strong>monuments</strong>, <strong>musées</strong>, <strong>places</strong>, <strong>jardins</strong>, <strong>patrimoine religieux</strong>. Avec la <strong>station de métro la plus proche</strong> pour chaque POI.',
        'cta'   => 'Voir les lieux →',
        'url'   => '/visiter/',
    ],
    [
        'icon'  => 'map',
        'title' => 'Itinéraires',
        'desc'  => 'Le planificateur d\'itinéraires multimodaux <strong>BougeaParis</strong> est en cours de développement. En attendant, explorez le réseau via les pages dédiées par mode et par ligne.',
        'cta'   => 'Découvrir la feuille de route →',
        'url'   => '/itineraires/',
    ],
    [
        'icon'  => 'activity',
        'title' => 'Trafic temps réel',
        'desc'  => 'L\'état du réseau aujourd\'hui, <strong>alimenté par les données officielles IDF Mobilités</strong> (source PRIM). Bulletins quotidiens, perturbations actives, recommandations.',
        'cta'   => 'Consulter le trafic →',
        'url'   => '/info-trafic/',
    ],
];

/**
 * Convertit une étiquette ligne ("M1", "RER A", "T3a") en slug modificateur
 * pour la classe CSS .line-pill--{slug}. Casse insensible, sans accents,
 * espaces remplacés par tirets.
 *
 * Exemples :
 *   "M1"    → "m1"
 *   "RER A" → "rer-a"
 *   "T3a"   → "t3a"
 *   "M3bis" → "m3bis"
 */
$linePillSlug = function (string $line): string {
    $s = mb_strtolower(trim($line), 'UTF-8');
    $s = preg_replace('/\s+/', '-', $s);
    return $s;
};
?>

<!-- =========================================================================
     SECTION 1 — Hero éditorial
     ========================================================================= -->
<section class="hero home-hero">
    <div class="container">
        <h1 class="hero__title">Se déplacer à Paris : le guide complet, station par station</h1>
        <p class="hero__subtitle">
            Métro, RER, bus, tramway : à chaque <strong>station</strong>, ce qu'il faut
            savoir pour s'orienter, et <strong>ce qu'il y a à voir autour</strong>.
            Plans, horaires, sorties, conseils touristiques. Et le
            <strong>trafic en temps réel</strong> pour adapter vos plans.
        </p>
    </div>
</section>

<!-- =========================================================================
     SECTION 2 — Module trafic temps réel (pleine largeur) + recherche ligne
     - partials/traffic-banner.php : bandeau stats (lit data/traffic/latest.json)
     - partials/line-search-widget.php : champ recherche avec dropdown lignes
       (réutilise le composant de /info-trafic/, mode 'metro' pour le label
       "Rechercher le trafic d'un métro à Paris")
     ========================================================================= -->
<section class="home-traffic">
    <div class="container">
        <?php $bannerMode = 'all'; include __DIR__ . '/../partials/traffic-banner.php'; ?>
        <?php $lineSearchMode = 'metro'; include __DIR__ . '/../partials/line-search-widget.php'; ?>
        <p class="home-traffic__cta">
            <a href="/info-trafic/" class="link-underline">Voir tous les bulletins quotidiens →</a>
        </p>
    </div>
</section>

<!-- =========================================================================
     SECTION 3 — Les 5 entrées du site
     ========================================================================= -->
<section class="section home-entries">
    <div class="container">
        <h2>Métro, Bus, RER : Se déplacer et visiter Paris</h2>
        <p class="section__intro">
            Quatre portes d'entrée pour explorer Paris en transport en commun :
            par mode (métro, RER, bus, tramway), par lieu à visiter, par itinéraire,
            ou par perturbation du jour. Choisissez l'angle qui correspond à votre besoin.
        </p>
        <ul class="home-entries-grid" role="list">
            <?php foreach ($entries as $entry): ?>
            <li class="home-entry-card">
                <a href="<?= e($entry['url']) ?>" class="home-entry-card__link">
                    <span class="home-entry-card__icon" aria-hidden="true">
                        <?php component('icon-menu', ['icon' => $entry['icon'], 'size' => 'md']); ?>
                    </span>
                    <h3 class="home-entry-card__title"><?= e($entry['title']) ?></h3>
                    <p class="home-entry-card__desc"><?= $entry['desc'] /* contient richText interne contrôlé */ ?></p>
                    <span class="home-entry-card__cta"><?= e($entry['cta']) ?></span>
                </a>
            </li>
            <?php endforeach; ?>
        </ul>
    </div>
</section>

<!-- =========================================================================
     SECTION 4 — Vitrine stations LOT 1 (6 cards)
     Layout desktop : grille 3 cols × 2 lignes
     Layout mobile : 4 visibles + CTA "Voir toutes les stations →" vers /metro/
     ========================================================================= -->
<section class="section section--alt home-stations">
    <div class="container">
        <h2>Découvrir Paris par ses stations</h2>
        <p class="section__intro">
            Chaque <strong>station de métro</strong> parisienne raconte une histoire
            et donne accès à un quartier entier. Notre guide propose un dossier
            détaillé pour les stations les plus emblématiques :
            <strong>plan d'accès</strong>, <strong>horaires de la ligne</strong>,
            <strong>sorties signalées</strong>, <strong>lieux à voir autour</strong>,
            <strong>anecdotes</strong> et <strong>conseils pratiques</strong>.
            Six stations sont déjà disponibles ; les autres arrivent au fil de la
            production éditoriale.
        </p>
        <div class="home-stations-grid">
            <?php foreach ($vitrineStations as $s):
                $hiddenClass = $s['hidden_mobile'] ? ' home-stations-grid__hidden-mobile' : '';
                $url         = '/metro/station/' . $s['slug'] . '/';
                $heroBase    = '/assets/img/stations/' . $s['slug'] . '/' . $s['slug'];
            ?>
            <article class="home-station-card<?= $hiddenClass ?>">
                <div class="home-station-card__image">
                    <picture>
                        <source srcset="<?= e(asset($heroBase . '-800.avif')) ?>" type="image/avif">
                        <source srcset="<?= e(asset($heroBase . '-800.webp')) ?>" type="image/webp">
                        <img src="<?= e(asset($heroBase . '-800.jpg')) ?>"
                             alt="<?= e($s['name']) ?>"
                             loading="lazy" decoding="async"
                             width="800" height="450">
                    </picture>
                </div>
                <div class="home-station-card__content">
                    <h3 class="home-station-card__name">
                        <a href="<?= e($url) ?>" class="home-station-card__name-link"><?= e($s['name']) ?></a>
                    </h3>
                    <div class="home-station-card__lines">
                        <?php foreach ($s['lines'] as $line): ?>
                        <span class="line-pill line-pill--<?= e(linePillShape($line)) ?> line-pill--<?= e($linePillSlug($line)) ?>"><?= e($line) ?></span>
                        <?php endforeach; ?>
                    </div>
                    <p class="home-station-card__tagline"><?= e($s['tagline']) ?></p>
                </div>
            </article>
            <?php endforeach; ?>
        </div>
        <p class="home-stations__cta-mobile">
            <a href="/metro/" class="btn btn--ghost">Voir toutes les stations →</a>
        </p>
    </div>
</section>

<!-- =========================================================================
     SECTION 5 — Top lieux à visiter par métro (8 POIs)
     Format .visiter-poi-card (réutilisation des styles déjà créés sur /visiter/)
     ========================================================================= -->
<section class="section home-pois">
    <div class="container">
        <h2>Visiter Paris en transport en commun</h2>
        <p class="section__intro">
            Les <strong>lieux incontournables</strong> de Paris sont presque tous
            accessibles en métro à moins de 5 minutes à pied d'une station. Pour
            chaque monument, musée ou jardin, nous indiquons la
            <strong>station de métro la plus proche</strong> et la
            <strong>sortie à privilégier</strong>.
        </p>
        <ul class="visiter-poi-grid" role="list">
            <?php foreach ($topPois as $poi): ?>
            <li class="visiter-poi-card">
                <div class="visiter-poi-card__image">
                    <img src="<?= e($poi['image_url']) ?>"
                         alt="<?= e($poi['name']) ?>"
                         loading="lazy" decoding="async"
                         referrerpolicy="no-referrer"
                         width="400" height="225">
                </div>
                <div class="visiter-poi-card__content">
                    <h3 class="visiter-poi-card__name"><?= e($poi['name']) ?></h3>
                    <div class="visiter-poi-card__station">
                        Station <?= stationLink($poi['station_name']) ?>
                    </div>
                    <div class="visiter-poi-card__lines">
                        <?php foreach ($poi['station_lines'] as $line): ?>
                        <span class="line-pill line-pill--<?= e(linePillShape($line)) ?> line-pill--<?= e($linePillSlug($line)) ?>"><?= e($line) ?></span>
                        <?php endforeach; ?>
                    </div>
                    <p class="visiter-poi-card__desc"><?= e($poi['description']) ?></p>
                </div>
            </li>
            <?php endforeach; ?>
        </ul>
        <p class="home-pois__cta">
            <a href="/visiter/" class="btn btn--ghost">Voir tous les lieux à visiter →</a>
        </p>
    </div>
</section>

<?php include __DIR__ . '/../ads/slot-in-article.php'; ?>

<!-- =========================================================================
     SECTION 6 — Le réseau en chiffres
     Réutilise partials/key-stats-grid.php
     ========================================================================= -->
<section class="section section--alt home-network">
    <div class="container">
        <h2>Le réseau de transport francilien en chiffres</h2>
        <p class="section__intro">
            L'un des réseaux de transport urbain les plus denses au monde.
            <strong>Cinq modes</strong> complémentaires couvrent Paris et l'ensemble
            de l'Île-de-France.
        </p>
        <?php
            // Sources : RATP officiel (16 lignes M1-M14+M3bis+M7bis, 13 lignes T1-T13)
            // SNCF officiel (8 lignes Transilien H/J/K/L/N/P/R/U)
            // RATP+Optile fusionnés en RATP Cap Île-de-France : ~350 lignes bus régionales
            $stats = $networkStats;
            include __DIR__ . '/../partials/key-stats-grid.php';
        ?>
    </div>
</section>

<!-- =========================================================================
     SECTION 7 — Notre approche du guide (3 USP + info-callout)
     ========================================================================= -->
<section class="section home-usp">
    <div class="container">
        <h2>BougeaParis.fr : Guide des transports parisiens</h2>
        <p class="section__intro">
            Un guide indépendant des transports parisiens, <strong>gratuit</strong>
            et <strong>sans publicité intrusive</strong>. Notre approche : croiser
            le transport et le tourisme, station par station.
        </p>
        <div class="home-usp-grid">
            <article class="home-usp-card">
                <h3>Des guides station par station</h3>
                <p>
                    Plutôt qu'une fiche technique sèche, chaque <strong>page station</strong>
                    raconte le quartier : <strong>histoire</strong>, <strong>anecdotes</strong>,
                    <strong>plan d'accès interne</strong>, <strong>sorties signalées</strong>
                    et <strong>lieux à voir autour</strong>. Plusieurs milliers de mots par
                    station, écrits à la main et mis à jour régulièrement.
                </p>
            </article>
            <article class="home-usp-card">
                <h3>Trafic temps réel</h3>
                <p>
                    Les <strong>perturbations du jour</strong> affichées sur la page d'accueil
                    et sur chaque page de ligne ou station concernée. Données
                    <strong>officielles IDF Mobilités</strong> (<strong>source PRIM</strong>),
                    agrégées avec un <strong>bulletin éditorial quotidien</strong> pour
                    le contexte.
                </p>
            </article>
            <article class="home-usp-card">
                <h3>Tous les modes, conseils touristiques inclus</h3>
                <p>
                    Tous les modes de transport franciliens — <strong>métro</strong>,
                    <strong>RER</strong>, <strong>bus</strong>, <strong>tramway</strong>,
                    <strong>Transilien</strong>, <strong>gares parisiennes</strong>,
                    <strong>liaisons aéroports</strong> — dans un seul guide. Pour chaque
                    station, les <strong>monuments</strong>, <strong>musées</strong> et
                    <strong>lieux à visiter</strong> à proximité avec la <strong>sortie à
                    privilégier</strong>. Une approche multimodale pensée pour les visiteurs.
                </p>
            </article>
        </div>

        <?php
            $icon    = '💡';
            $variant = 'info';
            $label   = 'À savoir';
            $body    = 'Tous les <strong>tarifs 2026</strong> affichés sur le site sont issus d\'une <strong>source unique</strong> mise à jour chaque janvier depuis la page officielle IDFM. Quand le tarif change, <strong>toutes les pages se mettent à jour automatiquement</strong>.';
            include __DIR__ . '/../partials/info-callout.php';
        ?>
    </div>
</section>

<!-- =========================================================================
     SECTION 8 — FAQ globale (8 questions + Schema.org FAQPage)
     Réutilise partials/faq-accordion.php
     ========================================================================= -->
<section class="section section--alt home-faq">
    <div class="container">
        <h2>Questions fréquentes</h2>
        <p class="section__intro">
            Les questions les plus fréquentes sur les <strong>transports parisiens</strong>
            en 2026 : tickets, horaires, accessibilité, aéroports.
        </p>
        <?php
            $openFirst = true;
            include __DIR__ . '/../partials/faq-accordion.php';
        ?>
    </div>
</section>

<!--
     Section 9 (maillage interne enrichi) supprimée le 2026-05-12.
     Raison : redondante avec Section 3 (mêmes destinations, même format cards).
     Le maillage interne reste assuré par la nav principale, les CTAs des sections
     et les liens éditoriaux dans les FAQ.
-->

<?php include __DIR__ . '/../ads/slot-footer.php'; ?>
