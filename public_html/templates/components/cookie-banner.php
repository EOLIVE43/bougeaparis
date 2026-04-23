<?php
/**
 * Banniere cookies RGPD simple (accepter / refuser)
 * Cache si l'utilisateur a deja choisi (localStorage).
 */
?>
<div class="bp-cookie-banner" id="bp-cookie-banner" hidden>
    <div class="bp-cookie-banner__inner">
        <div class="bp-cookie-banner__text">
            <p class="bp-cookie-banner__title"><strong>Cookies & vie privée</strong></p>
            <p class="bp-cookie-banner__desc">Nous utilisons des cookies pour mesurer l'audience du site (Google Analytics). Vos données restent anonymes et ne sont pas partagées. <a href="/confidentialite/">En savoir plus</a></p>
        </div>
        <div class="bp-cookie-banner__actions">
            <button type="button" class="bp-cookie-banner__btn bp-cookie-banner__btn--refuse" data-consent="denied">Refuser</button>
            <button type="button" class="bp-cookie-banner__btn bp-cookie-banner__btn--accept" data-consent="granted">Accepter</button>
        </div>
    </div>
</div>
<script>
(function(){
    var banner = document.getElementById('bp-cookie-banner');
    var consent = localStorage.getItem('bp_consent');
    if (consent === 'granted' || consent === 'denied') { return; }
    banner.hidden = false;
    banner.querySelectorAll('[data-consent]').forEach(function(btn){
        btn.addEventListener('click', function(){
            var value = btn.getAttribute('data-consent');
            localStorage.setItem('bp_consent', value);
            if (value === 'granted' && typeof gtag === 'function') {
                gtag('consent', 'update', {
                    'ad_storage': 'granted',
                    'ad_user_data': 'granted',
                    'ad_personalization': 'granted',
                    'analytics_storage': 'granted'
                });
            }
            banner.hidden = true;
        });
    });
})();
</script>
