<?php
class AngleRotator
{
    private $angles;

    public function __construct($configPath = null)
    {
        if ($configPath === null) {
            $configPath = __DIR__ . '/../config/angles.php';
        }

        if (!file_exists($configPath)) {
            throw new RuntimeException('Config angles introuvable : ' . $configPath);
        }

        $config = require $configPath;
        if (!is_array($config)) {
            throw new RuntimeException('config/angles.php doit retourner un tableau');
        }

        $this->angles = $config;
    }

    public function getAngleForToday()
    {
        return $this->getAngleForDate(date('Y-m-d'));
    }

    public function getAngleForDate($dateString)
    {
        $dt = DateTime::createFromFormat('Y-m-d', $dateString);
        if ($dt === false) {
            throw new InvalidArgumentException('Date invalide : ' . $dateString);
        }

        $dayOfWeek = (int)$dt->format('N');

        if (!isset($this->angles[$dayOfWeek])) {
            throw new RuntimeException('Aucun angle configure pour le jour ' . $dayOfWeek);
        }

        $angle = $this->angles[$dayOfWeek];
        $angle['day_of_week'] = $dayOfWeek;
        $angle['date'] = $dateString;
        $angle['day_label'] = $this->getDayLabelFr($dayOfWeek);

        return $angle;
    }

    private function getDayLabelFr($dayOfWeek)
    {
        $labels = array(
            1 => 'lundi',
            2 => 'mardi',
            3 => 'mercredi',
            4 => 'jeudi',
            5 => 'vendredi',
            6 => 'samedi',
            7 => 'dimanche',
        );
        return isset($labels[$dayOfWeek]) ? $labels[$dayOfWeek] : 'inconnu';
    }

    public function getAllAngles()
    {
        return $this->angles;
    }
}
