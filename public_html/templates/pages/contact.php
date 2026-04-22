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
        <p class="hero__subtitle">Une question, une suggestion, un signalement d'erreur ? Ecrivez-nous, nous lisons tous les messages.</p>
    </div>
</section>

<section class="section">
    <div class="container" style="max-width:700px;">
        <h2>Par email</h2>
        <p>Pour toute demande, ecrivez a <a href="mailto:<?= e($site['contact_email']) ?>"><?= e($site['contact_email']) ?></a>.</p>

        <p>Nous traitons notamment :</p>
        <ul>
            <li>Les signalements d'erreurs ou d'informations obsoletes</li>
            <li>Les suggestions de contenu ou de fonctionnalites</li>
            <li>Les demandes de partenariats editoriaux</li>
            <li>Les questions sur la vie privee et vos donnees</li>
        </ul>

        <p>Nous repondons generalement sous 48 a 72 heures ouvrees.</p>

        <h2>Vous etes journaliste ou professionnel ?</h2>
        <p>Pour toute demande presse, partenariat ou collaboration editoriale, merci de preciser votre media ou organisation dans le sujet de votre email.</p>
    </div>
</section>
