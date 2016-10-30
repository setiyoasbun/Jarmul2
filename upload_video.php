<?php
$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload2"]["name"]);
$target_name = basename($_FILES["fileToUpload2"]["name"]);
$videoFileType = pathinfo($target_file,PATHINFO_EXTENSION);
//$target_length = filesize($_FILES["fileToUpload"]["size"]);
/*echo $target_name;*/

/*$imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);*/
// Check if image file is a actual image or fake image
if(isset($_POST["submit2"])) {
    
    move_uploaded_file($_FILES["fileToUpload2"]["tmp_name"], $target_file);
                //header("Location: index.php");
    
    	$videoformat = $_POST["videoformat"];
        $audioformat = $_POST["audioformat"];
        $samplerate = $_POST["samplerate"];
        $channel = $_POST["channel"];
        $videocodec = $_POST["codec"];
        $width = $_POST["videowidth"];
        $height = $_POST["videoheight"];
        $fps = $_POST["fps"];
    	/*echo $format;*/
        exec("python video_converter.py ".$target_name." ".$videoformat." ".$audioformat." ".$samplerate." ".$channel." ".$videocodec." ".$width." ".$height." ".$fps." ");/*
        $d_file = $target_dir ."new-". basename($_FILES["fileToUpload"]["name"],$videoFileType).$videoformat;
        	echo $d_file;
        
        if (file_exists($target_file)) {
		    header('Content-Description: File Transfer');
		    header('Content-Type: application/image');
		    header('Content-Disposition: attachment; filename="'.$d_file.'"');
		    header('Cache-Control: private');
		    header('Content-Length: '.filesize($d_file));
		    header('Pragma: public');
		    ob_clean();
    		flush();
		    readfile($d_file);
		    exit;
		}*/

}
?>
