<?php
return [
    'seo' => [
        'title'       => 'Transilien SNCF : 8 lignes de trains de banlieue en Île-de-France',
        'description' => 'Guide du réseau Transilien : lignes H, J, K, L, N, P, R, U. Horaires, tarifs, gares principales pour les trajets de banlieue parisienne.',
        'canonical'   => 'https://bougeaparis.fr/transilien/',
        'og_type'     => 'article',
    ],
    'hero' => [
        'h1'       => 'Les trains Transilien',
        'subtitle' => 'Le réseau de trains de banlieue de la SNCF : 8 lignes qui relient Paris à toute l\'Île-de-France.',
        'chiffres' => [
            ['value' => '8', 'label' => 'Lignes'],
            ['value' => '380+', 'label' => 'Gares'],
            ['value' => '900', 'label' => 'Km de réseau'],
            ['value' => '1,4M', 'label' => 'Voyageurs/jour'],
        ],
    ],
    'intro' => <<<'HTML'
<p class="lead">
    Le <strong>réseau Transilien</strong> est exploité par la SNCF et regroupe les <strong>trains
    de banlieue</strong> qui relient Paris à l'ensemble de l'Île-de-France. Il compte
    <strong>8 lignes</strong> identifiées par une lettre (H, J, K, L, N, P, R, U) et dessert
    <strong>plus de 380 gares</strong>.
</p>
<p>
    Contrairement au RER qui traverse Paris, les lignes Transilien partent de l'une des grandes
    <strong>gares parisiennes</strong> (Gare du Nord, Saint-Lazare, Est, Lyon, Montparnasse, La
    Défense) et rayonnent vers la grande couronne.
</p>
<p>
    Le Transilien est essentiel pour les Franciliens qui travaillent à Paris et habitent en grande
    banlieue. Il est souvent complémentaire du RER sur les mêmes axes.
</p>
HTML,
    'section_lignes' => [
        'title' => 'Les 8 lignes Transilien',
        'content' => <<<'HTML'
<ul>
    <li><strong>Ligne H (bleu clair)</strong> : de Paris-Nord vers le nord (Pontoise, Creil, Persan-Beaumont, Luzarches).</li>
    <li><strong>Ligne J (jaune)</strong> : de Paris-Saint-Lazare vers l'ouest (Mantes, Gisors, Ermont).</li>
    <li><strong>Ligne K (marron)</strong> : de Paris-Nord vers Crépy-en-Valois.</li>
    <li><strong>Ligne L (mauve)</strong> : de Paris-Saint-Lazare vers l'ouest (Versailles, Cergy, Saint-Nom-la-Bretèche).</li>
    <li><strong>Ligne N (vert)</strong> : de Paris-Montparnasse vers Rambouillet, Dreux, Mantes.</li>
    <li><strong>Ligne P (rose)</strong> : de Paris-Est vers Meaux, Château-Thierry, Provins.</li>
    <li><strong>Ligne R (rose clair)</strong> : de Paris-Gare de Lyon vers Melun, Montereau, Montargis.</li>
    <li><strong>Ligne U (rouge)</strong> : unique ligne sans passage par Paris, relie La Défense à La Verrière.</li>
</ul>
HTML,
    ],
    'section_tarifs' => [
        'title' => 'Tarifs Transilien en 2026',
        'content' => <<<'HTML'
<p>
    Depuis 2025, le tarif unique <strong>2,50 euros</strong> s'applique pour les voyages en Transilien
    dans toute l'Île-de-France (zones 1 à 5). Les cartes Navigo sont valables sur l'ensemble du réseau.
</p>
HTML,
    ],
    'faq' => [
        'title' => 'Questions fréquentes sur le Transilien',
        'items' => [
            ['question' => 'Quelle est la différence entre le RER et le Transilien ?',
             'answer'   => '<p>Le <strong>RER</strong> traverse Paris de part en part. Le <strong>Transilien</strong> part d\'une gare parisienne et rayonne vers la banlieue, sans traverser Paris.</p>'],
            ['question' => 'Peut-on utiliser la Navigo dans les Transilien ?',
             'answer'   => '<p>Oui, la Navigo (Easy, Semaine, Mois, Annuel) est valable sur l\'ensemble du réseau Transilien en zones 1 à 5, sans supplément.</p>'],
            ['question' => 'Les Transilien circulent-ils le week-end ?',
             'answer'   => '<p>Oui, les Transilien circulent 7 jours sur 7, avec des fréquences réduites le week-end. Des <strong>travaux de maintenance</strong> peuvent interrompre le service certains week-ends.</p>'],
            ['question' => 'Peut-on voyager avec un vélo dans un Transilien ?',
             'answer'   => '<p>Oui, les vélos sont autorisés en dehors des heures de pointe (généralement avant 6h30, entre 9h et 16h30, après 19h en semaine, et toute la journée le week-end).</p>'],
            ['question' => 'Quelle ligne Transilien pour aller à Versailles ?',
             'answer'   => '<p>La <strong>ligne L</strong> dessert la gare de Versailles-Rive-Droite depuis Paris-Saint-Lazare. La ligne N et le RER C desservent aussi Versailles (autres gares).</p>'],
        ],
    ],
];
