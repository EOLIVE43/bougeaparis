<?php
/**
 * Page A propos
 */
$authors = Config::all('authors');
?>
<nav class="breadcrumb" aria-label="Fil d'Ariane">
    <div class="container">
        <ol class="breadcrumb__list">
            <li><a href="/">Accueil</a></li>
            <li class="breadcrumb__current">A propos</li>
        </ol>
    </div>
</nav>

<section class="hero">
    <div class="container">
        <h1 class="hero__title">A propos de BougeaParis.fr</h1>
        <p class="hero__subtitle">Un guide independant des transports parisiens, fait par des passionnes pour les Parisiens, les Franciliens et les visiteurs.</p>
    </div>
</section>

<section class="section">
    <div class="container" style="max-width:800px;">
        <h2>Notre mission</h2>
        <p>BougeaParis.fr a ete cree avec une ambition simple : offrir un guide complet, clair et a jour sur les transports en commun a Paris et en Ile-de-France. Que vous habitiez dans la capitale ou que vous veniez la visiter, vous trouverez ici toutes les informations dont vous avez besoin pour vous deplacer sereinement.</p>

        <p>Notre site couvre l'ensemble du reseau : metro, RER, bus, tramway, Transilien et acces aux aeroports. Pour chaque ligne et chaque station, nous compilons les plans, horaires, correspondances et conseils pratiques dans un format clair et facile a utiliser.</p>

        <h2>L'equipe</h2>
        <p>BougeaParis.fr est redige par une petite equipe passionnee :</p>

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
        <p>BougeaParis.fr est un site independant. Nous n'avons aucun lien commercial ni contractuel avec la RATP, la SNCF, Ile-de-France Mobilites ou tout autre operateur de transport. Les informations que nous publions sont issues des donnees ouvertes officielles (PRIM, data.iledefrance-mobilites.fr) et de notre veille editoriale.</p>

        <p>Les noms de lignes, les numeros et les couleurs utilisees sont des elements d'information voyageur reconnus d'utilite publique. Nous ne reproduisons aucun logo officiel.</p>

        <h2>Nous contacter</h2>
        <p>Une question, une suggestion, un signalement d'erreur ? Ecrivez-nous a <a href="mailto:<?= e($site['contact_email']) ?>"><?= e($site['contact_email']) ?></a>. Nous lisons tous les messages et repondons dans les meilleurs delais.</p>
    </div>
</section>
