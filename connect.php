<?php
  $Firstname = filter_input(INPUT_POST, 'firstname');
  $Lastname = filter_input(INPUT_POST, 'lastname');
  $Email = filter_input(INPUT_POST, 'email');
  $Password = filter_input(INPUT_POST, 'password');
  if (!empty($firstname)){
  if (!empty($lastname)){
  if (!empty($email)){
  if (!empty($Password)){
      $host = "localhost";
      $dbusername = "root";
      $dbpassword = "";
      $dbname = "youtube";

      //Create connection
      $conn = new mysqli ($host, $dbusername, $dbpassword, $dbname);

      if (mysqli_connect_error()){
          die('Connect Error('. mysqli_connect_errno().')'. mysqli_connect_error());

      }
      else{
          $sql = "INSERT INTO account(firstname, lastname, email, password)
          values ('$firstname','$lastname','$email','$password') ";
          if ($conn->query($sql)){
              echo "New record is inserted sucessfully";
          }
          else{
              echo "Error:".$sql."<br>".$conn->error;
          }
          $conn->close();
      }

  }
  else{
      echo "Password should not be empty";
      die();
  }

  }
  else{
      echo "Email should not be empty";
      die();
  }

  }
  else{
      echo "Last should not be empty";
      die();
  }

  }
  else{
      echo "Username should not be empty";
      die();
  }




?>