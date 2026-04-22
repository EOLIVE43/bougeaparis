<?php
/**
 * Slot AdSense - In-article
 */
$adsConfig = $ads ?? Config::all('ads');
if (!$adsConfig['enabled'] || empty($adsConfig['publisher_id']) || empty($adsConfig['slots']['in_article']['slot_id'])) {
    return;
}
$s = $adsConfig['slots']['in_article'];
?>
<div class="ad-slot ad-slot--in-article">
    <span class="ad-slot__label">Publicite</span>
    <ins class="adsbygoogle"
         style="display:block; text-align:center;"
         data-ad-layout="<?= e($s['layout']) ?>"
         data-ad-format="<?= e($s['format']) ?>"
         data-ad-client="<?= e($adsConfig['publisher_id']) ?>"
         data-ad-slot="<?= e($s['slot_id']) ?>"></ins>
    <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
</div>
