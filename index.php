<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Jarmul</title>
    <!-- Tell the browser to be responsive to screen width -->
    <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
    <!-- Bootstrap 3.3.5 -->
    <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.5.0/css/font-awesome.min.css">
    <!-- Ionicons -->
    <link rel="stylesheet" href="https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css">
    <!-- Theme style -->
    <link rel="stylesheet" href="dist/css/AdminLTE.min.css">
    <!-- AdminLTE Skins. Choose a skin from the css/skins
         folder instead of downloading all of them to reduce the load. -->
    <link rel="stylesheet" href="dist/css/skins/_all-skins.min.css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
        <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body class="hold-transition skin-blue" style="
    background-image: url('assets/Background.png');
    background-size: 100% 100%;">
    <?php
      if(isset($_GET['status']) && $_GET['status']=="bukanimage")
      {
        echo "<div class='alert alert-danger alert-dismissible' style='width: 45%; margin: 0 auto;margin-top: 3%;'>
                <button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;</button>
                <h4><i class='icon fa fa-ban'></i> Alert!</h4>
                This file is not a picture
              </div>";
      }
      else if(isset($_GET['status']) && $_GET['status']=="sukses")
      {
        echo "<div class='alert alert-success alert-dismissible' style='width: 45%; margin: 0 auto;margin-top: 3%;'>
                <button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;</button>
                <h4><i class='icon fa fa-check'></i> Success!</h4>
                File Successfully Converted!
              </div>";
      }
    ?>
<div>
  <div class="row">
  <div class="col-sm-12">
        <div class="nav-tabs-custom" style="width: 45%; margin: 0 auto; margin-top: 2%;">
            <ul class="nav nav-tabs">
              <li class="active"><a href="#tab_1" data-toggle="tab">Image Converter</a></li>
              <li><a href="#tab_2" data-toggle="tab">Audio Converter</a></li>
              <li><a href="#tab_3" data-toggle="tab">Video Converter</a></li>
            </ul>
            <div class="tab-content">
              <div class="tab-pane active" id="tab_1">
                <form role="form" action="upload.php" method="post" enctype="multipart/form-data">
                  <div class="box-body">
                  	<div class="form-group">
                      <label for="exampleInputFile">File input:</label>
                      <input type="file" name="fileToUpload" id="fileToUpload">
                    </div>

                    <div class="form-group">
                      <label for="exampleInputEmail1">Height:</label>
                      <input type="text" class="form-control" name="height" id="height" placeholder="Enter height in Pixel" value="0">
                    </div>
                    <div class="form-group">
                      <label for="exampleInputPassword1">Width:</label>
                      <input type="text" class="form-control" id="width" name="width" placeholder="Enter Width in Pixel" value="0">
                    </div>
                    <div class="form-group">
                      <label>Format:</label>
                      <select class="form-control" name="format">
                        <option>bmp</option>
                        <option>jpeg</option>
                        <option>png</option>
                        <option>tiff</option>
                      </select>
                    </div>
                    
                  </div><!-- /.box-body -->

                  <div class="box-footer">
                    <input type="submit" name="submit" class="btn btn-primary pull-right" value="Upload Image"></button>
                  </div>
                </form>
              </div>
              <!-- /.tab-pane -->
              <div class="tab-pane" id="tab_2">
                <form role="form" action="upload_audio.php" method="post" enctype="multipart/form-data">
                  <div class="box-body">
                    <div class="form-group">
                      <label for="exampleInputFile">File input:</label>
                      <input type="file" name="fileToUpload3" id="fileToUpload3">
                    </div>
                    <div class="form-group">
                      <label>Format:</label>
                      <select class="form-control" name="audioformat">
                        <option>mp3</option>
                        <option>mp4</option>
                        <option>ac3</option>
                        <option>aiff</option>
                        <option>ogg</option>                        
                      </select>
                    </div>
                    <div class="form-group">
                      <label for="exampleInputPassword1">bit-rate:</label>
                      <input type="text" class="form-control" id="bit-rate" name="bit-rate" placeholder="Enter bit-rate" value="0">
                    </div>
                    
                  </div><!-- /.box-body -->

                  <div class="box-footer">
                    <input type="submit" name="submit3" class="btn btn-primary pull-right" value="Upload Image"></button>
                  </div>
                </form>
              </div>
              <!-- /.tab-pane -->
              <div class="tab-pane" id="tab_3">
                <form role="form" action="upload_video.php" method="post" enctype="multipart/form-data">
                  <div class="box-body">
                    <div class="form-group">
                      <label for="exampleInputFile">File input:</label>
                      <input type="file" name="fileToUpload2" id="fileToUpload2">
                    </div>
                    <div class="form-group">
                      <label>Format:</label>
                      <select class="form-control" name="videoformat">
                        <option>mkv</option>
                        <option>avi</option>
                        <option>mp4</option>
                        <option>flv</option>
                        <option>mpg</option>
                      </select>
                    </div>
                    <div class="form-group">
                      <label>Audio Format:</label>
                      <select class="form-control" name="audioformat">
                        <option>aac</option>
                        <option>mp3</option>
                        <option>flac</option>
                        <option>ac3</option>
                      </select>
                    </div>
                    <div class="form-group">
                      <label>Audio Sample Rate:</label>
                      <select class="form-control" name="samplerate">
                        <option>8000</option>
                        <option>11025</option>
                        <option>16000</option>
                        <option>22050</option>
                        <option>32000</option>
                        <option>37800</option>
                        <option>44056</option>
                        <option>44100</option>
                      </select>
                    </div>
                    <div class="form-group">
                      <label>Audio Channel:</label>
                      <select class="form-control" name="channel">
                        <option>1</option>
                        <option>2</option>
                        <option>5 (Only for ac3)</option>
                      </select>
                    </div>
                    <div class="form-group">
                      <label>Video Codec:</label>
                      <select class="form-control" name="codec">
                        <option>h264</option>
                      </select>
                    </div>
                    <div class="form-group">
                      <label for="exampleInputPassword1">Video Width:</label>
                      <input type="text" class="form-control" id="videowidth" name="videowidth" placeholder="Enter Width in Pixel" value="0">
                    </div>
                    <div class="form-group">
                      <label for="exampleInputPassword1">Video Height:</label>
                      <input type="text" class="form-control" id="videoheight" name="videoheight" placeholder="Enter Height in Pixel" value="0">
                    </div>
                    <div class="form-group">
                      <label for="exampleInputPassword1">FPS:</label>
                      <input type="text" class="form-control" id="fps" name="fps" placeholder="Enter FPS" value="0">
                    </div>
                    
                  </div><!-- /.box-body -->

                  <div class="box-footer">
                    <input type="submit" name="submit2" class="btn btn-primary pull-right" value="Upload Image"></button>
                  </div>
                </form>
              </div>
              <!-- /.tab-pane -->
            </div>
            <!-- /.tab-content -->
          </div>
        </div>
      </div>

    <script src="plugins/jQuery/jQuery-2.1.4.min.js"></script>
    <!-- Bootstrap 3.3.5 -->
    <script src="bootstrap/js/bootstrap.min.js"></script>
    <!-- FastClick -->
    <script src="plugins/fastclick/fastclick.min.js"></script>
    <!-- AdminLTE App -->
    <script src="dist/js/app.min.js"></script>
    <!-- AdminLTE for demo purposes -->
    <script src="dist/js/demo.js"></script>

    <script type="text/javascript">
      

    </script>
    </body>
    </html>