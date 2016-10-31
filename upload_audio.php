<?php
$target_dir = "/home/daniel/rnd/Jarmul2/uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload3"]["name"]);
$target_name = basename($_FILES["fileToUpload3"]["name"]);
$audioFileType = pathinfo($target_file,PATHINFO_EXTENSION);
//$target_length = filesize($_FILES["fileToUpload"]["size"]);
/*echo $target_name;*/

/*$imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);*/
// Check if image file is a actual image or fake image
if(isset($_POST["submit3"])) {
   	//header("Location: index.php");
    if(move_uploaded_file($_FILES["fileToUpload3"]["tmp_name"], $target_file))
    {            //header("Location: index.php");
        // echo $target_file;
        // echo $_POST["audioformat"];
    }
    else{
        header("Location: index.php?status=bukanimage");
    }
    
        $audioformat = $_POST["audioformat"];
        $bitrate = $_POST["bit-rate"];

    	/*echo $format;*/
        exec("python audio_convert.py ".$target_name." ".$audioformat." ".$bitrate." ");/*
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
