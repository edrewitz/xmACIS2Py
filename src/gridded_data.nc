<!DOCTYPE html>
<!--[if IE 8]> <html lang="en" class="ie8"> <![endif]-->
<!--[if IE 9]> <html lang="en" class="ie9"> <![endif]-->
<!--[if !IE]><!--> <html lang="en"> <!--<![endif]-->
<head>
    <title>RCC-ACIS</title>

    <!-- Meta -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- CSS Global Compulsory-->
    <link rel="stylesheet" href="assets/plugins/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="stylesheet" href="assets/css/headers/header2.css">
    <!-- <link rel="stylesheet" href="assets/plugins/bootstrap/css/bootstrap-responsive.min.css"> -->
    <link rel="stylesheet" href="assets/css/responsive.css">
    <link rel="shortcut icon" href="favicon.ico">
    <!-- CSS Implementing Plugins -->
    <link rel="stylesheet" href="assets/plugins/font-awesome/css/font-awesome.css">
    <link rel="stylesheet" href="assets/plugins/flexslider/flexslider.css">
    <!-- CSS Page Style -->
    <link rel="stylesheet" href="assets/css/pages/page_search.css">
    <link rel="stylesheet" href="assets/css/pages/page_magazine.css">
    <!-- CSS Theme -->
    <link rel="stylesheet" href="assets/css/themes/default.css" id="style_color">
    <link rel="stylesheet" href="assets/css/themes/headers/default.css" id="style_color-header-2">
</head>

<body>

<div id="header"></div>

<!--=== Content Part ===-->
<div class="container">
    <div class="row magazine-page">
        <!-- Begin Content -->
        <div class="col-md-8">
           <div class="panel panel-warning">
              <div class="panel-heading">
                 <h3>ACIS Web Services</h3>
              </div>
              <div class="panel-body">
                 <div id="aciswsdoc"></div>

              </div>
           </div>
        </div>
        <!-- End Content -->

        <!-- Begin Sidebar -->
        <div class="col-md-4">
           <div class="well toc-indentation">

              <div id="aciswsdoctoc"></div>
           </div>
           <div id="sidebar"></div>

        </div>
        <!-- End Sidebar -->
    </div>
</div><!--/container-->
<!-- End Content Part -->

<div id="footer"></div>

<!-- JS Global Compulsory -->
<script type="text/javascript" src="assets/plugins/jquery-1.10.2.min.js"></script>
<script type="text/javascript" src="assets/plugins/jquery-migrate-1.2.1.min.js"></script>
<script type="text/javascript" src="assets/plugins/bootstrap/js/bootstrap.min.js"></script>
<script type="text/javascript" src="assets/plugins/hover-dropdown.min.js"></script>
<script type="text/javascript" src="assets/plugins/back-to-top.js"></script>
<!-- JS Implementing Plugins -->
<script type="text/javascript" src="assets/plugins/flexslider/jquery.flexslider-min.js"></script>
<!-- JS Page Level -->
<script type="text/javascript" src="assets/js/app.js"></script>
<script type="text/javascript">
    jQuery(document).ready(function() {
        App.init();
        App.initSliders();
    });
</script>
<!-- Definitions for included html files -->
<script>
$(function(){
  $("#header").load("header.html");
  $("#footer").load("footer.html");
  $("#sidebar").load("announce.html");
  $("#aciswsdoc").load("ACISWSdoc.html");
  $("#aciswsdoctoc").load("ACISWStoc.html");
});
</script>

<!--[if lt IE 9]>
	<script src="assets/plugins/respond.js"></script>
<![endif]-->

</body>
</html>
