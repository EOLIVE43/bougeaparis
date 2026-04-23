<?php
/**
 * Page À propos
 */
$authors = Config::all('authors');
?>

<nav class="breadcrumb" aria-label="Fil d'Ariane">
    <div class="container">
        <ol class="breadcrumb__list">
            <li><a href="/">Accueil</a></li>
            <li class="breadcrumb__current">À propos</li>
        </ol>
    </div>
</nav>

<section class="hero">
    <div class="container">
        <h1 class="hero__title">À propos de BougeaParis.fr</h1>
        <p class="hero__subtitle">Un guide indépendant des transports parisiens, fait par des passionnés pour les Parisiens, les Franciliens et les visiteurs.</p>
    </div>
</section>

<section class="section">
    <div class="container" style="max-width:800px;">
        <h2>Notre mission</h2>
        <p>BougeaParis.fr a été créé avec une ambition simple : offrir un guide complet, clair et à jour sur les transports en commun à Paris et en Île-de-France. Que vous habitiez dans la capitale ou que vous veniez la visiter, vous trouverez ici toutes les informations dont vous avez besoin pour vous déplacer sereinement.</p>
        <p>Notre site couvre l'ensemble du réseau : métro, RER, bus, tramway, Transilien et accès aux aéroports. Pour chaque ligne et chaque station, nous compilons les plans, horaires, correspondances et conseils pratiques dans un format clair et facile à utiliser.</p>

        <h2>L'équipe</h2>
        <p>BougeaParis.fr est rédigé par une petite équipe passionnée :</p>

        <div style="display:grid; grid-template-columns:1fr; gap:2rem; margin-top:2rem;">
            <?php foreach ($authors as $author): ?>
            <div style="display:flex; gap:1.5rem; align-items:flex-start;">
                <img src="<?= e($author['avatar']) ?>" alt="<?= e($author['name']) ?>" width="80" height="80" style="flex-shrink:0; border-radius:50%;">
                <div>
                    <h3 style="margin-bottom:0.25rem;"><a href="<?= e($author['url']) ?>"><?= e($author['name']) ?></a></h3>
                    <p style="color:var(--color-text-muted); font-size:0.875rem; margin-bottom:0.5rem;"><?= e($author['role']) ?></p>
                    <p><?= e($author['bio']) ?></p>
                </div>
            </div>
            <?php endforeach; ?>
        </div>

        <h2>Site non officiel</h2>
        <p>BougeaParis.fr est un site indépendant. Nous n'avons aucun lien commercial ni contractuel avec la RATP, la SNCF, Île-de-France Mobilités ou tout autre opérateur de transport. Les informations que nous publions sont issues des données ouvertes officielles (PRIM, data.iledefrance-mobilites.fr) et de notre veille éditoriale.</p>
        <p>Les noms de lignes, les numéros et les couleurs utilisées sont des éléments d'information voyageur reconnus d'utilité publique. Nous ne reproduisons aucun logo officiel.</p>

        <h2>Nous contacter</h2>
        <p>Une question, une suggestion, un signalement d'erreur ? Écrivez-nous à <a href="mailto:<?= e($site['contact_email']) ?>"><?= e($site['contact_email']) ?></a>. Nous lisons tous les messages et répondons dans les meilleurs délais.</p>
    </div>
</section>
