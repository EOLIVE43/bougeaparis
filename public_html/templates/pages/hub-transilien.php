<?php
$cocon_slug     = 'transilien';
$cocon_label    = 'Transilien';
$grid_component = 'line-grid-transilien';
$data_key       = 'transilien';

$tpl->partial('pages/hub-transport', [
    'cocon'          => $cocon,
    'lines'          => $lines,
    'cocon_slug'     => $cocon_slug,
    'cocon_label'    => $cocon_label,
    'grid_component' => $grid_component,
    'data_key'       => $data_key,
]);
