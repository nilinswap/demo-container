from locust import HttpLocust, TaskSet, task, between
import json


class UserBehavior(TaskSet):
    def on_start(self):
        pass  # add code that you want to run during ramp up

    def on_stop(self):
        pass  # add code that you want to run during ramp down

    @task(1)
    def registration(self):
        html = '''
        

<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
	<title></title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="x-apple-disable-message-reformatting">
	<!--<link href="https://fonts.googleapis.com/css?family=Montserrat:400,600,700,800" rel="stylesheet">-->

	<style type="text/css">
		html,
        body {
        	font-family: 'Montserrat', sans-serif;
            margin: 0 auto !important;
            padding: 0 !important;
            height: 100% !important;
            width: 100% !important;
            width: 100% !important;
        }
        label{
        	display: block;
			margin-bottom: 3px;
        }
        .wrapper{
            width: 909px;
            display: block;
        }
        .inner-wrapper{
        	width: 100%;
        }
        .logo{
        	height: 40px;
        }
        .policy-info{
        	width: 100%;
        }
        .veh-name{
        	font-size: 16px;
        	width: 100%;
        	font-weight: 400;
        }
        .veh-no{
        	text-transform: uppercase;
        	font-weight: 600;
        	font-size: 16px;
        	width: 100%;
        }
        .label1{
        	font-size: 16px;
        	color: #6950a1;
        	font-weight: 400;
        	width: 100%;
        }
        .label2{
        	font-size: 16px;
        	color: #000;
        	font-weight: 400;
        	width: 100%;
        }
        .label3{
        	font-size: 14px;
        	color: #53aa76;
        	font-weight: 800;
        	width: 100%;
        	text-transform: uppercase;
        }
        .label4{
        	font-size: 14px;
        	color: #939598;
        	font-weight: 800;
        	width: 100%;
        	text-transform: uppercase;
        }
        .row{
        	width: 100%;
        	display: block;
        }
        .claim-header1{
        	color: #6950a1;
        	font-weight: 800;
            font-size: 30px;
    		margin: 0 0 10px 0;
        }
        .claim-p1{
        	font-size: 20px;
        	font-weight: 600;
        	margin: 0 0 5px 0;
        }
        .discount{
        	border: 2px solid #6950a1;
        	border-radius: 25px;
        	color: #6950a1;
        	font-size: 12px;
            width: 160px;
    		text-align: center;
    		padding: 4px 5px;
    		float: right;
        }
        .discount label{
        	font-size: 10px;
        	width: 100%;
        }
        .claim-li label{
        	margin: 0 15px 0 0;
        	font-size: 12px;
        	font-weight: 400;
        	float: left;
        }
        .claim-li-dot:before{
        	content: '';
        	display: inline-block;
        	background: #000;
        	height: 5px;
        	width: 5px;
        	border-radius: 50%;
        	margin: 0 15px 0 0;
        	vertical-align: middle;
        }
        .workshop-header1{
        	color: #6950a1;
        	font-weight: 800;
            font-size: 20px;
    		margin: 0 0 10px 0;
        }
        .headerp-pol{
        	width: 100%;
        }
        .pvq-details{
        	width: 100%;
        	margin-bottom: 0px;
        }
        .idv{
        	width: 100%;
        }
		table > tbody > tr > td{
			vertical-align: top;
		}
        .header1 {
		    font-size: 14px;
		    margin-bottom: 8px;
		    text-transform: uppercase;
		    border-bottom: 3px solid #000;
		    font-weight: 800;
		}
		.label5 {
		    color: #777;
		    font-size: 12px;
		}
		.label6 {
		    color: #000;
		    font-size: 12px;
		}
		.form-group{
			/*margin-bottom: 3px;*/
			width: 100%;
		}
		.qr-code img{
			width: 100%;
		}
		.table1{
			width: 100%;
            /*border: 1px solid #ddd;*/
            border-collapse: collapse;
		}
		.table1 > thead > tr > th{
            background: #ddd;
            color: #000;
            font-size: 12px;
            font-weight: 600;
            padding: 6px 12px;
            border: 1px solid #ddd;
            vertical-align: top;
			text-align: left;
        }
        .table1 > tbody > tr > td{
            padding: 6px 12px;
            font-size: 12px;
            border: 1px solid #ddd;
            vertical-align: top;
			text-align: left;
        }
        .limitations p{
        	margin: 0 0 3px 0;
        	font-size: 12px;
        	font-weight: 400;
        }
        .insp{
        	margin: 5px 0 0 0;
        	height: 60px;
        }
        .insp-report-cropped-img {
          width: 78px;
          height: 60px;
        }
        .insp img{
        	height: 100%;
        	width: 100%;
        }
	</style>
</head>
<body>
<div class="wrapper">
	<div class="inner-wrapper">
		<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
			<tbody>
			<tr>
				<td style="width: 15%; vertical-align: middle;">
					<img class="logo" src="https://partner3.acko.com/static/images/acko_logo_2x.png">
				</td>
				<td style="width: 85%; vertical-align: middle;">
					<h2 style="margin: 0; font-size: 20px; font-weight: 800;">COMPREHENSIVE POLICY</h2>
					<p style="margin: 0; font-size: 14px;">Summary</p>
				</td>
			</tr>
			</tbody>
		</table>


		<div class="policy-info" style="margin: 20px 0;">
			<table style="border-collapse: collapse; width: 100%" cellpadding="0">
				<tbody>
				<tr>
					<td style="width: 33.33%; vertical-align: top;">
						<label class="veh-name">Honda City</label>
						<label class="veh-no">MH03</label>

						<label class="label1" style="margin-top: 10px;">Car owner</label>
						<label class="label2">Elton John</label>
						
					</td>
					<td style="width: 33.33%; vertical-align: top; position: relative;">
						<label class="label1">Valid from</label>
						<label class="veh-no">15 Feb 20</label>
						<img src="https://partner3.acko.com/docgen/static/img/arrow.png" style="position: absolute; right: 70px; top: 20px;">

						<label class="label1" style="margin-top: 10px;">Owner number</label>
						<label class="label2">9940319909</label>

						<div style="margin-top: 10px;">
							<label class="label1">Plan</label>
							<label class="label2">
								Comprehensive
								
        
							</label>
						</div>
					</td>
					<td style="width: 33.33%; vertical-align: top;">
						<label class="label1">Valid till (midnight)</label>
						<label class="veh-no">14 Feb 21</label>

						<label class="label1" style="margin-top: 10px;">Owner email</label>
						<label class="label2">iit2015085@iiita.ac.in</label>

						<table style="border-collapse: collapse; width: 100%; margin-top: 10px;">
							<tbody>
							<tr>
								<td style="width: 50%;">
									<label class="label1">Policy price</label>
									<label class="label2">₹ 17315.27</label>
								</td>
								<td style="width: 50%;">
									<label class="label1">Car value</label>
									<label class="label2">₹ 1344915.0</label>
								</td>
							</tr>
							</tbody>
						</table>
					</td>
				</tr>
				</tbody>
			</table>
		</div>
	</div>

	<p style="color: #8a8a8a; font-size: 12px; margin: 0px 0;">Please refer overlay for more details</p>
	<hr style="margin: 10px 0 0; width: 100%;" />
 
	<div class="inner-wrapper">
		<div class="row" style="margin-bottom: 10px;">
			<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
				<tbody>
				<tr>
					<td style="width: 100%; vertical-align: top;">
						<p style="font-size: 16px; width: 100%; margin-top: 40px; margin-bottom: 40px; line-height: 1.6;"><b>WELCOME!</b> We’re happy to have you at Acko, and promise to be there for you always. You’re now a part of the Acko Advantage program, which takes care of everything if your car ever runs into trouble.
              Just call us immediately on <b>1800 266 2256</b> when things go wrong and we’ll take it from there.</p>
					</td>
				</tr>
				</tbody>
			</table>
		</div>

		<table style="border-collapse: collapse; width: 100%; margin: 20px 0 20px 0;" cellpadding="3">
			<tbody>
      <tr>
				<td style="width: 50%; border-right: 0.5px solid #dcdce0;">
				</td>
        <td style="width: 25%; border-right: 0.5px solid #dcdce0;">
          <h2 class="claim-header1">Acko Advantage*</h2>
				</td>
        <td style="width: 25%;">
          <h2 class="claim-header1" style="color: #8d8e99;">Non-Acko Advantage</h2>
				</td>
      </tr>
			<tr>
				<td style="margin-top: 20px; width: 50%; border-right: 0.5px solid #dcdce0;">
          <table style="border-collapse: collapse; width: 100%;" cellpadding="0">
		      	<tbody>
		      	<tr>
		      		<td style="vertical-align: middle; width: 30%;">
		      			<img src="https://partner3.acko.com/docgen/static/img/AckoAdvantage_1.png" style="height: 50px; padding-left: 10px; padding-right: 10px;">
		      		</td>
		      		<td style="vertical-align: middle; width: 70%;">
		      			<label style="font-size: 16px; width: 70%; padding-right: 80px; line-height: 1.6;">Free car pick-up from home, office or accident site</label>
		      		</td>
		      	</tr>
		      	</tbody>
		      </table>
				</td>
        <td style="margin-top: 20px; width: 25%; border-right: 0.5px solid #dcdce0;">
          <img src="https://partner3.acko.com/docgen/static/img/green-tick-small.png" style="height: 20px; padding-left: 10px; padding-right: 10px;">
				</td>
        <td style="width: 25%; margin-top: 20px;">
          <img src="https://partner3.acko.com/docgen/static/img/cross.png" style="height: 20px; padding-left: 10px; padding-right: 10px;">
				</td>
      </tr>
      <tr>
				<td style="margin-top: 20px; width: 50%; border-right: 0.5px solid #dcdce0;">
          <table style="border-collapse: collapse; width: 100%;" cellpadding="0">
		      	<tbody>
		      	<tr>
		      		<td style="vertical-align: middle; width: 30%;">
		      			<img src="https://partner3.acko.com/docgen/static/img/AckoAdvantage_2.png" style="height: 50px; padding-left: 10px; padding-right: 10px;">
		      		</td>
		      		<td style="vertical-align: middle; width: 70%;">
		      			<label style="font-size: 16px; width: 70%; padding-right: 80px; line-height: 1.6;">Repairs at our network of expert garages.</label>
		      		</td>
		      	</tr>
		      	</tbody>
		      </table>
				</td>
        <td style="margin-top: 20px; width: 25%; border-right: 0.5px solid #dcdce0;">
          <img src="https://partner3.acko.com/docgen/static/img/green-tick-small.png" style="height: 20px; padding-left: 10px; padding-right: 10px;">
				</td>
        <td style="width: 25%; margin-top: 20px;">
          <img src="https://partner3.acko.com/docgen/static/img/cross.png" style="height: 20px; padding-left: 10px; padding-right: 10px;">
				</td>
      </tr>
      <tr>
				<td style="margin-top: 20px; width: 50%; border-right: 0.5px solid #dcdce0;">
          <table style="border-collapse: collapse; width: 100%;" cellpadding="0">
		      	<tbody>
		      	<tr>
		      		<td style="vertical-align: middle; width: 30%;">
		      			<img src="https://partner3.acko.com/docgen/static/img/AckoAdvantage_3.png" style="height: 50px; padding-left: 10px; padding-right: 10px;">
		      		</td>
		      		<td style="vertical-align: middle; width: 70%;">
		      			<label style="font-size: 16px; width: 70%; padding-right: 80px; line-height: 1.6;">3-day repair guarantee.</label>
		      		</td>
		      	</tr>
		      	</tbody>
		      </table>
				</td>
        <td style="margin-top: 20px; width: 25%; border-right: 0.5px solid #dcdce0;">
          <img src="https://partner3.acko.com/docgen/static/img/green-tick-small.png" style="height: 20px; padding-left: 10px; padding-right: 10px;">
				</td>
        <td style="width: 25%; margin-top: 20px;">
          <img src="https://partner3.acko.com/docgen/static/img/cross.png" style="height: 20px; padding-left: 10px; padding-right: 10px;">
				</td>
      </tr>
      <tr>
				<td style="margin-top: 20px; width: 50%; border-right: 0.5px solid #dcdce0;">
          <table style="border-collapse: collapse; width: 100%;" cellpadding="0">
		      	<tbody>
		      	<tr>
		      		<td style="vertical-align: middle; width: 30%;">
		      			<img src="https://partner3.acko.com/docgen/static/img/AckoAdvantage_4.png" style="height: 50px; padding-left: 10px; padding-right: 10px;">
		      		</td>
		      		<td style="vertical-align: middle; width: 70%;">
		      			<label style="font-size: 16px; width: 70%; padding-right: 80px; line-height: 1.6;">Cab voucher** worth Rs. 500/day if there's a repair delay.</label>
		      		</td>
		      	</tr>
		      	</tbody>
		      </table>
				</td>
        <td style="margin-top: 20px; width: 25%; border-right: 0.5px solid #dcdce0;">
          <img src="https://partner3.acko.com/docgen/static/img/green-tick-small.png" style="height: 20px; padding-left: 10px; padding-right: 10px;">
				</td>
        <td style="width: 25%; margin-top: 20px;">
          <img src="https://partner3.acko.com/docgen/static/img/cross.png" style="height: 20px; padding-left: 10px; padding-right: 10px;">
				</td>
      </tr>
      <tr>
				<td style="margin-top: 20px; width: 50%; border-right: 0.5px solid #dcdce0;">
          <table style="border-collapse: collapse; width: 100%;" cellpadding="0">
		      	<tbody>
		      	<tr>
		      		<td style="vertical-align: middle; width: 30%;">
		      			<img src="https://partner3.acko.com/docgen/static/img/AckoAdvantage_5.png" style="height: 50px; padding-left: 10px; padding-right: 10px;">
		      		</td>
		      		<td style="vertical-align: middle; width: 70%;">
		      			<label style="font-size: 16px; width: 70%; padding-right: 80px; line-height: 1.6;">Car drop at your doorstep.</label>
		      		</td>
		      	</tr>
		      	</tbody>
		      </table>
				</td>
        <td style="margin-top: 20px; width: 25%; border-right: 0.5px solid #dcdce0;">
          <img src="https://partner3.acko.com/docgen/static/img/green-tick-small.png" style="height: 20px; padding-left: 10px; padding-right: 10px;">
				</td>
        <td style="width: 25%; margin-top: 20px;">
          <img src="https://partner3.acko.com/docgen/static/img/cross.png" style="height: 20px; padding-left: 10px; padding-right: 10px;">
				</td>
      </tr>
      <tr>
				<td style="margin-top: 20px; width: 50%; border-right: 0.5px solid #dcdce0;">
          <table style="border-collapse: collapse; width: 100%;" cellpadding="0">
		      	<tbody>
		      	<tr>
		      		<td style="vertical-align: middle; width: 30%;">
		      			<img src="https://partner3.acko.com/docgen/static/img/AckoAdvantage_6.png" style="height: 50px; padding-left: 10px; padding-right: 10px;">
		      		</td>
		      		<td style="vertical-align: middle; width: 70%;">
		      			<label style="font-size: 16px; width: 70%; padding-right: 80px; line-height: 1.6;">Cashless and hassle-free processing.</label>
		      		</td>
		      	</tr>
		      	</tbody>
		      </table>
				</td>
        <td style="margin-top: 20px; width: 25%; border-right: 0.5px solid #dcdce0;">
          <img src="https://partner3.acko.com/docgen/static/img/green-tick-small.png" style="height: 20px; padding-left: 10px; padding-right: 10px;">
				</td>
        <td style="width: 25%; margin-top: 20px;">
          <img src="https://partner3.acko.com/docgen/static/img/green-tick-small.png" style="height: 20px; padding-left: 10px; padding-right: 10px;">
				</td>
      </tr>
			</tbody>
		</table>
    <p style="margin: 20px 0 5px 0; color: grey; font-size: 12px;">*Only applicable in selected cities provided you call us immediately - Ahmedabad | Bangalore | Chennai | Delhi | Hyderabad | Kolkata | Mumbai | Pune <br>
      **Cab vouchers available in the cities mentioned above. Please refer the <a href="https://partner3.acko.com/terms-and-conditions/cab-voucher-tnc/"> Terms & Conditions </a> for more details</p>
	</div>

	<!--<p class="claim-p1">CONTACT ACKO</p>
	<hr style="margin: 10px 0 20px 0; width: 100%;" />

	<div class="inner-wrapper">
		<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
			<tbody>
			<tr>
				<td style="vertical-align: middle; width: 10%;">
					<img src="https://partner3.acko.com/docgen/static/img/towing-van.jpg" style="height: 40px; padding-left: 10px;">
				</td>
				<td style="vertical-align: middle; width: 90%;">
					<label style="font-size: 18px; width: 100%; color: #6950a1; font-weight: 600;">Helpline for Elton John</label>
					<label style="font-size: 14px; width: 100%;">For claim registrations and emergencies, call <b>1800 266 2256</b></label>
				</td>
			</tr>
			</tbody>
		</table>
	</div>
-->
	<hr style="margin: 10px 0; width: 100%;" />

	<label style="font-size: 16px; width: 100%; color: #6950a1; font-weight: 600;">If you are a workshop or garage staff</label>
	<label style="font-size: 14px; width: 100%;">Please call Acko for quick settlements on 1800 209 9910 <span style="color: #8a8a8a;">[ GST# for workshop Invoice 27AAOCA9055C1ZJ ]</span></label>

	<div style="width: 100%; position: fixed; top: 1202px;">
		<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
			<tbody>
			<tr>
				<td style="width: 70%; vertical-align: bottom;">
					<label class="label6" style="font-weight: 600; width: 100%;">Acko General Insurance Ltd.</label>
					<label class="label6" style="width: 100%;">Unit No. 301, E Wing, Lotus Corporate Park, Off Western Express Highway, Goregaon (E), Mumbai- 400063</label>
					<label class="label6" style="width: 100%;">Email: hello@acko.com   |   Phone: 1800 266 2256   |   partner3.acko.com</label>
					<label class="label6" style="width: 100%;">Product: Private Car Package Policy | CIN : U66000MH2016PLC287385</label>
					<label class="label6" style="width: 100%;">IRDAI Reg No. 157 | HSN: 9971 | GST: 27AAOCA9055C1ZJ</label>
					<label class="label6" style="width: 100%;">UIN: IRDAN157P0007V01201718, A0019V01201819</label>
				</td>
				<td style="width: 30%; text-align: center; position: relative; vertical-align: bottom; text-align: right;">
					<label class="label2" style="text-align: right; margin: 0;">Page 1 of 5</label>
				</td>
			</tr>
			</tbody>
		</table>
	</div>

  <div style="page-break-after: always; margin-top: 50px;"></div>


	<div class="inner-wrapper">
		<div class="row" style="margin-top: 0px;">
			<h1 style="font-weight: 600; margin: 5px 0; font-size: 32px;">What’s Covered</h1>
			<p style="margin: 5px 0 30px 0; color: #8a8a8a; font-size: 12px;">A snapshot of all the coverages in this policy.</p>
			<table style="border-collapse: collapse;" cellpadding="0">
        <tbody>
				<tr>
					<td style="width: 27%; height: 115px; padding: 0 40px 20px 0; float: left; clear: right">
						<img src="https://partner3.acko.com/docgen/static/img/accidents_3x.png" style="height: 40px;">
						<p style="margin: 3px 0; font-size: 12px; color: #000; font-weight: 600;">Accidents</p>
						<p style="margin: 3px 0; font-size: 12px; color: #8a8a8a;">Damages to the car due to an accident.</p>
					</td>
					<td style="width: 27%; height: 115px; padding: 0 40px 20px 0; float: left; clear: right">
						<img src="https://partner3.acko.com/docgen/static/img/fire_3x.png" style="height: 40px;">
						<p style="margin: 3px 0; font-size: 12px; color: #000; font-weight: 600;">Fire</p>
						<p style="margin: 3px 0; font-size: 12px; color: #8a8a8a;">In case your car catches fire, resulting from self-ignition, explosion or lightning.</p>
					</td>
					<td style="width: 27%; height: 115px; padding: 0 40px 20px 0; float: left; clear: right">
						<img src="https://partner3.acko.com/docgen/static/img/theft_3x.png" style="height: 40px;">
						<p style="margin: 3px 0; font-size: 12px; color: #000; font-weight: 600;">Theft</p>
						<p style="margin: 3px 0; font-size: 12px; color: #8a8a8a;">If your car is stolen, we will pay you the value as per policy of your car.</p>
					</td>
				<!-- </tr> -->
				<!-- <tr> -->
					<td style="width: 27%; height: 115px; padding: 0 40px 20px 0; float: left; clear: right">
						<img src="https://partner3.acko.com/docgen/static/img/calamities_3x.png" style="height: 40px;">
						<p style="margin: 3px 0; font-size: 12px; color: #000; font-weight: 600;">Calamities</p>
						<p style="margin: 3px 0; font-size: 12px; color: #8a8a8a;">Damage due to natural or man made causes like earthquake, riots, etc.</p>
					</td>
					<td style="width: 27%; height: 115px; padding: 0 40px 20px 0; float: left; clear: right">
						<img src="https://partner3.acko.com/docgen/static/img/third_party_losses_3x.png" style="height: 40px;">
						<p style="margin: 3px 0; font-size: 12px; color: #000; font-weight: 600;">Third - Party Losses</p>
						<p style="margin: 3px 0; font-size: 12px; color: #8a8a8a;">Death, injury or property damage to any third party arising from your car.</p>
					</td>
     
				<!-- </tr> -->
				<!-- <tr> -->
					<td style="width: 27%; height: 115px; padding: 0 40px 20px 0; float: left; clear: right">
						<img src="https://partner3.acko.com/docgen/static/img/consumables_3x.png" style="height: 40px;">
						<p style="margin: 3px 0; font-size: 12px; color: #000; font-weight: 600;">Consumables</p>
						<p style="margin: 3px 0; font-size: 12px; color: #8a8a8a;">Covers the cost of consumables like nut, bolt, lubricant etc. consumed during car repair due to accident.</p>
					</td>

     

					

				
     
     
     
		<!-- </tr> -->
        <!-- <tr> -->
        
        
        
        <!-- </tr> -->
        <!-- <tr> -->
					
					
					
		</tr>
				</tbody>
			</table>
		</div>

		<!-- To handle wierd page break  -->
		<!--  -->
		<!-- To handle wierd page break  -->

		<div class="row" style="margin-top: 20px;">
			<h1 style="font-weight: 400; margin: 5px 0; font-size: 32px;">What’s Not Covered</h1>
			<p style="margin: 5px 0 30px 0; color: #8a8a8a; font-size: 12px;">A snapshot of all the coverages that are not covered in this policy.</p>
			<table style="border-collapse: collapse;" cellpadding="0">
				<tbody>
				<tr>
					<td style="width: 25%; padding: 0 40px 20px 0;">
						<p style="margin: 3px 0; font-size: 12px; color: #000; font-weight: 600;">Non-Accident Damage</p>
						<p style="margin: 3px 0; font-size: 12px; color: #8a8a8a;">Like depreciation, wear & tear, breakdown, failures & breakages, and deductibles.</p>
					</td>
					<td style="width: 25%; padding: 0 40px 20px 0;">
						<p style="margin: 3px 0; font-size: 12px; color: #000; font-weight: 600;">Consequential Loss & Contractual Liability</p>
						<p style="margin: 3px 0; font-size: 12px; color: #8a8a8a;">Indirect damage or liability arising due to your car accident.</p>
					</td>
					<td style="width: 25%; padding: 0 40px 20px 0;">
						<p style="margin: 3px 0; font-size: 12px; color: #000; font-weight: 600;">Nuclear Risk & War</p>
						<p style="margin: 3px 0; font-size: 12px; color: #8a8a8a;">Damages to your car due to nuclear risk, war & mutiny</p>
					</td>
					<td style="width: 25%; padding: 0 0 20px 0;">
						<p style="margin: 3px 0; font-size: 12px; color: #000; font-weight: 600;">Illegal Driving</p>
						<p style="margin: 3px 0; font-size: 12px; color: #8a8a8a;">Damage due to the car driven by a person without a valid driving license or under influence of liquor/drugs.</p>
					</td>
				</tr>
				<tr>
					<td style="width: 25%; padding: 0 40px 20px 0;">
						<p style="margin: 3px 0; font-size: 12px; color: #000; font-weight: 600;">Tyre, Tubes & Engine</p>
						<p style="margin: 3px 0; font-size: 12px; color: #8a8a8a;">Not included unless the tyre, tubes & engine are damaged due to an accident.</p>
					</td>
					<td style="width: 25%; padding: 0 40px 20px 0;">
						<p style="margin: 3px 0; font-size: 12px; color: #000; font-weight: 600;">Car Review Exception</p>
						<p style="margin: 3px 0; font-size: 12px; color: #8a8a8a;">Pre-existing Damages as found on vehicle inspection.</p>
					</td>
					<td style="width: 25%; padding: 0 40px 20px 0;">
						<p style="margin: 3px 0; font-size: 12px; color: #000; font-weight: 600;">Commercial usage of the Car</p>
						<p style="margin: 3px 0; font-size: 12px; color: #8a8a8a;">If the Car is registered as Private vehicle & if it is used for commercial purpose than the losses or liability due to accident during such usage is not covered in this policy.</p>
					</td>
     
				</tr>
				</tbody>
			</table>
		</div>

		

		<div style= "position: fixed; top: 2650px;">
			<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
				<tbody>
					<tr>
						<td style="width: 70%; vertical-align: bottom;">
							<p style="color: black; font-size: 10px;">The information provided herein above is for the purpose of illustration only. For more details on risk factors, terms, conditions and exclusions, please read the policy wordings ( <a href="https://partner3.acko.com/download">https://partner3.acko.com/download</a> ) carefully.
							</p>
						</td>
						<td style="width: 30%; text-align: center; position: relative; vertical-align: bottom; text-align: right;">
							<label class="label2" style="text-align: right; margin: 0;">Page 2 of 5</label>
						</td>
					</tr>
				</tbody>
			</table>
		</div>

    <div style="page-break-after: always; margin-top: 50px;"></div>

	</div>


	<div class="inner-wrapper">
   
			<label style="
			  position: absolute;
			  left: 10%;
			  top: 230%;
			  text-transform: uppercase;
			  font-weight: 600;
			  font-size: 60px;
			  border: 10px solid #000;
			  color: #000;
			  display: inline-block;
			  padding: 5px 25px;
			  letter-spacing: 15px;
			  transform: rotate(-45deg);
			  opacity: 0.2;
			">draft policy</label>
			
		<div class="headerp-pol">
			<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
				<tbody>
				<tr>
					<td style="width: 15%; vertical-align: middle;">
						<img class="logo" style="margin: 0; display: block;" src="https://partner3.acko.com/static/images/acko_logo_2x.png">
					</td>
					<td style="width: 75%; vertical-align: middle;">
						<h2 style="margin: 0; font-size: 20px; font-weight: 800;">COMPREHENSIVE POLICY</h2>
						<p style="margin: 0; font-size: 14px;">Private Car Package Policy</p>
					</td>

					<td style="width: 10%; vertical-align: middle;">
						<img style="width: 100%" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADkAAAA5AQAAAACkY74oAAABr0lEQVR4nGP4DwENDHgYH8QjrqZ9YW9g+H5pxyeOo98bGL6EbAt+8lQcyIicFlSnC2LEczqy2QIZ3y/8u2MZC1TzQTQ0NDQEqOv/t0DZDHugOX/CfzQcTjgOFKk0Kn1kkd7A8Ftyd/5eo+dAxlrNI5uW5QPNCZ5axuXwHihSkOQ/f018A8OPqX3SAc3tDQxfdZbU/2n1b2D45t30uCFiPVDNMpPAHl5+oMh80Y2zKtSBairMg4x7gCb/4YnvncEDtOvjesPYb5X7Gxh+MXoe2BIAdM+XEpO7b9vNGxg+BfJd3SfqDtRVfuPuqedAxj/Gc4yRDkCp33X8a+SbgA77dvCW9jPe6UBnlHanilsAbf/opddzMDIcqLjATEO6DGjX5zPG/MeWLwcyEtP3TP4AtOs/n3Npy1ygrk+vZyjbfy8HGjjl5vtqB5Bi44MbxHYC1fyelSrq4QgU+fHMrexVFdDSjzctGfgUgIr/f9h491N5PTAMpS1FzpkC/fX95vIYtfZ6UMh3OHYx+IMYfz6WrQTq+hL0KHehCNCn3+/tMGFt2A7UJXtLlSeQHW+cwhgA8lILLe4v8LUAAAAASUVORK5CYII=">
					</td>
				</tr>
				</tbody>
			</table>
		</div>

		<div class="pvq-details">
			<div class="">
				<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
					<tbody>
					<tr>
						<td style="width: 50%; vertical-align: top; padding-right: 30px;">
							<h3 class="header1">Policy Details</h3>
							<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
								<tbody>
								<tr>
									<td style="width: 40%;">
										<label class="label5">Insured Name:</label>
									</td>
									<td style="width: 60%;">
										<label class="label6">Elton John</label>
									</td>
								</tr>
								<tr>
									<td style="width: 40%;">
										<label class="label5">Address/Pincode:</label>
									</td>
									<td style="width: 60%;">
										<label class="label6">
                      
                      560034
										</label>
									</td>
								</tr>

								

								<tr>
									<td style="width: 40%;">
										<label class="label5">Period of Insurance:</label>
									</td>
									<td style="width: 60%;">
										<label class="label6">15 Feb 20 (00:00 hrs) to 14 Feb 21 (23:59 hrs)</label>
									</td>
								</tr>
								<tr>
									<td style="width: 40%;">
										<label class="label5">Policy Issuance Date:</label>
									</td>
									<td style="width: 60%;">
										<label class="label6">14 Feb 20</label>
									</td>
								</tr>
								<tr>
									<td style="width: 40%;">
										<label class="label5">Policy Number:</label>
									</td>
									<td style="width: 60%;">
										<label class="label6">DCCR00000025920/00</label>
									</td>
								</tr>
								</tbody>
							</table>
						</td>
						<td style="width: 50%; vertical-align: top; padding-left: 30px;">
							<h3 class="header1">Vehicle Details</h3>
							<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
								<tbody>
								<tr>
									<td style="width: 40%;">
										<label class="label5">Registration Number:</label>
									</td>
									<td style="width: 60%;">
										<label class="label6">MH03</label>
									</td>
								</tr>
								<tr>
									<td style="width: 40%;">
										<label class="label5">Make/Model:</label>
									</td>
									<td style="width: 60%;">
										<label class="label6">Honda City</label>
									</td>
								</tr>
								<tr>
									<td style="width: 40%;">
										<label class="label5">Purchase Year:</label>
									</td>
									<td style="width: 60%;">
										<label class="label6">2020</label>
									</td>
								</tr>
								<tr>
									<td style="width: 40%;">
										<label class="label5">Engine CC:</label>
									</td>
									<td style="width: 60%;">
										<label class="label6">1497</label>
									</td>
								</tr>
        
        
								</tbody>
							</table>
						</td>
					</tr>
					</tbody>
				</table>
			</div>

		</div>

		<div class="idv">
			<h3 class="header1" style="margin-bottom: 0;">INSURED DECLARED VALUE (IDV)</h3>

			<table class="table1" style="margin-bottom: 30px;">
				<thead>
				<tr>
					<th style="width: 25%;">Vehicle IDV (₹)</th>
					<th style="width: 25%;">Accessories (₹)</th>
					<th style="width: 25%;">Bifuel Kit (₹)</th>
					<th style="width: 25%;">Total IDV (₹)</th>
				</tr>
				</thead>
				<tbody>
				<tr>
					<td>1344915</td>
					<td>0.0</td>
					<td>0</td>
					<td>1344915.0</td>
				</tr>
				</tbody>
			</table>

			<h3 class="header1" style="margin-bottom: 0;">PREMIUM DETAILS (₹)</h3>
			<table class="table1">
				<thead>
				<tr>
					<th style="width: 50%;" colspan="2">Own Damage Premium (A)</th>
					<th style="width: 50%;" colspan="2">Liability Premium (B)</th>
				</tr>
				</thead>
				<tbody>
				
				<tr>
					
					<td style="border-right: none; border-bottom: none; border-top: none;">
						<label class="label5">Basic Own Damage</label>
					</td>
					<td style="text-align: right; border-left: none; border-bottom: none; border-top: none;">
						<label class="label5">₹ 11452.96</label>
					</td>
					
					<td style="border-right: none; border-bottom: none; border-top: none;">
						<label class="label5">Basic Third Party Liability</label>
					</td>
					<td style="text-align: right; border-left: none; border-bottom: none; border-top: none;">
						<label class="label5">₹ 3221.00</label>
					</td>
					
				</tr>
				
				<tr>
					<td style="border-right: none;">
						<label class="label6">Net Own Damage Premium (A)</label>
					</td>
					<td style="text-align: right; border-left: none;">
						<label class="label6">₹ 11452.96</label>
					</td>
					<td style="border-right: none;">
						<label class="label6">Net Liability Premium (B)</label>
					</td>
					<td style="text-align: right; border-left: none;">
						<label class="label6">₹ 3221.00</label>
					</td>
				</tr>
				<tr>
					<td style="border-right: none;" colspan="3">
						<label class="label5">Total Package Premium</label>
					</td>
					<td style="text-align: right; border-left: none;">
						<label class="label5">₹ 14673.96</label>
					</td>
				</tr>
				<tr>
					<td style="border-right: none;" colspan="3">
						<label class="label5">GST</label>
					</td>
					<td style="text-align: right; border-left: none;">
						<label class="label5">₹ 2641.31</label>
					</td>
				</tr>
				<tr>
					<td style="border-right: none;" colspan="3">
						<label class="label6">Total Premium</label>
					</td>
					<td style="text-align: right; border-left: none;">
						<label class="label6">₹ 17315.27</label>
					</td>
				</tr>
				</tbody>
			</table>
		</div>

		<div class="row" style="padding-left: 15px; margin-top: 5px;">
			<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
				<tbody>
				<tr>
					<td style="width: 15%;"><label class="label5">Geographical Area:</label></td>
					<td style="width: 10%;"><label class="label6">India</label></td>
					<td style="width: 20%;"><label class="label5">Voluntary Deductible:</label></td>
					<td style="width: 10%;"><label class="label6">₹ 0</label></td>
          <td style="width: 15%;">
              <label class="label5">Hypothecation:</label>
          </td>
          
            <td style="width: 30%;"><label class="label6">NA</label></td>
          

				</tr>
				<tr>
					<td><label class="label5">No-Claim Bonus:</label></td>
					<td><label class="label6">0%</label></td>
					<td><label class="label5">Compulsory Deductible:</label></td>
					<td><label class="label6">₹ 1000</label></td>
				</tr>
    
				</tbody>
			</table>
		</div>

		<div class="row limitations" style="margin: 15px 0;">
			<p>
              <b>Limitations As To Use:</b> The Policy covers use of the vehicle for any purpose other than:
                  a) Hire or Reward
                  b) Carriage of goods (other than samples or personal luggage)
                  c) Organized racing
                  d) Pace making
                  e) Speed testing
                  f) Reliability Trials
                  g) Any purpose in connection with Motor Trade.
              <b>Persons or Class of Persons entitled to drive:</b>
                  Any person ((including the insured), provided that a person driving holds a valid driving
                  license at the time of the accident and is not disqualified from holding or obtaining such a
                  license. Provided also that the person holding a valid learner's license may also drive
                  the vehicle and that such a person satisfies the requirements of Rule 3 of the Central Motor
                  Vehicles Rules, 1989.
              <b>Limits of Liability.</b>
                  1. Under Section II-1
                  (i) of the policy - Death of or bodily injury - Such amount as is necessary to meet the requirements of the Motor Vehicles Act, 1988.
                  2. Under Section II - 1(ii) of the policy -Damage to Third Party Property - Rs. 750000
                  
              <b>Terms, Conditions &amp; Exclusions:</b>
                As per the Indian Motor Tariff. A personal copy of the same is available free of cost on request &amp; the same is also available at our website.</p>
				
            <p>I / We hereby certify that the policy to which the certificate relates as well as the certificate of insurance are issued in accordance with the provision of chapter X, XI of Motor Vehicles Act, 1988. "The stamp duty of Rs. 0.50 paid by electronic medium vide GRAS Deface no. 0004976826201920 dated 19/12/2019 as prescribed in Government Notification Revenue & Forest Department No. Mudrank - 2017/C.R.97/M-1, dated 09/01/2018. GSTN: 27AAOCA9055C1ZJ. <b>IMPORTANT NOTICE:</b> The Insured is not indemnified if the vehicle is used or driven otherwise than in accordance with this Schedule. Any payment made by the Company by reason of wider terms appearing in the Certificate in order to comply with the Motor Vehicles Act, 1988 is recoverable from the Insured. See the clause headed "AVOIDANCE OF CERTAIN TERMS AND RIGHT OF RECOVERY” in the policy wordings. <b>Disclaimer:</b> The Policy shall be void from inception if the premium cheque is not realized. In the event of misrepresentation, fraud or non-disclosure of material fact, the Company reserves the right to cancel the Policy. The policy is issued basis the information provided by you, which is available with the company. In case of discrepancy/non recording of relevant information in the policy, the insured is requested to bring the same to the notice of the company within 15 days. This Policy is to be read in conjunction with the Policy wordings
              (<a href="https://acko.com/download">https://partner3.acko.com/download</a>) available on the website of the Company. On renewal, the benefits provided under the policy and/or terms and
              conditions of the policy including premium rate may be subject to change.</p>
				
		</div>

		<div class="row" style="margin-bottom: 30px;">
			<h3 class="header1">Intermediary Details</h3>
   
			<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
				<tbody>
				<tr>
					<td style="width: 15%;">
						<label class="label5">Policy Issuing Office:</label>
					</td>
					<td style="width: 20%;">
						<label class="label6">Direct - Mumbai</label>
					</td>
					<td style="width: 15%;">
						<label class="label5">Intermediary Name:</label>
					</td>
					<td style="width: 20%;">
						<label class="label6">Direct</label>
					</td>
				</tr>
				<tr>
					<td>
						<label class="label5">Phone Number:</label>
					</td>
					<td>
						<label class="label6">NA</label>
					</td>
					<td>
						<label class="label5">Intermediary Code:</label>
					</td>
					<td>
						<label class="label6">NA</label>
					</td>
				</tr>
				</tbody>
			</table>
   
		</div>

		<div class="row" style="position: fixed; top: 3880px">
			<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
				<tbody>
				<tr>
					<td style="width: 70%; vertical-align: bottom;">
						<label class="label6" style="font-weight: 600; width: 100%;">Acko General Insurance Ltd.</label>
						<label class="label6" style="width: 100%;">Unit No. 301, E Wing, Lotus Corporate Park, Off Western Express Highway, Goregaon (E), Mumbai- 400063</label>
						<label class="label6" style="width: 100%;">Email: hello@acko.com   |   Phone: 1800 266 2256   |   partner3.acko.com</label>
						<label class="label6" style="width: 100%;">Product: Private Car Package Policy | CIN : U66000MH2016PLC287385</label>
					<label class="label6" style="width: 100%;">IRDAI Reg No. 157 | HSN: 9971 | GST: 27AAOCA9055C1ZJ</label>
					<label class="label6" style="width: 100%;">UIN: IRDAN157P0007V01201718, A0019V01201819</label>
					</td>
					<td style="width: 30%; text-align: center; position: relative; vertical-align: bottom;">
						<img src="https://partner3.acko.com/docgen/static/img/stamp.png" style="height: 150px; position: absolute; left: -93px; top: -38px; transform: rotate(-15deg);">
						<img src="https://partner3.acko.com/docgen/static/img/sign.png" style="height: 80px;">

						<label class="label6" style="width: 100%; border-top: 1px solid #000; padding: 6px 0 0 0;">For Acko General Insurance Ltd.</label>
						<label class="label6" style="width: 100%;">Duly Constituted Attorney</label>
					</td>
				</tr>
                <tr>
                    <td style="width: 70%; vertical-align: bottom;"></td>
                    <td style="width: 30%; text-align: center; position: relative; vertical-align: bottom; text-align: right;">
                        <label class="label2" style="text-align: right; padding-right: 20px;">Page 3 of 5</label>
                    </td>
                </tr>
				</tbody>
			</table>
		</div>
    <div style="page-break-after: always; margin-top: 50px;"></div>
	</div>

	<div class="inner-wrapper">
		<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
			<tbody>
			<tr>
				<td style="width: 15%; vertical-align: middle;">
					<img class="logo" style="margin: 0; display: block;" src="https://partner3.acko.com/static/images/acko_logo_2x.png">
				</td>
				<td style="width: 85%; vertical-align: middle;">
					<h2 style="margin: 0; font-size: 20px; font-weight: 800;">PREMIUM RECEIPT</h2>
				</td>
			</tr>
			</tbody>
		</table>

		<p style="font-size: 16px; color: #000; margin: 40px 0;">Received with thanks from Elton John a sum of <b>₹ 17315.27</b> towards premium on Car Insurance Policy</p>

		<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
			<tbody>
			<tr>
				<td style="width: 50%; vertical-align: top; padding-right: 30px;">
					<h3 class="header1">INSURED Details</h3>
					<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
						<tbody>
						<tr>
							<td style="width: 40%;">
								<label class="label5">Name of Insured:</label>
							</td>
							<td style="width: 60%;">
								<label class="label6">Elton John</label>
							</td>
						</tr>


						

						<tr>
							<td style="width: 40%;">
								<label class="label5">Period of Insurance:</label>
							</td>
							<td style="width: 60%;">
								<label class="label6">15 Feb 20 (00:00 hrs) to 14 Feb 21 (23:59 hrs)</label>
							</td>
						</tr>
						<tr>
							<td style="width: 40%;">
								<label class="label5">Policy Number:</label>
							</td>
							<td style="width: 60%;">
								<label class="label6">DCCR00000025920/00</label>
							</td>
						</tr>
						</tbody>
					</table>
				</td>
				<td style="width: 50%; vertical-align: top; padding-left: 30px;">
				
				</td>
			</tr>
			</tbody>
		</table>

		<div class="row" style="margin-top: 40px;">
			<h3 class="header1" style="margin-bottom: 0;">PREMIUM DETAILS (₹)</h3>
			<table style="border-collapse: collapse; width: 100%; border: 1px solid #ddd; margin-bottom: 40px;">
				<tbody>
				<tr>
					<td style="border-bottom: 1px solid #ddd; padding: 3px 0 3px 10px;">
						<label class="label5">Gross Premium</label>
					</td>
					<td style="text-align: right; border-bottom: 1px solid #ddd; padding: 3px 10px 3px 0;">
						<label class="label5">₹14673.96</label>
					</td>
				</tr>
				<tr>
					<td style="border-bottom: 1px solid #ddd; padding: 3px 0 3px 10px;">
						<label class="label5">Add: Goods and Services Tax @ 18%</label>
					</td>
					<td style="text-align: right; border-bottom: 1px solid #ddd; padding: 3px 10px 3px 0;">
						<label class="label5">₹2641.31</label>
					</td>
				</tr>
				<tr>
					<td style="padding: 3px 0 3px 10px;">
						<label class="label6">Total Premium</label>
					</td>
					<td style="text-align: right; padding: 3px 10px 3px 0;">
						<label class="label6">₹17315.27</label>
					</td>
				</tr>
				</tbody>
			</table>

			<p style="margin: 40px 0 10px 0; font-size: 14px; text-transform: uppercase; font-weight: 600;"><b>Terms &amp; Conditions:</b></p>
			<p style="margin: 0; font-size: 12px; color: black; line-height: 1.5;">
					Issuance of this receipt does not amount to acceptance of the risk by Acko General Insurance
					Limited. The insurance cover for the risk shall be as per the terms and conditions of the
					Insurance Policy if and when issued.
					* Cheque/DD/PO receipt is valid subject to realization of the instrument.
			</p>
		</div>

		<div class="row" style="position: fixed; top: 5240px">
			<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
				<tbody>
				<tr>
					<td style="width: 70%; vertical-align: bottom;">
						<label class="label6" style="font-weight: 600; width: 100%;">Acko General Insurance Ltd.</label>
						<label class="label6" style="width: 100%;">Unit No. 301, E Wing, Lotus Corporate Park, Off Western Express Highway, Goregaon (E), Mumbai- 400063</label>
						<label class="label6" style="width: 100%;">Email: hello@acko.com   |   Phone: 1800 266 2256   |   partner3.acko.com</label>
					<label class="label6" style="width: 100%;">CIN : U66000MH2016PLC287385 | IRDAI Reg No. 157 | HSN: 9971 | GST: 27AAOCA9055C1ZJ</label>
					<label class="label6" style="width: 100%;">UIN: IRDAN157P0007V01201718, A0019V01201819</label>
					</td>
					<td style="width: 30%; vertical-align: bottom;">
						<img src="https://partner3.acko.com/docgen/static/img/sign.png" style="height: 80px;">

						<label class="label6" style="width: 100%; border-top: 1px solid #000; padding: 6px 0 0 0;">For Acko General Insurance Ltd.</label>
						<label class="label6" style="width: 100%;">Duly Constituted Attorney</label>
					</td>
				</tr>
                <tr>
                    <td style="width: 70%; vertical-align: bottom;"></td>
                    <td style="width: 30%; text-align: center; position: relative; vertical-align: bottom; text-align: right;">
                        <label class="label2" style="text-align: right; padding-right: 20px;">Page 4 of 5</label>
                    </td>
                </tr>
				</tbody>
			</table>
		</div>

		<div style="page-break-after: always; margin-top: 50px;"></div>
	</div>

	<div class="inner-wrapper">
		<div class="row">
			<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
				<tbody>
				<tr>
					<td style="width: 15%; vertical-align: middle;">
						<img class="logo" style="margin: 0; display: block;" src="https://partner3.acko.com/static/images/acko_logo_2x.png">
					</td>
					<td style="width: 85%; vertical-align: middle;">
						<h2 style="margin: 0; font-size: 20px; font-weight: 800;">PROPOSAL FORM</h2>
					</td>
				</tr>
				</tbody>
			</table>
		</div>

		<p style="font-size: 16px; color: #000; margin: 50px 0 20px 0;">Dear Elton John,</p>
		<p style="font-size: 16px; color: #000; margin: 20px 0 20px 0;">We wish to inform you that the Insurance policy number  <b> DCCR00000025920/00</b> has been issued on the basis of the information and declaration given by you, the transcript whereof is mentioned below. </p>

		<p style="font-size: 14px; color: #8a8a8a; margin: 15px 0;">Please be informed that this Policy shall be construed to be void ab initio/invalid in the event we find that you have not disclosed material or correct information required for the purpose of providing the below insurance cover and in case of any claim arising under the policy in such a scenario, we shall be under no obligation whatsoever to settle such claim to you and the premium paid by you under this policy shall stand fully forfeited.</p>

		<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
			<tbody>
			<tr>
				<td style="width: 50%; vertical-align: top; padding-right: 30px;">
					<h3 class="header1">POLICY Details</h3>
					<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
						<tbody>
						<tr>
							<td style="width: 40%;">
								<label class="label5">Policy Number:</label>
							</td>
							<td style="width: 60%;">
								<label class="label6">DCCR00000025920/00</label>
							</td>
						</tr>
						<tr>
							<td style="width: 40%;">
								<label class="label5">Period of Insurance:</label>
							</td>
							<td style="width: 60%;">
								<label class="label6">15 Feb 20 (00:00 hrs) to 14 Feb 21 (23:59 hrs)</label>
							</td>
						</tr>
						<tr>
							<td style="width: 40%;">
								<label class="label5">Policy Issuance Date:</label>
							</td>
							<td style="width: 60%;">
								<label class="label6">14 Feb 20</label>
							</td>
						</tr>
						</tbody>
					</table>
				</td>
				<td style="width: 50%; vertical-align: top; padding-left: 30px;">
					<h3 class="header1">PREVIOUS POLICY Details</h3>
					<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
						<tbody>
						<tr>
							<td style="width: 40%;">
								<label class="label5">Previous Policy Expired:</label>
							</td>
							
							<td style="width: 60%;">
									<label class="label6">Not Expired</label>
							</td>
							
						</tr>
						
						<tr>
								<td style="width: 40%;">
									<label class="label5">Previous Policy Insurer:</label>
								</td>
								<td style="width: 60%;">
									<label class="label6">Acko General Insurance</label>
								</td>
						</tr>
						</tbody>
					</table>
				</td>
			</tr>
			</tbody>
		</table>

		<table style="border-collapse: collapse; width: 100%; margin: 5px 0 0;" cellpadding="0">
			<tbody>
			<tr>
				<td style="width: 50%; vertical-align: top; padding-right: 30px;">
						<h3 class="header1">CAR Details</h3>
						<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
							<tbody>
							<tr>
								<td style="width: 60%;">
									<label class="label5">Car Number:</label>
								</td>
								<td style="width: 40%;">
									<label class="label6">MH03</label>
								</td>
							</tr>
							<tr>
								<td style="width: 60%;">
									<label class="label5">Make/Model:</label>
								</td>
								<td style="width: 40%;">
									<label class="label6">Honda City</label>
								</td>
							</tr>
							<tr>
								<td style="width: 60%;">
									<label class="label5">Type:</label>
								</td>
								<td style="width: 40%;">
									<label class="label6">Private</label>
								</td>
							</tr>
							<tr>
								<td style="width: 60%;">
									<label class="label5">Fuel Type:</label>
								</td>
								<td style="width: 40%;">
									<label class="label6">petrol</label>
								</td>
							</tr>
							<tr>
								<td style="width: 60%;">
									<label class="label5">Registration Year:</label>
								</td>
								<td style="width: 40%;">
									<label class="label6">2020</label>
								</td>
							</tr>
							<tr>
								<td style="width: 60%;">
									<label class="label5">Registration Month:</label>
								</td>
								<td style="width: 40%;">
									<label class="label6">Jan</label>
								</td>
							</tr>
							<tr>
								<td style="width: 60%;">
									<label class="label5">Insured Declared Value (IDV):</label>
								</td>
								<td style="width: 40%;">
									<label class="label6">1344915</label>
								</td>
							</tr>
							<tr>
								<td style="width: 60%;">
									<label class="label5">Accessories (IDV):</label>
								</td>
								<td style="width: 40%;">
									<label class="label6">0.0</label>
								</td>
							</tr>
       
       
							
							</tbody>
						</table>
				</td>
				<td style="width: 50%; vertical-align: top; padding-left: 30px;">
						<h3 class="header1">CAR OWNER Details</h3>
					<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
						<tbody>
						<tr>
							<td style="width: 40%;">
								<label class="label5">Name:</label>
							</td>
							<td style="width: 60%;">
								<label class="label6">Elton John</label>
							</td>
						</tr>
						<tr>
							<td style="width: 40%;">
								<label class="label5">Email Address:</label>
							</td>
							<td style="width: 60%;">
								<label class="label6">iit2015085@iiita.ac.in</label>
							</td>
						</tr>
						<tr>
							<td style="width: 40%;">
								<label class="label5">Mobile Number:</label>
							</td>
							<td style="width: 60%;">
								<label class="label6">9940319909</label>
							</td>
						</tr>
						
						
							<tr>
									<td style="width: 60%;">
										<label class="label5">NCB:</label>
									</td>
									<td style="width: 40%;">
										<label class="label6">0%</label>
									</td>
						</tr>
						
						<tr>
							<td style="width: 40%;">
								<label class="label5">Address/Pincode:</label>
							</td>
							<td style="width: 60%;">
								<label class="label6">
                  
                  560034
								</label>
							</td>
						</tr>

						
						
						</tbody>
					</table>
				</td>
			</tr>
			</tbody>
		</table>
		

    <h3 class="header1" style="margin-bottom: 0;">Cover Details</h3>
		<table class="table1" style="margin: 0 0 10px 0;">
			<thead>
			<tr>
				<th style="width: 60%;">Add-ons/ Others</th>
				<th style="width: 20%;">Included</th>
				<th style="width: 20%;">Excluded</th>
			</tr>
			</thead>
			<tbody>
			
			<tr>
					<td>PA Cover</td>
					<td>-</td>
					<td><img src="https://partner3.acko.com/docgen/static/img/green_tick_1x.png" style="height: 10px;" /></td>
			</tr>
			
			

			
			<tr>
				<td>Consumables</td>
				<td><img src="https://partner3.acko.com/docgen/static/img/green_tick_1x.png" style="height: 10px;" /></td>
				<td>-</td>
			</tr>
			
			<tr>
				<td>Zero Depreciation</td>
				<td>-</td>
				<td><img src="https://partner3.acko.com/docgen/static/img/green_tick_1x.png" style="height: 10px;" /></td>
			</tr>
			
			
   
   
   
   
   
   
			</tbody>
		</table>


		
		<p style="margin: 15px 0 10px 0; font-size: 14px; text-transform: uppercase; font-weight: 600;"><b>Terms &amp; Conditions:</b></p>
			<p style="margin: 0; font-size: 12px; color: black; line-height: 1.5;">
				“I/We desire to insure with Acko General Insurance Limited in respect of the vehicle described in
				this proposal form and confirm that the statements contained in this application are my/our true
				and accurate representations. I/We undertake that if any of the statements are found to be false
				or incorrect, the benefits under this policy would stand forfeited. I/We agree that this application
				and declaration shall be promissory and shall be the basis of the contract between me/us and
				Acko General Insurance Limited. I/We agree to the Company taking appropriate measures to
				capture the voice log for all such telephonic transactions carried out by me/us as required by the
				procedures/regulations internal or external to the Company and shall not hold the Company
				responsible or liable for relying/using such recorded telephonic conversation. In the event of
				nonrealization of the cheque or non-receipt of the amount of premium by the Company the
				policy shall be deemed cancelled ‘ab-initio’ and the Company shall not be responsible for any
				liabilities of whatsoever nature under this Policy.” I/We agree to receive ‘Certificate of Insurance
				or Policy Schedule’ only and shall access the policy terms, conditions and exclusions on the
				company’s website.</p>
		<div class="row" style="position: fixed; top:6570px">
			<table style="border-collapse: collapse; width: 100%;" cellpadding="0">
				<tbody>
				<tr>
					<td style="width: 70%; vertical-align: bottom;">
						<label class="label6" style="font-weight: 600; width: 100%;">Acko General Insurance Ltd.</label>
						<label class="label6" style="width: 100%;">Unit No. 301, E Wing, Lotus Corporate Park, Off Western Express Highway, Goregaon (E), Mumbai- 400063</label>
						<label class="label6" style="width: 100%;">Email: hello@acko.com   |   Phone: 1800 266 2256   |   partner3.acko.com</label>
						<label class="label6" style="width: 100%;">CIN : U66000MH2016PLC287385 | IRDAI Reg No. 157 | HSN: 9971 | GST: 27AAOCA9055C1ZJ</label>
						<label class="label6" style="width: 100%; margin-bottom: 0;">UIN: IRDAN157P0007V01201718, A0019V01201819</label>
					</td>
					<td style="width: 30%; vertical-align: bottom;">
						<img src="https://partner3.acko.com/docgen/static/img/sign.png" style="height: 80px;">

						<label class="label6" style="width: 100%; border-top: 1px solid #000; padding: 6px 0 0 0;">For Acko General Insurance Ltd.</label>
						<label class="label6" style="width: 100%; margin-bottom: 0;">Duly Constituted Attorney</label>
					</td>
				</tr>
                <tr>
                    <td style="width: 70%; vertical-align: bottom;"></td>
                    <td style="width: 30%; text-align: center; position: relative; vertical-align: bottom; text-align: right;">
                        <label class="label2" style="text-align: right; padding-right: 20px;">Page 5 of 5</label>
                    </td>
                </tr>
				</tbody>
			</table>
		</div>
		

	</div>
</div>
</body>
</html>


        '''
        URL = "pdf_html_lt/"
        PARAMS = {'html': html}
        data = json.dumps(PARAMS)
        self.client.post(URL, data = data)
    
    
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(1, 1)
    
# http://localhost:8050  
# http://wkpdfgen-prod.eba-78arf59s.ap-south-1.elasticbeanstalk.com/