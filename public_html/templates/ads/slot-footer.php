<?php
/**
 * Slot AdSense - Footer
 */
$adsConfig = $ads ?? Config::all('ads');
if (!$adsConfig['enabled'] || empty($adsConfig['publisher_id']) || empty($adsConfig['slots']['footer']['slot_id'])) {
    return;
}
$s = $adsConfig['slots']['footer'];
?>
<div class="ad-slot ad-slot--footer">
    <span class="ad-slot__label">Publicite</span>
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="<?= e($adsConfig['publisher_id']) ?>"
         data-ad-slot="<?= e($s['slot_id']) ?>"
         data-ad-format="<?= e($s['format']) ?>"
         data-full-width-responsive="true"></ins>
    <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
</div>
