function calc() {
  var sed;
  var h = document.getElementById('h').value;
  var w = document.getElementById('w').value;
  var age = document.getElementById('age').value;
  var act = document.getElementById('active').value;
  // No empty info is allowed.
  if (h == "" && w == "" && age == "") {
    alert("Please enter your height, weight, and age.");
    return false;
  } else if (w == "") {
    alert("Please enter your weight.");
    return false;
  } else if (h == "") {
    alert("Please enter your height.");
    return false;
  } else if (age == "") {
    alert("Please enter your age.");
    return false;
  }
  //H limit
  if (h < 10 || h > 300) {
    alert("Height is range from 10cm to 300cm.");
    return false;
  }
  //W limit
  if (w!=="" && (w < 10 || w > 500)) {
    alert("Weight is range from 10kg to 500kg.");
    return false;
  }
  // Condition
  if (gen[0].checked) {
    sed = Math.floor(655 + (9.6 * w) + (1.8 * h) - (4.7 * age));
  } else {
    sed = Math.floor(66 + (13.7 * w) + (5.0 * h) - (6.8 * age));
  }
  switch (act) {
    case '0':
      {
        var sede = Math.floor(sed * 1.0);
        document.getElementById('result').value = sede;
        break;
      }
    case '1':
      {
        var liga = Math.floor(sed * 1.375);
        document.getElementById('result').value = liga;
        break;
      }
    case '2':
      {
        var moda = Math.floor(sed * 1.55);
        document.getElementById('result').value = moda;
        break;
      }
    case '3':
      {
        var supa = Math.floor(sed * 1.725);
        document.getElementById('result').value = supa;
        break;
      }
    case '4':
      {
        var exta = Math.floor(sed * 1.9);
        document.getElementById('result').value = exta;
        break;
      }
    default:
      {
        break;
      }
  } //end switch
}
