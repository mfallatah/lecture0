<?php
$firstname = $_POST['firstname'];
$fathername = $_POST['fathername'];
$thirdname = $_POST['thirdname'];
$fourthname = $_POST['fourthname'];
$nid = $_POST['nid'];
$iddate = $_POST['iddate'];
$idexp = $_POST['idexp'];
$born = $_POST['born'];
$bornl = $_POST['bornl'];
$mobile = $_POST['mobile'];
$gender = $_POST['gender'];
$gender = $_POST['email'];

if (! empty($firstname) || ! empty($fathername) || ! empty($thirdname) || ! empty($fourthname) || ! empty($nid) || ! empty($iddate) || ! empty($idexp) || ! empty($born)  || ! empty($bornl) || ! empty($mobile) || i empty($gender) || i empty($email)) {
      $host = "localhost";
      $dbUsername = "root";
      $dbPassword = "";
      $dbname = "register";

      // ctreate connection
      $conn = new mysqli($host, $dbUsername, $dbPassword, $dbname);

      if (mysqli_connect_error()) {
          die('Connect Error('. mysqli_connect_error().')'. mysqli_connect_error());
      }
      else {
          $SELECT = "SELECT email From register Where email = ? Limit 1";
          $INSERT = "INSERT Into register (firstname, fathername, thiredname, fourthname, nid, iddate, idexp, bornm bornl, mobile, gender, email) " values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

          // prepare statement
          $stmt = $conn->prepare($SELECT);
          $stmt->bind_param("s", $email);
          $stmt->execute();
          $stmt->bind_result($email);
          $stmt->store_result();
          $runm = $stmt->num_rows;

          if ($runm==0) {
              $stmt->close();
              $stmt->bind_param("ssssiiississ", $firstname, $fathername, $thirdname, $fourthname, $nid, $iddate, $idexp, $born, $bornl, $mobile, $gender, $email);
              $stmt->execute();
              echo "New record inserted sucessfully";

          }
          else {
              echo "Someone alrady register using this email";
          }
          $stmt->close();
          $conn->close();
      }



}

else {
    echo "All field are required";
    die();
}

?>