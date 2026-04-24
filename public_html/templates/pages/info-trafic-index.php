<?php
/**
 * Template : info-trafic-index.php
 *
 * Page d'accueil de la rubrique /info-trafic/
 *
 * Version minimale ce soir : annonce + lien vers le(s) article(s) existant(s).
 * La version paginee complete viendra en Livraison 4.2.
 *
 * Donnees attendues :
 *   $articles : array de Article (peut etre vide)
 */

/** @var Article[] $articles */

$tpl->seo
    ->setTitle('Info-Trafic : état du réseau en temps réel')
    ->setDescription('Suivez chaque jour l\'état du trafic des transports en commun en Île-de-France : métro, RER, bus, tramway, Transilien. Informations quotidiennes et alertes.')
    ->setCanonical('/info-trafic/')
    ->setBreadcrumb([
        ['label' => 'Accueil',     'url' => '/'],
        ['label' => 'Info-Trafic', 'url' => '/info-trafic/'],
    ]);
?>

<div class="page-hub">

    <nav class="breadcrumb" aria-label="Fil d'Ariane">
        <ol>
            <li><a href="/">Accueil</a></li>
            <li aria-current="page">Info-Trafic</li>
        </ol>
    </nav>

    <header class="hub-header">
        <h1 class="hub-title">Info-Trafic en Île-de-France</h1>
        <p class="hub-intro">
            Chaque jour, retrouvez ici l'état du trafic des transports en commun franciliens :
            métro, RER, bus, tramway et Transilien. Perturbations, travaux, grèves,
            et conseils pour adapter vos trajets.
        </p>
    </header>

    <?php if (!empty($articles)): ?>
        <section class="article-list">
            <h2 class="sr-only">Articles récents</h2>
            <ul class="article-list__items">
                <?php foreach ($articles as $a): ?>
                    <?php $author = $a->getAuthorInfo(); ?>
                    <li class="article-card">
                        <a href="<?= e($a->getUrl()) ?>" class="article-card__link">
                            <?php if ($a->getImage()): ?>
                                <div class="article-card__image">
                                    <img src="<?= e($a->getImage()) ?>"
                                         alt="<?= e($a->getImageAlt()) ?>"
                                         width="600"
                                         height="315"
                                         loading="lazy"
                                         decoding="async">
                                </div>
                            <?php endif; ?>
                            <div class="article-card__body">
                                <time class="article-card__date" datetime="<?= e($a->getDateIso()) ?>">
                                    <?= e($a->getDateFormatted()) ?>
                                </time>
                                <h3 class="article-card__title"><?= e($a->getTitle()) ?></h3>
                                <?php if ($a->getExcerpt()): ?>
                                    <p class="article-card__excerpt"><?= e($a->getExcerpt()) ?></p>
                                <?php endif; ?>
                                <span class="article-card__author">
                                    Par <?= e($author['full_name'] ?? $author['name']) ?>
                                </span>
                            </div>
                        </a>
                    </li>
                <?php endforeach; ?>
            </ul>
        </section>
    <?php else: ?>
        <section class="info-box">
            <h2>Rubrique en cours de construction</h2>
            <p>
                Cette rubrique publiera chaque matin un bulletin détaillé sur l'état
                du trafic francilien. Les premiers articles arriveront très bientôt.
            </p>
            <p>
                En attendant, retrouvez toutes les informations sur les transports
                en Île-de-France dans nos <a href="/metro">pages dédiées au métro</a>,
                <a href="/rer">RER</a>, <a href="/bus">bus</a>, <a href="/tramway">tramway</a>,
                <a href="/transilien">Transilien</a> et <a href="/aeroports">aéroports</a>.
            </p>
        </section>
    <?php endif; ?>

</div>
