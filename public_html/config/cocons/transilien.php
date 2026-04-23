<?php
return [
    'seo' => [
        'title'       => 'Transilien SNCF : 8 lignes de trains de banlieue en Ile-de-France',
        'description' => 'Guide du reseau Transilien : lignes H, J, K, L, N, P, R, U. Horaires, tarifs, gares principales pour les trajets de banlieue parisienne.',
        'canonical'   => 'https://bougeaparis.fr/transilien/',
        'og_type'     => 'article',
    ],
    'hero' => [
        'h1'       => 'Les trains Transilien',
        'subtitle' => 'Le reseau de trains de banlieue de la SNCF : 8 lignes qui relient Paris a toute l\'Ile-de-France.',
        'chiffres' => [
            ['value' => '8', 'label' => 'Lignes'],
            ['value' => '380+', 'label' => 'Gares'],
            ['value' => '900', 'label' => 'Km de reseau'],
            ['value' => '1,4M', 'label' => 'Voyageurs/jour'],
        ],
    ],
    'intro' => <<<'HTML'
<p class="lead">
    Le <strong>reseau Transilien</strong> est exploite par la SNCF et regroupe les <strong>trains
    de banlieue</strong> qui relient Paris a l'ensemble de l'Ile-de-France. Il compte
    <strong>8 lignes</strong> identifiees par une lettre (H, J, K, L, N, P, R, U) et dessert
    <strong>plus de 380 gares</strong>.
</p>
<p>
    Contrairement au RER qui traverse Paris, les lignes Transilien partent de l'une des grandes
    <strong>gares parisiennes</strong> (Gare du Nord, Saint-Lazare, Est, Lyon, Montparnasse, La
    Defense) et rayonnent vers la grande couronne.
</p>
<p>
    Le Transilien est essentiel pour les Franciliens qui travaillent a Paris et habitent en grande
    banlieue. Il est souvent complementaire du RER sur les memes axes.
</p>
HTML,
    'section_lignes' => [
        'title' => 'Les 8 lignes Transilien',
        'content' => <<<'HTML'
<ul>
    <li><strong>Ligne H (bleu clair)</strong> : de Paris-Nord vers le nord (Pontoise, Creil, Persan-Beaumont, Luzarches).</li>
    <li><strong>Ligne J (jaune)</strong> : de Paris-Saint-Lazare vers l'ouest (Mantes, Gisors, Ermont).</li>
    <li><strong>Ligne K (marron)</strong> : de Paris-Nord vers Crepy-en-Valois.</li>
    <li><strong>Ligne L (mauve)</strong> : de Paris-Saint-Lazare vers l'ouest (Versailles, Cergy, Saint-Nom-la-Breteche).</li>
    <li><strong>Ligne N (vert)</strong> : de Paris-Montparnasse vers Rambouillet, Dreux, Mantes.</li>
    <li><strong>Ligne P (rose)</strong> : de Paris-Est vers Meaux, Chateau-Thierry, Provins.</li>
    <li><strong>Ligne R (rose clair)</strong> : de Paris-Gare de Lyon vers Melun, Montereau, Montargis.</li>
    <li><strong>Ligne U (rouge)</strong> : unique ligne sans passage par Paris, relie La Defense a La Verriere.</li>
</ul>
HTML,
    ],
    'section_tarifs' => [
        'title' => 'Tarifs Transilien en 2026',
        'content' => <<<'HTML'
<p>
    Depuis 2025, le tarif unique <strong>2,50 euros</strong> s'applique pour les voyages en Transilien
    dans toute l'Ile-de-France (zones 1 a 5). Les cartes Navigo sont valables sur l'ensemble du reseau.
</p>
HTML,
    ],
    'faq' => [
        'title' => 'Questions frequentes sur le Transilien',
        'items' => [
            ['question' => 'Quelle est la difference entre le RER et le Transilien ?',
             'answer'   => '<p>Le <strong>RER</strong> traverse Paris de part en part. Le <strong>Transilien</strong> part d\'une gare parisienne et rayonne vers la banlieue, sans traverser Paris.</p>'],
            ['question' => 'Peut-on utiliser la Navigo dans les Transilien ?',
             'answer'   => '<p>Oui, la Navigo (Easy, Semaine, Mois, Annuel) est valable sur l\'ensemble du reseau Transilien en zones 1 a 5, sans supplement.</p>'],
            ['question' => 'Les Transilien circulent-ils le week-end ?',
             'answer'   => '<p>Oui, les Transilien circulent 7 jours sur 7, avec des frequences reduites le week-end. Des <strong>travaux de maintenance</strong> peuvent interrompre le service certains week-ends.</p>'],
            ['question' => 'Peut-on voyager avec un velo dans un Transilien ?',
             'answer'   => '<p>Oui, les velos sont autorises en dehors des heures de pointe (generalement avant 6h30, entre 9h et 16h30, apres 19h en semaine, et toute la journee le week-end).</p>'],
            ['question' => 'Quelle ligne Transilien pour aller a Versailles ?',
             'answer'   => '<p>La <strong>ligne L</strong> dessert la gare de Versailles-Rive-Droite depuis Paris-Saint-Lazare. La ligne N et le RER C desservent aussi Versailles (autres gares).</p>'],
        ],
    ],
];
