function validatemedicine() {
  var Mediname = document.getElementById('Mediname').value;
  var cprice = document.getElementById('cprice').value;
  var sprice = document.getElementById('sprice').Value;
  var Mediconame = document.getElementById('Contactnumber').value;
  // var starttime = document.getElementById('Starttime').value;
  // var endtime = document.getElementById('endtime').value;

  // var bookerscheck = /^[A-Za-z.]{3,30}$/;
  // // var passwordcheck =/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,16}$/;
  // var pricecheck = /^[0-9]{9}$/;
  // var contactcheck = /^[789][0-9]{9}$/;
  // var startcheck = /^[0-9]{9}$/;

  var name = /^[A-Za-z.]$/;
  var costprice =/^[0-9]{9}$/;
  var sellingprice = /^[0-9]{9}$/;
  var companyname = /^[A-Za-z.]$/;

  if (name.test(Mediname)) {
    document.getElementById('Mediname error').innerHTML = " ";
  } else {
    document.getElementById('Mediname error').innerHTML = "** Medicine name is Invalid ";
    return false;
  }
  if (costprice.test(cprice)) {
    document.getElementById('cost price error').innerHTML = " ";
  } else {
    document.getElementById('cost price error').innerHTML = "** Cost Price is Invalid ";
    return false;
  }

  if (sellingprice.test(sprice)) {
    document.getElementById('selling price error').innerHTML = " ";
  } else {
    document.getElementById('selling price error').innerHTML = "** Selling Price is Invalid ";
    return false;
  }

  if (companyname.test(Mediconame)) {
    document.getElementById('Medicine company name error').innerHTML = " ";
  } else {
    document.getElementById('contacterror').innerHTML = "** Company name is Invalid ";
    return false;
  }


  // if (startcheck.test(starttime)) {
  //   document.getElementById('starterror').innerHTML = " ";
  // } else {
  //   document.getElementById('starterror').innerHTML = "** starttime is Invalid ";
  //   return false;
  // }


  // if (endcheck.test(endtime)) {
  //   document.getElementById('enderror').innerHTML = " ";
  // } else {
  //   document.getElementById('enderror').innerHTML = "** endtime is Invalid ";
  //   return false;
  // }



}