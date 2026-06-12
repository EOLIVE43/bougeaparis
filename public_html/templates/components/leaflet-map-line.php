<?php
/**
 * Composant leaflet-map-line : carte Leaflet OSM lazy au clic.
 *
 * CWV-safe :
 *  - Hauteur container FIXE (400 px) → CLS = 0 au clic
 *  - Leaflet (CSS + JS) chargé à la demande uniquement (async)
 *  - Feedback INP immédiat sur le clic (loading state)
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
  <button class="leaflet-load-btn" type="button"
          aria-label="Charger la carte interactive OpenStreetMap"
          data-target="<?= htmlspecialchars($mapId) ?>">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/>
      <line x1="8" y1="2" x2="8" y2="18"/>
      <line x1="16" y1="6" x2="16" y2="22"/>
    </svg>
    Voir la carte interactive (OpenStreetMap)
  </button>
  <div id="<?= htmlspecialchars($mapId) ?>"
       class="leaflet-map"
       data-stations='<?= htmlspecialchars(json_encode($stations, JSON_UNESCAPED_UNICODE), ENT_QUOTES) ?>'
       data-color="<?= htmlspecialchars($color) ?>"></div>
</div>
<script>
(function(){
  let leafletPromise = null;
  function loadLeaflet(){
    if (leafletPromise) return leafletPromise;
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
  document.querySelectorAll('.leaflet-load-btn').forEach(function(btn){
    btn.addEventListener('click', function(){
      const id = btn.dataset.target;
      const el = document.getElementById(id);
      if (!el) return;
      btn.disabled = true;
      btn.innerHTML = '<span class="leaflet-spinner"></span> Chargement…';
      loadLeaflet().then(function(L){
        btn.style.display = 'none';
        el.classList.add('is-active');
        const stations = JSON.parse(el.dataset.stations);
        const color = el.dataset.color;
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
      }).catch(function(){
        btn.disabled = false;
        btn.textContent = 'Erreur de chargement, réessayer';
      });
    }, { once: true });
  });
})();
</script>
<style>
.leaflet-wrapper { position: relative; height: 400px; background: #f5f7f9; border: 1px solid #E1F5EE; border-radius: 8px; overflow: hidden; margin: 2rem 0; }
.leaflet-load-btn {
  position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
  display: inline-flex; align-items: center; gap: .5rem;
  padding: .9rem 1.5rem;
  background: #0F6E56; color: #fff;
  border: none; border-radius: 8px;
  cursor: pointer;
  font: 600 .95rem system-ui, sans-serif;
  box-shadow: 0 4px 12px rgba(0,0,0,.1);
  transition: background .2s;
}
.leaflet-load-btn:hover { background: #085041; }
.leaflet-load-btn:disabled { background: #888; cursor: wait; }
.leaflet-map { position: absolute; inset: 0; display: none; }
.leaflet-map.is-active { display: block; }
.leaflet-spinner {
  width: 14px; height: 14px;
  border: 2px solid #fff; border-top-color: transparent;
  border-radius: 50%;
  animation: bp-leaflet-spin .8s linear infinite;
}
@keyframes bp-leaflet-spin { to { transform: rotate(360deg); } }
@media (max-width: 768px) {
  .leaflet-wrapper { height: 320px; }
}
</style>
