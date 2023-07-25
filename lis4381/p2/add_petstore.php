<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="My online portfolio that illustrates skills acquired while working through various project requirements.">
	<meta name="author" content="Christopher Valverde">
	<link rel="icon" href="favicon.ico">

	<title>LIS4381 - Project 2</title>
		<?php include_once("../css/include_css.php"); ?>
</head>
<body>

	<?php include_once("../global/nav.php"); ?>

	<div class="container">
		<div class="starter-template">
					<div class="page-header">
						<?php include_once("global/header.php"); ?>	
					</div>

					<h2>Pet Stores</h2>
					<h3> Basic server-side validation</h3>
					<h4> Server-side validation, and perpared statements (helps prevent SQL injection). Displays user-entered data, and permits users to add data. (See P2 to update and delete pet store data.)</h4>

						<form id="add_petstore" method="post" class="form-horizontal" action="add_petstore_process.php">
								<div class="form-group">
										<label class="col-sm-4 control-label">Name:</label>
										<div class="col-sm-4">
												<input type="text" class="form-control" name="name" placeholder="(max 30 characters)"/>
										</div>
								</div>

								<div class="form-group">
										<label class="col-sm-4 control-label">Street:</label>
										<div class="col-sm-4">
												<input type="text" class="form-control" name="street" placeholder="(max 30 characters)" />
										</div>
								</div>

								<div class="form-group">
										<label class="col-sm-4 control-label">City:</label>
										<div class="col-sm-4">
												<input type="text" class="form-control" name="city" placeholder="(max 30 characters)"/>
										</div>
								</div>

								<div class="form-group">
										<label class="col-sm-4 control-label">State:</label>
										<div class="col-sm-4">
												<input type="text" class="form-control" name="state" placeholder="Example: FL"/>
										</div>
								</div>

								<div class="form-group">
										<label class="col-sm-4 control-label">Zip:</label>
										<div class="col-sm-4">
												<input type="text" class="form-control" name="zip" placeholder="(5 or 9 digits no dashes)" />
										</div>
								</div>
								<div class="form-group">
										<label class="col-sm-4 control-label">Phone:</label>
										<div class="col-sm-4">
												<input type="text" class="form-control" name="phone" placeholder="(10 digits no other characters)"/>
										</div>
								</div>

								<div class="form-group">
										<label class="col-sm-4 control-label">Email:</label>
										<div class="col-sm-4">
												<input type="text" class="form-control" name="email" placeholder="Example: jdoe@email.com"/>
										</div>
								</div>

								<div class="form-group">
										<label class="col-sm-4 control-label">URL:</label>
										<div class="col-sm-4">
												<input type="text" class="form-control" name="URL" placeholder="Example: www.jdoe.com" />
										</div>
								</div>

								<div class="form-group">
										<label class="col-sm-4 control-label">YTD Sales:</label>
										<div class="col-sm-4">
												<input type="text" class="form-control" name="YTDSales" placeholder="Example: 100.00 (no other charcters)"/>
										</div>
								</div>

								<div class="form-group">
										<label class="col-sm-4 control-label">Notes:</label>
										<div class="col-sm-4">
												<input type="text" class="form-control" name="notes" />
										</div>
								</div>

								<div class="form-group">
									<div class="col-sm-6 col-sm-offset-3">
									<button type="submit" class="btn btn-primary" name="add" value="Add">Add</button>
										</div>
								</div>
						</form>

			<?php include_once "global/footer.php"; ?>
			
		</div> <!-- end starter-template -->
 </div> <!-- end container -->

	<!-- Bootstrap JavaScript
	================================================== -->
	<!-- Placed at end of document so pages load faster -->
			<?php //include_once("../js/include_js.php"); ?>

<script type="text/javascript">
 //See Regular Expressions: http://www.qcitr.com/usefullinks.htm#lesson7
 $(document).ready(function() {

	$('#defaultForm').formValidation({
			message: 'This value is not valid',
			icon: {
					valid: 'fa fa-check',
					invalid: 'fa fa-times',
					validating: 'fa fa-refresh'
			},
			fields: {
					name: {
							validators: {
									notEmpty: {
									 message: 'Name required'
									},
									stringLength: {
											min: 1,
											max: 30,
									 message: 'Name no more than 30 characters'
									},
									regexp: {
										//alphanumeric, hyphens, underscores, and spaces
										//regexp: /^[a-zA-Z0-9\-_\s]+$/,										
										//similar to: (though, \w supports other Unicode characters)
											regexp: /^[\w\-\s]+$/,
										message: 'Name can only contain letters, numbers, hyphens, and underscore'
									},									
							},
					},

					street: {
							validators: {
									notEmpty: {
											message: 'Street required'
									},
									stringLength: {
											min: 1,
											max: 30,
											message: 'Street no more than 30 characters'
									},
									regexp: {
										//street: only letters, numbers, commas, hyphens, space character, and periods
										regexp: /^[a-zA-Z0-9,\-\s\.]+$/,		
									message: 'Street can only contain letters, numbers, commas, hyphens, or periods'
									},									
							},
					},

					city: {
							validators: {
									notEmpty: {
									 message: 'City required'
									},
									stringLength: {
											min: 1,
											max: 30,
									 message: 'City no more than 30 characters'
									},
									regexp: {
										//alphanumeric, hyphens, underscores, and spaces
										//regexp: /^[a-zA-Z0-9\-_\s]+$/,										
										//similar to: (though, \w supports other Unicode characters)
											regexp: /^[a-zA-Z0-9\-\s]+$/,
										message: 'City can only contain letters, numbers, hyphens, and underscore'
									},									
							},
					},

					state: {
							validators: {
									notEmpty: {
									 message: 'State required'
									},
									stringLength: {
											min: 2,
											max: 2,
									 message: 'State no more than 2 characters'
									},
									regexp: {
										//alphanumeric, hyphens, underscores, and spaces
										//regexp: /^[a-zA-Z0-9\-_\s]+$/,										
										//similar to: (though, \w supports other Unicode characters)
											regexp: /^[a-zA-Z]+$/,
										message: 'State can only contain letters'
									},									
							},
					},

					zip: {
							validators: {
									notEmpty: {
									 message: 'Zip required'
									},
									stringLength: {
											min: 1,
											max: 9,
									 message: 'Zip no more than 9 characters'
									},
									regexp: {
										//alphanumeric, hyphens, underscores, and spaces
										//regexp: /^[a-zA-Z0-9\-_\s]+$/,										
										//similar to: (though, \w supports other Unicode characters)
											regexp: /^[0-9]+$/,
										message: 'Zip can only contain numbers'
									},									
							},
					},

					phone: {
							validators: {
									notEmpty: {
									 message: 'Phone required'
									},
									stringLength: {
											min: 1,
											max: 10,
									 message: 'Phone no more than 10 characters'
									},
									regexp: {
										//alphanumeric, hyphens, underscores, and spaces
										//regexp: /^[a-zA-Z0-9\-_\s]+$/,										
										//similar to: (though, \w supports other Unicode characters)
											regexp: /^[0-9]+$/,
										message: 'Phone can only contain numbers'
									},									
							},
					},

					email: {
							validators: {
									notEmpty: {
									 message: 'Email required'
									},
									stringLength: {
											min: 1,
											max: 100,
									 message: 'Email no more than 100 characters'
									},
									regexp: {
										//alphanumeric, hyphens, underscores, and spaces
										//regexp: /^[a-zA-Z0-9\-_\s]+$/,										
										//similar to: (though, \w supports other Unicode characters)
											regexp: /^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/,
										message: 'Must include valid email'
									},									
							},
					},

					URL: {
							validators: {
									notEmpty: {
									 message: 'URL required'
									},
									stringLength: {
											min: 1,
											max: 30,
									 message: 'Name no more than 30 characters'
									},
									regexp: {
										//alphanumeric, hyphens, underscores, and spaces
										//regexp: /^[a-zA-Z0-9\-_\s]+$/,										
										//similar to: (though, \w supports other Unicode characters)
											regexp: /^(https?:VV)?([\da-z\.-]+)\.([a-z\.]{2,6})([V\w \.-]*)*V?$/ ,
										message: 'URL can only contain letters, numbers, hyphens, and underscore'  
									},									
							},
					},

					YTDSales: {
							validators: {
									notEmpty: {
									 message: 'YTD Sales required'
									},
									stringLength: {
											min: 1,
											max: 11,
									 message: 'YTD Sales no more than 11 characters'
									},
									regexp: {
										//alphanumeric, hyphens, underscores, and spaces
										//regexp: /^[a-zA-Z0-9\-_\s]+$/,										
										//similar to: (though, \w supports other Unicode characters)
											regexp: /^[0-9\.]+$/,
										message: 'YTD Sales can only contain numbers, and decimal point'
									},									 
							},
					},
					
			}
	});
});
</script>

</body>
</html>
