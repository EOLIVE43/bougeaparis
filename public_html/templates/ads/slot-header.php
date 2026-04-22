<?php
/**
 * Slot AdSense - Header
 * S'active automatiquement quand enabled=true et slot_id rempli dans config/ads.php
 */
$adsConfig = $ads ?? Config::all('ads');
if (!$adsConfig['enabled'] || empty($adsConfig['publisher_id']) || empty($adsConfig['slots']['header']['slot_id'])) {
    return;
}
$s = $adsConfig['slots']['header'];
?>
<div class="ad-slot ad-slot--header">
    <span class="ad-slot__label">Publicite</span>
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="<?= e($adsConfig['publisher_id']) ?>"
         data-ad-slot="<?= e($s['slot_id']) ?>"
         data-ad-format="<?= e($s['format']) ?>"
         <?php if (!empty($s['layout'])): ?>data-full-width-responsive="true"<?php endif; ?>></ins>
    <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
</div>
