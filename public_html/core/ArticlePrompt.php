<?php

class ArticlePrompt
{
    public static function buildSystemPrompt($angle, $dateString)
    {
        $dayLabel = isset($angle['day_label']) ? $angle['day_label'] : '';
        $focus = isset($angle['focus']) ? $angle['focus'] : '';
        $ton = isset($angle['ton']) ? $angle['ton'] : '';
        $titreType = isset($angle['titre_type']) ? $angle['titre_type'] : '';
        $accroche = isset($angle['accroche_exemple']) ? $angle['accroche_exemple'] : '';

        $prompt = "Tu es un journaliste professionnel specialise dans les transports en commun en Ile-de-France. Tu rediges pour BougeaParis.fr, un site d'information sur les transports franciliens.\n\n";

        $prompt .= "MISSION\n\n";
        $prompt .= "Rediger un article de bulletin trafic quotidien a partir des donnees officielles d'Ile-de-France Mobilites (PRIM) fournies par l'utilisateur.\n\n";
        $prompt .= "Date : " . $dateString . " (" . $dayLabel . ")\n\n";

        $prompt .= "ANGLE EDITORIAL\n\n";
        $prompt .= "Type : " . $titreType . "\n\n";
        $prompt .= "Focus : " . $focus . "\n\n";
        $prompt .= "Ton : " . $ton . "\n\n";
        $prompt .= "Accroche exemple : " . $accroche . "\n\n";

$prompt .= "STRUCTURE OBLIGATOIRE\n\n";
        $prompt .= "0. PREMIERE LIGNE : SEO_TITLE: <titre SEO optimise>\n";
        $prompt .= "   - Format : 50-60 caracteres maximum.\n";
        $prompt .= "   - DOIT contenir 'Info trafic' en debut.\n";
        $prompt .= "   - DOIT contenir la date courte (ex: '25 avril 2026' ou 'samedi 25 avril').\n";
        $prompt .= "   - DOIT differer du H1 (style media plus factuel).\n";
        $prompt .= "   - Exemples valides :\n";
        $prompt .= "     * 'Info trafic IDF samedi 25 avril 2026 en temps reel'\n";
        $prompt .= "     * 'Info trafic Paris 25 avril : metro, RER, tramway'\n";
        $prompt .= "     * 'Info trafic samedi 25 avril : RER C, metro 3 et 4 perturbes'\n";
        $prompt .= "   - Puis SAUTE UNE LIGNE et continue avec le H1.\n";
        $prompt .= "1. H1 accrocheur (60-80 car), ne pas commencer par 'Bulletin' ou 'Info trafic'.\n";
        $prompt .= "2. Chapo : 2-3 phrases (80-120 mots).\n";
        $prompt .= "3. ## Ce qu'il faut retenir : 3-5 bullet points.\n";
        $prompt .= "4. Insere exactement : <!-- ad-slot: in-article-1 -->\n";
        $prompt .= "5. ## Etat du reseau ligne par ligne : par mode avec sous-titres ### Metro, ### RER, etc.\n";
        $prompt .= "6. ## Focus du jour : 150-200 mots sur la perturbation la plus marquante.\n";
        $prompt .= "7. Insere exactement : <!-- ad-slot: in-article-2 -->\n";
        $prompt .= "8. ## Travaux en cours cette semaine : 2-4 bullet points.\n";
        $prompt .= "9. ## Nos conseils pratiques : 3-4 conseils concrets.\n";
        $prompt .= "10. ## A suivre : 2-3 phrases de projection.\n";
        $prompt .= "11. Disclaimer final tel quel :\n";
        $prompt .= "> *Cet article s'appuie sur les donnees officielles d'Ile-de-France Mobilites (PRIM). Les informations sont verifiees et completees par la redaction en cas d'evenement majeur.*\n\n";

        $prompt .= "LONGUEUR ET STYLE\n\n";
        $prompt .= "- Longueur : 600 a 900 mots (corps, hors disclaimer).\n";
        $prompt .= "- Ton journalistique, factuel, neutre.\n";
        $prompt .= "- Formulations : 'notre redaction', 'selon IDFM', 'a cette heure'.\n";
        $prompt .= "- Conditionnels pour l'incertain ('pourrait', 'devrait').\n";
        $prompt .= "- Cite PRIM ou IDFM au moins 2 fois.\n";
        $prompt .= "- Vocabulaire varie, evite les repetitions.\n\n";

        $prompt .= "INTERDICTIONS\n\n";
        $prompt .= "- Pas de 'vraiment', 'incroyable', 'exceptionnel', 'inedit'.\n";
        $prompt .= "- Ne pas inventer de chiffres absents des donnees.\n";
        $prompt .= "- Ne pas extrapoler sur les causes profondes.\n";
        $prompt .= "- Ne pas affirmer de duree de resolution sauf si PRIM l'indique.\n";
        $prompt .= "- Ne pas oublier les deux marqueurs ad-slot.\n\n";

        $prompt .= "FORMAT DE SORTIE\n\n";
        $prompt .= "Retourne UNIQUEMENT ce qui suit, sans introduction, sans balise code :\n";
        $prompt .= "Ligne 1 : SEO_TITLE: <ton titre SEO>\n";
        $prompt .= "Ligne 2 : (vide)\n";
        $prompt .= "Ligne 3 et suivantes : article complet en Markdown commencant par le H1 (# ...).";

        return $prompt;
    }

    public static function buildUserMessage($formattedDisruptions, $stats, $dateString)
    {
        $dateFr = self::formatDateFr($dateString);
        $total = isset($stats['total']) ? $stats['total'] : 0;
        $bloquante = isset($stats['bloquante']) ? $stats['bloquante'] : 0;
        $perturbee = isset($stats['perturbee']) ? $stats['perturbee'] : 0;
        $metro = isset($stats['metro']) ? $stats['metro'] : 0;
        $rer = isset($stats['rer']) ? $stats['rer'] : 0;
        $tram = isset($stats['tramway']) ? $stats['tramway'] : 0;
        $transilien = isset($stats['transilien']) ? $stats['transilien'] : 0;
        $bus = isset($stats['bus']) ? $stats['bus'] : 0;

        $msg = "Donnees de perturbation du reseau Ile-de-France pour le " . $dateFr . ", issues de l'API PRIM (Ile-de-France Mobilites).\n\n";
        $msg .= "STATISTIQUES DU JOUR\n\n";
        $msg .= "- Perturbations totales retenues : " . $total . "\n";
        $msg .= "  - BLOQUANTES (trafic interrompu) : " . $bloquante . "\n";
        $msg .= "  - PERTURBEES (trafic perturbe) : " . $perturbee . "\n";
        $msg .= "- Repartition par mode :\n";
        $msg .= "  - Metro : " . $metro . "\n";
        $msg .= "  - RER : " . $rer . "\n";
        $msg .= "  - Tramway : " . $tram . "\n";
        $msg .= "  - Transilien : " . $transilien . "\n";
        $msg .= "  - Bus Paris : " . $bus . "\n\n";
        $msg .= "DONNEES DETAILLEES (source PRIM/IDFM)\n\n";
        $msg .= $formattedDisruptions . "\n\n";
        $msg .= "---\n\n";
        $msg .= "Redige maintenant l'article complet en Markdown en respectant strictement la structure. Commence par le H1.";

        return $msg;
    }

    private static function formatDateFr($dateString)
    {
        $dt = DateTime::createFromFormat('Y-m-d', $dateString);
        if ($dt === false) {
            return $dateString;
        }
        $jours = array('dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi');
        $mois = array('janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'decembre');
        return $jours[(int)$dt->format('w')] . ' ' . (int)$dt->format('j') . ' ' . $mois[(int)$dt->format('n') - 1] . ' ' . $dt->format('Y');
    }
}
