<?php
/**
 * Front controller - BougeaParis.fr
 *
 * Point d'entree unique de l'application.
 * .htaccess redirige toutes les requetes non-fichier vers ce fichier.
 */

// Chargement du noyau
require __DIR__ . '/core/Config.php';
require __DIR__ . '/core/bootstrap.php';

// Recuperer le chemin demande
$uri = parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH);
$uri = rtrim($uri, '/') ?: '/';

// Router simplifie
$routes = [
    '/'                   => 'home',
    '/metro'              => 'metro-hub',
    '/rer'                => 'rer-hub',
    '/bus'                => 'bus-hub',
    '/tramway'            => 'tramway-hub',
    '/aeroports'          => 'aeroports-hub',
    '/transilien'         => 'transilien-hub',
    '/blog'               => 'blog-index',
    '/a-propos'           => 'about',
    '/contact'            => 'contact',
    '/mentions-legales'   => 'legal',
    '/confidentialite'    => 'privacy',
    '/auteur/ludo'        => 'author-ludo',
    '/auteur/elodie'      => 'author-elodie',
];

if (isset($routes[$uri])) {
    $page = $routes[$uri];
} else {
    http_response_code(404);
    $page = '404';
}

// Verification que le template existe
$templatePath = __DIR__ . '/templates/pages/' . $page . '.php';
if (!file_exists($templatePath)) {
    // Fallback 404 si la page n'existe pas encore
    http_response_code(404);
    $page = '404';
}

// Rendu
$tpl = new Template($page);

// Configuration SEO par defaut selon la page
configureSeoForPage($tpl, $page, $uri);

$tpl->render();


/**
 * Configure les meta SEO par defaut pour chaque page
 */
function configureSeoForPage(Template $tpl, string $page, string $uri): void
{
    $site = Config::all('site');

    switch ($page) {
        case 'home':
            $tpl->seo
                ->setTitle('Guide des transports parisiens', true)
                ->setDescription('Metro, RER, bus, tramway, aeroports : retrouvez tout ce qu\'il faut savoir pour vous deplacer a Paris et en Ile-de-France. Horaires, itineraires, trafic en temps reel.')
                ->setCanonical('/')
                ->addSchema([
                    '@context' => 'https://schema.org',
                    '@type'    => 'WebSite',
                    'name'     => $site['brand_name'],
                    'alternateName' => 'Bouge a Paris',
                    'url'      => $site['url'],
                    'potentialAction' => [
                        '@type' => 'SearchAction',
                        'target' => [
                            '@type' => 'EntryPoint',
                            'urlTemplate' => $site['url'] . '/recherche/?q={search_term_string}',
                        ],
                        'query-input' => 'required name=search_term_string',
                    ],
                ])
                ->addSchema([
                    '@context' => 'https://schema.org',
                    '@type'    => 'Organization',
                    'name'     => $site['brand_name'],
                    'url'      => $site['url'],
                    'logo'     => $site['url'] . $site['logo_svg'],
                    'email'    => $site['contact_email'],
                ]);
            break;

        case 'metro-hub':
            $tpl->seo
                ->setTitle('Metro de Paris : lignes, stations et horaires')
                ->setDescription('Le guide complet du metro parisien : 16 lignes, plus de 300 stations, plans, horaires et trafic en temps reel.')
                ->setCanonical($uri . '/')
                ->setBreadcrumb([
                    ['label' => 'Accueil', 'url' => '/'],
                    ['label' => 'Metro',   'url' => '/metro/'],
                ]);
            break;

        case 'rer-hub':
            $tpl->seo
                ->setTitle('RER Paris : lignes A, B, C, D, E')
                ->setDescription('Le reseau RER d\'Ile-de-France : 5 lignes pour se deplacer rapidement entre Paris et la banlieue. Horaires, stations et trafic.')
                ->setCanonical($uri . '/')
                ->setBreadcrumb([
                    ['label' => 'Accueil', 'url' => '/'],
                    ['label' => 'RER',     'url' => '/rer/'],
                ]);
            break;

        case 'bus-hub':
            $tpl->seo
                ->setTitle('Bus a Paris : lignes de jour et Noctilien')
                ->setDescription('Le reseau de bus parisien : lignes de jour, bus de nuit Noctilien, arrets, horaires et trafic temps reel.')
                ->setCanonical($uri . '/')
                ->setBreadcrumb([
                    ['label' => 'Accueil', 'url' => '/'],
                    ['label' => 'Bus',     'url' => '/bus/'],
                ]);
            break;

        case 'tramway-hub':
            $tpl->seo
                ->setTitle('Tramway de Paris et d\'Ile-de-France')
                ->setDescription('Les 14 lignes de tramway de la region parisienne : trace, arrets, correspondances et horaires.')
                ->setCanonical($uri . '/')
                ->setBreadcrumb([
                    ['label' => 'Accueil', 'url' => '/'],
                    ['label' => 'Tramway', 'url' => '/tramway/'],
                ]);
            break;

        case 'aeroports-hub':
            $tpl->seo
                ->setTitle('Aeroports de Paris : CDG, Orly, Beauvais')
                ->setDescription('Comment rejoindre les aeroports parisiens : Charles-de-Gaulle, Orly et Beauvais. Train, bus, RER, taxi et VTC.')
                ->setCanonical($uri . '/')
                ->setBreadcrumb([
                    ['label' => 'Accueil',   'url' => '/'],
                    ['label' => 'Aeroports', 'url' => '/aeroports/'],
                ]);
            break;

        case 'transilien-hub':
            $tpl->seo
                ->setTitle('Transilien : trains de banlieue en Ile-de-France')
                ->setDescription('Les lignes Transilien H, J, K, L, N, P, R et U. Horaires, gares et informations sur les trains de banlieue parisiens.')
                ->setCanonical($uri . '/')
                ->setBreadcrumb([
                    ['label' => 'Accueil',    'url' => '/'],
                    ['label' => 'Transilien', 'url' => '/transilien/'],
                ]);
            break;

        case 'blog-index':
            $tpl->seo
                ->setTitle('Blog : actualites des transports parisiens')
                ->setDescription('Toute l\'actualite des transports a Paris : trafic, travaux, nouveautes du reseau, conseils pratiques et bons plans.')
                ->setCanonical('/blog/');
            break;

        case 'about':
            $tpl->seo
                ->setTitle('A propos')
                ->setDescription('Decouvrez BougeaParis.fr, le guide independant des transports parisiens redige par Ludo et Elodie.')
                ->setCanonical('/a-propos/');
            break;

        case 'contact':
            $tpl->seo
                ->setTitle('Contact')
                ->setDescription('Contactez l\'equipe de BougeaParis.fr pour toute question, suggestion ou signalement.')
                ->setCanonical('/contact/');
            break;

        case 'legal':
            $tpl->seo
                ->setTitle('Mentions legales')
                ->setDescription('Mentions legales de BougeaParis.fr.')
                ->setCanonical('/mentions-legales/');
            break;

        case 'privacy':
            $tpl->seo
                ->setTitle('Politique de confidentialite')
                ->setDescription('Politique de confidentialite et gestion des donnees sur BougeaParis.fr.')
                ->setCanonical('/confidentialite/');
            break;

        case 'author-ludo':
        case 'author-elodie':
            $slug = str_replace('author-', '', $page);
            $author = Config::get("authors.$slug");
            if ($author) {
                $tpl->seo
                    ->setTitle($author['name'] . ' - ' . $author['role'])
                    ->setDescription($author['bio'])
                    ->setCanonical($author['url']);
                $tpl->with('author', $author);
            }
            break;

        case '404':
            $tpl->seo
                ->setTitle('Page introuvable')
                ->setDescription('Cette page n\'existe pas ou a ete deplacee.');
            break;
    }
}
