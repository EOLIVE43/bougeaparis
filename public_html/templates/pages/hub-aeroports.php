<?php
$cocon_slug     = 'aeroports';
$cocon_label    = 'Aeroports';
$grid_component = 'airport-grid';
$data_key       = 'aeroports';

$tpl->partial('pages/hub-transport', [
    'cocon'          => $cocon,
    'lines'          => $lines,
    'cocon_slug'     => $cocon_slug,
    'cocon_label'    => $cocon_label,
    'grid_component' => $grid_component,
    'data_key'       => $data_key,
]);
