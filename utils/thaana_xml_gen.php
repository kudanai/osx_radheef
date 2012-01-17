<?php

//import and initialize the thaana_conversions library
//from jaa http://jawish.org

require 'thaana_conversions.obj.php';
$converter = new Thaana_Conversions();


//print out the header XML doctype declaration
openXML();

//now open the dictionary node. this is the top-level
//node under which the entries are created
open_dictionary();


/////---------------APPLICATION LOGIC GOES HERE-------------/////

if (($handle = fopen("radheef.csv", "r")) !== FALSE) {

  $i=1;
	while (($data = fgetcsv($handle,null,"\t")) !== FALSE) {

    //get the head-word forms
    $headASCII = $data[0];
    $headUTF = fixSyn($converter->convertAsciiToUtf8(strrev($data[0])));
    
    //open the entry node
    //open_entry(ID_safe(strrev($headASCII)),$headUTF);
    open_entry(ID_safe(strrev($headASCII))."_".($i++%10),$headUTF);
		
		//write index values
		write_index(fixSyn(strrev($headASCII)),$headUTF);
		write_index($headUTF,$headUTF);
		
		//now we get into the actual stuff displayed
		
		echo "<div class=\"align_right\" >\n";
		//print out the headword
		echo "    <h1>$headUTF</h1>\n";
		
		//print type if it exists
		if (! empty($data[2])) {
		  echo "    <span class=\"word_class\">".$converter->convertAsciiToUtf8(strrev($data[2]))."</span>\n";
		}
		//print definition
		echo "\n    <p>";
		  echo fixSyn($converter->convertAsciiToUtf8(strrev($data[1])));
		echo"</p>\n";
		
		//close the align block
		echo "</div>";
		
		close_entry();
	}
    fclose($handle);
}


close_dictionary();

///////---------------END OF APPLICATION LOGIC HERE------------/////



function openXML(){

	$xmlHeader = <<<HEAD
<?xml version="1.0" encoding="UTF-8"?>
<!--
  Apple Dictionary Development Kit compatible Dhivehi radheef.
  2012 kudanai (http://kudanai.com)
-->


HEAD;


	echo $xmlHeader;
}


//function opens the top-level dictionary node
function open_dictionary(){
  echo "<d:dictionary xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:d=\"http://www.apple.com/DTDs/DictionaryService-1.0.rng\">\n";
}

//called at the very end.
function close_dictionary(){
  echo "</d:dictionary>\n";
}


//create and entry-node
//requires entryID and entryTitle
//optional parental control arg. def=0

function open_entry($entryID,$entryTitle){
  echo "<d:entry id=\"$entryID\" d:title=\"$entryTitle\" >\n";
}

//terminate the entry node
function close_entry(){
  echo "</d:entry>\n\n";
}

//writes and index value
function write_index($value,$title){
  echo "  <d:index d:value=\"$value\" d:title=\"$title\" />\n";
}


//strip out whitespace
//replace with delimiter _
function ID_safe($data){
  return preg_replace("/\s+/", "_", $data); 
}


//fix the numbers
function fixSyn($line) {
		preg_match_all("/(\d+)/",$line,$matches);
		foreach($matches as $val) {
			foreach($val as $i){
			$line = str_replace($i,strrev("$i"),$line);
			}
		}
		
		//fix those pesky brackets
		$line=str_replace(array('(',')'), array('%%','('), $line);
		$line=str_replace('%%', ')', $line);


		//$line=preg_replace("/\)(\d+)\(\s+/","\n$1: ",$line);
		//$line=preg_replace("/\n(\d+):\s?\n(\d+):/","\n$1: ($2) ",$line);
		//$line=preg_replace("/\n(\d+):\s?\n/","($1)\n",$line);
		//$line=preg_replace("/(މިސާލު: )/","\n\t$1",$line);
		
		return $line;
}

?>
