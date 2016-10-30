
<?php
$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$target_name = basename($_FILES["fileToUpload"]["name"]);
//$target_length = filesize($_FILES["fileToUpload"]["size"]);
/*echo $target_name;*/
$uploadOk = 1;
$imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);
// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    if($check !== false) {
        $uploadOk = 1;
        move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file);
                //header("Location: index.php");
    } else {
        $uploadOk = 0;
        header("Location: index.php?status=bukanimage");
    }
    if ($uploadOk == 1) {
    	$format = $_POST["format"];
    	$height = $_POST["height"];
    	$width = $_POST["width"];
    	/*echo $format;*/
        exec("python Jarmul2.py ".$target_name." ".$format." ".$height." ".$width." ");
        $d_file = $target_dir ."new-". basename($_FILES["fileToUpload"]["name"],$imageFileType).$format;
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
		}

    } 
     else {
        echo "Sorry, there was an error uploading your file.";
    }
}
?>
