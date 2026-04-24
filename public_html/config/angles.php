<?php
/**
 * config/angles.php
 *
 * Les 7 angles editoriaux tournants pour l'auto-generation d'articles quotidiens.
 */

return array(

    // LUNDI - Anticipation de la semaine
    1 => array(
        'code' => 'semaine-a-venir',
        'titre_type' => 'Les lignes a eviter cette semaine',
        'focus' => "Anticipation : identifier les lignes les plus impactees cette semaine (travaux longs, perturbations persistantes). Donner au lecteur une vision d'ensemble pour preparer ses deplacements.",
        'ton' => 'Pratique et projectif. Adresse-toi directement au lecteur qui prepare sa semaine.',
        'accroche_exemple' => "Bonne nouvelle ou gros casse-tete ? Voici les lignes a surveiller cette semaine.",
    ),

    // MARDI - Zoom travaux
    2 => array(
        'code' => 'zoom-travaux',
        'titre_type' => 'Le point travaux du jour',
        'focus' => "Mise en avant des chantiers en cours. Expliquer la cause des travaux, leur duree, leur impact, et quand ils prendront fin. Privilegier les perturbations liees a la cause TRAVAUX.",
        'ton' => 'Informatif et pedagogique. Le lecteur doit comprendre pourquoi ca travaille.',
        'accroche_exemple' => "La modernisation du reseau continue. Voici les chantiers qui impactent votre trajet aujourd'hui.",
    ),

    // MERCREDI - Chiffres et data
    3 => array(
        'code' => 'chiffres',
        'titre_type' => 'Le trafic en chiffres',
        'focus' => "Donner des chiffres concrets : nombre de lignes perturbees, nombre de perturbations par mode, severite. Mettre en perspective avec le reseau global.",
        'ton' => 'Factuel et synthetique. Data-driven.',
        'accroche_exemple' => "X lignes perturbees ce matin en Ile-de-France. Tour d'horizon chiffre.",
    ),

    // JEUDI - Analyse d'actualite
    4 => array(
        'code' => 'analyse',
        'titre_type' => "Ce qu'il faut retenir du reseau aujourd'hui",
        'focus' => "Prendre du recul. Analyser une perturbation significative en detail (cause, impact, historique si possible, alternatives).",
        'ton' => 'Journalistique et pose. Comme un article de fond court.',
        'accroche_exemple' => "Une perturbation retient l'attention ce matin. Decryptage.",
    ),

    // VENDREDI - Preparer le week-end
    5 => array(
        'code' => 'weekend',
        'titre_type' => 'Preparer votre week-end transports',
        'focus' => "Anticiper le week-end : quels travaux sont programmes samedi-dimanche, quelles lignes risquent d'etre impactees, quels changements de service.",
        'ton' => 'Amical et pratique. On prepare le week-end du lecteur.',
        'accroche_exemple' => "Le week-end approche : voici ce qu'il faut savoir pour circuler sereinement.",
    ),

    // SAMEDI - Trajets culture et loisirs
    6 => array(
        'code' => 'culture-loisirs',
        'titre_type' => 'Trajets culture et loisirs',
        'focus' => "Angle touristique/loisirs. Etat du reseau avec un accent sur les lignes qui desservent les grands lieux culturels (Louvre, Versailles, La Defense, Disneyland, grands musees, stades).",
        'ton' => 'Decontracte et accueillant. Parle aux Parisiens comme aux visiteurs.',
        'accroche_exemple' => "Musee, concert, shopping : on fait le point sur les transports pour votre journee.",
    ),

    // DIMANCHE - Bilan et anticipation
    7 => array(
        'code' => 'bilan-semaine',
        'titre_type' => 'Bilan de la semaine et anticipation',
        'focus' => "Dimanche, on fait le bilan : quelles lignes ont ete les plus impactees cette semaine, qu'est-ce qui a ete resolu, qu'est-ce qui continue la semaine prochaine.",
        'ton' => 'Reflexif et projectif. Regard sur la semaine passee et la suivante.',
        'accroche_exemple' => "Semaine difficile sur le reseau ? Bilan et projection pour les jours a venir.",
    ),

);
