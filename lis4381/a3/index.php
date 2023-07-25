<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
		<meta name="description" content="My online portfolio that illustrates skills acquired while working through various project requirements.">
		<meta name="author" content="Christopher Valverde">
    <link rel="icon" href="favicon.ico">

		<title>CRS4381 - Assignment 3</title>		
		<?php include_once("../css/include_css.php"); ?>			
  </head>

  <body>

		<?php include_once("../global/nav.php"); ?>
		
		<div class="container">
			<div class="starter-template">
				<div class="page-header">
					<?php include_once("global/header.php"); ?>	
				</div>
				<p class="text-justify">
					<strong>Description:</strong> The expected norm...(Create my event app with working database and screenshot of records) 
				</p>

				<h4>Screenshot of ERD</h4>
				<img src="img/erd.png" class="img-responsive center-block" alt="records">

				<h4>Screenshot of opening user interface</h4>
				<img src="img/phone1.png" class="img-responsive center-block" alt="Interface 1">

				<h4>Screenshot of processing user input</h4>
				<img src="img/phone2.png" class="img-responsive center-block" alt="screenshot of processing user input">

				<h4>Screenshots of records in each table</h4>
				<img src="img/pet.png" class="img-responsive center-block" alt="pet table">
				<img src="img/petstore.png" class="img-responsive center-block" alt="petstore table">
				<img src="img/customer.png" class="img-responsive center-block" alt="customer table">
				
				<?php include_once "global/footer.php"; ?>

			</div> <!-- starter-template -->
    </div> <!-- end container -->

		<!-- Bootstrap JavaScript
				 ================================================== -->
		<!-- Placed at end of document so pages load faster -->		
		<?php include_once("../js/include_js.php"); ?>			
  </body>
</html>
