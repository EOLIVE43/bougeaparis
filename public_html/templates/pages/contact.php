<?php
/**
 * Page Contact
 */
?>

<nav class="breadcrumb" aria-label="Fil d'Ariane">
    <div class="container">
        <ol class="breadcrumb__list">
            <li><a href="/">Accueil</a></li>
            <li class="breadcrumb__current">Contact</li>
        </ol>
    </div>
</nav>

<section class="hero">
    <div class="container">
        <h1 class="hero__title">Nous contacter</h1>
        <p class="hero__subtitle">Une question, une suggestion, un signalement d'erreur ? Écrivez-nous, nous lisons tous les messages.</p>
    </div>
</section>

<section class="section">
    <div class="container" style="max-width:700px;">
        <h2>Par email</h2>
        <p>Pour toute demande, écrivez à <a href="mailto:<?= e($site['contact_email']) ?>"><?= e($site['contact_email']) ?></a>.</p>

        <p>Nous traitons notamment :</p>
        <ul>
            <li>Les signalements d'erreurs ou d'informations obsolètes</li>
            <li>Les suggestions de contenu ou de fonctionnalités</li>
            <li>Les demandes de partenariats éditoriaux</li>
            <li>Les questions sur la vie privée et vos données</li>
        </ul>
        <p>Nous répondons généralement sous 48 à 72 heures ouvrées.</p>

        <h2>Vous êtes journaliste ou professionnel ?</h2>
        <p>Pour toute demande presse, partenariat ou collaboration éditoriale, merci de préciser votre média ou organisation dans le sujet de votre email.</p>
    </div>
</section>
