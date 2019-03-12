<?php

// let php tokenize php

function tokenize($buf)
{
 $tokens = token_get_all($buf);

 foreach ($tokens as $token)
 {
  if (is_array($token))
  {
   //echo "Line {$token[2]}: ", token_name($token[0]), " ('{$token[1]}')", PHP_EOL;
   echo $token[2].";".$token[0].";".$token[1].PHP_EOL;
  }
 }
}

function tokenize_file($name)
{
 tokenize(file_get_contents($name));
}

tokenize_file("woppy/tokenize.php");


// EOF
