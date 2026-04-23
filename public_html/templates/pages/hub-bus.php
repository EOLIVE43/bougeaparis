<?php
$cocon_slug     = 'bus';
$cocon_label    = 'Bus';
$grid_component = 'line-grid-bus';
$data_key       = null;

$tpl->partial('pages/hub-transport', [
    'cocon'          => $cocon,
    'lines'          => $lines,
    'cocon_slug'     => $cocon_slug,
    'cocon_label'    => $cocon_label,
    'grid_component' => $grid_component,
    'data_key'       => $data_key,
]);
