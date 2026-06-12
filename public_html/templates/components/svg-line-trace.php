<?php
/**
 * Composant svg-line-trace : SVG inline du tracé d'une ligne.
 *
 * CWV-safe : SVG inline = pas de request réseau, LCP candidate.
 * Props attendus : $props['line_data'] = array décodé du JSON ligne.
 *   keys: code, name, color, stations[{name,lat,lng,is_terminus}]
 */
$line_data = $props['line_data'] ?? [];
$stations = $line_data['stations'] ?? [];
if (empty($stations)) return;

$color = $line_data['color'] ?? '#0F6E56';
$code  = $line_data['code']  ?? '';

$lats = array_column($stations, 'lat');
$lngs = array_column($stations, 'lng');
$minLat = min($lats); $maxLat = max($lats);
$minLng = min($lngs); $maxLng = max($lngs);

$svgW = 800; $svgH = 450;
$marginX = 70; $marginY = 50;

$project = function($lat, $lng) use ($minLat, $maxLat, $minLng, $maxLng, $svgW, $svgH, $marginX, $marginY) {
    $dxLng = max(0.0001, $maxLng - $minLng);
    $dyLat = max(0.0001, $maxLat - $minLat);
    $x = $marginX + ($lng - $minLng) / $dxLng * ($svgW - 2 * $marginX);
    $y = $marginY + ($maxLat - $lat) / $dyLat * ($svgH - 2 * $marginY);
    return [round($x, 1), round($y, 1)];
};

$pts = [];
foreach ($stations as $st) {
    [$x, $y] = $project($st['lat'], $st['lng']);
    $pts[] = "$x,$y";
}
$polylinePts = implode(' ', $pts);

$startName = $stations[0]['name'] ?? '';
$endName   = end($stations)['name'] ?? '';
$ariaLabel = "Plan ligne $code : $startName vers $endName, " . count($stations) . " stations";
?>
<svg viewBox="0 0 <?= $svgW ?> <?= $svgH ?>"
     xmlns="http://www.w3.org/2000/svg"
     class="line-svg-trace"
     role="img"
     aria-label="<?= htmlspecialchars($ariaLabel) ?>"
     preserveAspectRatio="xMidYMid meet">
  <rect width="<?= $svgW ?>" height="<?= $svgH ?>" fill="#F8FBFA"/>
  <polyline points="<?= $polylinePts ?>"
            fill="none"
            stroke="<?= htmlspecialchars($color) ?>"
            stroke-width="5"
            stroke-linejoin="round"
            stroke-linecap="round"/>
  <?php foreach ($stations as $i => $st):
      [$x, $y] = $project($st['lat'], $st['lng']);
      $isTerminus = !empty($st['is_terminus']);
      $r = $isTerminus ? 7 : 5;
      $textY = $y + (($i % 2 === 0) ? -14 : 18);
  ?>
    <circle cx="<?= $x ?>" cy="<?= $y ?>" r="<?= $r ?>" fill="#fff" stroke="<?= htmlspecialchars($color) ?>" stroke-width="2.5"/>
    <text x="<?= $x ?>" y="<?= round($textY, 1) ?>"
          text-anchor="middle"
          font-size="9"
          font-family="system-ui, -apple-system, sans-serif"
          fill="#1a1a1a"
          font-weight="<?= $isTerminus ? '700' : '500' ?>"><?= htmlspecialchars($st['name']) ?></text>
  <?php endforeach; ?>
  <g transform="translate(<?= $svgW - 130 ?>, 18)">
    <rect width="120" height="24" fill="<?= htmlspecialchars($color) ?>" rx="4"/>
    <text x="60" y="16" text-anchor="middle" font-size="12" font-weight="700" font-family="system-ui, sans-serif" fill="#fff">Tramway <?= htmlspecialchars($code) ?></text>
  </g>
</svg>
<style>
.line-svg-trace { width: 100%; max-width: 800px; height: auto; margin: 1.5rem auto; display: block; }
</style>
