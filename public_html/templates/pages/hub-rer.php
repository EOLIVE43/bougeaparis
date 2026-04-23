<?php
// Wrapper pour /rer/ : delegue au template generique avec les bons parametres
$cocon_slug     = 'rer';
$cocon_label    = 'RER';
$grid_component = 'line-grid-rer';
$data_key       = 'rer';

$tpl->partial('pages/hub-transport', [
    'cocon'          => $cocon,
    'lines'          => $lines,
    'cocon_slug'     => $cocon_slug,
    'cocon_label'    => $cocon_label,
    'grid_component' => $grid_component,
    'data_key'       => $data_key,
]);
