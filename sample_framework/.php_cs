<?php

return PhpCsFixer\Config::create()
    ->setRules(array(
        '@PSR2' => true,
        'binary_operator_spaces' = true,
        'blank_line_before_return' = true,
        'concat_space' = true,
        'mb_str_functions' = true,
        'method_separation' = true,
        'psr4' = true,
        'strict_param' => true,
        'array_syntax' => array('syntax' => 'short'),
    ));
