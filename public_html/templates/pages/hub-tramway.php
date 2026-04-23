<?php
$cocon_slug     = 'tramway';
$cocon_label    = 'Tramway';
$grid_component = 'line-grid-tram';
$data_key       = 'tramway';

$tpl->partial('pages/hub-transport', [
    'cocon'          => $cocon,
    'lines'          => $lines,
    'cocon_slug'     => $cocon_slug,
    'cocon_label'    => $cocon_label,
    'grid_component' => $grid_component,
    'data_key'       => $data_key,
]);
