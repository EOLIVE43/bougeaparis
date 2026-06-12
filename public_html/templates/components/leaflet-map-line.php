<?php
/**
 * Composant leaflet-map-line : carte Leaflet OSM auto-chargée via IntersectionObserver.
 *
 * CWV-safe :
 *  - Hauteur container FIXE (400 px) → CLS = 0
 *  - Skeleton state visible avant chargement Leaflet
 *  - Leaflet (CSS + JS) chargé à la demande quand la carte entre dans le viewport
 *  - rootMargin: 200px → anticipation 200px avant entrée viewport
 *  - Si l'utilisateur ne scrolle jamais, rien n'est chargé
 *
 * Props attendus :
 *   $props['line_data'] = JSON ligne (stations[], color, code)
 *   $props['map_id']    = optionnel, ID unique de la carte
 */
$line_data = $props['line_data'] ?? [];
$stations  = $line_data['stations'] ?? [];
if (empty($stations)) return;

$mapId = $props['map_id'] ?? 'map-line-' . strtolower($line_data['code'] ?? 'x');
$color = $line_data['color'] ?? '#0F6E56';
?>
<div class="leaflet-wrapper">
  <div id="<?= htmlspecialchars($mapId) ?>"
       class="leaflet-map"
       data-stations='<?= htmlspecialchars(json_encode($stations, JSON_UNESCAPED_UNICODE), ENT_QUOTES) ?>'
       data-color="<?= htmlspecialchars($color) ?>"
       role="region"
       aria-label="Carte interactive de la ligne <?= htmlspecialchars($line_data['code'] ?? '') ?>">
    <div class="leaflet-skeleton" aria-hidden="true">
      <div class="leaflet-skeleton__pulse">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/>
          <line x1="8" y1="2" x2="8" y2="18"/>
          <line x1="16" y1="6" x2="16" y2="22"/>
        </svg>
        <span>Chargement de la carte…</span>
      </div>
    </div>
  </div>
</div>
<script>
(function(){
  const el = document.getElementById('<?= htmlspecialchars($mapId) ?>');
  if (!el) return;

  let leafletPromise = null;
  function loadLeaflet(){
    if (leafletPromise) return leafletPromise;
    if (typeof L !== 'undefined') { leafletPromise = Promise.resolve(window.L); return leafletPromise; }
    leafletPromise = new Promise(function(resolve, reject){
      const css = document.createElement('link');
      css.rel = 'stylesheet';
      css.href = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css';
      css.crossOrigin = '';
      document.head.appendChild(css);
      const js = document.createElement('script');
      js.src = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js';
      js.crossOrigin = '';
      js.async = true;
      js.onload = function(){ resolve(window.L); };
      js.onerror = reject;
      document.head.appendChild(js);
    });
    return leafletPromise;
  }

  function initMap(){
    const stations = JSON.parse(el.dataset.stations);
    const color = el.dataset.color;
    // Vider le skeleton
    el.innerHTML = '';
    el.classList.add('is-active');
    const map = L.map(el, { scrollWheelZoom: false });
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© OpenStreetMap contributors', maxZoom: 18
    }).addTo(map);
    const pts = [];
    stations.forEach(function(st){
      const ll = [st.lat, st.lng];
      pts.push(ll);
      const popup = '<strong>' + st.name + '</strong>'
        + (st.correspondances && st.correspondances.length ? '<br>↔ ' + st.correspondances.join(', ') : '')
        + (st.is_terminus ? '<br><em>Terminus</em>' : '');
      L.circleMarker(ll, {
        radius: st.is_terminus ? 9 : 7,
        fillColor: color, color: '#000', weight: 2, fillOpacity: 0.95
      }).bindPopup(popup).addTo(map);
    });
    L.polyline(pts, { color: color, weight: 5, opacity: 0.85 }).addTo(map);
    map.fitBounds(pts, { padding: [20, 20] });
    map.on('click', function(){ map.scrollWheelZoom.enable(); });
  }

  // IntersectionObserver : déclenche le chargement quand la carte
  // approche du viewport (200px d'anticipation).
  if (typeof IntersectionObserver === 'undefined') {
    // Fallback navigateurs anciens : chargement immédiat
    loadLeaflet().then(initMap);
    return;
  }
  const observer = new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
      if (entry.isIntersecting) {
        observer.disconnect();
        loadLeaflet().then(initMap).catch(function(){
          el.innerHTML = '<div class="leaflet-skeleton"><div class="leaflet-skeleton__pulse"><span>Erreur de chargement de la carte. <a href="javascript:location.reload()">Réessayer</a></span></div></div>';
        });
      }
    });
  }, { rootMargin: '200px' });
  observer.observe(el);
})();
</script>
<style>
.leaflet-wrapper { margin: 1.5rem 0; }
.leaflet-map {
  position: relative;
  width: 100%;
  height: 400px;
  border: 1px solid #E1F5EE;
  border-radius: 8px;
  background: #f5f7f9;
  overflow: hidden;
}
.leaflet-skeleton {
  position: absolute; inset: 0;
  display: flex; align-items: center; justify-content: center;
  background: linear-gradient(135deg, #f8fbfa 0%, #e1f5ee 100%);
}
.leaflet-skeleton__pulse {
  display: flex; flex-direction: column; align-items: center; gap: .75rem;
  color: #0F6E56;
  opacity: .6;
  animation: bp-leaflet-pulse 1.6s ease-in-out infinite;
}
.leaflet-skeleton__pulse span { font: 500 .9rem system-ui, sans-serif; }
@keyframes bp-leaflet-pulse {
  0%, 100% { opacity: .4; }
  50%      { opacity: .85; }
}
@media (max-width: 768px) {
  .leaflet-map { height: 320px; }
}
</style>
