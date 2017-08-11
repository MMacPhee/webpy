<?php
	include ("phpgraphlib/phpgraphlib.php");

	$file = fopen('temps/'.$_POST["year"].'/'.$_POST["month"].'/'.$_POST["day"].'.txt', 'r');
	$tempArray = array();

	while($line = fgets($file)) {
		$val = floatval(substr($line, 0, 5));
		$time = substr($line, 17, 5);
		$tempArray[$time] = $val;
	}
	fclose($file);

	$graph = new PHPGraphLib(900, 600);
	$graph->addData($tempArray);
	$graph->setTitle('Apartment Temps');
	$graph->setBars(false);
	$graph->setLine(true);
	$graph->setDataPoints(true);
	$graph->setDataPointSize(4);
	$graph->setDataValues(false);
	$graph->setRange(10, 30);
	$graph->setXValuesInterval(2);
	$graph->createGraph();
?>
